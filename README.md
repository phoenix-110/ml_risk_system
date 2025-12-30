# Quant Trading Platform – Volatility-Focused Backtesting System

## Overview

This project is a **modular quantitative trading research and backtesting platform** focused on **volatility-driven strategies**, particularly those based on the VIX.

The system is designed with **clean separation of concerns**, **reproducibility**, and **realistic risk management**, following principles used in professional trading and research environments.

Key goals:
- Deterministic, reproducible backtests
- Clear separation between research, execution, and evaluation
- Extensible architecture for new strategies and data sources

---

## High-Level Architecture

```
data/        → Data ingestion & persistence (FRED, SQLite)
analysis/    → Research & diagnostics (volatility regimes, IV structure)
backtest/    → Strategy execution, risk, portfolio accounting
reports/     → Generated outputs (CSV / JSON / charts / HTML)
```

**Design Principle**

> Strategies express intent.  
> The engine executes.  
> Risk gates everything.  
> Metrics are pure functions.

---

## Data Layer (`data/`)

### VIX Data Source
- Source: FRED (`VIXCLS`)
- Reason: Stable, academic-grade volatility data
- Fetcher: `VIXFetcher` (stateless)
- Storage: SQLite via `TimeSeriesDB`

Properties:
- Fetchers are stateless and return normalized DataFrames
- Database writes are idempotent (`INSERT OR IGNORE`)
- Backtests are fully reproducible

---

## Research Layer (`analysis/`)

The `volatility_analysis.py` module is used for **research and diagnostics**, not execution.

It includes:
- VIX percentile analysis
- Volatility regime classification
- Term structure interpretation
- Strategy suitability signals (long-vol vs short-vol environments)

---

## Backtesting Engine (`backtest/`)

Execution flow:

```
Historical Data
      ↓
Strategy (intent)
      ↓
Risk Manager
      ↓
Portfolio (execution & accounting)
      ↓
Metrics Engine
      ↓
Reports
```

### Strategy Abstraction

Strategies implement:

```
on_bar(row, portfolio, context)
```

They return either:
- `None`, or
- `(symbol, qty, price)`

Strategies never execute trades directly.

---

## Risk Management

Centralized in `RiskManager`:
- Max position size
- Max drawdown (hard stop)
- Max leverage

All strategies are subject to the same risk constraints.

---

## Portfolio Accounting

The `Portfolio` class handles:
- Cash & positions
- Realized / unrealized PnL
- Equity curve
- Drawdowns & leverage

All accounting is mark-to-market.

---

## Metrics

Computed via `MetricsEngine`:
- Sharpe Ratio
- Sortino Ratio
- Max Drawdown
- Calmar Ratio
- Win Rate
- Profit Factor

Metrics are pure functions of portfolio state.

---

## Example Usage

```python
engine = BacktestEngine(initial_capital=100_000)
strategy = VIXLongVolStrategy()

portfolio, results = engine.run_with_strategy(strategy, days_back=252)

engine.generate_reports(
    portfolio,
    strategy_name=strategy.name,
    generate_charts=True
)
```

---

## Design Philosophy

- Reproducibility over live data
- Risk-first execution
- Clear separation of concerns
- Minimal but realistic assumptions

---

## Disclaimer

This project is for educational and research purposes only.
