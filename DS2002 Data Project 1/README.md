# DS2002 Data Project 1 – Cryptocurrency, Market Sentiment & Macro Factor ETL Pipeline by Anish Jagota

## Project Overview

This project implements a full ETL (Extract, Transform, Load) pipeline to analyze the relationship between **cryptocurrency market movements** and both **market sentiment** (via the Fear & Greed Index) and **macroeconomic indicators** (Gold, Oil, S&P 500 ETFs).  
It involves ingesting multi-source time series data, transforming it to a common structure, storing results in multiple formats, and analyzing correlations across different financial metrics.

## Folder Structure
DS2002 Data Project 1/
├── code.ipynb               # Main Jupyter Notebook
├── reflection.pdf           # Final reflection write-up
├── README.md                # This file
├── data/                    # Raw local CSVs
│   ├── ETHUSDT.csv
│   ├── DOGEUSDT.csv
│   └── SOLUSDT.csv


---

## ETL Pipeline Breakdown

### 1. **Data Ingestion**
- **Sentiment API:**  
  - Fetched daily Fear & Greed Index using [alternative.me](https://alternative.me/crypto/fear-and-greed-index/) API (JSON).
- **Macroeconomic API:**  
  - Retrieved Gold (GLD), Oil (USO), and S&P 500 (SPY) ETF prices from Yahoo Finance API (JSON).
- **Local CSVs:**  
  - Historical minute level crypto data for ETH, DOGE, SOL (from [Kaggle] (https://www.kaggle.com/datasets/kaanxtr/btc-price-1m)).

### 2. **Data Transformation**
- Floored crypto timestamps to daily using `.dt.floor('d')`.
- Aggregated OHLCV metrics by day (first open, last close, min low, max high, volume sum).
- Computed:
  - Daily percent change in price
  - Volatility metric: `(high - low) / open`
  - Lagged sentiment index (for next-day impact analysis)
  - Sentiment percent change

### 3. **Data Merging**
- Merged:
  - Crypto daily data with Fear & Greed sentiment (on date)
  - Crypto with macro ETFs using `pd.merge_asof()` (tolerance = 1 day)

### 4. **Data Storage**
- Saved transformed data in:
  - `.csv`
  - `.json`
  - `.sqlite` (using `sqlite3` and `pandas.to_sql()`)

---

## Correlation Metrics

For each cryptocurrency, correlation matrices were generated to analyze relationships between:

- **`fear_greed_index`** vs **`pct_change`**  
  → "Does price rise or fall based on sentiment levels?"

- **`sentiment_pct_change`** vs **`pct_change`**, **`volatility`**  
  → "Do rapid shifts in sentiment trigger volatility?"

- **`lagged_sentiment`** vs **`pct_change`**  
  → "Does yesterday’s sentiment influence today’s price?"

- **`pct_change`** vs **macroeconomic_pct_change**  
  → "Do crypto prices track broader financial indicators?"

---

## How to Use This Project

### Prerequisites
- Python 3.7+
- Libraries: `pandas`, `requests`, `matplotlib`, `sqlite3`
- Internet connection (for API access)

### Run Instructions
1. Open `code.ipynb` in Jupyter Notebook or Colab.
2. Upload the following local files:
   - `ETHUSDT.csv`, `DOGEUSDT.csv`, `SOLUSDT.csv`
3. Replace `API_KEY` with your personal Yahoo Finance API key.
4. Run all cells in order.

---

## Key Outputs

- Correlation coefficients for sentiment, price, and volatility.
- Clean merged datasets stored in CSV, JSON, and SQLite.
- Line plots showing Fear & Greed Index vs price change.

---

## Reflection

A detailed summary of:
- Overview
- Challenges encountered
- Design decisions
- Insights from correlation analysis
- Real-world utility of the pipeline

---





