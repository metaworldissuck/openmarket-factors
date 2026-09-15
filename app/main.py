from pathlib import Path
from fastapi import FastAPI, Query
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from .tpo_engine import calculate_profile, load_bars

ROOT = Path(__file__).resolve().parent.parent
app = FastAPI(title="TPO Market Workbench")
app.mount("/static", StaticFiles(directory=ROOT / "static"), name="static")


@app.get("/", include_in_schema=False)
def index() -> FileResponse:
    return FileResponse(ROOT / "templates" / "index.html")


@app.get("/api/analyze")
def analyze(
    ticker: str = Query("AAPL", min_length=1, max_length=12),
    market: str = Query("us", pattern="^(us|crypto)$"),
    days: int = Query(5, ge=1, le=30),
    tick_size: float = Query(0.5, gt=0, le=20),
):
    bars, source = load_bars(ticker.upper(), days, market)
    return calculate_profile(bars, ticker.upper(), source, tick_size, market)
