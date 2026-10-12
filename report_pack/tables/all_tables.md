# All the tables of the report pack

Created by `notebooks/05_report_pack.ipynb` from the files in `results/`. Rounded for the report; the exact values are in `results/` and in `report_tables.xlsx`.

## T01. Investment universe: 23 S&P 500 stocks and SPY, 2010-2026

*Report section: 1. Investment universe and data*

| Ticker | Sector | First date | Ann. return (CAGR) | Ann. volatility | Max drawdown | Avg. correlation with the other stocks |
|---|---|---|---|---|---|---|
| NVDA | Information Technology | 2010-01-05 | 45.6% | 45.4% | -66.3% | 0.35 |
| AAPL | Information Technology | 2010-01-05 | 26.8% | 28.1% | -43.8% | 0.38 |
| MSFT | Information Technology | 2010-01-05 | 20.2% | 26.1% | -37.1% | 0.40 |
| AVGO | Information Technology | 2010-01-05 | 39.9% | 38.3% | -48.3% | 0.35 |
| AMD | Information Technology | 2010-01-05 | 27.5% | 56.9% | -84.1% | 0.30 |
| MU | Information Technology | 2010-01-05 | 31.5% | 50.7% | -73.8% | 0.33 |
| BRK-B | Financials | 2010-01-05 | 13.0% | 19.2% | -29.6% | 0.44 |
| JPM | Financials | 2010-01-05 | 16.3% | 27.4% | -43.6% | 0.41 |
| V | Financials | 2010-01-05 | 19.3% | 24.8% | -36.4% | 0.40 |
| LLY | Health Care | 2010-01-05 | 26.3% | 26.7% | -34.5% | 0.25 |
| JNJ | Health Care | 2010-01-05 | 12.2% | 17.1% | -27.4% | 0.31 |
| AMZN | Consumer Discretionary | 2010-01-05 | 24.4% | 32.9% | -56.1% | 0.33 |
| TSLA | Consumer Discretionary | 2010-06-30 | 39.9% | 57.3% | -73.6% | 0.25 |
| T | Communication Services | 2010-01-05 | 8.4% | 21.0% | -39.4% | 0.28 |
| GOOGL | Communication Services | 2010-01-05 | 20.5% | 27.9% | -44.3% | 0.38 |
| GE | Industrials | 2010-01-05 | 11.2% | 31.6% | -81.2% | 0.35 |
| CAT | Industrials | 2010-01-05 | 19.9% | 29.9% | -44.6% | 0.38 |
| WMT | Consumer Staples | 2010-01-05 | 13.5% | 20.0% | -36.4% | 0.26 |
| COST | Consumer Staples | 2010-01-05 | 20.1% | 20.3% | -31.4% | 0.34 |
| XOM | Energy | 2010-01-05 | 9.3% | 25.0% | -62.4% | 0.32 |
| NEE | Utilities | 2010-01-05 | 14.7% | 22.3% | -45.0% | 0.28 |
| WELL | Real Estate | 2010-01-05 | 15.1% | 28.3% | -63.3% | 0.29 |
| LIN | Materials | 2010-01-05 | 13.0% | 21.2% | -32.6% | 0.41 |
| SPY | ETF (benchmark) | 2010-01-05 | 14.1% | 17.1% | -33.7% |  |

Note: Daily adjusted close prices from Yahoo Finance, 4 Jan 2010 - 18 Sep 2026. TSLA starts on 30 Jun 2010 (IPO). CAGR, volatility and maximum drawdown are computed on simple returns over the full sample.

## T02. Descriptive statistics of WMT and SPY log returns at three frequencies

*Report section: 2.1 Stylised facts*

| Asset | Frequency | N | Mean | Std. dev. | Min | Max | Skewness | Excess kurtosis | Ann. mean | Ann. volatility |
|---|---|---|---|---|---|---|---|---|---|---|
| WMT | Daily | 4202 | 0.05% | 1.26% | -12.08% | 11.07% | -0.255 | 14.32 | 12.7% | 20.0% |
| WMT | Weekly | 871 | 0.24% | 2.73% | -21.67% | 10.93% | -0.853 | 6.67 | 12.7% | 19.7% |
| WMT | Monthly | 199 | 1.06% | 5.17% | -16.98% | 13.78% | -0.360 | 0.84 | 12.7% | 17.9% |
| SPY | Daily | 4202 | 0.05% | 1.08% | -11.59% | 9.99% | -0.555 | 12.40 | 13.2% | 17.1% |
| SPY | Weekly | 871 | 0.25% | 2.24% | -15.72% | 11.41% | -0.740 | 5.83 | 13.1% | 16.2% |
| SPY | Monthly | 199 | 1.14% | 4.13% | -13.34% | 11.95% | -0.491 | 0.67 | 13.6% | 14.3% |

Note: Log returns from adjusted close prices. Weekly and monthly returns use period-end prices. Excess kurtosis = kurtosis - 3 (0 for a normal distribution).

## T03. Summary: is each stylised fact supported for WMT?

*Report section: 2.1 Stylised facts (summary)*

| Fact | Daily | Weekly | Monthly |
|---|---|---|---|
| 1. Little serial correlation | Supported (significant but tiny) | Supported | Supported |
| 2. Non-normal, fat tails | Supported | Supported | Supported |
| 3. Negative skewness | Not significant | Supported | Not significant |
| 4. Volatility clustering | Supported | Partial | Not supported |
| 5. Leverage effect | Supported | Not significant | Not significant |
| 6. Conditional non-normality | Supported | Supported | Supported |

Note: Based on the tests of tables T04-T12 (5% significance level).

## T04. Evidence for each stylised fact: statistic, p-value and conclusion (WMT, with SPY for comparison)

*Report section: 2.1 Stylised facts (summary)*

| Asset | Frequency | Fact | Statistic | p-value | Conclusion |
|---|---|---|---|---|---|
| WMT | Daily | 1. Little serial correlation | max \|ACF(1-5)\| = 0.041 | 0.001 | Supported (significant but tiny) |
| WMT | Daily | 2. Non-normal, fat tails | excess kurtosis = 14.32 | <0.001 | Supported |
| WMT | Daily | 3. Negative skewness | skewness = -0.255 | 0.273 | Not significant |
| WMT | Daily | 4. Volatility clustering | LB \|r\| p = 0.000 | <0.001 | Supported |
| WMT | Daily | 5. Leverage effect | gamma = 0.071 | 0.006 | Supported |
| WMT | Daily | 6. Conditional non-normality | z excess kurtosis = 15.67 | <0.001 | Supported |
| WMT | Weekly | 1. Little serial correlation | max \|ACF(1-5)\| = 0.095 | 0.141 | Supported |
| WMT | Weekly | 2. Non-normal, fat tails | excess kurtosis = 6.67 | <0.001 | Supported |
| WMT | Weekly | 3. Negative skewness | skewness = -0.853 | 0.026 | Supported |
| WMT | Weekly | 4. Volatility clustering | LB \|r\| p = 0.000 | 0.188 | Partial |
| WMT | Weekly | 5. Leverage effect | gamma = 0.001 | 0.979 | Not significant |
| WMT | Weekly | 6. Conditional non-normality | z excess kurtosis = 7.13 | <0.001 | Supported |
| WMT | Monthly | 1. Little serial correlation | max \|ACF(1-5)\| = 0.070 | 0.658 | Supported |
| WMT | Monthly | 2. Non-normal, fat tails | excess kurtosis = 0.84 | 0.006 | Supported |
| WMT | Monthly | 3. Negative skewness | skewness = -0.360 | 0.083 | Not significant |
| WMT | Monthly | 4. Volatility clustering | LB \|r\| p = 0.848 | 0.672 | Not supported |
| WMT | Monthly | 5. Leverage effect | gamma = 0.000 | 1.000 | Not significant |
| WMT | Monthly | 6. Conditional non-normality | z excess kurtosis = 0.66 | 0.029 | Supported |
| SPY | Daily | 1. Little serial correlation | max \|ACF(1-5)\| = 0.100 | <0.001 | Not supported |
| SPY | Daily | 2. Non-normal, fat tails | excess kurtosis = 12.40 | <0.001 | Supported |
| SPY | Daily | 3. Negative skewness | skewness = -0.555 | 0.113 | Not significant |
| SPY | Daily | 4. Volatility clustering | LB \|r\| p = 0.000 | <0.001 | Supported |
| SPY | Daily | 5. Leverage effect | gamma = 0.281 | <0.001 | Supported |
| SPY | Daily | 6. Conditional non-normality | z excess kurtosis = 3.17 | <0.001 | Supported |
| SPY | Weekly | 1. Little serial correlation | max \|ACF(1-5)\| = 0.089 | 0.024 | Supported (significant but tiny) |
| SPY | Weekly | 2. Non-normal, fat tails | excess kurtosis = 5.83 | <0.001 | Supported |
| SPY | Weekly | 3. Negative skewness | skewness = -0.740 | 0.029 | Supported |
| SPY | Weekly | 4. Volatility clustering | LB \|r\| p = 0.000 | <0.001 | Supported |
| SPY | Weekly | 5. Leverage effect | gamma = 0.454 | <0.001 | Supported |
| SPY | Weekly | 6. Conditional non-normality | z excess kurtosis = 2.34 | <0.001 | Supported |
| SPY | Monthly | 1. Little serial correlation | max \|ACF(1-5)\| = 0.125 | 0.248 | Supported |
| SPY | Monthly | 2. Non-normal, fat tails | excess kurtosis = 0.67 | 0.003 | Supported |
| SPY | Monthly | 3. Negative skewness | skewness = -0.491 | 0.005 | Supported |
| SPY | Monthly | 4. Volatility clustering | LB \|r\| p = 0.005 | <0.001 | Supported |
| SPY | Monthly | 5. Leverage effect | gamma = 0.571 | 0.583 | Not significant |
| SPY | Monthly | 6. Conditional non-normality | z excess kurtosis = 0.33 | <0.001 | Supported |

Note: p-value column: 1) Ljung-Box on returns at lag 10 (daily), 8 (weekly), 6 (monthly); 2) Jarque-Bera; 3) bootstrap test of skewness; 4) Ljung-Box on r^2 (the statistic column shows the Ljung-Box p-value on |r|; Partial = only one of the two is significant); 5) gamma of the GJR-GARCH (Student-t); 6) Jarque-Bera of the standardised residuals.

## T05. Autocorrelation of log returns, lags 1 to 5

*Report section: 2.1.1 Little or no serial correlation*

| Asset | Frequency | lag 1 | lag 2 | lag 3 | lag 4 | lag 5 | 95% band (±1.96/√N) |
|---|---|---|---|---|---|---|---|
| WMT | Daily | -0.034 | -0.006 | -0.009 | -0.041 | -0.011 | 0.030 |
| WMT | Weekly | -0.095 | 0.019 | -0.030 | 0.014 | -0.040 | 0.066 |
| WMT | Monthly | -0.070 | 0.014 | 0.036 | -0.050 | -0.059 | 0.139 |
| SPY | Daily | -0.100 | 0.062 | -0.038 | -0.040 | 0.001 | 0.030 |
| SPY | Weekly | -0.089 | 0.036 | -0.015 | -0.056 | -0.064 | 0.066 |
| SPY | Monthly | -0.125 | -0.117 | 0.027 | -0.058 | 0.001 | 0.139 |

Note: Values outside ±1.96/√N are significant at 5%.

## T06. Ljung-Box test on log returns (H0: no autocorrelation up to the lag)

*Report section: 2.1.1 Little or no serial correlation*

| Asset | Frequency | Series | Lag | Q stat | p-value | Reject H0 (5%) |
|---|---|---|---|---|---|---|
| WMT | Daily | r | 5 | 13.11 | 0.022 | Yes |
| WMT | Daily | r | 10 | 29.26 | 0.001 | Yes |
| WMT | Daily | r | 20 | 45.18 | 0.001 | Yes |
| WMT | Weekly | r | 4 | 9.24 | 0.055 | No |
| WMT | Weekly | r | 8 | 12.24 | 0.141 | No |
| WMT | Weekly | r | 12 | 18.20 | 0.110 | No |
| WMT | Monthly | r | 3 | 1.29 | 0.732 | No |
| WMT | Monthly | r | 6 | 4.14 | 0.658 | No |
| WMT | Monthly | r | 12 | 6.79 | 0.871 | No |
| SPY | Daily | r | 5 | 70.93 | <0.001 | Yes |
| SPY | Daily | r | 10 | 168.20 | <0.001 | Yes |
| SPY | Daily | r | 20 | 203.86 | <0.001 | Yes |
| SPY | Weekly | r | 4 | 11.05 | 0.026 | Yes |
| SPY | Weekly | r | 8 | 17.68 | 0.024 | Yes |
| SPY | Weekly | r | 12 | 22.74 | 0.030 | Yes |
| SPY | Monthly | r | 3 | 6.10 | 0.107 | No |
| SPY | Monthly | r | 6 | 7.87 | 0.248 | No |
| SPY | Monthly | r | 12 | 12.79 | 0.384 | No |

Note: A rejection with very small autocorrelations (table T05) means statistically significant but economically negligible dependence.

## T07. Normality and fat tails: excess kurtosis, Jarque-Bera and frequency of 3-sigma days

*Report section: 2.1.2 Non-normal distributions and fat tails*

| Asset | Frequency | Excess kurtosis | Kurtosis test p-value | Jarque-Bera | JB p-value | % \|z\|>3 (data) | % \|z\|>3 (normal) |
|---|---|---|---|---|---|---|---|
| WMT | Daily | 14.32 | <0.001 | 35953.8 | <0.001 | 1.38 | 0.27 |
| WMT | Weekly | 6.67 | <0.001 | 1722.1 | <0.001 | 1.72 | 0.27 |
| WMT | Monthly | 0.84 | 0.036 | 10.1 | 0.006 | 1.01 | 0.27 |
| SPY | Daily | 12.40 | <0.001 | 27147.2 | <0.001 | 1.43 | 0.27 |
| SPY | Weekly | 5.83 | <0.001 | 1312.1 | <0.001 | 1.38 | 0.27 |
| SPY | Monthly | 0.67 | 0.071 | 11.7 | 0.003 | 0.50 | 0.27 |

Note: "% |z|>3" = share of observations more than 3 standard deviations from the mean (0.27% under a normal distribution).

## T08. Asymmetry: skewness with a bootstrap test (robust to fat tails)

*Report section: 2.1.3 Asymmetry and negative skewness*

| Asset | Frequency | Skewness | Skewtest p (assumes normal tails) | Bootstrap 95% CI low | Bootstrap 95% CI high | Bootstrap p (skew >= 0) | N below -3σ | N above +3σ | Quantile 1% | Quantile 99% |
|---|---|---|---|---|---|---|---|---|---|---|
| WMT | Daily | -0.255 | <0.001 | -1.108 | 0.603 | 0.273 | 30 | 28 | -3.25% | 3.17% |
| WMT | Weekly | -0.853 | <0.001 | -1.768 | 0.003 | 0.026 | 9 | 6 | -7.95% | 7.67% |
| WMT | Monthly | -0.360 | 0.037 | -0.756 | 0.145 | 0.083 | 2 | 0 | -12.97% | 12.08% |
| SPY | Daily | -0.555 | <0.001 | -1.404 | 0.277 | 0.113 | 39 | 21 | -3.08% | 2.61% |
| SPY | Weekly | -0.740 | <0.001 | -1.510 | 0.014 | 0.029 | 8 | 4 | -6.05% | 5.69% |
| SPY | Monthly | -0.491 | 0.005 | -0.851 | -0.112 | 0.005 | 1 | 0 | -9.23% | 10.33% |

Note: The classical skewtest assumes normal tails and over-rejects with fat tails; the bootstrap (resampling the data) does not. Bootstrap p = share of bootstrap samples with skewness >= 0.

## T09. Volatility clustering: Ljung-Box on |r| and r^2 and ARCH-LM test

*Report section: 2.1.4 Volatility clustering*

| Asset | Frequency | Lag | LB \|r\| p-value | LB r² p-value | ARCH-LM stat | ARCH-LM p-value |
|---|---|---|---|---|---|---|
| WMT | Daily | 10 | <0.001 | <0.001 | 235.90 | <0.001 |
| WMT | Weekly | 8 | <0.001 | 0.188 | 8.90 | 0.351 |
| WMT | Monthly | 6 | 0.848 | 0.672 | 3.33 | 0.767 |
| SPY | Daily | 10 | <0.001 | <0.001 | 1214.48 | <0.001 |
| SPY | Weekly | 8 | <0.001 | <0.001 | 248.43 | <0.001 |
| SPY | Monthly | 6 | 0.005 | <0.001 | 28.15 | <0.001 |

Note: H0 = no autocorrelation in absolute / squared returns (no ARCH effects). Small p-values support volatility clustering.

## T10. GJR-GARCH(1,1) estimates with normal and Student-t innovations

*Report section: 2.1.5 Leverage effect*

| Asset | Frequency | Innovations | omega | alpha | gamma | gamma p-value | beta | persistence (α+γ/2+β) | nu (t d.o.f.) | Log-lik. | AIC | BIC |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| WMT | Daily | normal | 0.1425 | 0.0394 | 0.0811 | 0.202 | 0.8309 | 0.9108 |  | -6685.2 | 13380.4 | 13412.1 |
| WMT | Daily | t | 0.1190 | 0.0612 | 0.0706 | 0.006 | 0.8222 | 0.9188 | 3.93 | -6155.8 | 12323.6 | 12361.7 |
| WMT | Weekly | normal | 0.0226 | 0.0000 | 0.0000 | 1.000 | 0.9982 | 0.9982 |  | -2085.3 | 4180.6 | 4204.4 |
| WMT | Weekly | t | 0.3158 | 0.0451 | 0.0010 | 0.979 | 0.9151 | 0.9608 | 4.12 | -2025.0 | 4062.1 | 4090.7 |
| WMT | Monthly | normal | 3.0545 | 0.0807 | -0.0807 | 0.276 | 0.8493 | 0.8897 |  | -607.2 | 1224.5 | 1240.9 |
| WMT | Monthly | t | 0.0872 | 0.0000 | 0.0000 | 1.000 | 1.0000 | 1.0000 | 12.35 | -605.3 | 1222.6 | 1242.4 |
| SPY | Daily | normal | 0.0380 | 0.0156 | 0.2343 | <0.001 | 0.8279 | 0.9606 |  | -5309.7 | 10629.4 | 10661.1 |
| SPY | Daily | t | 0.0294 | 0.0000 | 0.2805 | <0.001 | 0.8332 | 0.9734 | 5.82 | -5176.5 | 10365.1 | 10403.1 |
| SPY | Weekly | normal | 0.4712 | 0.0094 | 0.4944 | <0.001 | 0.6615 | 0.9181 |  | -1796.2 | 3602.3 | 3626.2 |
| SPY | Weekly | t | 0.4259 | 0.0000 | 0.4542 | <0.001 | 0.6823 | 0.9094 | 8.13 | -1778.8 | 3569.5 | 3598.1 |
| SPY | Monthly | normal | 4.5371 | 0.0000 | 0.5184 | 0.013 | 0.4593 | 0.7185 |  | -545.9 | 1101.8 | 1118.2 |
| SPY | Monthly | t | 4.4928 | 0.0000 | 0.5710 | 0.583 | 0.4392 | 0.7247 | 14.31 | -545.5 | 1103.0 | 1122.7 |

Note: Returns in % (x100) for numerical stability. gamma > 0 and significant = negative shocks raise volatility more (leverage effect). The weekly-normal and monthly models are at the boundary of the parameter space (unreliable).

## T11. Correlation between r(t) and |r(t+k)| (daily)

*Report section: 2.1.5 Leverage effect*

| k (days ahead) | WMT | SPY |
|---|---|---|
| 1 | -0.073 | -0.117 |
| 2 | 0.001 | -0.151 |
| 3 | -0.025 | -0.107 |
| 4 | -0.043 | -0.165 |
| 5 | 0.007 | -0.071 |
| 6 | -0.013 | -0.124 |
| 7 | -0.016 | -0.050 |
| 8 | -0.014 | -0.074 |
| 9 | -0.002 | -0.052 |
| 10 | -0.014 | -0.067 |

Note: Negative values = falls are followed by larger absolute moves (leverage effect).

## T12. Standardised residuals of the GJR-GARCH: skewness, excess kurtosis and tests

*Report section: 2.1.6 Conditional non-normality*

| Asset | Frequency | Innovations | z skewness | z excess kurtosis | z JB p-value | LB z p-value | LB z² p-value |
|---|---|---|---|---|---|---|---|
| WMT | Daily | normal | -0.64 | 15.02 | <0.001 | 0.128 | 0.988 |
| WMT | Daily | t | -0.66 | 15.67 | <0.001 | 0.141 | 0.962 |
| WMT | Weekly | normal | -0.78 | 4.62 | <0.001 | 0.188 | 0.659 |
| WMT | Weekly | t | -0.99 | 7.13 | <0.001 | 0.297 | 1.000 |
| WMT | Monthly | normal | -0.25 | 0.53 | 0.110 | 0.751 | 0.828 |
| WMT | Monthly | t | -0.32 | 0.66 | 0.029 | 0.756 | 0.885 |
| SPY | Daily | normal | -0.73 | 2.60 | <0.001 | 0.509 | 0.537 |
| SPY | Daily | t | -0.79 | 3.17 | <0.001 | 0.353 | 0.662 |
| SPY | Weekly | normal | -0.84 | 2.32 | <0.001 | 0.448 | 0.850 |
| SPY | Weekly | t | -0.85 | 2.34 | <0.001 | 0.384 | 0.889 |
| SPY | Monthly | normal | -0.75 | 0.26 | <0.001 | 0.633 | 0.834 |
| SPY | Monthly | t | -0.78 | 0.33 | <0.001 | 0.599 | 0.794 |

Note: z = residual / conditional volatility. Excess kurtosis > 0 and a small Jarque-Bera p-value = conditional non-normality. LB z and LB z^2 check that the model removed the autocorrelation and the volatility clustering.

## T13. The portfolios compared: objective, inputs and parameters

*Report section: 3. Strategies: objectives and constraints*

| Strategy | Objective / allocation rule | What is estimated | Parameters and notes |
|---|---|---|---|
| a) Equally weighted (EW) | w_i = 1/N (N = 12 stocks drawn in each experiment) | nothing | Main benchmark of the brief |
| b) Markowitz mean-variance | max w'μ - (λ/2) w'Σw | μ and Σ (trailing 1 year) | Risk aversion λ = 3 (sensitivity: λ = 1 and 5) |
| c) Global minimum variance (GMV) | min w'Σw | Σ | Ignores expected returns |
| d) Max Sharpe | max (w'μ - r_f) / √(w'Σw) | μ, Σ and r_f (DGS3 of the last trading day before the rebalancing) | Tangency portfolio |
| e) Inverse volatility | w_i ∝ 1/σ_i | σ_i only (ignores correlations) | No optimiser |
| e) Risk parity (ERC) | equal risk contributions: w_i (Σw)_i / w'Σw = 1/N | Σ (with correlations) | Weights > 0 |
| f) Most diversified | max DR = w'σ / √(w'Σw) | Σ | Highest diversification ratio |
| f) Max decorrelation | min w'Cw (C = correlation matrix) | correlations only | Minimum variance as if all volatilities were equal |
| Group pick (23 stocks) | w_i = 1/N over all the group's stocks with data (23; 22 before TSLA) | nothing | The group's own selection; same rebalancing and costs |
| SPY (buy & hold) | bought at the start of the evaluation year and held | nothing | Market benchmark (investable S&P 500 ETF); no costs |

Note: Common constraints for every strategy: long-only (w_i >= 0), fully invested (Σw_i = 1), no leverage. Optimisers: scipy SLSQP (ftol 1e-10, retry with 1e-8; equal weights if both fail - 0 failures in the main run).

## T14. Backtest design and conventions (the same for every strategy)

*Report section: 3. Backtest design and assumptions*

| Item | Convention |
|---|---|
| Experiments | 100 contiguous three-year datasets (756 trading days) sampled at random, random seed 2026 (parameters fixed before the results were seen) |
| Assets per experiment | 12 stocks drawn at random from the 23 (only stocks with data in the whole window); the Group pick holds all of them |
| Split | Days 1-504: estimation period; days 505-756: out-of-sample evaluation (252 days). With the trailing 1-year window, the warm-up weights (held from day 379) use days 127-378 and the evaluation weights use days 253-504 and 379-630; only days 505-756 enter the metrics |
| Estimation window | Trailing 1 year (252 days), only data available before each rebalancing |
| Rebalancing | Semi-annual (every 126 trading days), first rebalancing one semester before the evaluation year; weights drift between rebalancings |
| Trading convention | Weights set with data up to the close of day t-1 and traded at that close (market-on-close), so they apply from day t; a one-day execution lag would be stricter |
| Returns | Simple returns for portfolios and wealth; log returns only for the stylised facts |
| Transaction costs | 10 bps per unit of two-way turnover Σ\|Δw\| (switching the whole portfolio costs 20 bps; robustness: 0, 25, 50 bps); the initial purchase happens at the warm-up rebalancing, before the evaluation year; SPY buy & hold has no costs |
| Risk-free rate | 3-year US Treasury yield (FRED DGS3), daily rate = annual / 252 |
| Metrics | Annualised return (geometric), volatility, Sharpe, Sortino, maximum drawdown, Calmar, Sterling = return / (\|MDD\| + 10%), turnover, effective N, diversification ratio, CAPM beta and alpha |
| Summary across experiments | Medians, dispersion (P25/P75), % of experiments that beat EW / the Group pick / SPY, ranks and head-to-head win rates (no significance tests: the windows overlap) |
| Robustness | Costs 0-50 bps; quarterly rebalancing; λ = 1, 3, 5; sub-periods and market regimes; new draw of stocks and all eligible stocks; strategies on the 23-stock universe |

## T15. Median performance of the 10 portfolios across the 100 experiments (net of 10 bps)

*Report section: 3. Results*

| Portfolio | Ann. return | Ann. volatility | Sharpe | Sortino | Max drawdown | Calmar | Sterling | Ann. return (gross) | Sharpe (gross) | Turnover (annual) | Effective N | Max weight | Diversification ratio (ex-ante) | Cost drag (bps) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| EW | 31.2% | 16.9% | 1.81 | 2.73 | -11.1% | 3.30 | 1.68 | 31.2% | 1.81 | 0.27 | 12.0 | 8.3% | 1.63 | 3.5 |
| Markowitz (λ=3) | 39.8% | 34.5% | 1.23 | 1.87 | -23.5% | 2.09 | 1.37 | 40.1% | 1.24 | 2.21 | 1.5 | 76.9% | 1.11 | 32.6 |
| GMV | 17.3% | 12.8% | 1.34 | 1.90 | -9.8% | 2.01 | 0.93 | 17.4% | 1.35 | 0.95 | 4.4 | 35.0% | 1.55 | 10.9 |
| Max Sharpe | 27.9% | 20.8% | 1.29 | 2.02 | -14.4% | 2.19 | 1.28 | 28.3% | 1.31 | 2.14 | 2.8 | 49.6% | 1.40 | 27.0 |
| Inverse vol | 25.7% | 14.7% | 1.78 | 2.64 | -9.8% | 3.16 | 1.47 | 25.7% | 1.78 | 0.27 | 10.9 | 12.8% | 1.64 | 3.4 |
| Risk parity (ERC) | 26.5% | 14.4% | 1.80 | 2.71 | -10.0% | 3.22 | 1.48 | 26.5% | 1.80 | 0.31 | 10.7 | 13.8% | 1.69 | 3.8 |
| Most diversified | 28.7% | 15.2% | 1.70 | 2.51 | -10.7% | 3.05 | 1.41 | 28.8% | 1.71 | 0.84 | 6.3 | 26.5% | 1.79 | 10.1 |
| Max decorrelation | 33.3% | 19.0% | 1.66 | 2.48 | -13.1% | 2.83 | 1.58 | 33.4% | 1.66 | 0.86 | 7.1 | 21.0% | 1.72 | 10.8 |
| Group pick (23 stocks) | 35.6% | 15.8% | 1.70 | 2.74 | -10.1% | 2.98 | 1.60 | 35.6% | 1.71 | 0.28 | 23.0 | 4.3% | 1.70 | 3.8 |
| SPY (buy & hold) | 17.7% | 14.0% | 1.13 | 1.66 | -9.4% | 2.00 | 0.89 | 17.7% | 1.13 | 0.00 |  |  |  | 0.0 |

Note: Medians of the 100 out-of-sample years. Sharpe and Sortino use the daily DGS3 rate. Sterling = return / (|MDD| + 10%). Effective N = 1/Σw² (12 = equal weights on 12 stocks). The diversification ratio is ex-ante (estimation sample).

## T16. Dispersion across the 100 experiments: 25th percentile, median and 75th percentile

*Report section: 3. Results*

| Portfolio | Sharpe P25 | Sharpe median | Sharpe P75 | Return P25 | Return median | Return P75 | Return std | Sterling P25 | Sterling median | Sterling P75 |
|---|---|---|---|---|---|---|---|---|---|---|
| EW | 0.72 | 1.81 | 2.43 | 13.3% | 31.2% | 46.5% | 21.7% | 0.51 | 1.68 | 2.51 |
| Markowitz (λ=3) | 0.47 | 1.23 | 1.87 | 10.0% | 39.8% | 90.7% | 67.8% | 0.34 | 1.37 | 2.83 |
| GMV | 0.56 | 1.34 | 1.89 | 10.1% | 17.3% | 28.4% | 12.8% | 0.49 | 0.93 | 1.54 |
| Max Sharpe | 0.57 | 1.29 | 1.98 | 11.0% | 27.9% | 52.7% | 40.2% | 0.44 | 1.28 | 2.12 |
| Inverse vol | 0.63 | 1.78 | 2.32 | 12.3% | 25.7% | 36.7% | 16.8% | 0.50 | 1.47 | 2.01 |
| Risk parity (ERC) | 0.61 | 1.80 | 2.40 | 12.0% | 26.5% | 38.0% | 17.2% | 0.53 | 1.48 | 2.20 |
| Most diversified | 0.78 | 1.70 | 2.37 | 12.6% | 28.7% | 39.3% | 21.7% | 0.61 | 1.41 | 2.18 |
| Max decorrelation | 0.72 | 1.66 | 2.36 | 15.4% | 33.3% | 51.1% | 33.0% | 0.57 | 1.58 | 2.66 |
| Group pick (23 stocks) | 0.86 | 1.70 | 2.62 | 14.5% | 35.6% | 45.4% | 20.5% | 0.70 | 1.60 | 2.75 |
| SPY (buy & hold) | 0.54 | 1.13 | 1.95 | 11.1% | 17.7% | 24.8% | 14.5% | 0.42 | 0.89 | 1.60 |

## T17. % of experiments in which each portfolio beats EW in the same experiment

*Report section: 3. Results*

| Portfolio | % beats EW: Sharpe | % beats EW: Ann. return | % beats EW: Max drawdown | % beats EW: Ann. volatility | % beats EW: Sterling |
|---|---|---|---|---|---|
| Markowitz (λ=3) | 21 | 57 | 9 | 1 | 45 |
| GMV | 31 | 26 | 65 | 98 | 30 |
| Max Sharpe | 34 | 54 | 27 | 19 | 46 |
| Inverse vol | 47 | 27 | 87 | 100 | 33 |
| Risk parity (ERC) | 51 | 26 | 86 | 100 | 32 |
| Most diversified | 47 | 39 | 61 | 75 | 40 |
| Max decorrelation | 41 | 64 | 26 | 27 | 54 |
| Group pick (23 stocks) | 62 | 49 | 55 | 56 | 54 |
| SPY (buy & hold) | 15 | 12 | 63 | 87 | 13 |

Note: Better = higher Sharpe, return and Sterling; smaller drawdown; lower volatility. 50% = as often better as worse.

## T18. % of experiments in which each portfolio beats the Group pick in the same experiment

*Report section: 3. Results*

| Portfolio | % beats Group pick: Sharpe | % beats Group pick: Ann. return | % beats Group pick: Max drawdown | % beats Group pick: Ann. volatility | % beats Group pick: Sterling |
|---|---|---|---|---|---|
| EW | 38 | 51 | 45 | 44 | 46 |
| Markowitz (λ=3) | 21 | 57 | 11 | 0 | 40 |
| GMV | 32 | 20 | 66 | 99 | 27 |
| Max Sharpe | 31 | 50 | 32 | 20 | 46 |
| Inverse vol | 39 | 29 | 72 | 86 | 35 |
| Risk parity (ERC) | 44 | 30 | 77 | 86 | 36 |
| Most diversified | 38 | 41 | 50 | 65 | 41 |
| Max decorrelation | 39 | 58 | 30 | 29 | 50 |
| SPY (buy & hold) | 8 | 4 | 62 | 96 | 6 |

Note: Better = higher Sharpe, return and Sterling; smaller drawdown; lower volatility. 50% = as often better as worse.

## T19. % of experiments in which each portfolio beats SPY in the same experiment

*Report section: 3. Results*

| Portfolio | % beats SPY: Sharpe | % beats SPY: Ann. return | % beats SPY: Max drawdown | % beats SPY: Ann. volatility | % beats SPY: Sterling |
|---|---|---|---|---|---|
| EW | 85 | 88 | 37 | 13 | 87 |
| Markowitz (λ=3) | 49 | 75 | 11 | 0 | 67 |
| GMV | 52 | 51 | 56 | 81 | 50 |
| Max Sharpe | 55 | 72 | 24 | 14 | 65 |
| Inverse vol | 86 | 85 | 59 | 44 | 88 |
| Risk parity (ERC) | 86 | 86 | 58 | 46 | 88 |
| Most diversified | 80 | 86 | 46 | 36 | 84 |
| Max decorrelation | 75 | 87 | 29 | 12 | 86 |
| Group pick (23 stocks) | 92 | 96 | 38 | 4 | 94 |

Note: Better = higher Sharpe, return and Sterling; smaller drawdown; lower volatility. 50% = as often better as worse.

## T20. Rank of each portfolio by net Sharpe ratio in each experiment (1 = best of 10)

*Report section: 3. Results*

| Portfolio | Average rank | Median rank | % ranked 1st | % in top 3 | % ranked last |
|---|---|---|---|---|---|
| Group pick (23 stocks) | 3.9 | 3.5 | 33 | 50 | 2 |
| Risk parity (ERC) | 4.2 | 4.0 | 3 | 35 | 0 |
| EW | 4.5 | 4.5 | 6 | 39 | 1 |
| Inverse vol | 4.7 | 5.0 | 3 | 27 | 0 |
| Most diversified | 4.8 | 5.0 | 11 | 34 | 1 |
| Max decorrelation | 5.0 | 5.0 | 10 | 36 | 2 |
| Max Sharpe | 6.4 | 8.0 | 12 | 25 | 11 |
| GMV | 6.6 | 8.0 | 13 | 27 | 30 |
| Markowitz (λ=3) | 7.3 | 9.0 | 8 | 20 | 30 |
| SPY (buy & hold) | 7.6 | 8.0 | 1 | 7 | 23 |

## T21. Head-to-head: % of experiments in which A (row) has a higher net Sharpe ratio than B (column)

*Report section: 3. Results: head-to-head comparison*

| Portfolio A (row) | EW | Markowitz (λ=3) | GMV | Max Sharpe | Inverse vol | Risk parity (ERC) | Most diversified | Max decorrelation | Group pick (23 stocks) | SPY (buy & hold) |
|---|---|---|---|---|---|---|---|---|---|---|
| EW |  | 79 | 69 | 66 | 53 | 49 | 53 | 59 | 38 | 85 |
| Markowitz (λ=3) | 21 |  | 45 | 37 | 21 | 21 | 25 | 25 | 21 | 49 |
| GMV | 31 | 55 |  | 48 | 29 | 28 | 31 | 34 | 32 | 52 |
| Max Sharpe | 34 | 63 | 52 |  | 34 | 30 | 33 | 32 | 31 | 55 |
| Inverse vol | 47 | 79 | 71 | 66 |  | 35 | 53 | 54 | 39 | 86 |
| Risk parity (ERC) | 51 | 79 | 72 | 70 | 65 |  | 57 | 57 | 44 | 86 |
| Most diversified | 47 | 75 | 69 | 67 | 47 | 43 |  | 56 | 38 | 80 |
| Max decorrelation | 41 | 75 | 66 | 68 | 46 | 43 | 44 |  | 39 | 75 |
| Group pick (23 stocks) | 62 | 79 | 68 | 69 | 61 | 56 | 62 | 61 |  | 92 |
| SPY (buy & hold) | 15 | 51 | 48 | 45 | 14 | 14 | 20 | 25 | 8 |  |

Note: Each cell compares two portfolios in the same 100 experiments; cell(A,B) + cell(B,A) = 100.

## T22. Average % of head-to-head comparisons won (against the other 9 portfolios)

*Report section: 3. Results: head-to-head comparison*

| Portfolio | Avg % won: Sharpe | Avg % won: Ann. return | Avg % won: Max drawdown | Avg % won: Ann. volatility | Avg % won: Sterling | Rivals beaten in > 50% (Sharpe) |
|---|---|---|---|---|---|---|
| Group pick (23 stocks) | 68 | 62 | 51 | 42 | 64 | 9 |
| Risk parity (ERC) | 65 | 47 | 73 | 74 | 54 | 8 |
| EW | 61 | 61 | 47 | 37 | 61 | 7 |
| Inverse vol | 59 | 44 | 71 | 70 | 50 | 6 |
| Most diversified | 58 | 53 | 57 | 60 | 54 | 5 |
| Max decorrelation | 55 | 65 | 33 | 27 | 62 | 4 |
| Max Sharpe | 40 | 56 | 31 | 21 | 50 | 3 |
| GMV | 38 | 29 | 69 | 96 | 33 | 2 |
| Markowitz (λ=3) | 29 | 62 | 9 | 1 | 50 | 0 |
| SPY (buy & hold) | 27 | 19 | 60 | 72 | 21 | 1 |

## T23. Median paired difference in net Sharpe ratio: A (row) minus B (column)

*Report section: 3. Results: head-to-head comparison*

| Portfolio A (row) | EW | Markowitz (λ=3) | GMV | Max Sharpe | Inverse vol | Risk parity (ERC) | Most diversified | Max decorrelation | Group pick (23 stocks) | SPY (buy & hold) |
|---|---|---|---|---|---|---|---|---|---|---|
| EW |  | 0.55 | 0.41 | 0.25 | 0.01 | -0.01 | 0.05 | 0.06 | -0.08 | 0.39 |
| Markowitz (λ=3) | -0.55 |  | -0.09 | -0.15 | -0.47 | -0.55 | -0.48 | -0.48 | -0.60 | -0.02 |
| GMV | -0.41 | 0.09 |  | -0.10 | -0.31 | -0.36 | -0.42 | -0.26 | -0.50 | 0.07 |
| Max Sharpe | -0.25 | 0.15 | 0.10 |  | -0.28 | -0.31 | -0.27 | -0.24 | -0.36 | 0.13 |
| Inverse vol | -0.01 | 0.47 | 0.31 | 0.28 |  | -0.02 | 0.03 | 0.05 | -0.13 | 0.38 |
| Risk parity (ERC) | 0.01 | 0.55 | 0.36 | 0.31 | 0.02 |  | 0.03 | 0.08 | -0.08 | 0.42 |
| Most diversified | -0.05 | 0.48 | 0.42 | 0.27 | -0.03 | -0.03 |  | 0.02 | -0.21 | 0.36 |
| Max decorrelation | -0.06 | 0.48 | 0.26 | 0.24 | -0.05 | -0.08 | -0.02 |  | -0.18 | 0.33 |
| Group pick (23 stocks) | 0.08 | 0.60 | 0.50 | 0.36 | 0.13 | 0.08 | 0.21 | 0.18 |  | 0.47 |
| SPY (buy & hold) | -0.39 | 0.02 | -0.07 | -0.13 | -0.38 | -0.42 | -0.36 | -0.33 | -0.47 |  |

## T24. Market risk against SPY: CAPM beta, Jensen's alpha, tracking error and information ratio (medians)

*Report section: 3. Results: market risk (CAPM)*

| Portfolio | Beta | Alpha (ann.) | Alpha t-stat | R² | Tracking error | Information ratio | % beta < 1 | % alpha > 0 | % alpha significant > 0 (t > 1.96) | % IR > 0 (beats SPY) |
|---|---|---|---|---|---|---|---|---|---|---|
| EW | 1.04 | 9.6% | 1.33 | 0.82 | 7.5% | 1.40 | 37 | 90 | 26 | 88 |
| Markowitz (λ=3) | 1.32 | 18.3% | 0.60 | 0.33 | 26.1% | 0.85 | 22 | 78 | 5 | 77 |
| GMV | 0.64 | 6.0% | 0.71 | 0.56 | 10.0% | 0.01 | 99 | 74 | 9 | 50 |
| Max Sharpe | 0.98 | 8.5% | 0.83 | 0.47 | 15.6% | 0.80 | 54 | 76 | 10 | 75 |
| Inverse vol | 0.93 | 7.2% | 1.30 | 0.85 | 5.6% | 1.03 | 76 | 92 | 31 | 85 |
| Risk parity (ERC) | 0.91 | 8.1% | 1.36 | 0.84 | 6.2% | 1.05 | 80 | 92 | 27 | 86 |
| Most diversified | 0.85 | 9.3% | 1.08 | 0.66 | 9.4% | 0.80 | 83 | 91 | 21 | 86 |
| Max decorrelation | 1.00 | 11.7% | 1.01 | 0.66 | 10.6% | 1.04 | 51 | 87 | 19 | 89 |
| Group pick (23 stocks) | 1.05 | 9.9% | 1.74 | 0.90 | 5.4% | 2.06 | 11 | 96 | 40 | 96 |

Note: Regression of the daily excess returns of each portfolio on those of SPY in each out-of-sample year (net of costs). Alpha annualised = daily alpha x 252. OLS t-statistics are only indicative (volatility clustering).

## T25. Median net Sharpe ratio with different transaction costs

*Report section: Robustness: transaction costs*

| Portfolio | 0 bps | 10 bps | 25 bps | 50 bps |
|---|---|---|---|---|
| EW | 1.808 | 1.806 | 1.804 | 1.801 |
| Markowitz (λ=3) | 1.241 | 1.232 | 1.219 | 1.196 |
| GMV | 1.349 | 1.338 | 1.321 | 1.294 |
| Max Sharpe | 1.305 | 1.288 | 1.262 | 1.250 |
| Inverse vol | 1.779 | 1.777 | 1.774 | 1.770 |
| Risk parity (ERC) | 1.803 | 1.801 | 1.797 | 1.791 |
| Most diversified | 1.707 | 1.701 | 1.691 | 1.675 |
| Max decorrelation | 1.664 | 1.658 | 1.649 | 1.634 |
| Group pick (23 stocks) | 1.705 | 1.704 | 1.701 | 1.697 |
| SPY (buy & hold) | 1.128 | 1.128 | 1.128 | 1.128 |

## T26. Rank by median net Sharpe ratio with different transaction costs (1 = best)

*Report section: Robustness: transaction costs*

| Portfolio | 0 bps | 10 bps | 25 bps | 50 bps |
|---|---|---|---|---|
| EW | 1 | 1 | 1 | 1 |
| Markowitz (λ=3) | 9 | 9 | 9 | 9 |
| GMV | 7 | 7 | 7 | 7 |
| Max Sharpe | 8 | 8 | 8 | 8 |
| Inverse vol | 3 | 3 | 3 | 3 |
| Risk parity (ERC) | 2 | 2 | 2 | 2 |
| Most diversified | 4 | 5 | 5 | 5 |
| Max decorrelation | 6 | 6 | 6 | 6 |
| Group pick (23 stocks) | 5 | 4 | 4 | 4 |
| SPY (buy & hold) | 10 | 10 | 10 | 10 |

## T27. Semi-annual vs quarterly rebalancing (medians, net of 10 bps)

*Report section: Robustness: rebalancing frequency*

| Portfolio | Sharpe (semi-annual) | Sharpe (quarterly) | Return (semi-annual) | Return (quarterly) | Turnover (semi-annual) | Turnover (quarterly) | % beats EW Sharpe (quarterly) |
|---|---|---|---|---|---|---|---|
| EW | 1.81 | 1.72 | 31.2% | 31.9% | 0.27 | 0.38 |  |
| Markowitz (λ=3) | 1.23 | 1.18 | 39.8% | 35.8% | 2.21 | 2.93 | 17 |
| GMV | 1.34 | 1.40 | 17.3% | 16.9% | 0.95 | 1.22 | 29 |
| Max Sharpe | 1.29 | 1.36 | 27.9% | 28.5% | 2.14 | 3.08 | 34 |
| Inverse vol | 1.78 | 1.73 | 25.7% | 25.8% | 0.27 | 0.38 | 42 |
| Risk parity (ERC) | 1.80 | 1.82 | 26.5% | 26.0% | 0.31 | 0.42 | 48 |
| Most diversified | 1.70 | 1.78 | 28.7% | 28.0% | 0.84 | 1.11 | 47 |
| Max decorrelation | 1.66 | 1.69 | 33.3% | 34.4% | 0.86 | 1.13 | 43 |
| Group pick (23 stocks) | 1.70 | 1.75 | 35.6% | 34.9% | 0.28 | 0.38 | 62 |
| SPY (buy & hold) | 1.13 | 1.13 | 17.7% | 17.7% | 0.00 | 0.00 | 15 |

## T28. Markowitz risk aversion: λ = 1, 3 and 5 between Max Sharpe, GMV and EW (medians)

*Report section: Robustness: Markowitz risk aversion*

| Portfolio | Ann. return | Ann. volatility | Sharpe | Max drawdown | Turnover (annual) | Effective N |
|---|---|---|---|---|---|---|
| EW | 31.2% | 16.9% | 1.81 | -11.1% | 0.27 | 12.0 |
| GMV | 17.3% | 12.8% | 1.34 | -9.8% | 0.95 | 4.4 |
| Markowitz (λ=5) | 34.5% | 29.8% | 1.31 | -20.9% | 2.37 | 2.0 |
| Markowitz (λ=3) | 39.8% | 34.5% | 1.23 | -23.5% | 2.21 | 1.5 |
| Markowitz (λ=1) | 42.6% | 40.5% | 1.11 | -27.2% | 2.00 | 1.0 |
| Max Sharpe | 27.9% | 20.8% | 1.29 | -14.4% | 2.14 | 2.8 |

## T29. Median net Sharpe ratio by sub-period of the evaluation year

*Report section: Robustness: dependence on the period*

| Portfolio | 2012-2016 | 2017-2020 | 2021-2026 |
|---|---|---|---|
| EW | 1.83 | 1.98 | 1.59 |
| Markowitz (λ=3) | 1.52 | 1.36 | 0.85 |
| GMV | 1.41 | 1.13 | 1.46 |
| Max Sharpe | 1.39 | 1.23 | 1.32 |
| Inverse vol | 1.83 | 1.88 | 1.54 |
| Risk parity (ERC) | 1.86 | 1.92 | 1.72 |
| Most diversified | 1.89 | 1.73 | 1.61 |
| Max decorrelation | 1.77 | 1.83 | 1.47 |
| Group pick (23 stocks) | 1.96 | 2.25 | 1.62 |
| SPY (buy & hold) | 1.47 | 1.93 | 0.77 |

## T30. Median Sharpe ratio and return in the experiments whose out-of-sample year had SPY down or up

*Report section: Robustness: dependence on the period*

| Portfolio | Sharpe: SPY down | Sharpe: SPY up | Return: SPY down | Return: SPY up |
|---|---|---|---|---|
| EW | 0.17 | 1.94 | 3.7% | 34.5% |
| Markowitz (λ=3) | -0.13 | 1.38 | -4.8% | 49.9% |
| GMV | -0.03 | 1.64 | 0.2% | 20.8% |
| Max Sharpe | 0.18 | 1.45 | 4.5% | 31.8% |
| Inverse vol | 0.14 | 1.88 | 3.8% | 27.8% |
| Risk parity (ERC) | 0.14 | 1.93 | 3.8% | 28.2% |
| Most diversified | 0.09 | 1.89 | 2.9% | 29.3% |
| Max decorrelation | 0.13 | 1.83 | 3.0% | 35.2% |
| Group pick (23 stocks) | 0.06 | 1.97 | 2.1% | 38.3% |
| SPY (buy & hold) | -0.30 | 1.35 | -5.4% | 20.4% |

Note: "SPY down" = 12 of the 100 experiments, with a negative SPY return in the out-of-sample year; they overlap and come from about four episodes (2015-16, 2018, 2019-20, 2021-23), so they are far fewer than 12 independent observations.

## T31. Do the results depend on the stocks drawn? Main draw, new draw and all eligible stocks

*Report section: Robustness: dependence on the asset subset*

| Portfolio | 12 stocks (main): Median Sharpe | 12 stocks (main): Rank | 12 stocks (main): Median return | 12 stocks (main): % beats EW (Sharpe) | 12 stocks (new draw): Median Sharpe | 12 stocks (new draw): Rank | 12 stocks (new draw): Median return | 12 stocks (new draw): % beats EW (Sharpe) | All eligible stocks: Median Sharpe | All eligible stocks: Rank | All eligible stocks: Median return | All eligible stocks: % beats EW (Sharpe) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| EW | 1.81 | 1.0 | 31.2% |  | 1.64 | 4.0 | 30.3% |  | 1.70 | 3.5 | 35.6% |  |
| Markowitz (λ=3) | 1.23 | 9.0 | 39.8% | 21 | 1.02 | 10.0 | 29.8% | 21 | 1.24 | 9.0 | 48.3% | 21 |
| GMV | 1.34 | 7.0 | 17.3% | 31 | 1.23 | 8.0 | 17.4% | 34 | 1.46 | 7.0 | 18.9% | 36 |
| Max Sharpe | 1.29 | 8.0 | 27.9% | 34 | 1.25 | 7.0 | 27.1% | 39 | 1.38 | 8.0 | 29.3% | 39 |
| Inverse vol | 1.78 | 3.0 | 25.7% | 47 | 1.58 | 6.0 | 26.0% | 47 | 1.66 | 5.0 | 27.9% | 40 |
| Risk parity (ERC) | 1.80 | 2.0 | 26.5% | 51 | 1.59 | 5.0 | 26.4% | 49 | 1.75 | 2.0 | 29.1% | 54 |
| Most diversified | 1.70 | 5.0 | 28.7% | 47 | 1.66 | 3.0 | 26.3% | 50 | 1.85 | 1.0 | 27.5% | 52 |
| Max decorrelation | 1.66 | 6.0 | 33.3% | 41 | 1.67 | 2.0 | 30.7% | 43 | 1.60 | 6.0 | 32.1% | 42 |
| Group pick (23 stocks) | 1.70 | 4.0 | 35.6% | 62 | 1.70 | 1.0 | 35.6% | 68 | 1.70 | 3.5 | 35.6% | 0 |
| SPY (buy & hold) | 1.13 | 10.0 | 17.7% | 15 | 1.13 | 9.0 | 17.7% | 19 | 1.13 | 10.0 | 17.7% | 8 |

Note: Same 100 periods. In "All eligible stocks", EW and the Group pick are the same portfolio (so they share the rank and the Group pick never "beats" EW).

## T32. The strategies applied to the group's 23 stocks (medians, net of 10 bps)

*Report section: Robustness: the 23-stock universe*

| Portfolio | Ann. return | Ann. volatility | Sharpe | Sortino | Max drawdown | Calmar | Sterling | Ann. return (gross) | Sharpe (gross) | Turnover (annual) | Effective N | Max weight | Diversification ratio (ex-ante) | Cost drag (bps) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Group pick (23 stocks) | 35.6% | 15.8% | 1.70 | 2.74 | -10.1% | 2.98 | 1.60 | 35.6% | 1.71 | 0.28 | 23.0 | 4.3% | 1.70 | 3.8 |
| Markowitz (λ=3) | 48.3% | 39.4% | 1.24 | 1.88 | -26.6% | 2.09 | 1.54 | 48.7% | 1.24 | 2.28 | 1.7 | 72.5% | 1.18 | 31.8 |
| GMV | 18.9% | 12.0% | 1.46 | 2.06 | -9.3% | 2.13 | 0.96 | 19.1% | 1.47 | 1.20 | 5.4 | 28.6% | 1.64 | 14.0 |
| Max Sharpe | 29.3% | 20.0% | 1.38 | 2.06 | -13.4% | 2.60 | 1.35 | 29.6% | 1.40 | 2.32 | 3.7 | 42.3% | 1.55 | 30.5 |
| Inverse vol | 27.9% | 14.1% | 1.66 | 2.57 | -8.6% | 3.02 | 1.41 | 27.9% | 1.66 | 0.28 | 20.7 | 7.2% | 1.69 | 3.6 |
| Risk parity (ERC) | 29.1% | 14.0% | 1.75 | 2.65 | -8.6% | 3.15 | 1.45 | 29.2% | 1.75 | 0.33 | 19.9 | 8.4% | 1.77 | 4.3 |
| Most diversified | 27.5% | 14.1% | 1.85 | 2.86 | -10.1% | 2.97 | 1.51 | 27.7% | 1.86 | 1.16 | 8.6 | 20.3% | 1.98 | 14.6 |
| Max decorrelation | 32.1% | 17.9% | 1.60 | 2.41 | -11.8% | 2.80 | 1.49 | 32.2% | 1.61 | 1.17 | 9.7 | 16.5% | 1.84 | 15.2 |
| SPY (buy & hold) | 17.7% | 14.0% | 1.13 | 1.66 | -9.4% | 2.00 | 0.89 | 17.7% | 1.13 | 0.00 |  |  |  | 0.0 |

Note: Here every strategy holds the same 23 stocks as the Group pick (EW on 23 stocks = the Group pick).

## T33. On the 23-stock universe: % of experiments in which each strategy beats the Group pick

*Report section: Robustness: the 23-stock universe*

| Portfolio | % beats Group pick: Sharpe | % beats Group pick: Ann. return | % beats Group pick: Max drawdown | % beats Group pick: Ann. volatility | % beats Group pick: Sterling | Median Sharpe difference vs Group pick |
|---|---|---|---|---|---|---|
| Markowitz (λ=3) | 21 | 63 | 8 | 0 | 51 | -0.49 |
| GMV | 36 | 20 | 68 | 100 | 25 | -0.27 |
| Max Sharpe | 39 | 60 | 30 | 23 | 54 | -0.22 |
| Inverse vol | 40 | 16 | 91 | 100 | 29 | -0.03 |
| Risk parity (ERC) | 54 | 23 | 93 | 100 | 35 | 0.01 |
| Most diversified | 52 | 40 | 63 | 73 | 43 | 0.02 |
| Max decorrelation | 42 | 63 | 29 | 33 | 63 | -0.07 |
| SPY (buy & hold) | 8 | 4 | 62 | 96 | 6 | -0.47 |

## T34. Full sample 2010-2026: Group pick vs SPY vs ^GSPC (descriptive only - biased by hindsight)

*Report section: Robustness / limitations: full sample*

| Portfolio | CAGR | Ann. volatility | Sharpe | Sortino | Max drawdown | Calmar | Avg. calendar-year max drawdown | Sterling | Final value of 1 USD |
|---|---|---|---|---|---|---|---|---|---|
| Group pick (23 stocks) | 25.8% | 18.4% | 1.24 | 1.78 | -32.2% | 0.80 | -12.8% | 1.13 | 46.0 |
| SPY (total return) | 14.1% | 17.1% | 0.75 | 1.05 | -33.7% | 0.42 | -12.8% | 0.62 | 9.0 |
| ^GSPC (price index) | 12.1% | 17.2% | 0.65 | 0.90 | -33.9% | 0.36 | -13.1% | 0.53 | 6.8 |

Note: The 23 stocks were chosen in 2026, so this is NOT out-of-sample evidence. Sterling uses the average of the 17 calendar-year maximum drawdowns (2026 = year to date). ^GSPC is a price index (no dividends).

## T35. Calendar-year returns: Group pick vs SPY vs ^GSPC (2026 = year to date, until 18 September)

*Report section: Robustness / limitations: full sample*

| Year | Group pick (23 stocks) | SPY (total return) | ^GSPC (price index) | Group pick minus SPY |
|---|---|---|---|---|
| 2010 | 12.5% | 13.1% | 11.0% | -0.6% |
| 2011 | 6.4% | 1.9% | 0.0% | 4.5% |
| 2012 | 14.6% | 16.0% | 13.4% | -1.4% |
| 2013 | 51.1% | 32.3% | 29.6% | 18.8% |
| 2014 | 19.2% | 13.5% | 11.4% | 5.7% |
| 2015 | 10.5% | 1.2% | -0.7% | 9.3% |
| 2016 | 33.0% | 12.0% | 9.5% | 21.0% |
| 2017 | 30.5% | 21.7% | 19.4% | 8.8% |
| 2018 | 2.5% | -4.6% | -6.2% | 7.1% |
| 2019 | 43.1% | 31.2% | 28.9% | 11.8% |
| 2020 | 49.4% | 18.3% | 16.3% | 31.1% |
| 2021 | 37.8% | 28.7% | 26.9% | 9.1% |
| 2022 | -14.9% | -18.2% | -19.4% | 3.3% |
| 2023 | 53.0% | 26.2% | 24.2% | 26.8% |
| 2024 | 40.0% | 24.9% | 23.3% | 15.1% |
| 2025 | 39.1% | 17.7% | 16.4% | 21.4% |
| 2026 (YTD) | 26.8% | 12.6% | 11.8% | 14.2% |

## T36. Optimisation failures in all the runs of the backtest

*Report section: Methods: optimisation failures*

| Item | Number |
|---|---|
| Optimisations that failed twice (equal weights used) | 0 |

Note: The brief asks to document failures. Each failed SLSQP optimisation is retried once with a looser tolerance; if it fails again, equal weights are used and the failure is logged in results/04_optimisation_failures.csv.

## T37. Trade-offs: return, downside risk, concentration, turnover and complexity (medians, net of 10 bps)

*Report section: 6. Conclusions and recommendation*

| Portfolio | Median return | Median volatility | Median max drawdown | Median Sharpe | % beats EW (Sharpe) | Effective N | Turnover (annual) | What is estimated | Complexity |
|---|---|---|---|---|---|---|---|---|---|
| EW | 31.2% | 16.9% | -11.1% | 1.81 |  | 12.0 | 0.27 | nothing | Low |
| Markowitz (λ=3) | 39.8% | 34.5% | -23.5% | 1.23 | 21 | 1.5 | 2.21 | expected returns, covariances, λ (optimiser) | High |
| GMV | 17.3% | 12.8% | -9.8% | 1.34 | 31 | 4.4 | 0.95 | covariances (optimiser) | Medium |
| Max Sharpe | 27.9% | 20.8% | -14.4% | 1.29 | 34 | 2.8 | 2.14 | expected returns, covariances, r_f (optimiser) | High |
| Inverse vol | 25.7% | 14.7% | -9.8% | 1.78 | 47 | 10.9 | 0.27 | volatilities only (simple formula) | Low |
| Risk parity (ERC) | 26.5% | 14.4% | -10.0% | 1.80 | 51 | 10.7 | 0.31 | covariances (optimiser) | Medium |
| Most diversified | 28.7% | 15.2% | -10.7% | 1.70 | 47 | 6.3 | 0.84 | covariances (optimiser) | Medium |
| Max decorrelation | 33.3% | 19.0% | -13.1% | 1.66 | 41 | 7.1 | 0.86 | correlations (optimiser) | Medium |
| Group pick (23 stocks) | 35.6% | 15.8% | -10.1% | 1.70 | 62 | 23.0 | 0.28 | nothing (but the stock selection was made with hindsight) | Low |
| SPY (buy & hold) | 17.7% | 14.0% | -9.4% | 1.13 | 15 |  | 0.00 | nothing (one ETF) | Lowest |

Note: Effective N = 1/Σw² (12 = equal weights on the 12 stocks of each experiment; the Group pick holds 22-23). Complexity = how much must be estimated and optimised at each rebalancing.

## TA01. Descriptive statistics of all 25 series (23 stocks, SPY, ^GSPC) at three frequencies

*Report section: Appendix: data*

| Asset | Frequency | N | Mean | Std. dev. | Min | Max | Skewness | Excess kurtosis | Ann. mean | Ann. volatility | JB p-value |
|---|---|---|---|---|---|---|---|---|---|---|---|
| NVDA | Daily | 4202 | 0.15% | 2.84% | -20.77% | 26.09% | 0.17 | 6.75 | 37.6% | 45.1% | <0.001 |
| NVDA | Weekly | 871 | 0.72% | 5.90% | -22.38% | 26.38% | 0.17 | 1.32 | 37.4% | 42.5% | <0.001 |
| NVDA | Monthly | 199 | 3.24% | 12.32% | -38.61% | 44.03% | -0.18 | 0.86 | 38.8% | 42.7% | 0.028 |
| AAPL | Daily | 4202 | 0.09% | 1.77% | -13.77% | 14.26% | -0.17 | 6.03 | 23.8% | 28.1% | <0.001 |
| AAPL | Weekly | 871 | 0.46% | 3.85% | -19.27% | 13.74% | -0.31 | 1.54 | 23.7% | 27.8% | <0.001 |
| AAPL | Monthly | 199 | 2.02% | 7.50% | -19.99% | 19.60% | -0.22 | -0.31 | 24.2% | 26.0% | 0.305 |
| MSFT | Daily | 4202 | 0.07% | 1.64% | -15.95% | 14.42% | -0.03 | 8.76 | 18.4% | 26.0% | <0.001 |
| MSFT | Weekly | 871 | 0.35% | 3.32% | -15.51% | 19.68% | 0.08 | 3.11 | 18.4% | 24.0% | <0.001 |
| MSFT | Monthly | 199 | 1.60% | 6.53% | -18.81% | 21.98% | -0.07 | 0.41 | 19.2% | 22.6% | 0.469 |
| AVGO | Daily | 4202 | 0.13% | 2.41% | -22.21% | 21.86% | -0.09 | 8.34 | 33.6% | 38.3% | <0.001 |
| AVGO | Weekly | 871 | 0.64% | 5.02% | -20.16% | 22.49% | 0.15 | 2.31 | 33.3% | 36.2% | <0.001 |
| AVGO | Monthly | 199 | 2.87% | 8.89% | -23.53% | 36.06% | 0.26 | 0.99 | 34.5% | 30.8% | 0.006 |
| AMD | Daily | 4202 | 0.10% | 3.55% | -27.75% | 42.06% | 0.30 | 8.73 | 24.3% | 56.3% | <0.001 |
| AMD | Weekly | 871 | 0.47% | 7.57% | -29.42% | 39.05% | 0.14 | 1.99 | 24.4% | 54.6% | <0.001 |
| AMD | Monthly | 199 | 2.08% | 16.23% | -52.85% | 55.54% | 0.01 | 0.80 | 25.0% | 56.2% | 0.072 |
| MU | Daily | 4202 | 0.11% | 3.19% | -22.09% | 21.06% | -0.08 | 4.02 | 27.4% | 50.6% | <0.001 |
| MU | Weekly | 871 | 0.52% | 6.72% | -31.10% | 32.02% | -0.21 | 1.51 | 27.1% | 48.5% | <0.001 |
| MU | Monthly | 199 | 2.37% | 13.82% | -39.37% | 63.00% | 0.29 | 1.74 | 28.5% | 47.9% | <0.001 |
| BRK-B | Daily | 4202 | 0.05% | 1.21% | -10.08% | 10.98% | -0.03 | 9.51 | 12.2% | 19.2% | <0.001 |
| BRK-B | Weekly | 871 | 0.23% | 2.50% | -14.40% | 9.32% | -0.20 | 2.61 | 12.2% | 18.0% | <0.001 |
| BRK-B | Monthly | 199 | 0.95% | 4.73% | -14.61% | 12.56% | -0.09 | -0.06 | 11.4% | 16.4% | 0.858 |
| JPM | Daily | 4202 | 0.06% | 1.72% | -16.21% | 16.56% | -0.11 | 9.43 | 15.1% | 27.4% | <0.001 |
| JPM | Weekly | 871 | 0.28% | 3.64% | -21.87% | 20.10% | -0.36 | 3.59 | 14.8% | 26.2% | <0.001 |
| JPM | Monthly | 199 | 1.32% | 7.16% | -25.97% | 19.50% | -0.65 | 1.55 | 15.9% | 24.8% | <0.001 |
| V | Daily | 4202 | 0.07% | 1.56% | -14.56% | 13.97% | -0.09 | 9.88 | 17.6% | 24.8% | <0.001 |
| V | Weekly | 871 | 0.34% | 3.12% | -18.13% | 18.15% | -0.26 | 4.89 | 17.6% | 22.5% | <0.001 |
| V | Monthly | 199 | 1.53% | 5.56% | -21.78% | 15.37% | -0.43 | 0.94 | 18.3% | 19.3% | 0.001 |
| LLY | Daily | 4202 | 0.09% | 1.67% | -15.24% | 14.57% | 0.36 | 11.21 | 23.4% | 26.6% | <0.001 |
| LLY | Weekly | 871 | 0.45% | 3.62% | -19.76% | 16.15% | -0.07 | 2.77 | 23.4% | 26.1% | <0.001 |
| LLY | Monthly | 199 | 1.97% | 6.70% | -19.57% | 22.17% | 0.11 | 0.62 | 23.6% | 23.2% | 0.160 |
| JNJ | Daily | 4202 | 0.05% | 1.08% | -10.58% | 7.69% | -0.30 | 8.71 | 11.5% | 17.1% | <0.001 |
| JNJ | Weekly | 871 | 0.22% | 2.26% | -11.34% | 10.89% | -0.16 | 2.16 | 11.5% | 16.3% | <0.001 |
| JNJ | Monthly | 199 | 0.97% | 4.48% | -12.96% | 13.47% | -0.05 | 0.09 | 11.6% | 15.5% | 0.931 |
| AMZN | Daily | 4202 | 0.09% | 2.07% | -15.14% | 14.62% | 0.10 | 6.11 | 21.8% | 32.8% | <0.001 |
| AMZN | Weekly | 871 | 0.42% | 4.28% | -15.62% | 17.74% | -0.02 | 1.49 | 21.7% | 30.9% | <0.001 |
| AMZN | Monthly | 199 | 1.87% | 8.51% | -27.12% | 24.11% | 0.00 | 0.50 | 22.5% | 29.5% | 0.354 |
| TSLA | Daily | 4080 | 0.13% | 3.60% | -23.65% | 21.83% | 0.00 | 4.73 | 33.6% | 57.1% | <0.001 |
| TSLA | Weekly | 846 | 0.67% | 7.54% | -29.92% | 34.16% | 0.19 | 1.47 | 34.7% | 54.4% | <0.001 |
| TSLA | Monthly | 194 | 2.81% | 16.44% | -45.78% | 59.37% | 0.46 | 0.85 | 33.7% | 56.9% | 0.002 |
| T | Daily | 4202 | 0.03% | 1.32% | -10.99% | 9.55% | -0.46 | 7.89 | 8.1% | 21.0% | <0.001 |
| T | Weekly | 871 | 0.16% | 2.86% | -19.19% | 13.57% | -0.35 | 4.30 | 8.3% | 20.6% | <0.001 |
| T | Monthly | 199 | 0.74% | 5.71% | -18.92% | 19.02% | -0.32 | 0.89 | 8.9% | 19.8% | 0.007 |
| GOOGL | Daily | 4202 | 0.07% | 1.75% | -12.37% | 15.06% | 0.15 | 6.82 | 18.7% | 27.8% | <0.001 |
| GOOGL | Weekly | 871 | 0.36% | 3.81% | -13.84% | 22.96% | 0.33 | 2.27 | 18.8% | 27.4% | <0.001 |
| GOOGL | Monthly | 199 | 1.63% | 7.37% | -19.78% | 29.13% | 0.13 | 0.49 | 19.6% | 25.5% | 0.268 |
| GE | Daily | 4202 | 0.04% | 1.99% | -16.44% | 13.74% | -0.17 | 6.81 | 10.6% | 31.6% | <0.001 |
| GE | Weekly | 871 | 0.20% | 4.37% | -19.59% | 18.18% | -0.34 | 2.74 | 10.1% | 31.5% | <0.001 |
| GE | Monthly | 199 | 0.90% | 9.08% | -31.40% | 31.62% | -0.14 | 1.79 | 10.8% | 31.4% | <0.001 |
| CAT | Daily | 4202 | 0.07% | 1.88% | -15.41% | 11.01% | -0.20 | 4.07 | 18.2% | 29.9% | <0.001 |
| CAT | Weekly | 871 | 0.34% | 4.08% | -19.76% | 14.24% | -0.27 | 1.22 | 17.9% | 29.4% | <0.001 |
| CAT | Monthly | 199 | 1.57% | 8.80% | -26.58% | 28.37% | -0.06 | 0.53 | 18.8% | 30.5% | 0.291 |
| WMT | Daily | 4202 | 0.05% | 1.26% | -12.08% | 11.07% | -0.25 | 14.32 | 12.7% | 20.0% | <0.001 |
| WMT | Weekly | 871 | 0.24% | 2.73% | -21.67% | 10.93% | -0.85 | 6.67 | 12.7% | 19.7% | <0.001 |
| WMT | Monthly | 199 | 1.06% | 5.17% | -16.98% | 13.78% | -0.36 | 0.84 | 12.7% | 17.9% | 0.006 |
| COST | Daily | 4202 | 0.07% | 1.28% | -13.30% | 9.49% | -0.42 | 8.34 | 18.4% | 20.3% | <0.001 |
| COST | Weekly | 871 | 0.35% | 2.78% | -17.74% | 12.26% | -0.43 | 3.23 | 18.3% | 20.0% | <0.001 |
| COST | Monthly | 199 | 1.58% | 5.36% | -16.66% | 13.83% | -0.40 | 0.35 | 19.0% | 18.6% | 0.041 |
| XOM | Daily | 4202 | 0.04% | 1.58% | -13.04% | 11.94% | -0.20 | 6.65 | 8.9% | 25.0% | <0.001 |
| XOM | Weekly | 871 | 0.17% | 3.46% | -22.40% | 15.47% | -0.40 | 4.41 | 8.8% | 25.0% | <0.001 |
| XOM | Monthly | 199 | 0.77% | 6.90% | -30.36% | 23.84% | -0.17 | 2.75 | 9.3% | 23.9% | <0.001 |
| NEE | Daily | 4202 | 0.05% | 1.41% | -14.41% | 12.83% | -0.45 | 10.13 | 13.7% | 22.4% | <0.001 |
| NEE | Weekly | 871 | 0.26% | 3.02% | -20.44% | 19.03% | -0.73 | 6.63 | 13.7% | 21.8% | <0.001 |
| NEE | Monthly | 199 | 1.21% | 5.52% | -17.82% | 17.80% | -0.56 | 1.16 | 14.5% | 19.1% | <0.001 |
| WELL | Daily | 4202 | 0.06% | 1.79% | -27.97% | 20.85% | -0.93 | 33.48 | 14.1% | 28.4% | <0.001 |
| WELL | Weekly | 871 | 0.27% | 4.08% | -36.62% | 41.81% | -0.12 | 24.50 | 14.0% | 29.4% | <0.001 |
| WELL | Monthly | 199 | 1.21% | 7.08% | -49.12% | 16.92% | -1.81 | 11.60 | 14.5% | 24.5% | <0.001 |
| LIN | Daily | 4202 | 0.05% | 1.33% | -10.85% | 11.06% | -0.08 | 6.13 | 12.3% | 21.2% | <0.001 |
| LIN | Weekly | 871 | 0.23% | 2.80% | -15.41% | 15.59% | -0.06 | 3.46 | 12.2% | 20.2% | <0.001 |
| LIN | Monthly | 199 | 1.10% | 5.09% | -12.71% | 15.16% | 0.04 | 0.25 | 13.2% | 17.6% | 0.750 |
| SPY | Daily | 4202 | 0.05% | 1.08% | -11.59% | 9.99% | -0.55 | 12.40 | 13.2% | 17.1% | <0.001 |
| SPY | Weekly | 871 | 0.25% | 2.24% | -15.72% | 11.41% | -0.74 | 5.83 | 13.1% | 16.2% | <0.001 |
| SPY | Monthly | 199 | 1.14% | 4.13% | -13.34% | 11.95% | -0.49 | 0.67 | 13.6% | 14.3% | 0.003 |
| ^GSPC | Daily | 4202 | 0.05% | 1.08% | -12.77% | 9.09% | -0.61 | 13.49 | 11.5% | 17.2% | <0.001 |
| ^GSPC | Weekly | 871 | 0.22% | 2.25% | -16.23% | 11.42% | -0.77 | 6.07 | 11.3% | 16.2% | <0.001 |
| ^GSPC | Monthly | 199 | 0.99% | 4.14% | -13.37% | 11.94% | -0.49 | 0.68 | 11.9% | 14.4% | 0.003 |

## TA02. The 100 experiments: periods and the 12 stocks drawn (seed 2026)

*Report section: Appendix: backtest design*

| Experiment | Estimation start | Evaluation start | Evaluation end | N eligible | Assets |
|---|---|---|---|---|---|
| 1 | 2019-03-05 | 2021-03-04 | 2022-03-02 | 23 | AAPL, AMD, AVGO, CAT, COST, GE, GOOGL, JNJ, JPM, LLY, V, WMT |
| 2 | 2014-01-10 | 2016-01-12 | 2017-01-10 | 23 | AAPL, AMD, AMZN, AVGO, COST, GOOGL, JNJ, JPM, MSFT, NVDA, T, TSLA |
| 3 | 2023-01-27 | 2025-01-31 | 2026-02-02 | 23 | AAPL, AMD, GOOGL, JNJ, JPM, LIN, MSFT, NEE, V, WELL, WMT, XOM |
| 4 | 2018-05-30 | 2020-06-01 | 2021-05-28 | 23 | AMD, BRK-B, COST, JNJ, JPM, LLY, MSFT, MU, T, V, WMT, XOM |
| 5 | 2013-02-25 | 2015-02-25 | 2016-02-24 | 23 | AMD, AMZN, BRK-B, COST, GOOGL, JNJ, JPM, LLY, NVDA, TSLA, WELL, XOM |
| 6 | 2015-12-15 | 2017-12-14 | 2018-12-14 | 23 | CAT, COST, GE, JPM, LLY, MSFT, NEE, NVDA, T, V, WELL, XOM |
| 7 | 2012-05-30 | 2014-06-03 | 2015-06-02 | 23 | AMD, AMZN, AVGO, CAT, GOOGL, MSFT, MU, NEE, T, TSLA, WMT, XOM |
| 8 | 2021-04-20 | 2023-04-20 | 2024-04-19 | 23 | BRK-B, CAT, GE, JNJ, JPM, LLY, MSFT, MU, NEE, TSLA, WELL, XOM |
| 9 | 2018-06-01 | 2020-06-03 | 2021-06-02 | 23 | AAPL, AVGO, CAT, GE, GOOGL, JNJ, JPM, MU, NVDA, TSLA, V, WMT |
| 10 | 2020-03-09 | 2022-03-08 | 2023-03-08 | 23 | AAPL, BRK-B, CAT, COST, JNJ, LIN, MSFT, NEE, NVDA, T, TSLA, XOM |
| 11 | 2019-04-24 | 2021-04-23 | 2022-04-21 | 23 | AAPL, AMD, BRK-B, COST, JNJ, JPM, MSFT, MU, NVDA, TSLA, V, WELL |
| 12 | 2021-11-05 | 2023-11-08 | 2024-11-07 | 23 | AAPL, AMD, AVGO, BRK-B, COST, GE, LLY, MSFT, NEE, TSLA, V, XOM |
| 13 | 2020-07-14 | 2022-07-14 | 2023-07-14 | 23 | AAPL, AVGO, BRK-B, CAT, GE, JNJ, JPM, LLY, MU, NVDA, TSLA, WELL |
| 14 | 2020-06-03 | 2022-06-02 | 2023-06-02 | 23 | AMD, AMZN, AVGO, CAT, LIN, LLY, MSFT, NEE, NVDA, T, TSLA, V |
| 15 | 2014-10-16 | 2016-10-17 | 2017-10-16 | 23 | AMD, BRK-B, COST, GOOGL, JPM, LLY, MSFT, NEE, T, TSLA, V, XOM |
| 16 | 2013-05-14 | 2015-05-14 | 2016-05-12 | 23 | AMZN, CAT, COST, GOOGL, JNJ, JPM, LLY, MSFT, MU, NEE, WELL, WMT |
| 17 | 2016-08-19 | 2018-08-21 | 2019-08-21 | 23 | AAPL, AMZN, AVGO, COST, GE, JPM, LLY, MU, NVDA, WELL, WMT, XOM |
| 18 | 2010-01-22 | 2012-01-23 | 2013-01-23 | 22 | AMD, COST, GOOGL, JPM, LIN, MSFT, MU, NEE, NVDA, T, V, WELL |
| 19 | 2010-04-08 | 2012-04-05 | 2013-04-09 | 22 | AMZN, BRK-B, CAT, GE, GOOGL, LLY, MSFT, NEE, NVDA, V, WMT, XOM |
| 20 | 2023-02-15 | 2025-02-20 | 2026-02-20 | 23 | AMD, AMZN, AVGO, BRK-B, CAT, COST, GOOGL, JNJ, LIN, MSFT, TSLA, WELL |
| 21 | 2022-08-24 | 2024-08-27 | 2025-08-28 | 23 | AAPL, AMD, CAT, COST, GE, JNJ, JPM, T, TSLA, WELL, WMT, XOM |
| 22 | 2018-09-07 | 2020-09-09 | 2021-09-08 | 23 | AAPL, AMZN, CAT, COST, JPM, LLY, MSFT, T, TSLA, V, WMT, XOM |
| 23 | 2014-11-28 | 2016-11-29 | 2017-11-28 | 23 | AAPL, AMD, AVGO, COST, GE, JPM, LLY, MU, T, WELL, WMT, XOM |
| 24 | 2010-05-10 | 2012-05-08 | 2013-05-09 | 22 | AAPL, AMD, AMZN, COST, GOOGL, JNJ, LLY, MU, T, WELL, WMT, XOM |
| 25 | 2010-03-23 | 2012-03-21 | 2013-03-22 | 22 | AAPL, AMD, BRK-B, CAT, COST, JPM, LIN, NEE, V, WELL, WMT, XOM |
| 26 | 2020-04-22 | 2022-04-21 | 2023-04-21 | 23 | AAPL, BRK-B, CAT, GE, JNJ, JPM, LLY, MU, NVDA, T, V, WELL |
| 27 | 2011-09-06 | 2013-09-09 | 2014-09-08 | 23 | AMD, AMZN, GE, GOOGL, JNJ, MSFT, MU, NEE, NVDA, TSLA, WMT, XOM |
| 28 | 2016-08-16 | 2018-08-16 | 2019-08-16 | 23 | AMZN, COST, GE, GOOGL, JNJ, LIN, LLY, MSFT, MU, T, WELL, XOM |
| 29 | 2015-01-21 | 2017-01-20 | 2018-01-19 | 23 | AMD, CAT, JPM, LIN, LLY, MSFT, MU, NEE, T, V, WMT, XOM |
| 30 | 2019-08-30 | 2021-08-31 | 2022-08-30 | 23 | AAPL, AMD, AMZN, AVGO, COST, GE, GOOGL, JNJ, MSFT, T, WELL, XOM |
| 31 | 2022-06-24 | 2024-06-27 | 2025-06-30 | 23 | AVGO, BRK-B, COST, JNJ, JPM, LIN, NVDA, T, TSLA, V, WMT, XOM |
| 32 | 2020-10-06 | 2022-10-06 | 2023-10-06 | 23 | AAPL, AMZN, CAT, COST, GOOGL, JNJ, LIN, NVDA, T, WELL, WMT, XOM |
| 33 | 2013-09-19 | 2015-09-21 | 2016-09-19 | 23 | AMZN, AVGO, BRK-B, GE, JPM, MSFT, MU, T, TSLA, V, WMT, XOM |
| 34 | 2012-03-19 | 2014-03-21 | 2015-03-20 | 23 | AAPL, AMD, AMZN, AVGO, GE, JNJ, JPM, LIN, LLY, MU, NVDA, V |
| 35 | 2014-03-31 | 2016-03-31 | 2017-03-29 | 23 | AAPL, AVGO, JNJ, JPM, LIN, LLY, NEE, NVDA, T, V, WMT, XOM |
| 36 | 2021-07-30 | 2023-08-02 | 2024-08-01 | 23 | AAPL, AMD, AVGO, CAT, JNJ, LIN, MSFT, NEE, NVDA, T, V, WMT |
| 37 | 2018-03-28 | 2020-03-30 | 2021-03-29 | 23 | AMZN, AVGO, CAT, COST, GOOGL, JPM, LIN, NEE, T, TSLA, V, WELL |
| 38 | 2020-09-09 | 2022-09-09 | 2023-09-11 | 23 | AAPL, AMD, AMZN, AVGO, BRK-B, GE, JPM, LIN, LLY, NVDA, T, XOM |
| 39 | 2011-04-26 | 2013-04-29 | 2014-04-28 | 23 | AAPL, AMD, AMZN, CAT, GE, LIN, MSFT, T, TSLA, V, WELL, WMT |
| 40 | 2021-05-03 | 2023-05-03 | 2024-05-02 | 23 | AAPL, AMZN, AVGO, GE, GOOGL, JPM, LLY, NVDA, TSLA, V, WELL, WMT |
| 41 | 2023-03-06 | 2025-03-10 | 2026-03-10 | 23 | AVGO, BRK-B, JNJ, JPM, LIN, LLY, MU, NEE, NVDA, V, WELL, WMT |
| 42 | 2018-11-06 | 2020-11-06 | 2021-11-05 | 23 | AMD, AMZN, BRK-B, GE, JNJ, LIN, MSFT, MU, NEE, T, TSLA, XOM |
| 43 | 2020-04-16 | 2022-04-14 | 2023-04-17 | 23 | AAPL, AMD, AMZN, COST, GOOGL, JNJ, JPM, MSFT, NVDA, T, V, XOM |
| 44 | 2014-11-21 | 2016-11-22 | 2017-11-21 | 23 | AAPL, BRK-B, CAT, COST, GE, JNJ, LLY, MSFT, MU, NEE, NVDA, XOM |
| 45 | 2017-03-06 | 2019-03-07 | 2020-03-05 | 23 | AAPL, BRK-B, CAT, COST, GE, LIN, LLY, MSFT, MU, NVDA, TSLA, WELL |
| 46 | 2015-01-21 | 2017-01-20 | 2018-01-19 | 23 | AVGO, BRK-B, CAT, GOOGL, JPM, MU, NEE, T, TSLA, V, WELL, WMT |
| 47 | 2012-06-20 | 2014-06-24 | 2015-06-23 | 23 | AAPL, CAT, COST, GE, JNJ, JPM, LIN, NEE, NVDA, V, WMT, XOM |
| 48 | 2019-01-09 | 2021-01-08 | 2022-01-06 | 23 | AMD, AVGO, BRK-B, CAT, COST, LIN, LLY, T, TSLA, V, WELL, WMT |
| 49 | 2015-10-08 | 2017-10-09 | 2018-10-08 | 23 | AAPL, AMD, AMZN, BRK-B, CAT, JNJ, JPM, LLY, NEE, T, V, XOM |
| 50 | 2011-05-20 | 2013-05-23 | 2014-05-22 | 23 | AMZN, BRK-B, CAT, COST, GOOGL, LIN, MSFT, NVDA, TSLA, V, WELL, XOM |
| 51 | 2018-12-21 | 2020-12-22 | 2021-12-21 | 23 | AAPL, AMD, AMZN, AVGO, GE, JPM, LIN, LLY, MU, NEE, NVDA, WMT |
| 52 | 2013-06-10 | 2015-06-10 | 2016-06-08 | 23 | AAPL, AMD, BRK-B, CAT, COST, JNJ, JPM, LLY, MSFT, NEE, WMT, XOM |
| 53 | 2018-09-11 | 2020-09-11 | 2021-09-10 | 23 | AAPL, AVGO, BRK-B, CAT, COST, LLY, MSFT, NVDA, TSLA, WELL, WMT, XOM |
| 54 | 2013-05-29 | 2015-05-29 | 2016-05-26 | 23 | AAPL, AVGO, COST, JNJ, LIN, LLY, MSFT, MU, NVDA, TSLA, V, WMT |
| 55 | 2014-05-23 | 2016-05-24 | 2017-05-23 | 23 | AMZN, AVGO, BRK-B, GOOGL, JNJ, JPM, NEE, NVDA, T, TSLA, V, WELL |
| 56 | 2017-01-12 | 2019-01-15 | 2020-01-14 | 23 | AAPL, AMD, AMZN, CAT, COST, GE, JNJ, LIN, LLY, MU, TSLA, WMT |
| 57 | 2016-01-08 | 2018-01-09 | 2019-01-09 | 23 | AAPL, AVGO, BRK-B, COST, GE, GOOGL, JNJ, LIN, T, TSLA, V, XOM |
| 58 | 2023-03-08 | 2025-03-12 | 2026-03-12 | 23 | AAPL, AVGO, CAT, COST, GE, JNJ, JPM, LIN, LLY, MU, NEE, T |
| 59 | 2023-08-23 | 2025-08-27 | 2026-08-27 | 23 | AAPL, AMZN, BRK-B, GE, GOOGL, JNJ, JPM, LIN, MSFT, MU, T, TSLA |
| 60 | 2016-02-24 | 2018-02-23 | 2019-02-25 | 23 | AAPL, AMZN, AVGO, CAT, COST, GOOGL, JNJ, JPM, MSFT, T, TSLA, V |
| 61 | 2016-02-03 | 2018-02-02 | 2019-02-04 | 23 | AAPL, AMD, AMZN, AVGO, BRK-B, COST, LLY, MU, NVDA, TSLA, V, WMT |
| 62 | 2017-11-08 | 2019-11-11 | 2020-11-09 | 23 | AMZN, BRK-B, COST, JNJ, JPM, LLY, MSFT, NVDA, T, V, WELL, XOM |
| 63 | 2020-10-07 | 2022-10-07 | 2023-10-09 | 23 | AMD, AMZN, AVGO, GE, JPM, MU, NVDA, T, TSLA, V, WELL, XOM |
| 64 | 2019-11-26 | 2021-11-26 | 2022-11-25 | 23 | AVGO, CAT, COST, GE, GOOGL, JNJ, JPM, LLY, NVDA, V, WMT, XOM |
| 65 | 2022-02-02 | 2024-02-06 | 2025-02-06 | 23 | AAPL, AMD, AMZN, CAT, COST, GE, JPM, LIN, MSFT, MU, V, WMT |
| 66 | 2022-07-01 | 2024-07-05 | 2025-07-08 | 23 | AMD, AVGO, COST, GE, GOOGL, JNJ, MSFT, NVDA, T, V, WELL, WMT |
| 67 | 2018-08-20 | 2020-08-20 | 2021-08-19 | 23 | AMD, AMZN, JNJ, JPM, MSFT, MU, NVDA, TSLA, V, WELL, WMT, XOM |
| 68 | 2010-12-30 | 2013-01-02 | 2013-12-31 | 23 | AAPL, GE, JPM, LIN, LLY, MSFT, MU, NVDA, T, TSLA, WELL, WMT |
| 69 | 2022-12-21 | 2024-12-24 | 2025-12-26 | 23 | AAPL, AMD, BRK-B, CAT, COST, LIN, MSFT, MU, NEE, NVDA, WELL, WMT |
| 70 | 2018-06-20 | 2020-06-22 | 2021-06-21 | 23 | AAPL, AMD, AMZN, BRK-B, COST, LIN, LLY, MSFT, T, TSLA, V, WMT |
| 71 | 2010-06-17 | 2012-06-15 | 2013-06-18 | 22 | AAPL, AVGO, COST, GE, JNJ, LIN, LLY, MSFT, NEE, V, WMT, XOM |
| 72 | 2019-07-19 | 2021-07-20 | 2022-07-19 | 23 | AAPL, BRK-B, CAT, GE, JNJ, LIN, LLY, MSFT, MU, T, V, WMT |
| 73 | 2011-02-16 | 2013-02-20 | 2014-02-19 | 23 | AAPL, AMZN, CAT, GOOGL, JNJ, JPM, LIN, LLY, MSFT, NEE, NVDA, WMT |
| 74 | 2016-01-19 | 2018-01-18 | 2019-01-17 | 23 | AAPL, AMD, BRK-B, JPM, LIN, LLY, MSFT, NEE, NVDA, T, TSLA, WELL |
| 75 | 2015-03-30 | 2017-03-29 | 2018-03-28 | 23 | AAPL, GE, JNJ, LIN, MSFT, MU, NEE, NVDA, T, TSLA, WMT, XOM |
| 76 | 2022-07-14 | 2024-07-17 | 2025-07-18 | 23 | AMD, BRK-B, CAT, COST, GE, GOOGL, MSFT, NEE, NVDA, V, WMT, XOM |
| 77 | 2011-02-24 | 2013-02-27 | 2014-02-26 | 23 | AMZN, AVGO, BRK-B, COST, GE, GOOGL, LLY, MU, NVDA, WELL, WMT, XOM |
| 78 | 2020-07-01 | 2022-07-01 | 2023-07-03 | 23 | AMD, AMZN, CAT, JNJ, LIN, LLY, MU, NEE, TSLA, WELL, WMT, XOM |
| 79 | 2011-10-06 | 2013-10-09 | 2014-10-08 | 23 | AAPL, AMZN, AVGO, CAT, COST, GE, GOOGL, JPM, LLY, MSFT, NVDA, WELL |
| 80 | 2017-11-03 | 2019-11-06 | 2020-11-04 | 23 | AAPL, AMD, CAT, COST, GE, JNJ, JPM, LIN, MU, WELL, WMT, XOM |
| 81 | 2018-03-21 | 2020-03-23 | 2021-03-22 | 23 | AAPL, AMD, AVGO, BRK-B, JNJ, JPM, LIN, LLY, MSFT, NVDA, V, WMT |
| 82 | 2011-04-29 | 2013-05-02 | 2014-05-01 | 23 | AAPL, AMZN, BRK-B, COST, JNJ, JPM, LLY, MSFT, T, TSLA, WMT, XOM |
| 83 | 2012-11-19 | 2014-11-19 | 2015-11-18 | 23 | AAPL, BRK-B, CAT, COST, GOOGL, JNJ, LLY, MSFT, T, TSLA, WELL, WMT |
| 84 | 2021-03-02 | 2023-03-02 | 2024-03-01 | 23 | AAPL, AMD, AMZN, BRK-B, CAT, LIN, MU, NVDA, TSLA, V, WELL, WMT |
| 85 | 2012-08-06 | 2014-08-08 | 2015-08-07 | 23 | AAPL, AMD, COST, GE, JNJ, JPM, LIN, MSFT, MU, V, WELL, WMT |
| 86 | 2023-06-14 | 2025-06-18 | 2026-06-18 | 23 | AAPL, AMZN, COST, GE, GOOGL, LIN, MSFT, NEE, V, WELL, WMT, XOM |
| 87 | 2021-10-07 | 2023-10-10 | 2024-10-09 | 23 | AMD, AMZN, BRK-B, COST, JNJ, LIN, NVDA, T, V, WELL, WMT, XOM |
| 88 | 2011-02-18 | 2013-02-22 | 2014-02-21 | 23 | BRK-B, CAT, GE, JNJ, JPM, LLY, MSFT, MU, T, TSLA, WELL, WMT |
| 89 | 2013-05-29 | 2015-05-29 | 2016-05-26 | 23 | CAT, GE, JNJ, JPM, LLY, MSFT, MU, NVDA, T, TSLA, V, WELL |
| 90 | 2014-01-21 | 2016-01-21 | 2017-01-19 | 23 | AAPL, AMD, AMZN, BRK-B, COST, GOOGL, JNJ, MSFT, NVDA, T, V, WELL |
| 91 | 2012-01-04 | 2014-01-07 | 2015-01-06 | 23 | AAPL, AMD, AMZN, AVGO, BRK-B, CAT, COST, GOOGL, MSFT, T, WELL, WMT |
| 92 | 2010-04-12 | 2012-04-10 | 2013-04-11 | 22 | AMZN, AVGO, COST, GE, GOOGL, JPM, LIN, MSFT, NEE, NVDA, T, XOM |
| 93 | 2018-05-29 | 2020-05-29 | 2021-05-27 | 23 | AMD, COST, GE, GOOGL, JPM, LLY, MSFT, NEE, T, TSLA, WELL, XOM |
| 94 | 2017-03-16 | 2019-03-19 | 2020-03-17 | 23 | AMD, AMZN, AVGO, GE, GOOGL, JPM, LLY, NEE, NVDA, V, WELL, WMT |
| 95 | 2021-08-18 | 2023-08-21 | 2024-08-20 | 23 | AMD, BRK-B, GE, GOOGL, JPM, LIN, MSFT, MU, NEE, NVDA, T, XOM |
| 96 | 2018-05-09 | 2020-05-11 | 2021-05-10 | 23 | AMZN, AVGO, BRK-B, LIN, LLY, MSFT, NVDA, T, TSLA, WELL, WMT, XOM |
| 97 | 2021-07-08 | 2023-07-11 | 2024-07-10 | 23 | AAPL, AVGO, BRK-B, COST, GE, JNJ, JPM, LIN, MU, NVDA, TSLA, WMT |
| 98 | 2011-05-27 | 2013-05-31 | 2014-05-30 | 23 | AAPL, AMZN, AVGO, BRK-B, CAT, GOOGL, JNJ, LLY, NVDA, T, V, WELL |
| 99 | 2014-10-13 | 2016-10-12 | 2017-10-11 | 23 | AVGO, COST, GE, GOOGL, JPM, MSFT, MU, NEE, NVDA, T, V, XOM |
| 100 | 2020-05-12 | 2022-05-11 | 2023-05-11 | 23 | AVGO, CAT, COST, GE, GOOGL, MSFT, MU, NEE, NVDA, TSLA, V, WMT |

## TA03. Illustration: weights of each strategy with the last 12 months of data (23 stocks)

*Report section: Appendix: strategies*

| Stock | EW | Markowitz (λ=3) | GMV | Max Sharpe | Inverse vol | Risk parity (ERC) | Most diversified | Max decorrelation |
|---|---|---|---|---|---|---|---|---|
| NVDA | 4.3% | 0.0% | 5.7% | 0.0% | 3.2% | 3.2% | 4.1% | 5.5% |
| AAPL | 4.3% | 0.0% | 1.3% | 10.9% | 4.8% | 3.8% | 1.1% | 1.0% |
| MSFT | 4.3% | 0.0% | 5.4% | 2.4% | 3.7% | 4.8% | 6.5% | 7.5% |
| AVGO | 4.3% | 0.0% | 2.7% | 0.0% | 2.6% | 2.6% | 3.6% | 5.9% |
| AMD | 4.3% | 12.1% | 0.0% | 4.3% | 1.7% | 1.5% | 1.4% | 3.6% |
| MU | 4.3% | 76.3% | 2.1% | 9.1% | 1.5% | 1.8% | 3.1% | 8.9% |
| BRK-B | 4.3% | 0.0% | 22.0% | 1.5% | 8.2% | 8.1% | 9.3% | 4.8% |
| JPM | 4.3% | 0.0% | 0.8% | 0.0% | 5.4% | 3.7% | 0.0% | 0.0% |
| V | 4.3% | 0.0% | 3.0% | 2.4% | 5.4% | 5.3% | 5.9% | 4.6% |
| LLY | 4.3% | 0.0% | 0.0% | 0.9% | 3.4% | 3.2% | 4.1% | 5.2% |
| JNJ | 4.3% | 11.6% | 10.2% | 33.5% | 6.3% | 6.1% | 5.4% | 3.6% |
| AMZN | 4.3% | 0.0% | 1.4% | 0.0% | 3.5% | 3.0% | 2.5% | 3.0% |
| TSLA | 4.3% | 0.0% | 0.0% | 0.0% | 2.6% | 2.0% | 0.8% | 1.2% |
| T | 4.3% | 0.0% | 6.0% | 0.0% | 4.7% | 6.8% | 9.5% | 8.5% |
| GOOGL | 4.3% | 0.0% | 2.2% | 4.6% | 3.8% | 2.8% | 1.4% | 1.6% |
| GE | 4.3% | 0.0% | 1.1% | 0.0% | 3.6% | 2.8% | 3.2% | 3.7% |
| CAT | 4.3% | 0.0% | 0.7% | 0.0% | 3.0% | 2.2% | 0.0% | 0.0% |
| WMT | 4.3% | 0.0% | 0.8% | 0.0% | 4.6% | 4.3% | 4.4% | 4.0% |
| COST | 4.3% | 0.0% | 8.1% | 0.0% | 6.0% | 6.1% | 5.3% | 3.7% |
| XOM | 4.3% | 0.0% | 11.9% | 21.9% | 4.6% | 10.5% | 15.3% | 14.0% |
| NEE | 4.3% | 0.0% | 2.3% | 0.0% | 5.7% | 4.0% | 0.0% | 0.0% |
| WELL | 4.3% | 0.0% | 4.2% | 8.4% | 5.3% | 5.2% | 6.5% | 5.3% |
| LIN | 4.3% | 0.0% | 8.0% | 0.0% | 6.3% | 6.3% | 6.5% | 4.4% |

## TA04. Illustration: ex-ante characteristics of each strategy (last 12 months, 23 stocks)

*Report section: Appendix: strategies*

| Portfolio | Exp. return | Volatility | Sharpe (ex-ante) | Effective N (1/Σw²) | Max weight | N assets with w > 1% | Diversification ratio |
|---|---|---|---|---|---|---|---|
| EW | 34.9% | 12.8% | 2.35 | 23.0 | 4.3% | 23 | 2.56 |
| Markowitz (λ=3) | 190.3% | 67.2% | 2.76 | 1.6 | 76.3% | 3 | 1.09 |
| GMV | 21.4% | 7.6% | 2.17 | 9.9 | 22.0% | 17 | 3.21 |
| Max Sharpe | 60.7% | 11.8% | 4.72 | 5.2 | 33.5% | 10 | 2.58 |
| Inverse vol | 24.3% | 9.3% | 2.08 | 20.3 | 8.2% | 23 | 2.96 |
| Risk parity (ERC) | 24.7% | 8.4% | 2.35 | 18.4 | 10.5% | 23 | 3.27 |
| Most diversified | 26.2% | 8.2% | 2.60 | 13.7 | 15.3% | 19 | 3.45 |
| Max decorrelation | 41.8% | 12.6% | 2.94 | 14.9 | 14.0% | 19 | 2.76 |

## TA05. Inverse volatility vs ERC: weights and risk contributions (last 12 months, 23 stocks)

*Report section: Appendix: strategies*

| Stock | Weight IV | Risk contrib. IV | Weight ERC | Risk contrib. ERC | Avg. correlation with others |
|---|---|---|---|---|---|
| NVDA | 3.2% | 4.4% | 3.2% | 4.3% | 0.08 |
| AAPL | 4.8% | 5.4% | 3.8% | 4.3% | 0.10 |
| MSFT | 3.7% | 2.7% | 4.8% | 4.3% | 0.03 |
| AVGO | 2.6% | 4.4% | 2.6% | 4.3% | 0.08 |
| AMD | 1.7% | 5.0% | 1.5% | 4.3% | 0.09 |
| MU | 1.5% | 3.8% | 1.8% | 4.3% | 0.06 |
| BRK-B | 8.2% | 3.9% | 8.1% | 4.3% | 0.06 |
| JPM | 5.4% | 6.5% | 3.7% | 4.3% | 0.13 |
| V | 5.4% | 4.0% | 5.3% | 4.3% | 0.06 |
| LLY | 3.4% | 4.5% | 3.2% | 4.3% | 0.08 |
| JNJ | 6.3% | 3.8% | 6.1% | 4.3% | 0.06 |
| AMZN | 3.5% | 5.3% | 3.0% | 4.3% | 0.10 |
| TSLA | 2.6% | 5.8% | 2.0% | 4.3% | 0.11 |
| T | 4.7% | 1.4% | 6.8% | 4.3% | -0.01 |
| GOOGL | 3.8% | 6.6% | 2.8% | 4.3% | 0.14 |
| GE | 3.6% | 6.6% | 2.8% | 4.3% | 0.14 |
| CAT | 3.0% | 6.5% | 2.2% | 4.3% | 0.13 |
| WMT | 4.6% | 3.9% | 4.3% | 4.3% | 0.06 |
| COST | 6.0% | 3.2% | 6.1% | 4.3% | 0.04 |
| XOM | 4.6% | -1.0% | 10.5% | 4.3% | -0.07 |
| NEE | 5.7% | 5.6% | 4.0% | 4.3% | 0.11 |
| WELL | 5.3% | 4.0% | 5.2% | 4.3% | 0.06 |
| LIN | 6.3% | 3.6% | 6.3% | 4.3% | 0.05 |

## TA06. Average weight of each stock when it is drawn, by strategy

*Report section: Appendix: weights*

| Stock | EW | Markowitz (λ=3) | GMV | Max Sharpe | Inverse vol | Risk parity (ERC) | Most diversified | Max decorrelation |
|---|---|---|---|---|---|---|---|---|
| NVDA | 8.3% | 30.2% | 0.9% | 11.6% | 5.0% | 4.9% | 5.3% | 8.7% |
| AAPL | 8.3% | 8.9% | 3.2% | 7.4% | 7.5% | 7.2% | 5.5% | 6.3% |
| MSFT | 8.3% | 2.1% | 3.2% | 3.2% | 8.2% | 7.3% | 3.3% | 3.3% |
| AVGO | 8.3% | 12.2% | 0.7% | 5.7% | 6.2% | 5.7% | 3.8% | 5.5% |
| AMD | 8.3% | 10.1% | 0.3% | 4.6% | 4.2% | 4.4% | 6.0% | 11.5% |
| MU | 8.3% | 11.5% | 0.2% | 3.6% | 4.8% | 4.7% | 5.2% | 9.1% |
| BRK-B | 8.3% | 0.3% | 13.6% | 6.1% | 11.7% | 9.6% | 0.5% | 0.3% |
| JPM | 8.3% | 2.5% | 3.6% | 5.5% | 8.2% | 7.5% | 4.5% | 4.5% |
| V | 8.3% | 6.1% | 4.5% | 5.2% | 9.2% | 8.0% | 2.6% | 2.5% |
| LLY | 8.3% | 17.2% | 6.7% | 19.9% | 8.7% | 9.8% | 15.5% | 13.9% |
| JNJ | 8.3% | 0.2% | 31.8% | 7.1% | 12.5% | 13.4% | 14.9% | 9.6% |
| AMZN | 8.3% | 12.1% | 4.2% | 9.3% | 6.7% | 6.6% | 7.9% | 9.1% |
| TSLA | 8.3% | 27.5% | 0.3% | 13.0% | 4.0% | 4.7% | 9.1% | 17.6% |
| T | 8.3% | 3.0% | 18.3% | 9.8% | 10.5% | 11.4% | 12.4% | 9.9% |
| GOOGL | 8.3% | 2.5% | 3.4% | 3.7% | 7.9% | 7.3% | 5.7% | 6.0% |
| GE | 8.3% | 12.5% | 2.9% | 8.7% | 7.7% | 7.3% | 5.8% | 7.1% |
| CAT | 8.3% | 5.2% | 2.5% | 6.5% | 7.6% | 7.3% | 6.5% | 6.7% |
| WMT | 8.3% | 4.3% | 23.3% | 10.6% | 11.1% | 12.5% | 21.0% | 15.0% |
| COST | 8.3% | 4.5% | 16.4% | 12.9% | 10.5% | 10.2% | 8.4% | 6.1% |
| XOM | 8.3% | 9.6% | 9.7% | 9.0% | 9.0% | 9.4% | 10.4% | 9.8% |
| NEE | 8.3% | 0.8% | 16.8% | 13.3% | 9.9% | 11.6% | 17.4% | 13.7% |
| WELL | 8.3% | 8.2% | 11.1% | 11.8% | 8.8% | 10.3% | 15.8% | 14.3% |
| LIN | 8.3% | 0.2% | 8.9% | 1.7% | 10.3% | 9.0% | 2.8% | 2.1% |

## TA07. Head-to-head: % of experiments in which A (row) has a higher return than B (column)

*Report section: Appendix: head-to-head comparison*

| Portfolio A (row) | EW | Markowitz (λ=3) | GMV | Max Sharpe | Inverse vol | Risk parity (ERC) | Most diversified | Max decorrelation | Group pick (23 stocks) | SPY (buy & hold) |
|---|---|---|---|---|---|---|---|---|---|---|
| EW |  | 43 | 74 | 46 | 73 | 74 | 61 | 36 | 51 | 88 |
| Markowitz (λ=3) | 57 |  | 66 | 63 | 62 | 62 | 61 | 56 | 57 | 75 |
| GMV | 26 | 34 |  | 28 | 27 | 25 | 27 | 25 | 20 | 51 |
| Max Sharpe | 54 | 37 | 72 |  | 60 | 58 | 57 | 48 | 50 | 72 |
| Inverse vol | 27 | 38 | 73 | 40 |  | 39 | 38 | 29 | 29 | 85 |
| Risk parity (ERC) | 26 | 38 | 75 | 42 | 61 |  | 36 | 31 | 30 | 86 |
| Most diversified | 39 | 39 | 73 | 43 | 62 | 64 |  | 31 | 41 | 86 |
| Max decorrelation | 64 | 44 | 75 | 52 | 71 | 69 | 69 |  | 58 | 87 |
| Group pick (23 stocks) | 49 | 43 | 80 | 50 | 71 | 70 | 59 | 42 |  | 96 |
| SPY (buy & hold) | 12 | 25 | 49 | 28 | 15 | 14 | 14 | 13 | 4 |  |

## TA08. Head-to-head: % of experiments in which A (row) has a smaller maximum drawdown than B (column)

*Report section: Appendix: head-to-head comparison*

| Portfolio A (row) | EW | Markowitz (λ=3) | GMV | Max Sharpe | Inverse vol | Risk parity (ERC) | Most diversified | Max decorrelation | Group pick (23 stocks) | SPY (buy & hold) |
|---|---|---|---|---|---|---|---|---|---|---|
| EW |  | 91 | 35 | 73 | 13 | 14 | 39 | 74 | 45 | 37 |
| Markowitz (λ=3) | 9 |  | 7 | 8 | 7 | 7 | 7 | 11 | 11 | 11 |
| GMV | 65 | 93 |  | 87 | 56 | 56 | 67 | 78 | 66 | 56 |
| Max Sharpe | 27 | 92 | 13 |  | 16 | 14 | 23 | 40 | 32 | 24 |
| Inverse vol | 87 | 93 | 44 | 84 |  | 47 | 68 | 84 | 72 | 59 |
| Risk parity (ERC) | 86 | 93 | 44 | 86 | 53 |  | 71 | 89 | 77 | 58 |
| Most diversified | 61 | 93 | 33 | 77 | 32 | 29 |  | 90 | 50 | 46 |
| Max decorrelation | 26 | 89 | 22 | 60 | 16 | 11 | 10 |  | 30 | 29 |
| Group pick (23 stocks) | 55 | 89 | 34 | 68 | 28 | 23 | 50 | 70 |  | 38 |
| SPY (buy & hold) | 63 | 89 | 44 | 76 | 41 | 42 | 54 | 71 | 62 |  |

## TA09. Head-to-head: % of experiments in which A (row) has a lower volatility than B (column)

*Report section: Appendix: head-to-head comparison*

| Portfolio A (row) | EW | Markowitz (λ=3) | GMV | Max Sharpe | Inverse vol | Risk parity (ERC) | Most diversified | Max decorrelation | Group pick (23 stocks) | SPY (buy & hold) |
|---|---|---|---|---|---|---|---|---|---|---|
| EW |  | 99 | 2 | 81 | 0 | 0 | 25 | 73 | 44 | 13 |
| Markowitz (λ=3) | 1 |  | 0 | 2 | 0 | 0 | 0 | 2 | 0 | 0 |
| GMV | 98 | 100 |  | 100 | 93 | 95 | 99 | 100 | 99 | 81 |
| Max Sharpe | 19 | 98 | 0 |  | 5 | 4 | 3 | 27 | 20 | 14 |
| Inverse vol | 100 | 100 | 7 | 95 |  | 41 | 63 | 95 | 86 | 44 |
| Risk parity (ERC) | 100 | 100 | 5 | 96 | 59 |  | 72 | 100 | 86 | 46 |
| Most diversified | 75 | 100 | 1 | 97 | 37 | 28 |  | 100 | 65 | 36 |
| Max decorrelation | 27 | 98 | 0 | 73 | 5 | 0 | 0 |  | 29 | 12 |
| Group pick (23 stocks) | 56 | 100 | 1 | 80 | 14 | 14 | 35 | 71 |  | 4 |
| SPY (buy & hold) | 87 | 100 | 19 | 86 | 56 | 54 | 64 | 88 | 96 |  |

## TA10. Head-to-head: % of experiments in which A (row) has a higher Sterling ratio than B (column)

*Report section: Appendix: head-to-head comparison*

| Portfolio A (row) | EW | Markowitz (λ=3) | GMV | Max Sharpe | Inverse vol | Risk parity (ERC) | Most diversified | Max decorrelation | Group pick (23 stocks) | SPY (buy & hold) |
|---|---|---|---|---|---|---|---|---|---|---|
| EW |  | 55 | 70 | 54 | 67 | 68 | 60 | 46 | 46 | 87 |
| Markowitz (λ=3) | 45 |  | 59 | 55 | 47 | 46 | 48 | 43 | 40 | 67 |
| GMV | 30 | 41 |  | 35 | 29 | 29 | 28 | 29 | 27 | 50 |
| Max Sharpe | 46 | 45 | 65 |  | 49 | 48 | 49 | 40 | 46 | 65 |
| Inverse vol | 33 | 53 | 71 | 51 |  | 37 | 45 | 40 | 35 | 88 |
| Risk parity (ERC) | 32 | 54 | 71 | 52 | 63 |  | 49 | 42 | 36 | 88 |
| Most diversified | 40 | 52 | 72 | 51 | 55 | 51 |  | 42 | 41 | 84 |
| Max decorrelation | 54 | 57 | 71 | 60 | 60 | 58 | 58 |  | 50 | 86 |
| Group pick (23 stocks) | 54 | 60 | 73 | 54 | 65 | 64 | 59 | 50 |  | 94 |
| SPY (buy & hold) | 13 | 33 | 50 | 35 | 12 | 12 | 16 | 14 | 6 |  |

## TA11. On the 23-stock universe: head-to-head comparison by net Sharpe ratio

*Report section: Appendix: the 23-stock universe*

| Portfolio A (row) | Group pick (23 stocks) | Markowitz (λ=3) | GMV | Max Sharpe | Inverse vol | Risk parity (ERC) | Most diversified | Max decorrelation | SPY (buy & hold) |
|---|---|---|---|---|---|---|---|---|---|
| Group pick (23 stocks) |  | 79 | 64 | 61 | 60 | 46 | 48 | 58 | 92 |
| Markowitz (λ=3) | 21 |  | 46 | 22 | 21 | 22 | 25 | 31 | 52 |
| GMV | 36 | 54 |  | 42 | 33 | 29 | 22 | 33 | 53 |
| Max Sharpe | 39 | 78 | 58 |  | 38 | 37 | 36 | 37 | 70 |
| Inverse vol | 40 | 79 | 67 | 62 |  | 23 | 41 | 53 | 99 |
| Risk parity (ERC) | 54 | 78 | 71 | 63 | 77 |  | 42 | 61 | 100 |
| Most diversified | 52 | 75 | 78 | 64 | 59 | 58 |  | 64 | 93 |
| Max decorrelation | 42 | 69 | 67 | 63 | 47 | 39 | 36 |  | 89 |
| SPY (buy & hold) | 8 | 48 | 47 | 30 | 1 | 0 | 7 | 11 |  |
