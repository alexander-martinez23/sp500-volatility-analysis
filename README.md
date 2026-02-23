# Cross-Sectional Volatility & Market Stress Analysis

## Overview

This project analyzes 25+ years of historical S&P 500 constituent data (~2.7 million stock-day observations) to study market volatility dynamics and systemic stress behavior.

The analysis focuses on:

- Daily return construction across multiple equities  
- Rolling volatility modeling to examine risk clustering  
- Cross-sectional dispersion as a measure of systemic market stress  
- Extreme tail events (< -10% daily returns)  
- Volatility regime comparison (pre- and post-2008 financial crisis)

---

## Dataset

The dataset contains daily historical price data for S&P 500 constituent stocks over 25+ years.

Each row represents one stock on one trading day and includes:

- Ticker  
- Date  
- Open  
- High  
- Low  
- Close  
- Adjusted Close  
- Volume  

Due to licensing and size constraints, the dataset is not included in this repository.

To run this project, provide a CSV file named:

with the columns listed above.

---

## Methodology

### 1. Return Engineering
- Computed daily percentage returns using adjusted close prices  
- Applied grouped calculations by ticker to preserve panel data structure  

### 2. Volatility Modeling
- Estimated 30-day rolling volatility per asset  
- Measured yearly return standard deviation  

### 3. Cross-Sectional Dispersion
- Calculated daily standard deviation of returns across all tickers  
- Used dispersion spikes as indicators of systemic stress  

### 4. Tail Risk Analysis
- Identified extreme crash days (< -10% returns)  
- Aggregated crash frequency by year  

### 5. Regime Comparison
- Compared overall volatility before and after 2008  
- Examined structural shifts in market risk dynamics  

---

## Key Findings

- Cross-sectional volatility spikes during major crises (e.g., 2008 Global Financial Crisis, 2020 COVID-19 shock)  
- Extreme crash events cluster during systemic stress periods  
- Post-2008 volatility remains structurally elevated relative to earlier years  
- Rolling volatility demonstrates risk clustering behavior consistent with financial theory  

---

## Technologies Used

- Python  
- Pandas (groupby operations, rolling statistics, time-series processing)  
- NumPy  
- Matplotlib  

---

## How to Run

1. Install required packages: "pip install pandas numpy matplotlib"
2. Place "SP500_USA.csv" in the project directory
3. Run: "python analysis.py"
