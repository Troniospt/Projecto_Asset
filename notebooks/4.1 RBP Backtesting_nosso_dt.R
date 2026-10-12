# -------------------------------------------------------------------------------------------
# Backtesting Risk-Based Portfolios (RBP)
# -------------------------------------------------------------------------------------------

rm(list=ls(all.names = TRUE))
graphics.off()
close.screen(all.screens = TRUE)
erase.screen()
windows.options(record=TRUE)
options(scipen=999)

setwd('C:/Users/anton/Desktop/Pós-Grad/Asset Pricing and Portfolio Management')

library(pacman)
if (!require("pacman")) {install.packages("pacman")}

p_load(xts)                   # to manipulate time series of stock data
p_load(portfolioBacktest)     # portfolio Backtesting
p_load(riskParityPortfolio)   # RPP
p_load(PerformanceAnalytics)  # to compute performance measures
p_load(CVXR)                  # Convex Optimization in R
p_load(DT)                    # R interface to the JavaScript library DataTable
p_load(ggplot2)               # plot

# -------------------------------------------------------------------------------------------
# Loading Data
# -------------------------------------------------------------------------------------------
library(xts)
library(portfolioBacktest)
raw_csv <- read.csv("precos_limpos.csv", row.names = 1, check.names = FALSE)

acoes <- c("NVDA", "AAPL", "MSFT", "AVGO", "AMD", "MU", "BRK-B", "JPM", "V", 
           "LLY", "JNJ", "AMZN", "TSLA", "T", "GOOGL", "GE", "CAT", "WMT", 
           "COST", "XOM", "NEE", "WELL", "LIN")

todas_colunas <- c(acoes, "SPY")
df_subset <- raw_csv[, todas_colunas]
df_clean <- na.omit(df_subset)

prices_xts <- as.xts(df_clean, order.by = as.Date(rownames(df_clean)))

# Extrair SPY mantendo formato de matriz xts e renomear a coluna para "index"
index_xts <- prices_xts[, "SPY", drop = FALSE]
colnames(index_xts) <- "index"

# Estrutura correta para o portfolioBacktest
faang_data <- list(
  adjusted = prices_xts[, acoes],
  index    = index_xts
)
# -------------------------------------------------------------------------------------------
# Portfolio definitions
# -------------------------------------------------------------------------------------------
# --- 2.1 Quintile Portfolio ---
Quintile_fun <- function(dataset, ...) {
  X <- diff(log(dataset$adjusted))[-1]
  N <- ncol(X)
  ranking <- sort(colMeans(X), decreasing = TRUE, index.return = TRUE)$ix
  w <- rep(0, N)
  w[ranking[1:round(N/5)]] <- 1/round(N/5)
  names(w) <- colnames(X)
  return(w)
}

# --- 2.2 Global Minimum-Variance Portfolio (GMVP) ---
GMVP_fun <- function(dataset, ...) {
  X <- diff(log(dataset$adjusted))[-1]
  Sigma <- cov(X)
  w_ <- Variable(nrow(Sigma))
  prob <- Problem(Minimize(quad_form(w_, Sigma)),
                  constraints = list(w_ >= 0, sum(w_) == 1))
  result <- solve(prob)
  w <- as.vector(result$getValue(w_))
  names(w) <- colnames(Sigma)
  return(w)
}

# --- 2.3 Markowitz Mean-Variance Portfolio ---
Markowitz_fun <- function(dataset, lambda = 0.5, ...) {
  X <- diff(log(dataset$adjusted))[-1]
  mu <- colMeans(X)
  Sigma <- cov(X)
  w_ <- Variable(nrow(Sigma))
  prob <- Problem(Maximize(t(mu) %*% w_ - lambda * quad_form(w_, Sigma)),
                  constraints = list(w_ >= 0, sum(w_) == 1))
  result <- solve(prob)
  w <- as.vector(result$getValue(w_))
  names(w) <- colnames(Sigma)
  return(w)
}

# --- 2.4 Maximum Sharpe Ratio Portfolio (MSRP) ---
MaxSharpe_fun <- function(dataset, ...) {
  X <- diff(log(dataset$adjusted))[-1]
  mu <- colMeans(X)
  Sigma <- cov(X)
  
  # Apenas resolve se a média de retornos for positiva
  if (all(mu <= 0)) mu <- rep(1, length(mu))
  
  w_ <- Variable(nrow(Sigma))
  prob <- Problem(Minimize(quad_form(w_, Sigma)),
                  constraints = list(w_ >= 0, t(mu) %*% w_ == 1))
  result <- solve(prob)
  w <- as.vector(result$getValue(w_)/sum(result$getValue(w_)))
  names(w) <- colnames(Sigma)
  return(w)
}
# Inverse volatility portfolio (IVP)

IVP_fun <- function(dataset, ...) {
  X <- diff(log(dataset$adjusted))[-1]  # compute log returns
  Sigma <- cov(X)  # compute SCM
  # design IVP
  w <- riskParityPortfolio(Sigma, formulation='diag')$w
  return(w)
}

# Risk Parity Portfolio (RPP)

RPP_fun <- function(dataset, ...) {
  X <- diff(log(dataset$adjusted))[-1]  # compute log returns
  Sigma <- cov(X) 
  # design RPP
  w <- riskParityPortfolio(Sigma)$w
  return(w)
}

# Most diversified portfolio (MDP)

MSRP_fun <- function(mu, Sigma) {
  w_ <- Variable(nrow(Sigma))
  prob <- Problem(Minimize(quad_form(w_, Sigma)),
                  constraints = list(w_ >= 0, t(mu) %*% w_ == 1))
  result <- CVXR::solve(prob)
  w <- as.vector(result$getValue(w_)/sum(result$getValue(w_)))
  names(w) <- colnames(Sigma)
  return(w)
}

MDP_fun <- function(dataset, ...) {
  X <- diff(log(dataset$adjusted))[-1]  # compute log returns
  Sigma <- cov(X)    
  mu = sqrt(diag(Sigma))
  w <- MSRP(mu = sqrt(diag(Sigma)), Sigma)
  return(w)
}
# --- 2.8 Maximum Decorrelation Portfolio (MaxDec) ---
MaxDec_fun <- function(dataset, ...) {
  X <- diff(log(dataset$adjusted))[-1]
  R <- cor(X) # Usa a matriz de correlação em vez da covariância
  mu <- rep(1, nrow(R))
  
  w_ <- Variable(nrow(R))
  prob <- Problem(Minimize(quad_form(w_, R)),
                  constraints = list(w_ >= 0, t(mu) %*% w_ == 1))
  result <- solve(prob)
  w <- as.vector(result$getValue(w_)/sum(result$getValue(w_)))
  names(w) <- colnames(R)
  return(w)
}

# -------------------------------------------------------------------------------------------
# Backtesting and Plotting
# -------------------------------------------------------------------------------------------

portfolios <- list(
  "Quintile"   = Quintile_fun,
  "GMVP"       = GMVP_fun,
  "Markowitz"  = Markowitz_fun,
  "MaxSharpe"  = MaxSharpe_fun,
  "IVP"        = IVP_fun,
  "RPP"        = RPP_fun,
  "MDP"        = MDP_fun,
  "MaxDec"     = MaxDec_fun
)

bt <- portfolioBacktest(
  portfolios,                      # 1st positional argument: Portfolio list
  list(faang_data),                # 2nd positional argument: Dataset list
  benchmarks      = c("1/N", "index"),
  rebalance_every = 21 * 3,        # Quarterly rebalancing
  optimize_every  = 21 * 3,
  lookback        = 252,           # 1-year lookback window
  shortselling    = FALSE,
  cost            = list(buy = 0e-4, sell = 0e-4, short = 0e-4, long_leverage = 0e-4),
  show_progress_bar = TRUE
)
names(bt)

# Tabela resumo de performance (Ordenada por Sharpe Ratio)
res_sum <- backtestSummary(bt, summary_fun = median)
summaryTable(res_sum, type = "DT", order_col = "Sharpe ratio", order_dir = "desc")

# Gráficos comparativos
summaryBarPlot(res_sum, measures = c("Sharpe ratio", "max drawdown"))

# Gráfico de Drawdowns de todas as carteiras e benchmarks
backtestChartDrawdown(bt, c("GMVP", "Markowitz", "RPP", "MDP", "1/N", "index"), type = "ggplot2")






# plot assets exposures over time
#backtestChartStackedBar(bt, portfolio = "IVP", legend = TRUE) +
 # scale_y_continuous(labels = scales::percent)


# Select several performance measures of one specific portfolio:

# Print selected performance criteria (sharpe ratio, max drawdown,...) of each portfolio
#backtestSelector(bt, portfolio_name = "RPP", 
 #                measures = c("Sharpe ratio", "max drawdown"))

#backtestSelector(bt, portfolio_name = "MDP", 
 #                measures = c("Sharpe ratio", "max drawdown"))




# Tables of several performance measures of the portfolios (classified by performance criteria):

# Portfolio's performance in tables 
ppt <- backtestTable(bt, measures = c("Sharpe ratio", "max drawdown"))
ppt

# Summary of performance measures:
res_sum <- backtestSummary(bt, summary_fun = median)
names(res_sum)

res_sum$performance_summary

apply(ppt$`Sharpe ratio`, 2, median)


# -------------------------------------------------------------------------------------------
# Visualizing Results
# -------------------------------------------------------------------------------------------

# Performance table:
summaryTable(res_sum, type = "DT", 
             order_col = "Sharpe ratio",   # performance measure to be used to sort the rows
             order_dir = "desc")


# Barplot (summaryTable() information in a visual way):
summaryBarPlot(res_sum, measures = c("Sharpe ratio", "max drawdown"))


backtestChartDrawdown(bt, c("IVP", "RPP", "MDP","1/N", "index"), 
                      type = c("ggplot2"))





