# Report pack - index of figures and tables

Created automatically by `notebooks/05_report_pack.ipynb` (do not edit by hand: run the notebook again).
Figures are in `figures/` (numbered in the order of the report); tables are in `tables/report_tables.xlsx` (one sheet per table), `tables/<number>_<name>.csv` and `tables/all_tables.md`.
The written guide with the key findings and numbers is `REPORT_NOTES.md`.

## Figures

| No. | File | Report section | Caption (suggested) | Made by | Main / Appendix |
|---|---|---|---|---|---|
| F01 | `figures/F01_04_universe_correlations.png` | 1. Investment universe and data | Correlation of the daily returns of the 23 selected stocks, 2010-2026 (Yahoo Finance adjusted close prices). | notebook 04, section 2 | Main |
| F02 | `figures/F02_04_risk_free_rate.png` | 1. Data / 3. Assumptions | Risk-free rate: 3-year US Treasury constant-maturity yield (FRED series DGS3), annual %, used as r_f (daily rate = annual / 252). | notebook 04, section 2 | Main |
| F03 | `figures/F03_day_log_returns.png` | 2.1.1 Serial correlation / 2.1.4 Volatility clustering | Daily log returns of Walmart (WMT), 2010-2026. | notebook 02 | Main |
| F04 | `figures/F04_03_acf_returns_wmt.png` | 2.1.1 Little or no serial correlation | Autocorrelation function of WMT log returns at daily, weekly and monthly frequency, with 95% bands (±1.96/√N). | notebook 03, section 3 | Main |
| F05 | `figures/F05_wmt_distribution_with_normal.png` | 2.1.2 Non-normality and fat tails | Histogram of WMT daily log returns with the fitted normal density (same mean and standard deviation). | notebook 02 | Main |
| F06 | `figures/F06_03_qqplot_normal_wmt_3freq.png` | 2.1.2 Non-normality and fat tails / 2.1.3 Asymmetry | Normal Q-Q plots of WMT log returns at daily, weekly and monthly frequency. | notebook 03, section 4 | Main |
| F07 | `figures/F07_03_rolling_volatility_wmt.png` | 2.1.4 Volatility clustering | WMT daily log returns (top) and their 21-day rolling volatility, annualised (bottom): calm and turbulent periods alternate. | notebook 03, section 6 | Main |
| F08 | `figures/F08_03_acf_abs_squared_wmt.png` | 2.1.4 Volatility clustering | Autocorrelation of absolute and squared WMT log returns at daily, weekly and monthly frequency. | notebook 03, section 6 | Main |
| F09 | `figures/F09_03_news_impact_curve.png` | 2.1.5 Leverage effect | News impact curve of the daily GJR-GARCH(1,1) model with Student-t innovations: next-day variance after a negative vs a positive shock of the same size. | notebook 03, section 7 | Main |
| F10 | `figures/F10_03_leverage_correlation.png` | 2.1.5 Leverage effect | Correlation between the daily return r(t) and the absolute return k days later \|r(t+k)\|, WMT and SPY (negative = leverage effect). | notebook 03, section 7 | Main |
| F11 | `figures/F11_03_conditional_volatility_wmt.png` | 2.1.5 Leverage effect / 2.1.4 Volatility clustering | Conditional volatility of WMT estimated with the daily GJR-GARCH(1,1) model (annualised). | notebook 03, section 7 | Main |
| F12 | `figures/F12_03_qqplot_std_residuals_wmt.png` | 2.1.6 Conditional non-normality | Q-Q plots of the standardised residuals of the GJR-GARCH model against the normal and the Student-t distribution, WMT, three frequencies. | notebook 03, section 8 | Main |
| F13 | `figures/F13_04_weights_illustration.png` | 3. Strategies: objectives and constraints | Weights of each strategy estimated with the last 12 months of data on the 23 stocks (illustration, not a backtest result). | notebook 04, section 4 | Main |
| F14 | `figures/F14_04_risk_contributions_iv_vs_erc.png` | 3. Strategies: inverse volatility vs equal risk contributions | Weights and risk contributions of inverse volatility and risk parity (ERC): with correlated assets, inverse volatility does not equalise risk contributions. | notebook 04, section 4 | Main |
| F15 | `figures/F15_04_efficient_frontier.png` | 3. Strategies: Markowitz vs GMV vs Max Sharpe | In-sample efficient frontier (last 12 months, long-only) with the position of each strategy; Markowitz with λ = 3 is distinct from GMV and Max Sharpe. | notebook 04, section 4 | Main |
| F16 | `figures/F16_04_experiment_design.png` | 3. Backtest design | The 100 sampled 3-year periods (grey = 2-year estimation, blue = out-of-sample year) and how often each stock was drawn (seed 2026). | notebook 04, section 5 | Main |
| F17 | `figures/F17_04_boxplots_metrics.png` | 3. Results: distribution across the 100 experiments | Distribution across the 100 experiments of the Sharpe ratio, return, volatility, maximum drawdown, Sortino and Sterling ratios of the 10 portfolios (net of 10 bps). | notebook 04, section 9.2 | Main |
| F18 | `figures/F18_04_risk_return_and_beats_ew.png` | 3. Results: risk-return and comparison with EW | Left: median risk and return of each portfolio. Right: % of experiments in which each portfolio beats the equally weighted benchmark (EW). | notebook 04, section 9.2 | Main |
| F19 | `figures/F19_04_beats_group_pick_and_spy.png` | 3. Results: comparison with the Group pick and SPY | % of experiments in which each portfolio beats the Group pick (left) and SPY (right) on Sharpe, return, drawdown and Sterling. | notebook 04, section 9.2 | Main |
| F20 | `figures/F20_04_pairwise_sharpe.png` | 3. Results: head-to-head comparison of all portfolios | Head-to-head comparison: % of experiments in which the row portfolio has a higher net Sharpe ratio than the column portfolio. | notebook 04, section 9.5 | Main |
| F21 | `figures/F21_04_turnover_costs_concentration.png` | 3. Results: turnover, costs and concentration | Median annual turnover, cost drag (bps per year at 10 bps) and effective number of stocks of each portfolio. | notebook 04, section 9.3 | Main |
| F22 | `figures/F22_04_capm_beta_alpha.png` | 3. Results: market risk (CAPM) | CAPM beta and annualised Jensen's alpha of each portfolio against SPY, estimated in each out-of-sample year (100 experiments, net of costs). | notebook 04, section 9.7 | Main |
| F23 | `figures/F23_04_wealth_example.png` | 3. Results: an example during a crisis | Growth of 1 USD in the out-of-sample year of one experiment that includes the March 2020 crash (net of costs). | notebook 04, section 9.6 | Main |
| F24 | `figures/F24_04_cost_sensitivity.png` | Robustness: transaction costs | Median Sharpe ratio of each portfolio with 0, 10, 25 and 50 bps of transaction costs. | notebook 04, section 10.1 | Main |
| F25 | `figures/F25_04_sharpe_diff_vs_ew_over_time.png` | Robustness: dependence on the period | Sharpe ratio of each portfolio minus that of EW, by evaluation year of the experiment. | notebook 04, section 10.4 | Main |
| F26 | `figures/F26_04_universe23_boxplot_sharpe.png` | Robustness: the strategies on the group's 23-stock universe | Net Sharpe ratio of the strategies applied to all 23 stocks (the same stocks as the Group pick), 100 experiments. | notebook 04, section 11 | Main |
| F27 | `figures/F27_04_fullsample_wealth.png` | Robustness / limitations: full sample (hindsight bias) | Growth of 1 USD, 2010-2026: Group pick vs SPY vs ^GSPC (log scale). Biased by hindsight: the 23 stocks were chosen in 2026. | notebook 04, section 12 | Main |
| F28 | `figures/F28_04_calendar_year_returns.png` | Robustness / limitations: full sample (hindsight bias) | Calendar-year returns of the Group pick, SPY and ^GSPC (2026 = year to date, until 18 September). | notebook 04, section 12 | Main |
| A01 | `figures/A01_normalized_price_history.png` | Appendix: data | Normalised adjusted price of Walmart (initial value = 1), 2010-2026. | notebook 02 | Appendix |
| A02 | `figures/A02_wmt_moving_averages.png` | Appendix: data | Walmart adjusted price with 30-day and 200-day moving averages. | notebook 02 | Appendix |
| A03 | `figures/A03_week_log_returns.png` | Appendix: stylised facts | Weekly log returns of Walmart. | notebook 02 | Appendix |
| A04 | `figures/A04_month_log_returns.png` | Appendix: stylised facts | Monthly log returns of Walmart. | notebook 02 | Appendix |
| A05 | `figures/A05_wmt_log_returns_distribution.png` | Appendix: stylised facts | Distribution of WMT log returns at daily, weekly and monthly frequency. | notebook 02 | Appendix |
| A06 | `figures/A06_wmt_log_returns_vs_normal.png` | Appendix: stylised facts | WMT daily log returns compared with simulated normal returns (Gaussian white noise) of the same mean and volatility. | notebook 02 | Appendix |
| A07 | `figures/A07_04_pairwise_win_rates.png` | Appendix: head-to-head comparison | Head-to-head win rates of the 10 portfolios on Sharpe, return, maximum drawdown, volatility and Sterling, and the median paired Sharpe difference. | notebook 04, section 9.5 | Appendix |
| A08 | `figures/A08_04_universe23_pairwise_sharpe.png` | Appendix: the 23-stock universe | Head-to-head Sharpe comparison of the strategies applied to the 23-stock universe. | notebook 04, section 11 | Appendix |
| A09 | `figures/A09_04_fullsample_drawdowns.png` | Appendix: full sample | Drawdowns of the Group pick, SPY and ^GSPC, 2010-2026. | notebook 04, section 12 | Appendix |
| A10 | `figures/A10_04_avg_weight_by_stock.png` | Appendix: weights | Average weight of each stock when it is drawn, by strategy (equal weight would be 8.3%). | notebook 04, section 10.5 | Appendix |

## Tables

| No. | Title | Report section | Excel sheet | CSV |
|---|---|---|---|---|
| T01 | Investment universe: 23 S&P 500 stocks and SPY, 2010-2026 | 1. Investment universe and data | `T01 universe` | `tables/T01_universe.csv` |
| T02 | Descriptive statistics of WMT and SPY log returns at three frequencies | 2.1 Stylised facts | `T02 descriptive_wmt_spy` | `tables/T02_descriptive_wmt_spy.csv` |
| T03 | Summary: is each stylised fact supported for WMT? | 2.1 Stylised facts (summary) | `T03 facts_summary_wmt` | `tables/T03_facts_summary_wmt.csv` |
| T04 | Evidence for each stylised fact: statistic, p-value and conclusion (WMT, with SPY for comparison) | 2.1 Stylised facts (summary) | `T04 facts_evidence` | `tables/T04_facts_evidence.csv` |
| T05 | Autocorrelation of log returns, lags 1 to 5 | 2.1.1 Little or no serial correlation | `T05 acf_returns` | `tables/T05_acf_returns.csv` |
| T06 | Ljung-Box test on log returns (H0: no autocorrelation up to the lag) | 2.1.1 Little or no serial correlation | `T06 ljung_box_returns` | `tables/T06_ljung_box_returns.csv` |
| T07 | Normality and fat tails: excess kurtosis, Jarque-Bera and frequency of 3-sigma days | 2.1.2 Non-normal distributions and fat tails | `T07 normality` | `tables/T07_normality.csv` |
| T08 | Asymmetry: skewness with a bootstrap test (robust to fat tails) | 2.1.3 Asymmetry and negative skewness | `T08 skewness` | `tables/T08_skewness.csv` |
| T09 | Volatility clustering: Ljung-Box on \|r\| and r^2 and ARCH-LM test | 2.1.4 Volatility clustering | `T09 vol_clustering` | `tables/T09_vol_clustering.csv` |
| T10 | GJR-GARCH(1,1) estimates with normal and Student-t innovations | 2.1.5 Leverage effect | `T10 gjr_garch` | `tables/T10_gjr_garch.csv` |
| T11 | Correlation between r(t) and \|r(t+k)\| (daily) | 2.1.5 Leverage effect | `T11 leverage_correlation` | `tables/T11_leverage_correlation.csv` |
| T12 | Standardised residuals of the GJR-GARCH: skewness, excess kurtosis and tests | 2.1.6 Conditional non-normality | `T12 std_residuals` | `tables/T12_std_residuals.csv` |
| T13 | The portfolios compared: objective, inputs and parameters | 3. Strategies: objectives and constraints | `T13 strategy_definitions` | `tables/T13_strategy_definitions.csv` |
| T14 | Backtest design and conventions (the same for every strategy) | 3. Backtest design and assumptions | `T14 backtest_design` | `tables/T14_backtest_design.csv` |
| T15 | Median performance of the 10 portfolios across the 100 experiments (net of 10 bps) | 3. Results | `T15 median_metrics` | `tables/T15_median_metrics.csv` |
| T16 | Dispersion across the 100 experiments: 25th percentile, median and 75th percentile | 3. Results | `T16 dispersion` | `tables/T16_dispersion.csv` |
| T17 | % of experiments in which each portfolio beats EW in the same experiment | 3. Results | `T17 beats_ew` | `tables/T17_beats_ew.csv` |
| T18 | % of experiments in which each portfolio beats the Group pick in the same experiment | 3. Results | `T18 beats_group_pick` | `tables/T18_beats_group_pick.csv` |
| T19 | % of experiments in which each portfolio beats SPY in the same experiment | 3. Results | `T19 beats_spy` | `tables/T19_beats_spy.csv` |
| T20 | Rank of each portfolio by net Sharpe ratio in each experiment (1 = best of 10) | 3. Results | `T20 rankings` | `tables/T20_rankings.csv` |
| T21 | Head-to-head: % of experiments in which A (row) has a higher net Sharpe ratio than B (column) | 3. Results: head-to-head comparison | `T21 pairwise_sharpe` | `tables/T21_pairwise_sharpe.csv` |
| T22 | Average % of head-to-head comparisons won (against the other 9 portfolios) | 3. Results: head-to-head comparison | `T22 pairwise_avg_win_rate` | `tables/T22_pairwise_avg_win_rate.csv` |
| T23 | Median paired difference in net Sharpe ratio: A (row) minus B (column) | 3. Results: head-to-head comparison | `T23 pairwise_median_sharpe_diff` | `tables/T23_pairwise_median_sharpe_diff.csv` |
| T24 | Market risk against SPY: CAPM beta, Jensen's alpha, tracking error and information ratio (medians) | 3. Results: market risk (CAPM) | `T24 capm` | `tables/T24_capm.csv` |
| T25 | Median net Sharpe ratio with different transaction costs | Robustness: transaction costs | `T25 sharpe_by_cost` | `tables/T25_sharpe_by_cost.csv` |
| T26 | Rank by median net Sharpe ratio with different transaction costs (1 = best) | Robustness: transaction costs | `T26 ranking_by_cost` | `tables/T26_ranking_by_cost.csv` |
| T27 | Semi-annual vs quarterly rebalancing (medians, net of 10 bps) | Robustness: rebalancing frequency | `T27 semiannual_vs_quarterly` | `tables/T27_semiannual_vs_quarterly.csv` |
| T28 | Markowitz risk aversion: λ = 1, 3 and 5 between Max Sharpe, GMV and EW (medians) | Robustness: Markowitz risk aversion | `T28 lambda_sensitivity` | `tables/T28_lambda_sensitivity.csv` |
| T29 | Median net Sharpe ratio by sub-period of the evaluation year | Robustness: dependence on the period | `T29 sharpe_by_subperiod` | `tables/T29_sharpe_by_subperiod.csv` |
| T30 | Median Sharpe ratio and return in the years in which SPY fell or rose | Robustness: dependence on the period | `T30 market_regime` | `tables/T30_market_regime.csv` |
| T31 | Do the results depend on the stocks drawn? Main draw, new draw and all eligible stocks | Robustness: dependence on the asset subset | `T31 subset_comparison` | `tables/T31_subset_comparison.csv` |
| T32 | The strategies applied to the group's 23 stocks (medians, net of 10 bps) | Robustness: the 23-stock universe | `T32 universe23_medians` | `tables/T32_universe23_medians.csv` |
| T33 | On the 23-stock universe: % of experiments in which each strategy beats the Group pick | Robustness: the 23-stock universe | `T33 universe23_beats_group_pick` | `tables/T33_universe23_beats_group_pick.csv` |
| T34 | Full sample 2010-2026: Group pick vs SPY vs ^GSPC (descriptive only - biased by hindsight) | Robustness / limitations: full sample | `T34 fullsample_metrics` | `tables/T34_fullsample_metrics.csv` |
| T35 | Calendar-year returns: Group pick vs SPY vs ^GSPC (2026 = year to date, until 18 September) | Robustness / limitations: full sample | `T35 calendar_year_returns` | `tables/T35_calendar_year_returns.csv` |
| T36 | Optimisation failures in all the runs of the backtest | Methods: optimisation failures | `T36 optimisation_failures` | `tables/T36_optimisation_failures.csv` |
| A01 | Descriptive statistics of all 25 series (23 stocks, SPY, ^GSPC) at three frequencies | Appendix: data | `A01 descriptive_all_assets` | `tables/A01_descriptive_all_assets.csv` |
| A02 | The 100 experiments: periods and the 12 stocks drawn (seed 2026) | Appendix: backtest design | `A02 experiment_design` | `tables/A02_experiment_design.csv` |
| A03 | Illustration: weights of each strategy with the last 12 months of data (23 stocks) | Appendix: strategies | `A03 weights_illustration` | `tables/A03_weights_illustration.csv` |
| A04 | Illustration: ex-ante characteristics of each strategy (last 12 months, 23 stocks) | Appendix: strategies | `A04 illustration_characteristic` | `tables/A04_illustration_characteristics.csv` |
| A05 | Inverse volatility vs ERC: weights and risk contributions (last 12 months, 23 stocks) | Appendix: strategies | `A05 iv_vs_erc` | `tables/A05_iv_vs_erc.csv` |
| A06 | Average weight of each stock when it is drawn, by strategy | Appendix: weights | `A06 avg_weight_by_stock` | `tables/A06_avg_weight_by_stock.csv` |
| A07 | Head-to-head: % of experiments in which A (row) has a higher return than B (column) | Appendix: head-to-head comparison | `A07 pairwise_return` | `tables/A07_pairwise_return.csv` |
| A08 | Head-to-head: % of experiments in which A (row) has a smaller maximum drawdown than B (column) | Appendix: head-to-head comparison | `A08 pairwise_max_drawdown` | `tables/A08_pairwise_max_drawdown.csv` |
| A09 | Head-to-head: % of experiments in which A (row) has a lower volatility than B (column) | Appendix: head-to-head comparison | `A09 pairwise_volatility` | `tables/A09_pairwise_volatility.csv` |
| A10 | Head-to-head: % of experiments in which A (row) has a higher Sterling ratio than B (column) | Appendix: head-to-head comparison | `A10 pairwise_sterling` | `tables/A10_pairwise_sterling.csv` |
| A11 | On the 23-stock universe: head-to-head comparison by net Sharpe ratio | Appendix: the 23-stock universe | `A11 universe23_pairwise_sharpe` | `tables/A11_universe23_pairwise_sharpe.csv` |
