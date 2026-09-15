# TPO Market Workbench

A small US equities market analysis tool based on Time Price Opportunity (TPO) theory.

## Run with uv and Python 3.14

```bash
uv sync
uv run uvicorn app.main:app --reload
```

Open http://127.0.0.1:8000.

## Deploy on Render

Use the following settings for a Render Web Service:

- Build Command: `uv sync --frozen && uv cache prune --ci`
- Start Command: `uv run uvicorn app.main:app --host 0.0.0.0 --port $PORT`
- Health Check Path: `/`

The same settings are included in `render.yaml` for Blueprint deployments.

The app attempts to load delayed 30-minute Yahoo Finance bars. If the network request is unavailable, it uses deterministic demo bars so the TPO workstation remains usable.

## What it computes

- TPO profile by price level
- Point of Control (POC)
- Value Area High / Low using a 70% TPO rule
- Initial Balance from the first two 30-minute bars
- Session range and a plain-language market posture
