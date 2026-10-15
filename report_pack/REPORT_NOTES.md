# Report notes — key findings, numbers and text for the group report

APPM Group Project 2026/27 · NOVA IMS · Postgraduate Programme in Data Science for Finance

This guide has everything the group needs to **write the report**: what each section must say, the key numbers (taken from
`results/` — every number here can be traced to a table of the pack), which figure and table to use, the assumptions to state,
the limitations, a suggested recommendation, references, the reproducibility appendix and a list of **corrections to the current
draft** (`reports/202627 - Asset Pricing & Portfolio Management.docx`).

- Figures `F01`–`F28` and `FA01`–`FA12` (appendix): `report_pack/figures/` — captions in `INDEX.md`.
- Tables `T01`–`T44` and `TA01`–`TA12` (appendix): `report_pack/tables/report_tables.xlsx` (one sheet each), CSV, `all_tables.md` and
  one PNG image per table in `report_pack/tables/png/`.
- `INDEX.md` has a **"Suggested placement"** column: 21 items marked **Main text (core)** (the core evidence for an investment committee);
  everything else is marked **Appendix** (the group decides). The brief wants decisions in the main text and technical output in the appendix — 28 figures and
  44 tables in the main text would be far too many.
- "≈" = rounded; "median" = median of the 100 out-of-sample years; all backtest returns are **net of 10 bps** unless stated.
- The report should be written **for an investment committee** (brief): main text = decisions and evidence, appendix = technical output.

Suggested structure (brief, p. 3): **Executive summary and recommendation → Data → Methods and assumptions → Results → Robustness checks
and limitations → Conclusions → References and reproducibility appendix.** The draft's numbering (1. universe, 2.1 stylised facts,
3. strategies) fits inside it as below.

---

## 0. Executive summary and recommendation (draft for the first page)

> We built a universe of 23 large S&P 500 stocks covering all 11 GICS sectors (2010–2026, daily data) and compared eight portfolio
> construction rules — equal weights (EW), Markowitz mean-variance (λ = 3), global minimum variance (GMV), maximum Sharpe ratio,
> inverse volatility, equal risk contribution (ERC), most diversified and maximum decorrelation — with the group's own selection held in
> equal weights (the "Group pick", 23 stocks) and with the index (SPY). We used a walk-forward backtest of 100 randomly sampled three-year
> windows (two years of estimation, one out-of-sample year), each with 12 randomly drawn stocks, semi-annual rebalancing, long-only and
> fully invested portfolios, 10 bps transaction costs and the 3-year US Treasury yield as the risk-free rate. Because the 100 windows
> overlap (about 7 experiments share each day), we only call a difference **clear** when its uncertainty band excludes 50%.
>
> **What is clear.** Strategies that rely on estimated expected returns (Markowitz, Max Sharpe) are highly concentrated, turn over about
> eight times more and lose to simple equal weights (Markowitz has a lower Sharpe ratio than EW in 79% of the experiments). The
> **low-risk strategies** (inverse volatility, ERC) cut volatility in 100% of the experiments and the maximum drawdown in about 86%, with
> turnover as low as EW. ERC is the most robust of the eight rules (best average rank in almost every variant, and clearly better than
> inverse volatility). **What is not clear:** ERC, inverse volatility, most diversified and EW cannot be separated on the Sharpe ratio.
>
> **Against the index.** All portfolios built from the 23 stocks earned far more than SPY, but this is mostly **hindsight**: the 23 stocks
> are today's largest companies. Without the five biggest winners of 2010-2026 the return advantage largely disappears, while ERC then has
> **lower volatility than SPY in 89% and a smaller drawdown in 79% of the experiments**, with a similar or higher Sharpe ratio.
>
> **Recommendation:** for an investor choosing between the index and a rules-based portfolio of large US stocks, who wants a smoother path
> without giving up risk-adjusted return, we recommend **risk parity (ERC)**; the honest expectation is **lower risk at a similar
> risk-adjusted return**, not a higher return. SPY remains the default for an investor who does not want to run a stock portfolio. We do not
> recommend unconstrained Markowitz or Max Sharpe. We would reconsider if ERC's realised volatility stops being below the index's, in a
> crash in which correlations jump (ERC did not protect in March 2020), if leadership concentrates in a few volatile mega-caps, or with an
> ex-ante universe rule that removes the hindsight.

(Numbers: T15, T17, T38, T43, T44; see sections 4–6 below.)

---

## 1. Investment universe and data (draft section 1)

**What to say**

- **Universe:** 23 S&P 500 stocks, about one per 5% of GICS level-1 sector weight and at least one per sector (11 sectors), choosing the
  largest companies in each sector (draft table — keep it). Benchmarks: **SPY** (investable ETF, total return through adjusted prices)
  and **^GSPC** (the S&P 500 index: not investable, price index without dividends). Distinguishing them is a requirement of the brief.
- **Inclusion rule (write it explicitly):** every stock must have at least **15 years** of daily prices up to September 2026 (the brief's
  minimum). **TSLA** (listed 29 June 2010, 16.2 years) qualifies; **META** (listed 18 May 2012, 14.3 years) does not and was replaced by
  **AT&T (T)**, a Communication Services stock with the full history. **⚠ To confirm by the group:** the draft says T is "the next
  highest-weighted stock of the sector". In recent sector weightings NFLX (and possibly TMUS and DIS) rank above T. Check the iShares
  holdings file and date you used; if T is not next, give the real reason (e.g. a defensive telecom name with the full history) and drop
  the "next largest" claim. Replacing a 2012 IPO by a long-listed company also slightly *reduces* the hindsight in the universe.
- **Source and extraction date:** Yahoo Finance via the `yfinance` Python library, **adjusted close prices**, daily, from **4 January 2010 to
  18 September 2026** (4,203 trading days). Extraction date: **between 21 and 29 September 2026** — the code uses `end = 2026-09-21`, the
  CSV files were first committed to the group repository on 29 September 2026, and no dividend paid after 18 September had been applied
  to the adjusted prices. **⚠ The brief asks for the extraction date: write the exact day if the member who ran notebook 01 can confirm it**
  (e.g. the creation date of the original CSV file on their computer); otherwise write the range and how it was established.
- **Why January 2010:** the first full year in which all the selected stocks except TSLA already trade (AVGO listed in August 2009, V in
  March 2008); it gives 16.7 years (> 15 required). The 2008-09 financial crisis is therefore **outside the sample** (see limitations, 5.4).
- **Risk-free rate:** **FRED series DGS3** (3-year US Treasury constant-maturity yield), downloaded manually on **8 October 2026** (last
  observation 6 October 2026). Why DGS3: it matches the 3-year horizon of each experiment, it is an official daily series with a documented
  source and date, and its average over 2010-2026 is about 1.85%. Daily rate = annual yield / 252; on bond-market holidays (about 30 days,
  e.g. Columbus and Veterans Day) the last available value is used. (The draft used a 10-year yield from Yahoo — say why it changed.)
- **Returns:** daily log returns ln(P_t / P_t-1); weekly and monthly log returns from **period-end prices** (last trading day of the week /
  month; equivalent to summing daily log returns). The incomplete month of September 2026 is dropped (199 monthly and 871 weekly returns).
- **Dividends and corporate actions (brief requirement):** Yahoo's *Close* is already split-adjusted (WMT 3-for-1 in February 2024; the splits
  of NVDA, AVGO, AMZN, GOOGL, TSLA, AAPL; BRK-B 50-for-1 in January 2010; GE's 1-for-8 reverse split in 2021), so a split never looks like a
  crash. The **adjusted close** that we use also adjusts for **cash dividends** (including COST's special dividends) and for **spin-offs**
  (AT&T → Warner Bros. Discovery 2022; GE → GE HealthCare 2023 and GE Vernova 2024), so returns are approximately total returns.
  Histories are those of today's company (LIN before October 2018 is Praxair; WELL was Health Care REIT; AVGO was Avago Technologies).
- **Currency:** all securities trade in USD on US exchanges — no conversion.
- **Trading calendar:** the SPY (NYSE/Nasdaq) calendar; all series aligned to it; dates at day level (time zones removed).
- **Missing observations / shorter histories:** only **TSLA** has missing data (its first **122 sessions** are empty). They are **not
  filled**: TSLA is simply not eligible in the backtest windows that start on or before 29 June 2010 (6 of the 100 windows). Notebook 01,
  section 9, re-checks the frozen files (no other gaps; weekly/monthly returns equal the sum of the daily log returns).
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
20 Feb 2018, 16 Nov 2017) and the October 2015 guidance cut (`results/03_largest_residuals.csv`), plus the COVID days of March 2020
(17 March 2020, +11.1%, is the largest daily rise; 12 March 2020, −9.5%). Its defensive profile shows in a lower
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
it ignores volatility clustering, so its p-values are approximate. The main p-value is one-sided (share of resampled skewness values ≥ 0);
T08 also shows a **centred** and a **two-sided** version as a sensitivity check — quote all three (2.1.3). The GJR-GARCH p-values use
**robust (Bollerslev-Wooldridge, QMLE) standard errors** (the default of the `arch` library) — say so: with non-robust standard errors the
daily γ of the normal model would also be significant. Two decision rules to state: an autocorrelation below 0.10 in absolute value is called
"tiny" (it explains less than 1% of the variance); a GJR-GARCH fit **at the boundary** of the parameter space (β > 0.999 or
α + γ/2 < 0.01, i.e. no volatility dynamics) is not used as evidence, and the cell becomes **Inconclusive**.

**Summary table for the report: T03** (supported / not, by fact and frequency) and **T04** (statistic, p-value, conclusion).

| Fact | Daily | Weekly | Monthly |
|---|---|---|---|
| 1. Little serial correlation | Supported (significant but tiny) | Supported | Supported |
| 2. Non-normal, fat tails | Supported | Supported | Supported |
| 3. Negative skewness | Not significant | Supported | Not significant |
| 4. Volatility clustering | Supported | Partial | Not supported |
| 5. Leverage effect | Supported | Not significant | Inconclusive (GARCH at boundary) |
| 6. Conditional non-normality | Supported | Supported | Inconclusive (GARCH at boundary) |

Two cells need a sentence in the text: **weekly skewness** is significant only in the one-sided test and depends on one week (2.1.3); **weekly
clustering** is "Partial" because one week hides it in the r² test (2.1.4).

### 2.1.1 Little or no serial correlation (F03, F04; T05, T06)

- Daily ACF at lags 1–5 between −0.041 and −0.006 (95% band ±0.030): lag 1 = −0.034, lag 4 = −0.041 → just outside the band.
  Ljung-Box rejects at daily frequency (p = 0.022 at lag 5, 0.001 at lags 10 and 20) — **statistically significant but economically
  negligible** (an autocorrelation of −0.04 explains ≈ 0.2% of the variance).
- Weekly: lag-1 ACF −0.095 (band ±0.066), but Ljung-Box does **not** reject (p = 0.055, 0.141, 0.110 at lags 4, 8, 12).
- Monthly: all ACFs inside the band (±0.139); Ljung-Box p = 0.73, 0.66, 0.87.
- Once volatility is modelled, the daily autocorrelation disappears: Ljung-Box on the GJR-GARCH-t standardised residuals p = 0.14 (T12).
  The plain Ljung-Box test assumes constant variance, so with volatility clustering it rejects too easily.
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
- Bootstrap test (H0: skewness ≥ 0), three versions (T08):

  | p-value | Daily | Weekly | Monthly |
  |---|---|---|---|
  | one-sided (main) | 0.273 | **0.026** | 0.083 |
  | centred, one-sided (sensitivity) | 0.287 | 0.031 | 0.040 |
  | two-sided (sensitivity) | 0.545 | 0.053 | 0.166 |

  The two-sided 95% bootstrap intervals include 0 at all three frequencies — at weekly frequency only just (−1.77 to +0.003).
- **One week drives the weekly result:** without the week ending 20 May 2022 (−21.7%, after quarterly results) the weekly skewness falls
  from −0.85 to −0.32 (notebook 03, section 6).
- Conclusion: negative skewness is **weak evidence at best**: significant at weekly frequency only in the one-sided tests and because of one
  week; at monthly frequency only in the centred version; never two-sided. Daily skewness is dominated by a few extreme days in both tails
  (30 days below −3σ, 28 above +3σ). Do not over-claim.
- This replaces the draft's planned `skewtest` (which assumes normal tails and rejects symmetry at every frequency, p ≤ 0.037 — misleading here).
- Kurtosis (draft's bullet 3): excess kurtosis > 0 at all frequencies (see 2.1.2).

### 2.1.4 Volatility clustering (F03, F07, F08, F11; T09)

- Daily: Ljung-Box on |r| p < 0.001 and on r² p < 0.001; ARCH-LM(10) = 235.9, p < 0.001 → **strongly supported**.
- Weekly: Ljung-Box on |r| p < 0.001 but on r² p = 0.188 and ARCH-LM p = 0.351 → **partial**. The r² test is very sensitive to one
  outlier: **without the week ending 20 May 2022 its p-value falls to 0.002**. The |r| test, less affected by outliers, is the more reliable
  one here — so weekly clustering is probably present but masked by one extreme week.
- Monthly: no evidence (|r| p = 0.848, r² p = 0.672, ARCH-LM p = 0.767) → **not supported**.
- GJR-GARCH persistence (α + γ/2 + β) ≈ 0.92 at daily frequency (Student-t).
- Conclusion: clustering is a **high-frequency** phenomenon for WMT; SPY shows it at all three frequencies (T09) — the market index is more
  affected by common volatility shocks than a defensive stock.

### 2.1.5 Leverage effect (F09, F10, F11; T10, T11)

- GJR-GARCH(1,1), daily, **Student-t**: γ = 0.071, **p = 0.006** → negative shocks raise next-day variance more than positive shocks of the same size
  (news impact curve F09 is steeper on the left). With **normal** innovations γ = 0.081 but p = 0.202 (not significant) — the fat tails
  matter for the inference; report the Student-t model (lower AIC: 12,323.6 vs 13,380.4). These p-values use robust standard errors;
  with non-robust ones the normal-model γ would also be significant (p < 0.001), so the *existence* of the daily effect does not depend on
  the distribution, only how strongly it shows.
- Correlation of r(t) with |r(t+1)|: −0.073 for WMT (SPY: −0.117, negative up to 10 days) — a weak but negative relation.
- Weekly: γ not significant in the Student-t model (p = 0.98). Monthly: the Student-t model is **at the boundary** (α = 0, β = 1: no
  volatility dynamics), so the monthly cell is **Inconclusive** — say so. Model-free check, one period ahead: corr(r_t, |r_t+1|) =
  −0.064 weekly (95% band ±0.066) and −0.045 monthly (±0.139) — negative but inside the band (SPY: −0.285 and −0.369, outside it). At those
  frequencies the honest conclusion is "no evidence", not "evidence against".
- Conclusion: **supported at daily frequency only**; much weaker than for SPY (daily γ = 0.281, p < 0.001), which is consistent with WMT's
  defensive profile.
- Technical note: returns were multiplied by 100 before estimating the GARCH models (standard for numerical stability).

### 2.1.6 Conditional non-normality (F12; T12)

- Standardised residuals z = ε/σ of the daily GJR-GARCH-t: excess kurtosis **15.7**, skewness −0.66, Jarque-Bera p < 0.001 → the volatility model
  removes the clustering (Ljung-Box on z² p = 0.96) but **not** the fat tails.
- Estimated Student-t degrees of freedom ν ≈ 3.9 (daily) and 4.1 (weekly) — very heavy tails; Q-Q plots against the Student-t fit much better
  than against the normal (F12), with some departures in the extreme tail remaining.
- **Why is the kurtosis of z (15.7) higher than that of the raw returns (14.3)?** The biggest earnings-day jumps hit when the predicted volatility
  was *low* (σ_t ≈ 0.95% on 14 Oct 2015, 1.15% on 17 May 2022, 1.06% on 16 Nov 2017, against an average of 1.18%), so dividing by σ_t makes them
  even bigger z-scores (−11.2, −10.6, +9.7), while crisis days are absorbed (17 March 2020: σ_t = 4.67%, z = 2.4). With ν ≈ 3.9 (< 4) the fitted
  distribution has no finite fourth moment, so the kurtosis numbers are descriptive and driven by a handful of days (without the 5 largest
  |z|: 7.7). The Jarque-Bera rejection is what matters.
- Weekly: z excess kurtosis 7.1 (JB p < 0.001). Monthly: 0.66 (JB p = 0.029 with the t model, 0.110 with the normal), but the monthly t model is
  at the boundary → **Inconclusive**.
- Conclusion: **supported at daily and weekly frequency** → Gaussian innovations are inadequate; a Student-t is a better description.

**Overall conclusion of section 2.1:** the evidence supports little serial correlation and non-normality with fat tails at all frequencies,
and conditional non-normality at daily and weekly frequency; volatility clustering and the leverage effect are clear at daily frequency but
fade with aggregation (the monthly GARCH models are degenerate, so those cells are inconclusive); negative skewness is weak (one-sided,
weekly, driven by one week). As the brief asks, not every fact holds at every frequency. For portfolio construction this
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
| Group pick | 1/N on all 23 group stocks (22 before TSLA) | The group's own universe in equal weights; same rules as the strategies |
| SPY | buy & hold | Market benchmark, no costs |

- **Common constraints:** long-only (w ≥ 0), fully invested (Σw = 1), no leverage, no weight caps.
- **Markowitz is distinct from GMV and Max Sharpe** (brief requirement): with λ = 3 the investor trades some variance for return; λ → ∞ gives
  GMV, and the tangency (Max Sharpe) portfolio corresponds to a different point of the frontier. F15 shows the three on the in-sample frontier.
  In the 23-stock illustration, Markowitz holds 3 stocks with a 76% maximum weight, Max Sharpe 10 stocks and GMV 17 (table TA04).
  **Why λ = 3:** a moderate, commonly used value of risk aversion, set in the first version of the backtest code and never changed
  (the brief: "do not tune parameters"); λ = 1 and 5 are shown only as a sensitivity check.
- **Inverse volatility vs ERC when assets are correlated** (brief requirement): inverse volatility equalises w_i·σ_i but ignores correlations,
  so the risk contributions are not equal — in the 23-stock illustration they range from **−1% to 6.6%** of portfolio risk, while ERC gives
  exactly **4.3% (= 1/23)** to every stock; ERC gives less weight to stocks that are highly correlated with the others (F14, table TA05).
- **Estimation:** μ and Σ from the trailing 252 daily simple returns, annualised (×252); optimisation with `scipy.optimize` (SLSQP);
  if it fails, one retry with a looser tolerance, then equal weights (logged). **0 optimisation failures** in all runs (T36) — the brief asks to
  document failures and not to remove runs silently. Because "no failure" only means that the optimiser stopped normally, notebook 04
  (section 8) also checks the solutions: in every rebalancing the weights add up
  to 1 (largest error 4·10⁻¹⁶) and are never negative, and the ERC risk contributions equal 1/N to within 0.01% of 1/N (largest gap 8·10⁻⁶).
- **Max Sharpe safety rule:** if no stock has an expected return above r_f, the tangency portfolio does not exist; the rule then uses the GMV
  weights and logs it. It never happened in our runs (the log is empty).
- **Group pick vs EW:** both use equal weights, but EW holds the 12 stocks drawn at random in each experiment (it tests an *allocation rule*),
  while the Group pick holds **all** the group's stocks. Since EW's 12 stocks are drawn from the same 23, the comparison measures the effect of
  holding **23 stocks instead of 12** (more diversification), **not stock-picking skill** — do not call it "stock selection" in the report. On
  the full 23-stock universe the two are identical (checked in notebook 04, section 10.6). It also means that rankings which include the Group
  pick mix two universe sizes; T32–T33 compare all the strategies on the same 23 stocks.

### 3.2 Backtest design (T14; F16; table TA02)

- **100 experiments**, random seed **2026**: each = one contiguous 3-year window (756 trading days) + 12 stocks drawn from the 23 (only stocks
  with data in the whole window). The same periods and stocks are used for every strategy (brief requirement).
- **Why 12 of 23:** about half the universe gives the largest number of different subsets (C(23,12) = 1,352,078), so two experiments share only
  ≈ 6.3 stocks on average; and 12 stocks with 252 daily observations (N/T ≈ 0.05) keep the sample covariance matrix well conditioned. The
  checks with a new random draw and with all eligible stocks (T31, TA12) show that the main conclusions do not depend on this choice.
- **Split** (the brief asks to specify it): in each 756-day window, days 1–504 are the estimation period and **days 505–756 the out-of-sample
  year** (252 days). With the trailing 252-day window, the warm-up weights (held from day 379) use days 127–378, and the evaluation weights use
  days 253–504 (applied from day 505) and 379–630 (from day 631); days 1–126 are not used and only days 505–756 enter the metrics.
  Out-of-sample years run from Jan 2012 to Aug 2026; they start in only 14 calendar years (98 distinct start dates), so they overlap heavily:
  each day belongs to ≈ 7 experiments on average and at most 13 out-of-sample years do not overlap (section 4.2, T38).
- **Trailing 1-year estimation window**; **semi-annual rebalancing** (every 126 trading days); the first rebalancing is one semester before the
  evaluation year (warm-up), so the portfolio already exists on day 1 of the evaluation.
- **No look-ahead inside the backtest:** weights use only data up to the close of t−1 (returns and DGS3) and are traded at that close
  (market-on-close), so they apply from day t. The brief says to "execute trades after the information becomes available": trading at the same
  close as the last price used is the usual backtest convention but slightly optimistic, so we also ran the whole backtest **one day later**
  (estimation up to t−2, trade at the close of t−1): the order by average rank does not change and the median Sharpe ratios move by
  at most 0.065 (T42, section 5.1).
  Eligibility requires data over the whole 3-year window; strictly this uses information about the evaluation year, but here it only excludes
  TSLA from the 6 windows that start before its IPO (missing *past* data), so it introduces no look-ahead in practice.
  **The universe itself is chosen ex post** (today's largest stocks) — say so here and refer to 5.4 and T43.
- **Parameters fixed in advance** (brief: "agreed before comparing results"): semi-annual rebalancing and 10 bps were specified in the group's
  draft before any backtest was run; λ = 3, 12 stocks, the 1-year window and seed 2026 were set in the first version of the backtest code
  (7 October 2026) and never changed. The alternatives are reported only as robustness checks. (Write it this way: it can be verified in the
  git history.)
- **Weights drift** between rebalancing dates; **turnover** = Σ|Δw| between the drifted and the target weights (purchases + sales);
  **cost** = 10 bps per unit of this two-way turnover (switching the whole portfolio costs 20 bps), deducted on the rebalancing day. The initial
  purchase happens at the warm-up rebalancing, before the evaluation year. Returns reported **before and after costs** (brief requirement).
- **Why semi-annual:** the brief suggests quarterly as a common convention "to be agreed"; the group chose semi-annual in its draft, before
  any result (half the trading; and with a 1-year estimation window, quarterly re-estimation reuses 75% of the same data, so much of the extra
  trading reacts to noise). Lower costs alone are not a strong argument at 10 bps, so **show the quarterly results next to the main ones**
  (T27): experiment by experiment the Sharpe ratios change by at most ≈ 0.04 and the average ranks barely move.

### 3.3 Performance measures and conventions (state them precisely — brief requirement)

- **Annualised return** (geometric): (Π(1+R_t))^(252/n) − 1. **Volatility:** sd(R_t)·√252.
- **Sharpe:** mean(R_t − r_f,t) / sd(R_t − r_f,t) · √252, with the daily DGS3 rate (annual yield / 252).
- **Sortino:** mean excess return / downside deviation √mean(min(R_t − r_f,t, 0)²) · √252.
- **Maximum drawdown:** largest fall from a previous peak of wealth (starting at 1). **Calmar:** return / |MDD|.
- **Sterling:** return / (|MDD| + 10%) — the original definition uses the *average annual* drawdown over several years; with a 1-year
  evaluation window it becomes that year's MDD, so this is a **1-year variant**. The +10% is about half of the denominator (median |MDD| ≈ 9–14%
  for all portfolios except Markowitz), so it ranks the portfolios almost like the return does (rank correlation with the return ≈ 0.96). Say this in the report,
  and use **Calmar** (no +10%) as the drawdown-based ratio for the comparisons.
- **Turnover** (sum over the evaluation year), **cost drag** (gross minus net annual return — a little larger than cost × turnover, because the
  money paid in costs would otherwise have compounded over the rest of the year), **effective N** = 1/Σw², **maximum weight**,
  **diversification ratio** (ex-ante).
- **CAPM (Lab 4.1):** R_p − r_f = α + β(R_SPY − r_f) + ε on the 252 daily returns of each out-of-sample year → β, Jensen's α (×252), tracking error
  and information ratio against SPY.
- **Summaries across experiments:** medians, dispersion (P25/P75), % of experiments in which a portfolio beats EW (and the Group pick and SPY)
  **in the same experiment**, **average rank** in each experiment (more stable than the rank of the medians, which sit close together) and
  head-to-head win rates. **No significance tests that assume independence:** the windows overlap, so the 100 experiments are not independent
  (brief requirement — say it explicitly); the uncertainty of the key win rates is shown with a **cluster bootstrap by start year** (T38).

---

## 4. Results (draft section 3, second part)

### 4.1 Main table — medians across the 100 experiments, net of 10 bps (T15; F17, F18)

| Portfolio | Return | Volatility | Sharpe | Max DD | Calmar | Sterling | Turnover | Eff. N |
|---|---|---|---|---|---|---|---|---|
| EW | 31.2% | 16.9% | 1.81 | −11.1% | 3.30 | 1.68 | 0.27 | 12.0 |
| Markowitz (λ=3) | 39.8% | 34.5% | 1.23 | −23.5% | 2.09 | 1.37 | 2.21 | 1.5 |
| GMV | 17.3% | 12.8% | 1.34 | −9.8% | 2.01 | 0.93 | 0.95 | 4.4 |
| Max Sharpe | 27.9% | 20.8% | 1.29 | −14.4% | 2.19 | 1.28 | 2.14 | 2.8 |
| Inverse vol | 25.7% | 14.7% | 1.78 | −9.8% | 3.16 | 1.47 | 0.27 | 10.9 |
| Risk parity (ERC) | 26.5% | 14.4% | 1.80 | −10.0% | 3.22 | 1.48 | 0.31 | 10.7 |
| Most diversified | 28.7% | 15.2% | 1.70 | −10.7% | 3.05 | 1.41 | 0.84 | 6.3 |
| Max decorrelation | 33.3% | 19.0% | 1.66 | −13.1% | 2.83 | 1.58 | 0.86 | 7.1 |
| Group pick (23 stocks) | 35.6% | 15.8% | 1.70 | −10.1% | 2.98 | 1.60 | 0.28 | 23.0 |
| SPY (buy & hold) | 17.7% | 14.0% | 1.13 | −9.4% | 2.00 | 0.89 | 0.00 | — |

(Sortino, gross figures, cost drag, maximum weight and diversification ratio are also in T15.)

**Important:** the absolute returns are very high (median ≈ 31% for EW) because the 23 stocks are today's large winners (survivorship and
selection bias, section 5.4). **Compare the strategies with each other, and read the comparison with SPY with the hindsight warning.**

### 4.2 How sure are we? (T38)

The 100 out-of-sample years overlap: each day belongs to ≈ 7 experiments on average (between 1 and 14), at most **13** out-of-sample years
do not overlap, and they start in only **14** calendar years. So "% of experiments" are much less precise than 100 independent tests.
T38 gives a 95% band for the key comparisons (cluster bootstrap: whole start years resampled 2,000 times). A difference is **clear** only if
its band excludes 50%:

| Clear (band excludes 50%) | Not clear (band includes 50%) |
|---|---|
| Markowitz loses to EW on Sharpe (beats it in 21%, band 11–32%) | ERC vs EW on Sharpe (51%, band 36–68%) |
| GMV loses to EW on Sharpe (31%, band 17–48%) | Inverse vol vs EW (47%, 30–67%), most diversified vs EW (47%, 32–66%) |
| ERC beats inverse vol (65%, band 54–78%) | Max Sharpe vs EW (34%, 20–50%), Max decorrelation vs EW (41%, 32–53%) |
| ERC lower volatility than EW (100%) and smaller drawdown (86%, 77–93%) | Group pick vs ERC (56%, 43–68%) |
| Every 23-stock portfolio beats SPY on Sharpe (ERC 86%, EW 85%, Group pick 92%) | ERC vs SPY on volatility (46%, 30–63%) and drawdown (58%, 44–72%) |
| Group pick beats EW (62%, band 50–72%: at the limit) | |

### 4.3 Key findings (with the numbers)

1. **EW is very hard to beat, and the top group cannot be separated** (T17, T38). ERC (median Sharpe 1.80) and inverse vol (1.78) are level
   with EW (1.81); none of the 8 strategies beats EW on the Sharpe ratio in more than 51% of the experiments. Consistent with DeMiguel,
   Garlappi & Uppal (2009). By **average rank** in each experiment (more stable than ranks of medians), ERC is the best of the 8 rules
   (4.19 vs EW 4.49; T20).
2. **Estimation error sinks the return-based optimisers.** Markowitz: effective N ≈ 1.5, average maximum weight ≈ 77%, turnover ≈ 8× EW (2.21 vs
   0.27 per year), volatility 34.5%, drawdown −23.5%; the highest median return (39.8%) but the widest dispersion (std of annual return 0.68 vs
   0.22 for EW, T16) and a smaller drawdown than EW in only 9% of the experiments. Max Sharpe is similar (Sharpe above EW in 34%). 1-year mean
   returns point to the recent winners, which do not always keep winning.
3. **Low-risk family:** volatility lower than EW in 98–100% of the experiments, maximum drawdown smaller in 65–87% (GMV 65%, ERC 86%, IV 87%), but
   return above EW in only 26–27%. Inverse vol and ERC do it with EW-like turnover (≈ 0.3) and well-diversified weights (effective N ≈ 11 of 12);
   GMV is concentrated (effective N ≈ 4.4, max weight ≈ 35%) and has the lowest return (17.3%).
4. **Drawdown-based ratios (T17).** Because the low-risk strategies give up return (ERC ≈ 4.6 percentage points less than EW in the same
   experiment), their return per unit of drawdown is only level with EW: **Calmar** — ERC beats EW in 49% of the experiments, IV 44%; on the
   **1-year Sterling** ratio they are behind (32–33%). The Sterling ratio the brief asks for is computed here in a 1-year variant
   (|MDD| + 10%): the 10% is about half of the denominator, so it ranks the portfolios almost like the return does (say this in the report).
5. **The Group pick** (our 23 stocks in equal weights): best average rank (3.9 of 10; 1st in 33% of the experiments, top 3 in 50%) and the most
   head-to-head wins on the Sharpe ratio (68% on average; T20–T22). **The edge comes from holding 23 stocks instead of 12** (diversification),
   not from better stocks: EW's 12 stocks are drawn from the same 23, the Group pick earns more than EW in only 49% of the experiments (mean
   returns ≈ 32% for both), its median Sharpe (1.70) is below EW's (1.81), and on the same 23 stocks it is simply EW — ERC and most diversified
   match it (54% and 52%, T33). It beats 5 of the 9 rivals on return and only 4 of 9 on volatility and drawdown (TA07–TA09).
6. **Head-to-head ranking by Sharpe** (average % of comparisons won, T22): Group pick 68%, ERC 65%, EW 61%, inverse vol 59%, most diversified 58%,
   max decorrelation 55% | Max Sharpe 40%, GMV 38%, Markowitz 29%, SPY 27%. On volatility the order reverses: GMV 96%, ERC 74%, SPY 72%,
   inverse vol 70%. No portfolio wins on every metric.
7. **SPY** has the lowest median Sharpe (1.13) and one of the lowest returns (17.7%). Its median drawdown is the smallest (−9.4%), but in the same
   experiment inverse vol, ERC and GMV have a smaller drawdown than SPY in 56–59% of the cases (T19) — medians and paired comparisons answer
   different questions. Every 23-stock portfolio earns more than SPY in most experiments (from 51% for GMV to 96% for the Group pick): mostly
   the selection bias of the universe (5.4).
8. **Market risk (CAPM vs SPY, T24, F22):** every portfolio has a positive median Jensen's alpha (+6.0% GMV … +18.3% Markowitz), significant
   (t > 1.96) in only 5–40% of the experiments and mostly due to the selection bias. Betas: GMV 0.64 (below 1 in 99% of the experiments), most
   diversified 0.85, ERC 0.91, inverse vol 0.93, EW 1.04, Group pick 1.05, Markowitz 1.32. The Group pick tracks SPY most closely (R² ≈ 0.90,
   tracking error ≈ 5.4%). ("% IR > 0" = share of years with a higher average daily return than SPY.)
9. **Turnover and costs (F21):** cost drag ≈ 3.4–3.8 bps per year for EW, inverse vol, ERC and the Group pick; ≈ 33 bps for Markowitz (≈ 1% in the
   worst experiment). The cost drag is a little larger than cost × turnover (e.g. Markowitz 33 vs 22 bps) because the money paid in costs would
   otherwise have compounded over the rest of the year. Gross and net figures: T15.
10. **Example during a crisis (F23):** experiment 62 (out-of-sample year 11 Nov 2019 – 9 Nov 2020) shows the paths of all portfolios through the
    March 2020 crash — an illustration only (one experiment is not evidence); T44 has the three experiments that contain the crash.
11. **Trade-offs in one table (T37):** return, volatility, drawdown, Sharpe, % beats EW, effective N, turnover, what is estimated and complexity.

---

## 5. Robustness checks and limitations

### 5.1 Robustness (notebook 04, sections 10–12)

- **Higher costs (T25, T26, T41):** from 0 to 50 bps the average rank of each portfolio moves by less than 0.1 (ERC 4.21 → 4.12, EW 4.52 → 4.45);
  only most diversified and the Group pick swap places in the ranking of medians (1.707 vs 1.705 at 0 bps). Markowitz loses ≈ 0.045 of median
  Sharpe between 0 and 50 bps, EW only ≈ 0.007. In this liquid universe, what separates the strategies is estimation error, not costs.
- **Quarterly rebalancing (T27, the brief's suggested convention):** experiment by experiment, the Sharpe ratio of each portfolio changes by at
  most ≈ 0.04 (median paired change) and the % beating EW by at most 5 percentage points; the average ranks barely move (ERC 4.34, EW 4.37).
  The ranking of the **medians** changes more (EW falls from 1st to 5th) only because the medians sit close together — show the quarterly
  column next to the main one. Turnover rises by 29–44%.
- **Markowitz risk aversion (T28):** λ = 1 → effective N = 1.0 (one stock), volatility 40.5%, Sharpe 1.11; λ = 5 → effective N ≈ 2.0, volatility
  29.8%, Sharpe 1.31. A higher λ moves Markowitz towards GMV but does not solve the concentration (Lab 3.1 risk-aversion effect).
- **Sub-periods (T29, T39, F25):** experiments are assigned by the middle of their out-of-sample year (32 / 27 / 41 experiments). The Group pick
  beats EW in 69% (2012-16), 63% (2017-20) and 56% (2021-26) of the experiments — its edge shrinks in the most recent period; ERC 50 / 44 / 56%;
  Markowitz deteriorates (37 / 15 / 12%).
- **Market regimes (T30, T40):** in the 12 experiments whose out-of-sample year had a negative SPY return (overlapping windows from about four
  episodes — 2015-16, 2018, 2019-20, 2021-23; median SPY return −5.4%), all 23-stock portfolios did much better than SPY (EW +3.7%), which is
  mostly the selection bias. The relevant evidence is relative: **ERC, inverse vol and GMV had a smaller drawdown than EW in 92%** of those
  experiments (11 of 12), the Group pick in only 25%; ERC had the best average Sharpe rank (4.4) in those years.
- **Crash (T44):** in the three experiments that contain March 2020, ERC, inverse vol and GMV fell about as much as EW (e.g. experiment 62:
  ERC −31.1%, EW −29.4%, SPY −33.7%): correlations jumped towards 1 and diversification stopped working. Their drawdown protection comes from
  moderate sell-offs (2018, 2022), not crashes.
- **Execution lag (T42):** trading one day later (estimation up to t−2) leaves the order by average rank unchanged (by medians, only most
  diversified and the Group pick swap, a tie at 1.704); medians move by at most +0.065 (Markowitz) and the %
  beating EW by at most 2 percentage points → the same-close convention is not driving the results.
- **Asset subset (T31, TA12):** with a new random draw of 12 stocks or with all eligible stocks, the order inside the top group changes (by
  medians), but by average rank ERC is the best of the 8 rules in all three versions (4.19 / 4.26 / 4.00) and Markowitz and Max Sharpe stay at the
  bottom.
- **Hindsight in the universe (T43):** without the five biggest winners of 2010-2026 (NVDA, AVGO, TSLA, MU, AMD — also among the most volatile
  stocks), drawing the 12 stocks from the other 18 on the same periods: the EW − ERC return gap falls from 4.6 to 0.9 percentage points, ERC
  beats EW in 52% of the experiments, Markowitz loses its top return (18.1% vs EW 21.9%; Sharpe 0.75), and **ERC has lower volatility than SPY in
  89% and a smaller drawdown in 79%** of the experiments (main universe: 46% and 58%), with a higher Sharpe in 83%. A sensitivity check, not an
  unbiased result.
- **Strategies on the group's 23 stocks (T32, T33, F26):** most diversified (median Sharpe 1.85) and ERC (1.75) vs the Group pick (1.70): they beat
  it in only 52% and 54% of the experiments (median paired differences +0.02 and +0.01); ERC has lower volatility in 100% and a smaller drawdown in
  93%, but more return in only 23%.

### 5.2 The Group pick over the full sample (T34, T35, F27, F28) — appendix only (descriptive, biased by hindsight)

- 2010-01-05 to 2026-09-18, semi-annual rebalancing, 10 bps: **1 USD → 46.0 USD** (CAGR 25.8%, volatility 18.4%, Sharpe 1.24, max drawdown −32.2%) vs
  SPY 9.0 USD (14.1%, 17.1%, 0.75, −33.7%) and ^GSPC 6.8 USD (12.1%, price index); the Group pick beat SPY in 15 of 17 calendar years.
- **Not evidence that the pick would have beaten the market in real time** — the 23 stocks were chosen in 2026. Put it in the appendix, with the
  warning. (Its Sterling ratio uses the average of 17 calendar-year drawdowns + 10%, unlike the backtest.)

### 5.3 What the brief asks to document (checklist)

- Asset eligibility (only stocks with data in the whole window; TSLA not eligible in 6 windows) ✔ · sample size (100 × 252 out-of-sample days) and
  overlap (T38) ✔ · missing data (not filled) ✔ · optimisation failures (0, T36) ✔ · survivorship bias and reliance on today's universe (5.4, T43) ✔ ·
  turnover and performance before and after costs (T15) ✔ · cost convention and ranking under higher costs (T25, T26, T41) ✔ · dependence on the
  period and the asset subset (T29–T31, T39, T40) ✔ · overlapping windows not treated as independent tests (T38) ✔.

### 5.4 Limitations (copy into the report)

- **Survivorship and selection bias.** The 23 stocks were chosen in September 2026 among today's largest companies; the brief allows today's
  universe if it is discussed ("discuss survivorship bias and any reliance on today's asset universe"). It inflates the absolute returns of every
  portfolio and every comparison with SPY, and it is **not neutral between strategies**: the biggest winners are also the most volatile stocks, so
  it flatters EW, Max decorrelation and Markowitz against the low-risk strategies (T43). Drawing 12 of the 23 at random does not remove it.
  Rules that underweight volatile stocks are also supported by the documented low-volatility effect (Ang et al. 2006; Baker, Bradley & Wurgler 2011;
  Frazzini & Pedersen 2014), which this hindsight universe works against.
- **Overlapping experiments:** ≈ 7 experiments per day, at most 13 non-overlapping years; we report medians, dispersion, frequencies and
  cluster-bootstrap bands, not tests that assume independence.
- **Few stress episodes:** the sample starts in 2010 (all stocks but TSLA trade), so the 2008-09 crisis is excluded; only 12 experiments have a
  falling market, and the one crash (2020) shows no protection.
- **Estimation error:** 1-year sample means are very noisy (mainly hurts Markowitz and Max Sharpe); no shrinkage or weight limits (extensions A and B).
- **Execution and costs:** same-close trading (a one-day lag changes nothing material, T42); fixed proportional costs, no market impact or taxes;
  SPY's ≈ 0.09% fee is already in its price.
- **Risk-free rate:** the 3-year Treasury matches the 3-year horizon of each experiment and is an official daily series, but it carries some
  duration risk (a 3-month T-bill is the textbook choice). Its level lowers every Sharpe/Sortino ratio by ≈ r_f/σ — more for low-volatility
  portfolios — and enters the Max Sharpe optimisation; returns, volatility, drawdowns, Calmar and Sterling do not depend on it.
- **Drawdown ratios:** with one evaluation year, the 1-year Sterling is dominated by its +10% and Calmar uses a single year's drawdown.
- **Statistics:** the skewness bootstrap resamples individual days (ignores volatility clustering); CAPM OLS t-statistics are only indicative.
- **Universe:** only US large caps; results may not transfer to other markets or asset classes.

---

## 6. Conclusions and recommendation (investor objective + when to reconsider — brief requirement)

- **Target investor:** a long-term investor in US large-cap equities choosing between **buying the index (SPY)** and running a **rules-based
  portfolio of large US stocks**, who wants **lower volatility and drawdowns without giving up risk-adjusted return**, at low cost and low complexity.
- **Recommendation: risk parity (ERC).** Evidence: the most robust of the 8 rules (best average rank in the main run, with a new draw of stocks,
  with all eligible stocks, with a one-day lag, and in the years in which SPY fell; level with EW under quarterly rebalancing); clearly better than
  inverse vol (65%, band 54–78%); volatility always below EW and drawdown below EW in 86% of the experiments (92% when the market fell); turnover ≈ 0.3
  per year (cost ≈ 4 bps); diversified weights (effective N ≈ 11 of 12); beta ≈ 0.91.
- **What to promise against the index:** the higher returns of all 23-stock portfolios are mostly hindsight. Once the five biggest winners are
  removed, ERC has **lower volatility than SPY in 89%** of the experiments and a **smaller drawdown in 79%**, with a higher Sharpe ratio in 83% —
  so the realistic benefit is a **smoother path at a similar risk-adjusted return**, not a higher return. In the main (hindsight) universe ERC is
  only level with SPY on risk.
- **SPY remains the default** for an investor who does not want to run a stock portfolio: cheaper, simpler, no selection risk.
- **For an investor who accepts equity volatility for return:** equal weights over a broad universe (the Group pick is EW on 23 stocks) — but the
  universe must be chosen by a rule that does not use hindsight.
- **Not recommended:** unconstrained Markowitz and Max Sharpe (extreme concentration, ≈ 8× the turnover, clearly worse than EW).
- **When to reconsider (measurable triggers):** (i) ERC's realised volatility over the last 24 months is not below SPY's; (ii) a crash in which
  correlations jump (as in March 2020) — ERC gives no protection there; (iii) market leadership concentrated in a few high-volatility mega-caps,
  where ERC lags EW and the index; (iv) costs or turnover much higher than here; (v) weight limits or a shrinkage covariance (brief extensions A and
  B) could make Markowitz and Max Sharpe usable; (vi) a universe defined by an **ex-ante rule** (e.g. the largest stocks of each sector at each
  date), which is the real test without hindsight.
- "A strategy that performs poorly can still support a strong project if the analysis explains why" (brief): Markowitz's failure is the clearest
  illustration of estimation error — explain it.

---

## 7. References (suggested; add the course materials)

- Ang, A., Hodrick, R. J., Xing, Y., & Zhang, X. (2006). The cross-section of volatility and expected returns. *Journal of Finance*, 61(1), 259–299.
- Bacon, C. R. (2008). *Practical Portfolio Performance Measurement and Attribution* (2nd ed.). Wiley. (Sortino, Calmar, Sterling ratios.)
- Baker, M., Bradley, B., & Wurgler, J. (2011). Benchmarks as limits to arbitrage: Understanding the low-volatility anomaly. *Financial Analysts Journal*, 67(1), 40–54.
- Black, F. (1976). Studies of stock price volatility changes. *Proceedings of the 1976 Meetings of the American Statistical Association, Business and Economic Statistics Section*, 177–181.
- Bollerslev, T. (1986). Generalized autoregressive conditional heteroskedasticity. *Journal of Econometrics*, 31(3), 307–327.
- Bollerslev, T., & Wooldridge, J. M. (1992). Quasi-maximum likelihood estimation and inference in dynamic models with time-varying covariances. *Econometric Reviews*, 11(2), 143–172. (Robust standard errors of the GJR-GARCH.)
- Choueifaty, Y., & Coignard, Y. (2008). Toward maximum diversification. *Journal of Portfolio Management*, 35(1), 40–51.
- *Maximum decorrelation portfolio:* cite the source used in Lab 5 (risk-based portfolios) of the course.
- Cont, R. (2001). Empirical properties of asset returns: stylized facts and statistical issues. *Quantitative Finance*, 1(2), 223–236.
- DeMiguel, V., Garlappi, L., & Uppal, R. (2009). Optimal versus naive diversification: How inefficient is the 1/N portfolio strategy? *Review of Financial Studies*, 22(5), 1915–1953.
- Efron, B. (1979). Bootstrap methods: Another look at the jackknife. *Annals of Statistics*, 7(1), 1–26.
- Engle, R. F. (1982). Autoregressive conditional heteroscedasticity with estimates of the variance of United Kingdom inflation. *Econometrica*, 50(4), 987–1007.
- Engle, R. F., & Ng, V. K. (1993). Measuring and testing the impact of news on volatility. *Journal of Finance*, 48(5), 1749–1778.
- Frazzini, A., & Pedersen, L. H. (2014). Betting against beta. *Journal of Financial Economics*, 111(1), 1–25.
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
- **Data:** Yahoo Finance (via the `yfinance` Python library), adjusted daily prices, extracted between 21 and 29 September 2026 [write the exact date if known]. Board of Governors of the
  Federal Reserve System (US), *Market Yield on U.S. Treasury Securities at 3-Year Constant Maturity* [DGS3], retrieved from FRED, Federal Reserve
  Bank of St. Louis, https://fred.stlouisfed.org/series/DGS3, 8 October 2026. BlackRock iShares (sector weights, September 2026 — as in the draft; [write the exact file and date]).
- **Course:** Bravo, J. M. (2026). *Asset Pricing & Portfolio Management* — project brief and Labs 1–5 (NOVA IMS).

---

## 8. Reproducibility appendix (brief: "include all supporting files needed to reproduce the results")

- **Code:** GitHub repository, notebooks `01_data_collection` (data, not re-run: it would download new prices), `02_walmart_eda`, `03_stylised_facts_garch`,
  `04_strategies_backtest`, `05_report_pack` (this folder). Each is also saved as HTML (acceptable for submission according to the brief).
- **Data:** `notebooks/data/` (frozen prices and returns, WMT history, FRED DGS3 with its download date in `risk_free_DGS3_info.txt`).
- **Randomness:** seed **2026** (100 experiments; also the 2,000-resample skewness bootstrap in notebook 03), 2027 (the "new draw" robustness
  check), 2028 (the draw without the five biggest winners, T43), 2029 (the cluster bootstrap of the uncertainty bands, T38) and 123 (the
  simulated normal series of notebook 02, figure FA06); NumPy's legacy `RandomState`, frozen across versions.
- **Data checks:** notebook 01, section 9, re-checks the frozen CSV files (4,203 days; only TSLA has missing values, 122 sessions before its first
  price; weekly and monthly returns equal the sum of the daily log returns, largest difference ≈ 2·10⁻¹⁵). Notebook 04, section 8, checks the
  optimiser solutions (weights add up to 1, no negative weights, ERC risk contributions equal 1/N).
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
2. **Data source and extraction date:** say "stocks, SPY and ^GSPC from Yahoo Finance (adjusted close), extracted on [date] September 2026
   (between 21 and 29 September if the exact day cannot be confirmed); risk-free rate from FRED". Add the data-treatment paragraph
   (dividends, splits, spin-offs, currency, calendar, missing data, SPY vs ^GSPC), the reason for starting in 2010 and the inclusion rule —
   section 1 of these notes.
3. **META footnote:** "approximately 550 trading days missing" → **599 trading days** (listed 18 May 2012). TSLA: 122 trading days (OK), and say how it
   is treated (not filled; not eligible in 6 of the 100 windows). State the **15-year inclusion rule** that explains why TSLA stays and META goes,
   and check the claim that T is the next-largest stock of the sector (section 1).
4. **"All selected assets remain eligible throughout the backtest period"** — not exactly: TSLA is not eligible in windows starting before 30 June 2010.
5. **"This bias may be partially mitigated through the analysis of 100 randomly selected portfolios"** — incorrect: random subsets of the same 23
   survivors keep the bias. Replace with the limitation in 5.4.
6. **"Using the same set of securities ensures that performance differences are driven primarily by the allocation methodology"** — in each experiment all
   strategies use the same 12 drawn stocks (true), but the Group pick uses all 23; explain the difference (3.1).
7. **Metrics list:** add the **Sterling ratio** (required: "a drawdown-based measure such as the Sterling ratio") and define the conventions
   (annualisation, risk-free, Sterling denominator — section 3.3); say that the 1-year Sterling ranks almost like the return and add **Calmar**.
   Diversification ratio is ex-ante.
8. **Markowitz:** replace the open notes ("target return... / risk aversion...") with the decision: λ = 3, sensitivity λ = 1 and 5 (T28).
9. **Strategies e) and f)** have no description in the draft → use T13 and the inverse-vol vs ERC paragraph (3.1).
10. **2.1.1:** add the ACF and Ljung-Box results at the three frequencies (T05, T06, F04). **2.1.2–2.1.6:** add the weekly and monthly evidence
    ("complementar com info mensal") — section 2 of these notes.
11. **2.1.3:** replace the planned `skewtest` with the bootstrap test (T08); the draft's three bullets become: skewness negative at all frequencies but
    significant only weekly, one-sided (p = 0.026; two-sided 0.053), and driven by one week (May 2022).
12. **2.1.5:** report the GJR-GARCH γ and p-value (daily Student-t: γ = 0.071, p = 0.006). **If any GARCH figure or number in the draft comes from the
    version of notebook 02 in the group repository's `main` branch, replace it:** that version fits the GARCH on unscaled returns, so the optimiser
    stays at its starting values (α = 0.05, γ = 0.10, β = 0.80) — those estimates are not valid. Use F09–F12 and T10.
13. **Section 3 results** do not exist yet in the draft → section 4 of these notes; add the robustness and limitations (section 5) and the
    recommendation (section 6).
14. **Cover page:** names and student numbers; **executive summary** first (section 0); **references** and **reproducibility appendix** at the end.
15. The rebalancing is **semi-annual** (draft: OK); show the quarterly results (the brief's suggestion) next to the main ones (T27), and the
    one-day execution lag (T42).
16. **"The 100 historical simulations use a three-year rolling window"** → they are 100 randomly sampled (overlapping) contiguous three-year windows,
    each with 12 randomly drawn stocks; the *rolling* part is the 1-year estimation window re-estimated at each rebalancing inside each window.
17. **Selection rule:** "one stock per 5% of sector weight" gives Consumer Staples (~6%) one stock, but the table has two (WMT and COST) — the rule
    alone gives 22 stocks. Explain why Consumer Staples has two (e.g. to include WMT, the stock of the single-share study). Also, the sector weights
    in the draft table add up to 98.5%, not 100% — round them or add the missing 1.5% (e.g. cash/other in the ETF).
18. **Cost convention:** "0.10% (10 bps) all-in cost" → say "10 bps per unit of turnover Σ|Δw| (purchases + sales)".
19. **Submission:** Moodle, by **30 October 2026**; group report + one individual report per member (`FirstName_Surname_StudentNumber.pdf`),
    PDF or Word (an HTML notebook is also acceptable), with all supporting files (code, data or data-retrieval instructions, Excel workbooks).
20. **Group pick wording:** wherever the draft or the results say the Group pick shows the group's "stock selection", replace it with "holding all
    23 stocks instead of 12" (section 3.1) — EW's 12 stocks come from the same 23.
21. **Monthly GARCH:** the monthly leverage-effect and conditional-non-normality cells are **Inconclusive** (the monthly GARCH has no volatility
    dynamics); do not write "supported" or "rejected" there (T03).

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
