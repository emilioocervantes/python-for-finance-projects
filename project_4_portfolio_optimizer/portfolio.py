import numpy as np


#Portfolio Return--------------------------------------------------------------------------------------------

def calculate_portfolio_return(weights, annual_returns):
    #Calculating the portfolio's expected annual return
    portfolio_return = np.dot(weights, annual_returns)

    return portfolio_return


#Portfolio Volatility----------------------------------------------------------------------------------------

def calculate_portfolio_volatility(weights, covariance_matrix):
    #Calculating the portfolio variance using asset weights and covariances
    portfolio_variance = np.dot(
        weights.T,
        np.dot(covariance_matrix, weights)
    )

    #Converting variance into annual volatility
    portfolio_volatility = np.sqrt(portfolio_variance)

    return portfolio_volatility


#Sharpe Ratio--------------------------------------------------------------------------------------------------

def calculate_sharpe_ratio(
    portfolio_return,
    portfolio_volatility,
    risk_free_rate
):
    #Measuring excess of return earned per each unit of risk
    sharpe_ratio = (
        portfolio_return - risk_free_rate
    ) / portfolio_volatility

    return sharpe_ratio