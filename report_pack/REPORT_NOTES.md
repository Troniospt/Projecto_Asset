# Report notes — key findings, numbers and text for the group report

APPM Group Project 2026/27 · NOVA IMS · Postgraduate Programme in Data Science for Finance

This guide has everything the group needs to **write the report**: what each section must say, the key numbers (taken from
`results/` — every number here can be traced to a table of the pack), which figure and table to use, the assumptions to state,
the limitations, a suggested recommendation, references, the reproducibility appendix and a list of **corrections to the current
draft** (`reports/202627 - Asset Pricing & Portfolio Management.docx`).

- Figures `F01`–`F28` (main text) and `FA01`–`FA10` (appendix): `report_pack/figures/` — captions in `INDEX.md`.
- Tables `T01`–`T37` (main text) and `TA01`–`TA11` (appendix): `report_pack/tables/report_tables.xlsx` (one sheet each), CSV and `all_tables.md`.
- "≈" = rounded; "median" = median of the 100 out-of-sample years; all backtest returns are **net of 10 bps** unless stated.
- The report should be written **for an investment committee** (brief): main text = decisions and evidence, appendix = technical output.

Suggested structure (brief, p. 3): **Executive summary and recommendation → Data → Methods and assumptions → Results → Robustness checks
and limitations → Conclusions → References and reproducibility appendix.** The draft's numbering (1. universe, 2.1 stylised facts,
3. strategies) fits inside it as below.

---

## 0. Executive summary and recommendation (draft for the first page)

> We built a universe of 23 large S&P 500 stocks covering all 11 GICS sectors (2010–2026, daily data) and compared eight portfolio
> construction rules — equal weights (EW), Markowitz mean-variance (λ = 3), global minimum variance (GMV), maximum Sharpe ratio,
> inverse volatility, equal risk contribution (ERC), most diversified and maximum decorrelation — together with the group's own
> selection held in equal weights (the "Group pick", 23 stocks) and the SPY ETF. We used a walk-forward backtest of 100 randomly
> sampled three-year windows (two years of estimation, one out-of-sample year), each with 12 randomly drawn stocks, semi-annual
> rebalancing, long-only and fully invested portfolios, 10 bps transaction costs and the 3-year US Treasury yield as the risk-free rate.
>
> **No optimised strategy beats simple equal weighting consistently.** The best of them (ERC and inverse volatility) match EW's
> risk-adjusted return (median Sharpe 1.80 and 1.78 vs 1.81), and none beats it on the Sharpe ratio in more than 51% of the experiments, while the
> strategies that rely on estimated expected returns (Markowitz and Max Sharpe) are highly concentrated, turn over about eight times
> more and beat EW on the Sharpe ratio in only 21–34% of the experiments — a direct consequence of estimation error.
> The **low-risk strategies** (inverse volatility and ERC) reduce volatility in 100% of the experiments and the maximum drawdown in
> 86–87%, at the cost of ≈ 5 percentage points of annual return, with turnover as low as EW. The Group pick wins the most
> head-to-head comparisons on the Sharpe ratio, but its advantage over the market is inflated by hindsight in the choice of the 23 stocks.
>
> **Recommendation:** for a long-term investor in US equities who wants to reduce volatility and drawdowns at low cost and low
> complexity, we recommend **risk parity (ERC)** — or inverse volatility, which is even simpler. For an investor who accepts equity
> volatility in exchange for return, **equal weights** remain the most robust choice. We do not recommend unconstrained Markowitz or
> Max Sharpe. We would reconsider if correlations change sharply, if the market becomes very concentrated in a few winners, or if
> weight limits or shrinkage estimators are introduced.

(Numbers: T15, T17, F18; see sections 4–6 below.)

---

## 1. Investment universe and data (draft section 1)

**What to say**

- **Universe:** 23 S&P 500 stocks, about one per 5% of GICS level-1 sector weight and at least one per sector (11 sectors), choosing the
  largest companies in each sector (draft table — keep it). Benchmarks: **SPY** (investable ETF, total return through adjusted prices)
  and **^GSPC** (the S&P 500 index: not investable, price index without dividends). Distinguishing them is a requirement of the brief.
- **Source and extraction date:** Yahoo Finance via the `yfinance` Python library, **adjusted close prices**, daily, from **4 January 2010 to
  18 September 2026** (4,203 trading days — more than the 15 years required). Extraction date: **between 18 and 29 September 2026 —
  the group must write the exact date** (it is not recorded in the files). Risk-free rate: **FRED series DGS3** (3-year US Treasury
  constant-maturity yield), downloaded on **8 October 2026** (last observation 6 October 2026).
- **Returns:** daily log returns ln(P_t / P_t-1); weekly and monthly log returns from **period-end prices** (last trading day of the week /
  month; equivalent to summing daily log returns). The incomplete month of September 2026 is dropped (199 monthly and 871 weekly returns).
- **Dividends and corporate actions:** adjusted close prices include cash dividends and splits (e.g. Walmart's 3-for-1 split in February 2024
  does not appear as a crash).
- **Currency:** all securities trade in USD on US exchanges — no conversion.
- **Trading calendar:** the SPY (NYSE/Nasdaq) calendar; all series aligned to it; dates at day level (time zones removed).
- **Missing observations / shorter histories:** only **TSLA** has missing data (IPO 29 June 2010: its first **122 sessions** are empty). They are
  **not filled**: TSLA is simply not eligible in the backtest windows that start on or before 29 June 2010 (6 of the 100 windows).
  **META** was excluded because it listed on 18 May 2012 (**599 trading days** missing from the start of the sample) and was replaced by
  **AT&T (T)**, the next largest company of the sector.
- **Portfolio returns** use **simple** returns (brief); log returns are used only for the stylised facts.

**Use:** T01 (universe: sector, first date, CAGR, volatility, max drawdown, average correlation), F01 (correlation heatmap), F02 (risk-free rate),
TA01 (descriptive statistics of all 25 series at three frequencies). Key numbers from T01: CAGRs range from ≈ 8% (T) to ≈ 46% (NVDA),
volatilities from ≈ 17% (JNJ) to ≈ 57% (AMD, TSLA); average pairwise correlation ≈ 0.25–0.44 per stock; SPY CAGR ≈ 14.1%, volatility ≈ 17.1%,
maximum drawdown ≈ −33.7%.

---

## 2. Stylised facts of Walmart (draft section 2.1)

**Why WMT:** a large, defensive, liquid consumer-staples stock, chosen *ex ante* as a case where returns might be close to normal (keep the
draft's argument as the motivation). *Ex post* the tails say otherwise: WMT has the **2nd-highest daily (14.3) and weekly (6.7) excess kurtosis of
the 25 series** (only WELL is higher; table TA01), driven by a few very large one-day moves — mostly earnings announcements (e.g. 17 May 2022,
20 Feb 2018, 16 Nov 2017), the October 2015 guidance cut and March 2020 (`results/03_largest_residuals.csv`). Its defensive profile shows in a lower
volatility and a weak leverage effect, not in thinner tails. Normality is rejected for all 25 series at daily and weekly frequency (p < 0.001), but at
monthly frequency it is **not rejected at 5% for 10 of the 23 stocks** (AAPL, MSFT, AMD, BRK-B, LLY, JNJ, AMZN, GOOGL, CAT, LIN; TA01) — so the
draft's closing sentence ("those of the selected portfolio stocks ... are also unlikely to be normally distributed") holds at daily and weekly
frequency only. SPY is shown alongside as a comparison (T02 and T04–T12 include SPY).

**Tests used (state them in the methods):** ACF and Ljung-Box (serial correlation); excess kurtosis, Jarque-Bera, share of 3-sigma days and
Q-Q plots (non-normality); skewness with a **bootstrap** test (the classical `skewtest` assumes normal tails and over-rejects with fat tails —
it gives p ≤ 0.037 at every frequency, which is misleading); Ljung-Box on |r| and r² and the ARCH-LM test (volatility clustering);
GJR-GARCH(1,1) with normal and Student-t innovations, correlation of r(t) with |r(t+k)| and the news impact curve (leverage effect);
standardised GJR-GARCH residuals (conditional non-normality). All at daily, weekly and monthly frequency (except the r(t)–|r(t+k)| correlation
and the news impact curve, which are daily only), 5% significance level. The skewness bootstrap uses 2,000 resamples of individual days (seed 2026);
it ignores volatility clustering, so its p-values are approximate.

**Summary table for the report: T03** (supported / not, by fact and frequency) and **T04** (statistic, p-value, conclusion).

| Fact | Daily | Weekly | Monthly |
|---|---|---|---|
| 1. Little serial correlation | Supported (significant but tiny) | Supported | Supported |
| 2. Non-normal, fat tails | Supported | Supported | Supported |
| 3. Negative skewness | Not significant | Supported | Not significant |
| 4. Volatility clustering | Supported | Partial | Not supported |
| 5. Leverage effect | Supported | Not significant | Not significant |
| 6. Conditional non-normality | Supported | Supported | Supported |

### 2.1.1 Little or no serial correlation (F03, F04; T05, T06)

- Daily ACF at lags 1–5 between −0.041 and −0.006 (95% band ±0.030): lag 1 = −0.034, lag 4 = −0.041 → just outside the band.
  Ljung-Box rejects at daily frequency (p = 0.022 at lag 5, 0.001 at lags 10 and 20) — **statistically significant but economically
  negligible** (an autocorrelation of −0.04 explains ≈ 0.2% of the variance).
- Weekly: lag-1 ACF −0.095 (band ±0.066), but Ljung-Box does **not** reject (p = 0.055, 0.141, 0.110 at lags 4, 8, 12).
- Monthly: all ACFs inside the band (±0.139); Ljung-Box p = 0.73, 0.66, 0.87.
- Conclusion: **supported** at all frequencies; the small negative daily autocorrelation is typical (bid-ask bounce / microstructure).
  SPY has stronger daily autocorrelation (lag 1 = −0.100, LB p < 0.001).
- This answers the draft's note "complementar com ACF dos retornos e Ljung-Box; usar info diária e mensal".

### 2.1.2 Non-normal distributions and fat tails (F05, F06; T02, T07)

- Excess kurtosis: **14.32 (daily)**, 6.67 (weekly), 0.84 (monthly) — fat tails decline with aggregation, as expected.
- Jarque-Bera p < 0.001 (daily and weekly) and **p = 0.006 (monthly)** → normality rejected at every frequency.
- Days beyond ±3σ: **1.38%** of daily observations vs 0.27% under normality (≈ 5 times more); weekly 1.72%.
- Largest daily moves: −12.1% and +11.1%; 1% / 99% daily quantiles −3.25% / +3.17%.
- Q-Q plots (F06): strong tail departures at daily and weekly frequency, much smaller at monthly frequency.
- Conclusion: **supported, particularly at daily frequency** (exactly as the brief puts it).

### 2.1.3 Asymmetry / negative skewness (F06; T08)

- Skewness: −0.255 (daily), **−0.853 (weekly)**, −0.360 (monthly) — negative at every frequency.
- Bootstrap test (H0: skewness ≥ 0): p = 0.273 (daily), **p = 0.026 (weekly)**, p = 0.083 (monthly). The two-sided 95% bootstrap intervals
  include 0 at all three frequencies — at weekly frequency only just (−1.77 to +0.003) — so the weekly result is **borderline**: significant in
  the one-sided test at 5% (which corresponds to a 90% interval).
- Conclusion: negative skewness is **significant only at weekly frequency** (and only marginally, one-sided); daily skewness is dominated by a few
  extreme days in both tails (30 days below −3σ, 28 above +3σ). Do not over-claim.
- This replaces the draft's planned `skewtest` (which assumes normal tails and rejects symmetry at every frequency, p ≤ 0.037 — misleading here).
- Kurtosis (draft's bullet 3): excess kurtosis > 0 at all frequencies (see 2.1.2).

### 2.1.4 Volatility clustering (F03, F07, F08, F11; T09)

- Daily: Ljung-Box on |r| p < 0.001 and on r² p < 0.001; ARCH-LM(10) = 235.9, p < 0.001 → **strongly supported**.
- Weekly: Ljung-Box on |r| p < 0.001 but on r² p = 0.188 and ARCH-LM p = 0.351 → **partial**.
- Monthly: no evidence (|r| p = 0.848, r² p = 0.672, ARCH-LM p = 0.767) → **not supported**.
- GJR-GARCH persistence (α + γ/2 + β) ≈ 0.92 at daily frequency (Student-t).
- Conclusion: clustering is a **high-frequency** phenomenon for WMT; SPY shows it at all three frequencies (T09) — the market index is more
  affected by common volatility shocks than a defensive stock.

### 2.1.5 Leverage effect (F09, F10, F11; T10, T11)

- GJR-GARCH(1,1), daily, **Student-t**: γ = 0.071, **p = 0.006** → negative shocks raise next-day variance more than positive shocks of the same size
  (news impact curve F09 is steeper on the left). With **normal** innovations γ = 0.081 but p = 0.202 (not significant) — the fat tails
  matter for the inference; report the Student-t model (lower AIC: 12,323.6 vs 13,380.4).
- Correlation of r(t) with |r(t+1)|: −0.073 for WMT (SPY: −0.117, negative up to 10 days) — a weak but negative relation.
- Weekly and monthly: γ not significant (p = 0.98 and 1.00); several of these models are at the boundary of the parameter space
  (e.g. monthly t: α = 0, β = 1), so they are **unreliable** — say so. The GJR γ is the only weekly/monthly evidence on the leverage effect
  (there is no weekly/monthly chart), so at those frequencies the honest conclusion is "no evidence", not "evidence against".
- Conclusion: **supported at daily frequency only**; much weaker than for SPY (daily γ = 0.281, p < 0.001), which is consistent with WMT's
  defensive profile.
- Technical note: returns were multiplied by 100 before estimating the GARCH models (standard for numerical stability).

### 2.1.6 Conditional non-normality (F12; T12)

- Standardised residuals z = ε/σ of the daily GJR-GARCH-t: excess kurtosis **15.7**, skewness −0.66, Jarque-Bera p < 0.001 → the volatility model
  removes the clustering (Ljung-Box on z² p = 0.96) but **not** the fat tails.
- Estimated Student-t degrees of freedom ν ≈ 3.9 (daily) and 4.1 (weekly) — very heavy tails; Q-Q plots against the Student-t fit much better
  than against the normal (F12), with some departures in the extreme tail remaining.
- Weekly: z excess kurtosis 7.1 (JB p < 0.001). Monthly: 0.66 (JB p = 0.029 with the t model, 0.110 with the normal) — weak, and the monthly
  models are unreliable.
- Conclusion: **supported** (clearly at daily and weekly frequency) → Gaussian innovations are inadequate; a Student-t is a better description.

**Overall conclusion of section 2.1:** the evidence supports little serial correlation, non-normality with fat tails and conditional
non-normality at all frequencies; volatility clustering and the leverage effect are clear at daily frequency but fade with aggregation;
negative skewness is weak (significant only weekly). As the brief asks, not every fact holds at every frequency. For portfolio construction this
means that volatility and correlations change over time (a reason to re-estimate with a rolling window) and that variance understates tail risk
(a reason to also report drawdowns and the Sterling/Sortino ratios).

---

## 3. Methods and assumptions (draft section 3, first part)

### 3.1 The strategies — objective and constraints (T13; F13, F14, F15)

| Strategy | Objective | Notes |
|---|---|---|
| a) EW | w_i = 1/N | Main benchmark; nothing to estimate |
| b) Markowitz | max w'μ − (λ/2) w'Σw, **λ = 3** | Sensitivity λ = 1 and 5 (T28) |
| c) GMV | min w'Σw | Ignores expected returns |
| d) Max Sharpe | max (w'μ − r_f)/√(w'Σw) | Tangency portfolio, r_f = DGS3 of the last trading day before the rebalancing |
| e) Inverse volatility | w_i ∝ 1/σ_i | Ignores correlations |
| e) Risk parity (ERC) | w_i(Σw)_i / w'Σw = 1/N for every i | Uses the full covariance matrix |
| f) Most diversified | max DR = w'σ / √(w'Σw) | Choueifaty & Coignard (2008) |
| f) Max decorrelation | min w'Cw (C = correlation matrix) | Minimum variance with equal volatilities |
| Group pick | 1/N on all 23 group stocks (22 before TSLA) | The group's own selection; same rules as the strategies |
| SPY | buy & hold | Market benchmark, no costs |

- **Common constraints:** long-only (w ≥ 0), fully invested (Σw = 1), no leverage, no weight caps.
- **Markowitz is distinct from GMV and Max Sharpe** (brief requirement): with λ = 3 the investor trades some variance for return; λ → ∞ gives
  GMV, and the tangency (Max Sharpe) portfolio corresponds to a different point of the frontier. F15 shows the three on the in-sample frontier.
  In the 23-stock illustration, Markowitz holds 3 stocks with a 76% maximum weight, Max Sharpe 10 stocks and GMV 17 (table TA04).
  **Why λ = 3:** a moderate, commonly used risk aversion, fixed before the results were seen (as the brief requires: "do not tune parameters");
  λ = 1 and 5 are shown only as a sensitivity check.
- **Inverse volatility vs ERC when assets are correlated** (brief requirement): inverse volatility equalises w_i·σ_i but ignores correlations,
  so the risk contributions are not equal — in the 23-stock illustration they range from **−1% to 6.6%** of portfolio risk, while ERC gives
  exactly **4.3% (= 1/23)** to every stock; ERC gives less weight to stocks that are highly correlated with the others (F14, table TA05).
- **Estimation:** μ and Σ from the trailing 252 daily simple returns, annualised (×252); optimisation with `scipy.optimize` (SLSQP);
  if it fails, one retry with a looser tolerance, then equal weights (logged). **0 optimisation failures** in all runs (T36) — the brief asks to
  document failures and not to remove runs silently.
- **Group pick vs EW:** both use equal weights, but EW holds the 12 stocks drawn at random in each experiment (it tests an *allocation rule*),
  while the Group pick holds all the group's stocks (it tests the group's *stock selection*). On the full 23-stock universe they are identical
  (checked in notebook 04, section 10.6).

### 3.2 Backtest design (T14; F16; table TA02)

- **100 experiments**, random seed **2026**: each = one contiguous 3-year window (756 trading days) + 12 stocks drawn from the 23 (only stocks
  with data in the whole window). The same periods and stocks are used for every strategy (brief requirement).
- **Split** (the brief asks to specify it): in each 756-day window, days 1–504 are the estimation period and **days 505–756 the out-of-sample
  year** (252 days). With the trailing 252-day window, the warm-up weights (held from day 379) use days 127–378, and the evaluation weights use
  days 253–504 (applied from day 505) and 379–630 (from day 631); days 1–126 are not used and only days 505–756 enter the metrics.
  Out-of-sample years run from Jan 2012 to Aug 2026; they start in only 14 calendar years (98 distinct start dates), so they overlap heavily.
- **Trailing 1-year estimation window**; **semi-annual rebalancing** (every 126 trading days); the first rebalancing is one semester before the
  evaluation year (warm-up), so the portfolio already exists on day 1 of the evaluation.
- **No look-ahead:** weights use only data up to the close of t−1 (returns and DGS3) and are traded at that close (market-on-close), so they
  apply from day t; a one-day execution lag would be stricter — state this assumption. Eligibility requires data over the whole 3-year window;
  strictly this uses information about the evaluation year, but here it only excludes TSLA from the 6 windows that start before its IPO
  (missing *past* data), so it introduces no look-ahead in practice.
- **Parameters fixed in advance** (brief: "agreed before comparing results"): λ = 3, semi-annual rebalancing, 10 bps, 12 stocks per experiment,
  1-year window and seed 2026 were set before the results were seen; the alternatives are reported only as robustness checks.
- **Weights drift** between rebalancing dates; **turnover** = Σ|Δw| between the drifted and the target weights (purchases + sales);
  **cost** = 10 bps per unit of this two-way turnover (switching the whole portfolio costs 20 bps), deducted on the rebalancing day. The initial
  purchase happens at the warm-up rebalancing, before the evaluation year. Returns reported **before and after costs** (brief requirement).
- **Why semi-annual:** the brief suggests quarterly as a common convention "to be agreed"; the group chose semi-annual (lower turnover) and
  tested quarterly as a robustness check (section 5).

### 3.3 Performance measures and conventions (state them precisely — brief requirement)

- **Annualised return** (geometric): (Π(1+R_t))^(252/n) − 1. **Volatility:** sd(R_t)·√252.
- **Sharpe:** mean(R_t − r_f,t) / sd(R_t − r_f,t) · √252, with the daily DGS3 rate (annual yield / 252).
- **Sortino:** mean excess return / downside deviation √mean(min(R_t − r_f,t, 0)²) · √252.
- **Maximum drawdown:** largest fall from a previous peak of wealth (starting at 1). **Calmar:** return / |MDD|.
- **Sterling:** return / (|MDD| + 10%) — the original definition; with a 1-year evaluation window the "average annual drawdown" is that year's MDD.
- **Turnover** (sum over the evaluation year), **cost drag** (gross minus net return), **effective N** = 1/Σw², **maximum weight**,
  **diversification ratio** (ex-ante).
- **CAPM (Lab 4.1):** R_p − r_f = α + β(R_SPY − r_f) + ε on the 252 daily returns of each out-of-sample year → β, Jensen's α (×252), tracking error
  and information ratio against SPY.
- **Summaries across experiments:** medians, dispersion (P25/P75), % of experiments in which a portfolio beats EW (and the Group pick and SPY)
  **in the same experiment**, ranks and head-to-head win rates. **No significance tests across experiments:** the windows overlap, so the
  100 experiments are not independent (brief requirement — say it explicitly).

---

## 4. Results (draft section 3, second part)

### 4.1 Main table — medians across the 100 experiments, net of 10 bps (T15; F17, F18)

| Portfolio | Return | Volatility | Sharpe | Max DD | Sterling | Turnover | Eff. N |
|---|---|---|---|---|---|---|---|
| EW | 31.2% | 16.9% | 1.81 | −11.1% | 1.68 | 0.27 | 12.0 |
| Markowitz (λ=3) | 39.8% | 34.5% | 1.23 | −23.5% | 1.37 | 2.21 | 1.5 |
| GMV | 17.3% | 12.8% | 1.34 | −9.8% | 0.93 | 0.95 | 4.4 |
| Max Sharpe | 27.9% | 20.8% | 1.29 | −14.4% | 1.28 | 2.14 | 2.8 |
| Inverse vol | 25.7% | 14.7% | 1.78 | −9.8% | 1.47 | 0.27 | 10.9 |
| Risk parity (ERC) | 26.5% | 14.4% | 1.80 | −10.0% | 1.48 | 0.31 | 10.7 |
| Most diversified | 28.7% | 15.2% | 1.70 | −10.7% | 1.41 | 0.84 | 6.3 |
| Max decorrelation | 33.3% | 19.0% | 1.66 | −13.1% | 1.58 | 0.86 | 7.1 |
| Group pick (23 stocks) | 35.6% | 15.8% | 1.70 | −10.1% | 1.60 | 0.28 | 23.0 |
| SPY (buy & hold) | 17.7% | 14.0% | 1.13 | −9.4% | 0.89 | 0.00 | — |

(Sortino, Calmar, gross figures, cost drag, maximum weight and diversification ratio are also in T15.)

**Important:** the absolute returns are very high (median ≈ 31% for EW) because the 23 stocks are today's large winners (survivorship and
selection bias, section 5.4). **Compare the strategies with each other, not with history.**

### 4.2 Key findings (with the numbers)

1. **EW is very hard to beat** among the 8 strategies (T17, F18). No optimised strategy beats EW on the Sharpe ratio consistently: the best
   (ERC 51%, inverse vol 47%, most diversified 47%) are close to a coin toss; ERC (1.80) and inverse vol (1.78) have practically the same median
   Sharpe as EW (1.81). Consistent with DeMiguel, Garlappi & Uppal (2009).
2. **Low-risk family** (GMV, inverse vol, ERC): volatility lower than EW in **98–100%** of the experiments and maximum drawdown smaller in
   **65–87%**, but return above EW in only **26–27%**. Inverse vol and ERC do it with EW-like turnover (≈ 0.3 per year) and well-diversified
   portfolios (effective N ≈ 11 of 12); GMV is concentrated (effective N ≈ 4.4, max weight ≈ 35%) and has the lowest median return (17.3%).
3. **Strategies that use expected returns** (Markowitz, Max Sharpe): very concentrated (Markowitz effective N ≈ 1.5, average maximum weight
   ≈ 77%), turnover ≈ 8× EW (2.21 vs 0.27 per year), higher volatility (34.5%) and drawdowns (−23.5%); Markowitz has the highest median
   return (39.8%) but the widest dispersion (standard deviation of annual return 0.68 vs 0.22 for EW, T16) and a smaller drawdown than EW in only
   **9%** of the experiments. Sharpe above EW in only 21% (Markowitz) and 34% (Max Sharpe). → **Estimation error:** 1-year mean returns point to
   the recent winners, which do not always keep winning.
4. **Most diversified and max decorrelation** sit in between: more return than the low-risk family, turnover ≈ 3× EW (≈ 0.85), moderate
   concentration (effective N 6.3–7.1). Max decorrelation earns more than EW in 64% of the experiments but with higher volatility.
5. **The Group pick** (23 stocks, equal weights) — the group's own portfolio (T15, T17–T22, F19, F20):
   - **best average rank** by Sharpe (3.9 of 10; 1st in 33% of the experiments, top 3 in 50%; T20) and the most head-to-head wins on the Sharpe
     ratio (68% on average; it beats **each** of the other 9 portfolios in more than half of the experiments — 56% vs ERC, 62% vs EW, 79% vs
     Markowitz, 92% vs SPY; T21, T22);
   - but its **median Sharpe (1.70) is not the highest** (EW 1.81, ERC 1.80): the median of each column and the comparison inside each
     experiment answer different questions. Its edge is **consistency** — the highest 25th percentile of the Sharpe ratio (0.86 vs 0.72 for EW; T16);
   - against EW: higher Sharpe in 62%, lower volatility in 56%, but higher return in only **49%** (median paired return difference ≈ −0.5 pp;
     mean returns ≈ 32% for both). Its advantage over EW comes from **diversification** (23 vs 12 stocks), not from better stocks (EW's 12 stocks are
     drawn from the same 23);
   - on other metrics it does not dominate: it beats 5 of 9 rivals on return and only 4 of 9 on volatility and drawdown (tables TA07–TA09).
6. **Head-to-head ranking by Sharpe** (average % of comparisons won, T22): Group pick 68%, ERC 65%, EW 61%, inverse vol 59%, most diversified 58%,
   max decorrelation 55% | Max Sharpe 40%, GMV 38%, Markowitz 29%, SPY 27%. On volatility the order reverses: GMV wins 96% of its comparisons,
   ERC 74%, SPY 72%, inverse vol 70% (T22). → **No portfolio wins on every metric**; the choice depends on the investor's objective.
7. **SPY** has the lowest median Sharpe (1.13) and one of the lowest returns (17.7%), but the smallest median drawdown (−9.4%) and low volatility
   (14.0%). Every portfolio built from the 23 stocks earns more than SPY in most experiments (from 51% for GMV to 96% for the Group pick; T19) —
   **mainly the selection bias** of the universe, not skill of the strategies.
8. **Market risk (CAPM vs SPY, T24, F22):** every portfolio has a positive median Jensen's alpha (+6.0% per year GMV … +18.3% Markowitz), but it is
   significant (t > 1.96) in only 5–40% of the experiments, and it mostly reflects the selection bias. Betas: GMV clearly defensive (β ≈ 0.64,
   below 1 in 99% of the experiments); most diversified 0.85, ERC 0.91, inverse vol 0.93; EW 1.04 and the Group pick 1.05 slightly above the
   market; Markowitz 1.32. The Group pick tracks SPY most closely (R² ≈ 0.90, tracking error ≈ 5.4%) and has the highest information ratio (≈ 2.1).
9. **Turnover and costs (F21):** with 10 bps the cost drag is small — ≈ 3.4–3.8 bps per year for EW, inverse vol, ERC and the Group pick;
   ≈ 33 bps for Markowitz (the most expensive; ≈ 1% in the worst experiment). Performance before and after costs: T15 (gross vs net columns).
10. **Example during a crisis (F23):** experiment 62 (out-of-sample year 11 Nov 2019 – 9 Nov 2020, one of the three experiments that include the
    March 2020 crash) shows the paths of all portfolios — use it only as an illustration (one experiment is not evidence).
11. **Trade-offs in one table (T37):** return, volatility, drawdown, Sharpe, % beats EW, effective N, turnover, what is estimated and complexity —
    the brief asks to discuss exactly these trade-offs.

---

## 5. Robustness checks and limitations

### 5.1 Robustness (notebook 04, sections 10–12)

- **Higher costs (T25, T26, F24):** from 0 to 50 bps the ranking by median Sharpe practically does not change (only most diversified and the Group
  pick swap places 4–5, because their medians are almost equal: 1.707 vs 1.705 at 0 bps). Markowitz loses ≈ 0.045 of Sharpe between 0 and 50 bps,
  EW only ≈ 0.007. In this universe of very liquid stocks, what separates the strategies is estimation error, not costs. (Brief: "test whether
  rankings change under less favourable cost assumptions" → essentially not: the only change is a swap between two near-tied portfolios.)
- **Quarterly rebalancing (T27):** turnover +29–44% without a consistent improvement (some medians up, others down); with quarterly rebalancing
  ERC has the highest median Sharpe (1.83) and the Group pick still beats EW in 62% of the experiments → semi-annual is enough.
- **Markowitz risk aversion (T28):** λ = 1 → effective N = 1.0 (a single stock), return 42.6%, volatility 40.5%, Sharpe 1.11; λ = 5 → effective
  N ≈ 2.0, volatility 29.8%, Sharpe 1.31. A higher λ moves Markowitz towards GMV but does **not** solve the concentration (Lab 3.1 risk-aversion effect).
- **Sub-periods (T29, F25):** the Group pick has the highest median Sharpe in 2012–2016 (1.96) and 2017–2020 (2.25) but not in 2021–2026 (1.62 vs ERC
  1.72); Markowitz deteriorates in 2021–2026 (0.85).
- **Market regimes (T30):** in the 12 of the 100 experiments whose out-of-sample year had a negative SPY return (overlapping windows from about
  four episodes — 2015–16, 2018, 2019–20 and 2021–23 — so far fewer than 12 independent observations; median SPY return −5.4%), EW, inverse vol and ERC still had small positive
  median returns (≈ +3.7–3.8%) and Sharpe ≈ 0.14–0.17; Markowitz was the only strategy with a negative median return (−4.8%); the Group pick (+2.1%,
  Sharpe 0.06) is **less defensive** than the low-risk strategies.
- **Asset subset (T31):** with a new random draw of 12 stocks (same periods), the order among the top strategies changes (EW drops from 1st to 4th;
  max decorrelation rises to 2nd); with all eligible stocks, most diversified is 1st. → **The differences among the top strategies are not robust**;
  what is robust is that Markowitz and Max Sharpe are at the bottom and the low-risk strategies have lower volatility. (Brief: "show whether
  conclusions depend on the sampled period or asset subset".)
- **Strategies on the group's own 23 stocks (T32, T33, F26):** most diversified (median Sharpe 1.85) and ERC (1.75) have a higher median Sharpe than the
  Group pick (1.70) but beat it in only 52% and 54% of the experiments (median paired differences +0.02 and +0.01) — a coin toss. They reduce risk
  (ERC: lower volatility in 100%, smaller drawdown in 93% of the experiments) but earn less (more return in only 23%). → Optimisers can reduce the risk
  of the group's pick but do not add risk-adjusted return robustly.

### 5.2 The Group pick over the full sample (T34, T35, F27, F28) — descriptive only

- 2010-01-05 to 2026-09-18, semi-annual rebalancing, 10 bps: **1 USD → 46.0 USD** (CAGR 25.8%, volatility 18.4%, Sharpe 1.24, max drawdown −32.2%) vs
  SPY 9.0 USD (14.1%, 17.1%, 0.75, −33.7%) and ^GSPC 6.8 USD (12.1%, price index); the Group pick beat SPY in **15 of 17** calendar years
  (exceptions 2010 and 2012).
- **This is not evidence that the pick would have beaten the market in real time** — the 23 stocks were chosen in 2026, with hindsight.
  Present it only as a description, with the warning. If T34 is shown, note that its Sterling ratio uses the average of the 17 calendar-year maximum
  drawdowns + 10% (the original definition), unlike the backtest, where the evaluation window is a single year.

### 5.3 What the brief asks to document (checklist)

- Asset eligibility (only stocks with data in the whole window; TSLA not eligible in 6 windows) ✔ · sample size (100 × 252 out-of-sample days) ✔ ·
  missing data (not filled) ✔ · optimisation failures (0, T36) ✔ · survivorship bias (5.4) ✔ · turnover and performance before and after costs (T15) ✔ ·
  cost convention and ranking under higher costs (T25, T26) ✔ · overlapping windows not independent (3.3) ✔.

### 5.4 Limitations (copy into the report)

- **Survivorship and selection bias:** the 23 stocks were chosen in September 2026 among today's largest companies (NVDA, AVGO, LLY…). This inflates
  the absolute returns of every strategy and especially the comparison with SPY. **Drawing 12 of the 23 at random does not remove the bias** (all 23 are
  survivors) — correct the draft's sentence that says it may be "partially mitigated through the analysis of 100 randomly selected portfolios".
  Comparisons *between* strategies are less affected, but rules that chase past winners (Markowitz, Max Sharpe) may benefit from it.
- **Overlapping experiments:** the 100 windows share years, so they are not independent; we report medians, dispersion and frequencies, not p-values.
- **Estimation error:** 1-year sample means are very noisy; this mainly hurts Markowitz and Max Sharpe. No shrinkage or weight limits were used
  (extensions A and B of the brief).
- **Costs:** fixed proportional costs, no market impact, taxes or bid-ask spread variation; SPY's ≈ 0.09% fee is already in its price.
- **Risk-free rate:** the 3-year Treasury carries some duration risk (a 3-month T-bill would be the "purer" choice). Its level lowers every
  Sharpe/Sortino ratio by ≈ r_f/σ — more for low-volatility portfolios — and enters the Max Sharpe optimisation, so it can slightly affect
  Sharpe-based comparisons; returns, volatility, drawdowns, Calmar and Sterling do not depend on it.
- **Bootstrap of skewness** resamples individual days (i.i.d.) and ignores volatility clustering — its p-values are approximate.
- **Execution:** trades at the close of the day whose data set the weights (market-on-close); a one-day lag would be more conservative.
- **Universe:** only US large caps; results may not transfer to other markets or asset classes.
- **CAPM:** OLS t-statistics assume i.i.d. errors, which daily returns violate (volatility clustering) — indicative only.

---

## 6. Conclusions and recommendation (investor objective + when to reconsider — brief requirement)

- **Target investor:** a long-term investor in US equities (e.g. a pension fund or a prudent private investor) who wants to **reduce volatility and
  drawdowns** with low costs and low complexity.
- **Recommendation: risk parity (ERC)** — or inverse volatility, which is simpler and has similar medians; in the same experiment, though, ERC has
  the higher Sharpe ratio in 65% of the cases (T21) and in 77% on the 23-stock universe (table TA11), which supports ERC. Evidence: median Sharpe
  equal to EW (1.80 vs 1.81), volatility lower than EW in 100% of the experiments and maximum drawdown smaller in 86%, beta ≈ 0.91, turnover ≈ 0.3
  per year (cost ≈ 4 bps), well-diversified weights (effective N ≈ 11 of 12), and it stays in the upper half of the ranking in every robustness
  check (2nd at every cost level, 1st with quarterly rebalancing and in 2021–2026, 2nd with all eligible stocks; but 4th in 2017–2020, 4th when SPY
  fell and 5th of 10 with a new draw of stocks — T25–T31). Cost of the choice: ≈ 5 pp less return per year than EW (26.5% vs 31.2%).
- **For an investor who accepts equity volatility for return:** equal weights — the simplest and most robust rule (nothing to estimate). On the
  group's 23 stocks, that is the **Group pick**: the most consistent risk-adjusted performer in our tests, but present its advantage over SPY
  with the selection-bias warning.
- **Not recommended:** unconstrained Markowitz and Max Sharpe (extreme concentration, ≈ 8× the turnover, unstable results).
- **When to reconsider:** (i) if correlations change sharply (ERC depends on the covariance matrix); (ii) if the market becomes very concentrated
  in a few winners (EW and ERC hold little of them); (iii) if costs or the universe are very different (illiquid stocks); (iv) if weight limits or a
  shrinkage covariance are added (brief extensions A and B), which may stabilise Markowitz and Max Sharpe; (v) for the Group pick, if the stocks
  were chosen with information available at each date (removing the selection bias).
- "A strategy that performs poorly can still support a strong project if the analysis explains why" (brief): Markowitz's failure is the clearest
  illustration of estimation error — explain it.

---

## 7. References (suggested; add the course materials)

- Bacon, C. R. (2008). *Practical Portfolio Performance Measurement and Attribution* (2nd ed.). Wiley. (Sortino, Calmar, Sterling ratios.)
- Black, F. (1976). Studies of stock price volatility changes. *Proceedings of the 1976 Meetings of the American Statistical Association, Business and Economic Statistics Section*, 177–181.
- Bollerslev, T. (1986). Generalized autoregressive conditional heteroskedasticity. *Journal of Econometrics*, 31(3), 307–327.
- Choueifaty, Y., & Coignard, Y. (2008). Toward maximum diversification. *Journal of Portfolio Management*, 35(1), 40–51.
- *Maximum decorrelation portfolio:* cite the source used in Lab 5 (risk-based portfolios) of the course.
- Cont, R. (2001). Empirical properties of asset returns: stylized facts and statistical issues. *Quantitative Finance*, 1(2), 223–236.
- DeMiguel, V., Garlappi, L., & Uppal, R. (2009). Optimal versus naive diversification: How inefficient is the 1/N portfolio strategy? *Review of Financial Studies*, 22(5), 1915–1953.
- Efron, B. (1979). Bootstrap methods: Another look at the jackknife. *Annals of Statistics*, 7(1), 1–26.
- Engle, R. F. (1982). Autoregressive conditional heteroscedasticity with estimates of the variance of United Kingdom inflation. *Econometrica*, 50(4), 987–1007.
- Engle, R. F., & Ng, V. K. (1993). Measuring and testing the impact of news on volatility. *Journal of Finance*, 48(5), 1749–1778.
- Glosten, L. R., Jagannathan, R., & Runkle, D. E. (1993). On the relation between the expected value and the volatility of the nominal excess return on stocks. *Journal of Finance*, 48(5), 1779–1801.
- Jarque, C. M., & Bera, A. K. (1980). Efficient tests for normality, homoscedasticity and serial independence of regression residuals. *Economics Letters*, 6(3), 255–259.
- Jensen, M. C. (1968). The performance of mutual funds in the period 1945–1964. *Journal of Finance*, 23(2), 389–416.
- Ledoit, O., & Wolf, M. (2003). Honey, I shrunk the sample covariance matrix. UPF Economics and Business Working Paper No. 691 (cited in the brief).
- Ljung, G. M., & Box, G. E. P. (1978). On a measure of lack of fit in time series models. *Biometrika*, 65(2), 297–303.
- Maillard, S., Roncalli, T., & Teïletche, J. (2010). The properties of equally weighted risk contribution portfolios. *Journal of Portfolio Management*, 36(4), 60–70.
- Markowitz, H. (1952). Portfolio selection. *Journal of Finance*, 7(1), 77–91.
- Sharpe, W. F. (1964). Capital asset prices: A theory of market equilibrium under conditions of risk. *Journal of Finance*, 19(3), 425–442.
- Sharpe, W. F. (1966). Mutual fund performance. *Journal of Business*, 39(1), 119–138.
- Sortino, F. A., & van der Meer, R. (1991). Downside risk. *Journal of Portfolio Management*, 17(4), 27–31.
- Young, T. W. (1991). Calmar ratio: A smoother tool. *Futures*, 20(1), 40.
- **Data:** Yahoo Finance (via the `yfinance` Python library), adjusted daily prices, extracted September 2026 [exact date]. Board of Governors of the
  Federal Reserve System (US), *Market Yield on U.S. Treasury Securities at 3-Year Constant Maturity* [DGS3], retrieved from FRED, Federal Reserve
  Bank of St. Louis, https://fred.stlouisfed.org/series/DGS3, 8 October 2026. BlackRock iShares (sector weights, September 2026 — as in the draft).
- **Course:** Bravo, J. M. (2026). *Asset Pricing & Portfolio Management* — project brief and Labs 1–5 (NOVA IMS).

---

## 8. Reproducibility appendix (brief: "include all supporting files needed to reproduce the results")

- **Code:** GitHub repository, notebooks `01_data_collection` (data, not re-run: it would download new prices), `02_walmart_eda`, `03_stylised_facts_garch`,
  `04_strategies_backtest`, `05_report_pack` (this folder). Each is also saved as HTML (acceptable for submission according to the brief).
- **Data:** `notebooks/data/` (frozen prices and returns, WMT history, FRED DGS3 with its download date in `risk_free_DGS3_info.txt`).
- **Randomness:** seed **2026** (100 experiments; also the 2,000-resample skewness bootstrap in notebook 03), 2027 (the "new draw" robustness
  check) and 123 (the simulated normal series of notebook 02, figure FA06); NumPy's legacy `RandomState`, frozen across versions.
- **Environment:** Python 3.11–3.13 with the versions pinned in `requirements.txt` (numpy 2.2.6, pandas 2.2.3, scipy 1.15.3, statsmodels 0.14.4,
  arch 7.2.0, matplotlib 3.10.3, openpyxl 3.1.5). Tested: Python 3.11 and 3.13 give **bit-for-bit identical** tables and figures.
- **How to run:** on GitHub → Actions → "Run notebooks" → Run workflow (runs 02–05 and commits the results; run it on a fork or a branch — it
  refuses to run on `main` of the group repository), or locally:
  `pip install -r requirements.txt`, then run the notebooks in order (details in the repository README).
- **Outputs:** `figures/` (all charts), `results/` (all tables as CSV and Excel: `03_stylised_facts.xlsx`, `04_strategies_backtest.xlsx`), and this
  `report_pack/` folder.

---

## 9. Corrections and gaps in the current draft (to do before submission)

1. **Risk-free rate:** the draft says "10-year U.S. Treasury yield ... obtained from Yahoo Finance". The analysis uses the **3-year Treasury yield
   (FRED DGS3)**, downloaded from FRED on 8 October 2026. Fix in section 2 ("Calculations") and in the constraints list of section 3.
2. **Data source and extraction date:** say "stocks, SPY and ^GSPC from Yahoo Finance (adjusted close), extracted on [date] September 2026; risk-free
   rate from FRED". Add the data-treatment paragraph (dividends/splits, currency, calendar, missing data, SPY vs ^GSPC) — section 1 of these notes.
3. **META footnote:** "approximately 550 trading days missing" → **599 trading days** (listed 18 May 2012). TSLA: 122 trading days (OK), and say how it
   is treated (not filled; not eligible in 6 of the 100 windows).
4. **"All selected assets remain eligible throughout the backtest period"** — not exactly: TSLA is not eligible in windows starting before 30 June 2010.
5. **"This bias may be partially mitigated through the analysis of 100 randomly selected portfolios"** — incorrect: random subsets of the same 23
   survivors keep the bias. Replace with the limitation in 5.4.
6. **"Using the same set of securities ensures that performance differences are driven primarily by the allocation methodology"** — in each experiment all
   strategies use the same 12 drawn stocks (true), but the Group pick uses all 23; explain the difference (3.1).
7. **Metrics list:** add the **Sterling ratio** (required: "a drawdown-based measure such as the Sterling ratio") and define the conventions
   (annualisation, risk-free, Sterling denominator — section 3.3). Diversification ratio is ex-ante.
8. **Markowitz:** replace the open notes ("target return... / risk aversion...") with the decision: λ = 3, sensitivity λ = 1 and 5 (T28).
9. **Strategies e) and f)** have no description in the draft → use T13 and the inverse-vol vs ERC paragraph (3.1).
10. **2.1.1:** add the ACF and Ljung-Box results at the three frequencies (T05, T06, F04). **2.1.2–2.1.6:** add the weekly and monthly evidence
    ("complementar com info mensal") — section 2 of these notes.
11. **2.1.3:** replace the planned `skewtest` with the bootstrap test (T08); the draft's three bullets become: skewness negative at all frequencies but
    significant only weekly (p = 0.026).
12. **2.1.5:** report the GJR-GARCH γ and p-value (daily Student-t: γ = 0.071, p = 0.006). **If any GARCH figure or number in the draft comes from the
    version of notebook 02 in the group repository's `main` branch, replace it:** that version fits the GARCH on unscaled returns, so the optimiser
    stays at its starting values (α = 0.05, γ = 0.10, β = 0.80) — those estimates are not valid. Use F09–F12 and T10.
13. **Section 3 results** do not exist yet in the draft → section 4 of these notes; add the robustness and limitations (section 5) and the
    recommendation (section 6).
14. **Cover page:** names and student numbers; **executive summary** first (section 0); **references** and **reproducibility appendix** at the end.
15. The rebalancing is **semi-annual** (draft: OK); mention that quarterly (the brief's suggestion) was tested as robustness.
16. **"The 100 historical simulations use a three-year rolling window"** → they are 100 randomly sampled (overlapping) contiguous three-year windows,
    each with 12 randomly drawn stocks; the *rolling* part is the 1-year estimation window re-estimated at each rebalancing inside each window.
17. **Selection rule:** "one stock per 5% of sector weight" gives Consumer Staples (~6%) one stock, but the table has two (WMT and COST) — the rule
    alone gives 22 stocks. Explain why Consumer Staples has two (e.g. to include WMT, the stock of the single-share study). Also, the sector weights
    in the draft table add up to 98.5%, not 100% — round them or add the missing 1.5% (e.g. cash/other in the ETF).
18. **Cost convention:** "0.10% (10 bps) all-in cost" → say "10 bps per unit of turnover Σ|Δw| (purchases + sales)".
19. **Submission:** Moodle, by **30 October 2026**; group report + one individual report per member (`FirstName_Surname_StudentNumber.pdf`),
    PDF or Word (an HTML notebook is also acceptable), with all supporting files (code, data or data-retrieval instructions, Excel workbooks).

---

## 10. Course content used (Labs) and ideas for the individual project

| Lab | Where it is used |
|---|---|
| Lab 1 – Empirical properties of asset returns | Notebooks 02 and 03 (stylised facts) |
| Lab 2 – Heuristic portfolios | EW, inverse volatility, the Group pick |
| Lab 3 / 3.1 – Markowitz, risk-aversion effect | Markowitz λ = 3; sensitivity λ = 1, 3, 5 (T28); efficient frontier (F15) |
| Lab 4 – Backtesting strategies | The 100-experiment walk-forward backtest |
| Lab 4.1 – CAPM beta estimation | Section 9.7 of notebook 04: beta, Jensen's alpha, tracking error, information ratio (T24, F22) |
| Lab 5 – Risk-based portfolios (incl. MDP) | GMV, inverse vol, ERC, most diversified, max decorrelation |
| Lab 6 – Hierarchical risk parity | Not in the group brief → **individual project option b)** |
| Lab 7 – Black-Litterman | Not in the brief's list → possible "another clearly specified and justified strategy" (option j) in the individual project |
| Lab 8 – Fama-French / Lab 9 – Statistical factor models | Not required; a factor regression of the backtest returns could extend the CAPM analysis (needs the Fama-French factors from Kenneth French's website) |

**Individual project (6/20, one report per member, `FirstName_Surname_StudentNumber.pdf`):** use the same dataset and backtest
(`results/04_experiment_design.csv` has the 100 periods and stocks), compare with the group benchmarks (EW, ERC, the Group pick, SPY) using the
same conventions, and say whether the alternative improves the decision **after costs** and whether it justifies the extra complexity.
