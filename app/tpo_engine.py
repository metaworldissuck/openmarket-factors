from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
import hashlib
import math
import random
from typing import Any


@dataclass(frozen=True)
class Bar:
    timestamp: datetime
    open: float
    high: float
    low: float
    close: float
    volume: int
    delta: float | None = None


def _round_tick(value: float, tick_size: float) -> float:
    return round(round(value / tick_size) * tick_size, 2)


def _format_price(value: float) -> str:
    return f"{value:,.2f}"


def generate_demo_bars(ticker: str, sessions: int = 5) -> list[Bar]:
    seed = int(hashlib.sha256(ticker.upper().encode()).hexdigest()[:8], 16)
    rng = random.Random(seed)
    base = {"AAPL": 228.0, "MSFT": 510.0, "NVDA": 178.0, "TSLA": 347.0, "AMZN": 232.0}.get(ticker.upper(), 180.0)
    bars: list[Bar] = []
    start = datetime.now(timezone.utc).replace(hour=13, minute=30, second=0, microsecond=0) - timedelta(days=sessions * 2)
    price = base
    for day in range(sessions):
        session_start = start + timedelta(days=day * 2)
        while session_start.weekday() >= 5:
            session_start += timedelta(days=1)
        price *= 1 + rng.uniform(-0.006, 0.006)
        for index in range(13):
            timestamp = session_start + timedelta(minutes=index * 30)
            drift = math.sin((day * 13 + index) / 5.2) * 0.32 + rng.uniform(-0.44, 0.44)
            open_price = price
            close = max(1, price + drift)
            high = max(open_price, close) + rng.uniform(0.08, 0.32)
            low = min(open_price, close) - rng.uniform(0.08, 0.32)
            volume = int(rng.uniform(800_000, 2_600_000) * (1.8 if index in (0, 1, 12) else 1))
            bars.append(Bar(timestamp, open_price, high, low, close, volume))
            price = close
    return bars


def generate_crypto_demo_bars(ticker: str, sessions: int = 5) -> list[Bar]:
    seed = int(hashlib.sha256(f"crypto:{ticker.upper()}".encode()).hexdigest()[:8], 16)
    rng = random.Random(seed)
    base = {"BTC": 104_000.0, "ETH": 3_700.0, "SOL": 230.0}.get(ticker.upper(), 100.0)
    bars: list[Bar] = []
    start = datetime.now(timezone.utc).replace(minute=0, second=0, microsecond=0) - timedelta(hours=sessions * 24)
    price = base
    for index in range(sessions * 24):
        timestamp = start + timedelta(hours=index)
        drift = math.sin(index / 7.0) * base * 0.0018 + rng.uniform(-base * 0.003, base * 0.003)
        open_price = price
        close = max(0.01, price + drift)
        high = max(open_price, close) + rng.uniform(0, base * 0.0015)
        low = min(open_price, close) - rng.uniform(0, base * 0.0015)
        volume = int(rng.uniform(800, 6_000) * (1.8 if index % 24 in (0, 8, 16) else 1))
        bars.append(Bar(timestamp, open_price, high, low, close, volume))
        price = close
    return bars


def _parse_yahoo_bars(ticker: str, days: int = 5) -> tuple[list[Bar] | None, str | None]:
    from urllib.parse import urlencode
    from urllib.request import Request, urlopen
    import json

    params = urlencode({"range": f"{max(days, 1)}d", "interval": "30m", "includePrePost": "false", "events": "div,splits"})
    last_error = "unknown Yahoo response"
    for host in ("query1.finance.yahoo.com", "query2.finance.yahoo.com"):
        try:
            url = f"https://{host}/v8/finance/chart/{ticker.upper()}?{params}"
            request = Request(url, headers={"User-Agent": "Mozilla/5.0 (compatible; TPO-Market-Workbench/0.1)", "Accept": "application/json"})
            with urlopen(request, timeout=15) as response:
                payload = json.loads(response.read().decode("utf-8"))
            chart = payload.get("chart", {})
            if chart.get("error"):
                last_error = chart["error"].get("description", "Yahoo chart error")
                continue
            result = (chart.get("result") or [None])[0]
            if not result:
                last_error = "Yahoo returned no chart result"
                continue
            timestamps = result.get("timestamp", [])
            quote = result.get("indicators", {}).get("quote", [{}])[0]
            bars: list[Bar] = []
            for index, timestamp in enumerate(timestamps):
                values = [quote.get(key, [None] * len(timestamps))[index] for key in ("open", "high", "low", "close", "volume")]
                if any(value is None for value in values):
                    continue
                bars.append(Bar(datetime.fromtimestamp(timestamp, tz=timezone.utc), *values))
            if bars:
                return bars, None
            last_error = "Yahoo returned no usable bars"
        except Exception as error:
            last_error = f"{type(error).__name__}: {error}"
    return None, last_error


def _parse_binance_bars(ticker: str, days: int = 5) -> tuple[list[Bar], list[float]] | None:
    try:
        from urllib.parse import urlencode
        from urllib.request import Request, urlopen
        import json

        symbol = ticker.upper().replace("-USD", "") + "USDT"
        params = urlencode({"symbol": symbol, "interval": "1h", "limit": min(days * 24, 1000)})
        request = Request(f"https://api.binance.com/api/v3/klines?{params}", headers={"User-Agent": "tpo-market-workbench/0.1"})
        with urlopen(request, timeout=8) as response:
            payload = json.loads(response.read().decode("utf-8"))
        bars: list[Bar] = []
        deltas: list[float] = []
        for row in payload:
            open_price, high, low, close, volume = map(float, (row[1], row[2], row[3], row[4], row[5]))
            taker_buy_volume = float(row[9])
            bars.append(Bar(datetime.fromtimestamp(row[0] / 1000, tz=timezone.utc), open_price, high, low, close, int(volume), 2 * taker_buy_volume - volume))
        return bars if bars else None
    except Exception:
        return None


def load_bars(ticker: str, days: int = 5, market: str = "us") -> tuple[list[Bar], str]:
    if market == "crypto":
        live_bars = _parse_binance_bars(ticker, days)
        if live_bars:
            return live_bars, "Binance spot 1h klines"
        return generate_crypto_demo_bars(ticker, days), "Synthetic crypto demo tape (Binance unavailable)"
    live_bars, yahoo_error = _parse_yahoo_bars(ticker, days)
    if live_bars:
        return live_bars, "Yahoo Finance delayed data"
    return generate_demo_bars(ticker, days), f"Synthetic demo tape (Yahoo unavailable: {yahoo_error})"


def _session_label(timestamp: datetime) -> str:
    return timestamp.date().isoformat()


def _period_letter(index: int) -> str:
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    return alphabet[index % len(alphabet)]


def calculate_profile(bars: list[Bar], ticker: str, source: str, tick_size: float = 0.5, market: str = "us") -> dict[str, Any]:
    if not bars:
        raise ValueError("No bars available")
    if market == "crypto":
        tick_size = max(tick_size, bars[-1].close * 0.0005)
    levels: dict[float, list[str]] = {}
    volumes: dict[float, int] = {}
    session_names: list[str] = []
    session_map: dict[str, list[Bar]] = {}
    for bar in bars:
        label = _session_label(bar.timestamp)
        session_map.setdefault(label, []).append(bar)
        if label not in session_names:
            session_names.append(label)
    for label in session_names:
        for bar_index, bar in enumerate(session_map[label]):
            letter = _period_letter(bar_index)
            low = math.floor(bar.low / tick_size) * tick_size
            high = math.ceil(bar.high / tick_size) * tick_size
            level = low
            while level <= high + 0.0001:
                level = _round_tick(level, tick_size)
                levels.setdefault(level, []).append(letter)
                volumes[level] = volumes.get(level, 0) + int(bar.volume / max(1, round((high - low) / tick_size) + 1))
                level += tick_size
    sorted_levels = sorted(levels)
    total_tpo = sum(len(value) for value in levels.values())
    poc = max(sorted_levels, key=lambda level: (len(levels[level]), level))
    target = total_tpo * 0.70
    included = {poc}
    total = len(levels[poc])
    while total < target and (min(included) > sorted_levels[0] or max(included) < sorted_levels[-1]):
        lower = next((level for level in reversed(sorted_levels) if level < min(included)), None)
        upper = next((level for level in sorted_levels if level > max(included)), None)
        lower_count = len(levels[lower]) if lower is not None else -1
        upper_count = len(levels[upper]) if upper is not None else -1
        chosen = upper if upper_count > lower_count else lower
        if chosen is None:
            break
        included.add(chosen)
        total += len(levels[chosen])
    val, vah = min(included), max(included)
    current = bars[-1].close
    opening = bars[0].open
    delta = current - opening
    last_session = session_names[-1]
    last_bars = session_map[last_session]
    ib_bars = last_bars[:2]
    ib_high = max(bar.high for bar in ib_bars)
    ib_low = min(bar.low for bar in ib_bars)
    last_session_high = max(bar.high for bar in last_bars)
    last_session_low = min(bar.low for bar in last_bars)
    indicators = calculate_vwap_cvd(bars, market)
    return {
        "ticker": ticker.upper(),
        "source": source,
        "bars": len(bars),
        "sessions": len(session_names),
        "last_updated": bars[-1].timestamp.isoformat(),
        "current_price": round(current, 2),
        "change": round(delta, 2),
        "change_pct": round(delta / opening * 100, 2),
        "profile": [
            {"price": round(level, 2), "tpo": len(levels[level]), "letters": "".join(levels[level]), "volume": volumes[level]}
            for level in reversed(sorted_levels)
        ],
        "levels": {"poc": round(poc, 2), "vah": round(vah, 2), "val": round(val, 2), "ib_high": round(ib_high, 2), "ib_low": round(ib_low, 2), "session_high": round(last_session_high, 2), "session_low": round(last_session_low, 2)},
        "sessions_detail": [
            {"date": label, "high": round(max(bar.high for bar in session_map[label]), 2), "low": round(min(bar.low for bar in session_map[label]), 2), "close": round(session_map[label][-1].close, 2), "volume": sum(bar.volume for bar in session_map[label])}
            for label in session_names
        ],
        "read": _build_read(current, poc, vah, val, ib_high, ib_low),
        "market": market,
        "indicators": indicators,
    }


def calculate_vwap_cvd(bars: list[Bar], market: str) -> dict[str, Any]:
    cumulative_delta = 0.0
    cumulative_pv = 0.0
    cumulative_volume = 0.0
    series = []
    for index, bar in enumerate(bars):
        typical_price = (bar.high + bar.low + bar.close) / 3
        cumulative_pv += typical_price * bar.volume
        cumulative_volume += bar.volume
        delta = bar.delta if bar.delta is not None else (bar.volume if bar.close >= bar.open else -bar.volume)
        cumulative_delta += delta
        series.append({"time": bar.timestamp.isoformat(), "price": round(bar.close, 6), "vwap": round(cumulative_pv / cumulative_volume, 6), "cvd": round(cumulative_delta, 2), "delta": round(delta, 2)})
    previous = series[-2] if len(series) > 1 else series[-1]
    current = series[-1]
    price_above = current["price"] >= current["vwap"]
    cvd_rising = current["cvd"] >= previous["cvd"]
    if price_above and cvd_rising:
        signal = "Bullish confirmation"
        detail = "Price is above VWAP and CVD is rising. Look for pullbacks that hold VWAP."
        tone = "bullish"
    elif not price_above and not cvd_rising:
        signal = "Bearish confirmation"
        detail = "Price is below VWAP and CVD is falling. Watch failed VWAP reclaims."
        tone = "bearish"
    else:
        signal = "Mixed pressure"
        detail = "Price and order-flow pressure disagree. Wait for VWAP and CVD to align."
        tone = "mixed"
    return {
        "vwap": current["vwap"],
        "cvd": current["cvd"],
        "cvd_change": round(current["cvd"] - previous["cvd"], 2),
        "signal": signal,
        "detail": detail,
        "tone": tone,
        "mode": "estimated from candle direction" if market == "us" else "Binance taker-buy volume",
        "series": series,
    }


def _build_read(current: float, poc: float, vah: float, val: float, ib_high: float, ib_low: float) -> dict[str, str]:
    if current > vah:
        posture = "Above value"
        detail = "Price is accepting above the value area. Watch whether the prior VAH becomes support or price rotates back into value."
        tone = "expansion"
    elif current < val:
        posture = "Below value"
        detail = "Price is trading below the value area. A reclaim of VAL would be the first sign of rotation back toward accepted prices."
        tone = "rejection"
    else:
        posture = "Inside value"
        detail = "Price is rotating inside accepted value. The cleanest read is usually a break and hold beyond VAH or VAL."
        tone = "balance"
    return {"posture": posture, "detail": detail, "tone": tone, "ib": f"Initial balance {ib_low:.2f} – {ib_high:.2f}", "poc": f"POC at {poc:.2f}"}
