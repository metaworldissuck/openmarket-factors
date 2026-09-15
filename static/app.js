const form = document.querySelector('#analyzeForm');
const marketInput = document.querySelector('#market');
const tickerInput = document.querySelector('#ticker');
const daysInput = document.querySelector('#days');
const tickSizeInput = document.querySelector('#tickSize');
const analyzeButton = document.querySelector('#analyzeButton');
const instrumentNames = { AAPL: 'Apple Inc.', MSFT: 'Microsoft Corp.', NVDA: 'NVIDIA Corp.', TSLA: 'Tesla Inc.', AMZN: 'Amazon.com Inc.' };
const cryptoNames = { BTC: 'Bitcoin', ETH: 'Ethereum', SOL: 'Solana' };

const money = value => Number(value).toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
const compact = value => new Intl.NumberFormat('en-US', { notation: 'compact', maximumFractionDigits: 1 }).format(value);

function setText(id, value) { document.querySelector(`#${id}`).textContent = value; }

function metric(value, digits = 2) { return Number(value).toLocaleString('en-US', { maximumFractionDigits: digits }); }

function renderIndicatorChart(indicators) {
  const host = document.querySelector('#indicatorChart');
  const series = indicators.series;
  const width = 820;
  const height = 220;
  const pad = { top: 14, right: 12, bottom: 18, left: 12 };
  const prices = series.flatMap(point => [point.price, point.vwap]);
  const priceMin = Math.min(...prices);
  const priceMax = Math.max(...prices);
  const cvdValues = series.map(point => point.cvd);
  const cvdMin = Math.min(...cvdValues, 0);
  const cvdMax = Math.max(...cvdValues, 0);
  const x = index => pad.left + (index / Math.max(1, series.length - 1)) * (width - pad.left - pad.right);
  const scale = (value, min, max, top, bottom) => bottom - ((value - min) / Math.max(0.000001, max - min)) * (bottom - top);
  const priceY = value => scale(value, priceMin, priceMax, pad.top, 126);
  const cvdY = value => scale(value, cvdMin, cvdMax, 148, height - pad.bottom);
  const path = (key, transform) => series.map((point, index) => `${index ? 'L' : 'M'}${x(index).toFixed(2)},${transform(point[key]).toFixed(2)}`).join(' ');
  const zeroY = cvdY(0);
  host.innerHTML = `<svg class="indicator-svg" viewBox="0 0 ${width} ${height}" preserveAspectRatio="none" aria-label="VWAP and CVD signal chart"><line x1="${pad.left}" y1="${zeroY}" x2="${width - pad.right}" y2="${zeroY}" stroke="#2a3935"/><path d="${path('cvd', cvdY)}" fill="none" stroke="#ff8068" stroke-width="2"/><path d="${path('price', priceY)}" fill="none" stroke="#d6f36b" stroke-width="2"/><path d="${path('vwap', priceY)}" fill="none" stroke="#8de4d2" stroke-width="2" stroke-dasharray="5 4"/><text x="${pad.left}" y="12" fill="#8e9c99" font-size="10">price / VWAP</text><text x="${pad.left}" y="145" fill="#8e9c99" font-size="10">CVD</text></svg>`;
}

function updateMarketCopy() {
  const crypto = marketInput.value === 'crypto';
  if ((crypto && ['AAPL', 'MSFT', 'NVDA', 'TSLA', 'AMZN'].includes(tickerInput.value)) || (!crypto && ['BTC', 'ETH', 'SOL'].includes(tickerInput.value))) tickerInput.value = crypto ? 'BTC' : 'AAPL';
  document.querySelector('#marketKicker').textContent = crypto ? 'Market structure / crypto spot' : 'Market structure / US equities';
  document.querySelector('#ticker').placeholder = crypto ? 'BTC' : 'AAPL';
  document.querySelector('#tickSize').value = crypto ? '1' : '0.5';
}

function renderProfile(data) {
  const host = document.querySelector('#profileChart');
  const rows = data.profile;
  const maxTpo = Math.max(...rows.map(row => row.tpo));
  const maxVolume = Math.max(...rows.map(row => row.volume));
  const width = 820;
  const height = 460;
  const top = 14;
  const bottom = 20;
  const plotHeight = height - top - bottom;
  const rowHeight = Math.max(7, Math.min(18, plotHeight / rows.length));
  const x0 = 96;
  const chartWidth = 570;
  const value = data.levels;
  const grid = [];
  const labels = [];
  rows.forEach((row, index) => {
    const y = top + index * rowHeight;
    const isPoc = Math.abs(row.price - value.poc) < 0.001;
    const inValue = row.price <= value.vah && row.price >= value.val;
    const inIb = row.price <= value.ib_high && row.price >= value.ib_low;
    const tpoWidth = (row.tpo / maxTpo) * chartWidth;
    const volumeWidth = (row.volume / maxVolume) * 96;
    const fill = isPoc ? '#d6f36b' : inValue ? '#8de4d2' : '#536b64';
    const opacity = isPoc ? 1 : inValue ? .8 : .47;
    const levelMark = isPoc ? 'POC' : row.price === value.vah ? 'VAH' : row.price === value.val ? 'VAL' : '';
    grid.push(`<line x1="${x0}" y1="${y + rowHeight / 2}" x2="${x0 + chartWidth + 115}" y2="${y + rowHeight / 2}" stroke="#253531" stroke-width="1" opacity=".55"/>`);
    grid.push(`<rect x="${x0}" y="${y + 1}" width="${tpoWidth}" height="${Math.max(4, rowHeight - 2)}" fill="${fill}" opacity="${opacity}"/>`);
    grid.push(`<rect x="${x0 + chartWidth + 14}" y="${y + 2}" width="${volumeWidth}" height="${Math.max(2, rowHeight - 4)}" fill="#ff8068" opacity=".4"/>`);
    grid.push(`<text x="${x0 + 8}" y="${y + rowHeight / 2 + 3.5}" fill="#16221f" font-size="${Math.max(8, rowHeight - 3)}" font-family="DM Sans, sans-serif" font-weight="700">${row.letters}</text>`);
    labels.push(`<text x="${x0 - 12}" y="${y + rowHeight / 2 + 4}" text-anchor="end" fill="${isPoc ? '#d6f36b' : '#8e9c99'}" font-size="11" font-family="DM Sans, sans-serif">${money(row.price)}</text>`);
    if (levelMark) labels.push(`<text x="${x0 + chartWidth + 123}" y="${y + rowHeight / 2 + 4}" fill="${isPoc ? '#d6f36b' : '#8de4d2'}" font-size="9" font-family="DM Sans, sans-serif">${levelMark}</text>`);
    if (inIb && index % 2 === 0) grid.push(`<rect x="${x0 - 5}" y="${y}" width="${chartWidth + 5}" height="${rowHeight}" fill="#ff8068" opacity=".035"/>`);
  });
  const title = `<text x="${x0}" y="${height - 3}" fill="#64716f" font-size="9" font-family="DM Sans, sans-serif">TPO letters / 30-minute periods</text><text x="${x0 + chartWidth + 14}" y="${height - 3}" fill="#64716f" font-size="9" font-family="DM Sans, sans-serif">relative volume</text>`;
  host.innerHTML = `<svg class="profile-svg" viewBox="0 0 ${width} ${height}" preserveAspectRatio="none" aria-label="TPO profile for ${data.ticker}">${grid.join('')}${labels.join('')}${title}</svg>`;
  setText('profileSummary', `${rows.length} price levels · ${rows.reduce((sum, row) => sum + row.tpo, 0)} TPO prints`);
}

function render(data) {
  const ticker = data.ticker;
  const crypto = data.market === 'crypto';
  setText('tickerBadge', ticker);
  setText('instrumentName', (crypto ? cryptoNames[ticker] : instrumentNames[ticker]) || `${ticker} market profile`);
  setText('venueLine', crypto ? 'Crypto spot / 24 hour market' : 'NYSE / Regular trading hours');
  setText('currentPrice', `${crypto ? '$' : '$'}${money(data.current_price)}`);
  const change = `${data.change >= 0 ? '+' : ''}${money(data.change)} (${data.change_pct >= 0 ? '+' : ''}${data.change_pct}%)`;
  const changeNode = document.querySelector('#changeValue');
  changeNode.textContent = change;
  changeNode.className = `change ${data.change >= 0 ? 'positive' : 'negative'}`;
  setText('postureValue', data.read.posture);
  setText('postureDetail', data.read.detail);
  setText('sourceLabel', data.source);
  setText('updatedLabel', `updated ${new Date(data.last_updated).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}`);
  setText('pocValue', `$${money(data.levels.poc)}`);
  setText('vahValue', `$${money(data.levels.vah)}`);
  setText('valValue', `$${money(data.levels.val)}`);
  setText('ibHighValue', `$${money(data.levels.ib_high)}`);
  setText('ibLowValue', `$${money(data.levels.ib_low)}`);
  setText('thesisText', `${data.read.poc}. ${data.read.ib} Current read: ${data.read.posture.toLowerCase()}.`);
  setText('sessionCount', `${data.sessions} sessions`);
  document.querySelector('#sessionRows').innerHTML = data.sessions_detail.map(session => `<tr><td>${session.date}</td><td>$${money(session.high)}</td><td>$${money(session.low)}</td><td>$${money(session.close)}</td><td>${compact(session.volume)}</td></tr>`).join('');
  renderProfile(data);
  const indicators = data.indicators;
  setText('vwapValue', `$${metric(indicators.vwap)}`);
  setText('cvdValue', metric(indicators.cvd));
  setText('cvdChange', `${indicators.cvd_change >= 0 ? '+' : ''}${metric(indicators.cvd_change)}`);
  setText('indicatorMode', indicators.mode);
  setText('signalValue', indicators.signal);
  setText('signalDetail', indicators.detail);
  document.querySelector('#signalBox').className = `signal-box ${indicators.tone}`;
  renderIndicatorChart(indicators);
}

async function analyze(event) {
  event?.preventDefault();
  const ticker = tickerInput.value.trim().toUpperCase();
  if (!ticker) return;
  tickerInput.value = ticker;
  analyzeButton.disabled = true;
  analyzeButton.textContent = 'Loading...';
  setText('sourceLabel', `Loading ${ticker} profile`);
  setText('postureDetail', 'Fetching market data and calculating VWAP / CVD');
  try {
    const params = new URLSearchParams({ ticker, market: marketInput.value, days: daysInput.value, tick_size: tickSizeInput.value });
    const response = await fetch(`/api/analyze?${params}`);
    if (!response.ok) throw new Error('Profile unavailable');
    render(await response.json());
  } catch (error) {
    setText('sourceLabel', 'Profile unavailable');
    setText('postureDetail', `Unable to load ${ticker}. Check the symbol or try again.`);
    setText('signalValue', 'No data');
    setText('signalDetail', 'The market request failed or timed out.');
    document.querySelector('#signalBox').className = 'signal-box mixed';
  } finally {
    analyzeButton.disabled = false;
    analyzeButton.textContent = 'Analyze';
  }
}

form.addEventListener('submit', analyze);
marketInput.addEventListener('change', updateMarketCopy);
updateMarketCopy();
analyze();
