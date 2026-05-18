#By Emilio Ortiz Cervantes, contact me on LinkedIn https://www.linkedin.com/in/emilioortizcervantes/

#Educational purposes only, not financial advice

import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#User inputs

ticker = "MSFT"
revenue_growth = 0.06
terminal_growth = 0.025

#Downloading financial data

company = yf.Ticker(ticker)
income_statement = company.income_stmt
balance_sheet = company.balance_sheet
cash_flow = company.cashflow
company_info = company.info
full_company_name = company_info["longName"]

#Filtering key rows

revenue = income_statement.loc["Total Revenue"]
ebit = income_statement.loc["Operating Income"]
tax_expense = income_statement.loc["Tax Provision"]
pretax_income = income_statement.loc["Pretax Income"]

capex = cash_flow.loc["Capital Expenditure"]
free_cash_flow = cash_flow.loc["Free Cash Flow"]

depreciation_amortization = cash_flow.loc["Depreciation Amortization Depletion"]

cash = balance_sheet.loc["Cash And Cash Equivalents"]
total_debt = balance_sheet.loc["Total Debt"]

#Most recent values

latest_revenue = revenue.iloc[0]
latest_fcf = free_cash_flow.iloc[0]
latest_cash = cash.iloc[0]
latest_debt = total_debt.iloc[0]
latest_capex = capex.iloc[0]

#Average margins

ebit_margin = (ebit / revenue).mean()
tax_rate = (tax_expense / pretax_income).mean()
fcf_margin = (free_cash_flow / revenue).mean()

#Forecasting revenue for the next 5 years

projected_revenue_1 = latest_revenue * (1 + revenue_growth)
projected_revenue_2 = projected_revenue_1 * (1 + revenue_growth)
projected_revenue_3 = projected_revenue_2 * (1 + revenue_growth)
projected_revenue_4 = projected_revenue_3 * (1 + revenue_growth)
projected_revenue_5 = projected_revenue_4 * (1 + revenue_growth)

projected_fcf_1 = projected_revenue_1 * fcf_margin
projected_fcf_2 = projected_revenue_2 * fcf_margin
projected_fcf_3 = projected_revenue_3 * fcf_margin
projected_fcf_4 = projected_revenue_4 * fcf_margin
projected_fcf_5 = projected_revenue_5 * fcf_margin

years = [1, 2, 3, 4, 5]

#Market data for valuation

beta = company_info["beta"]
shares_outstanding = company_info["sharesOutstanding"]
current_price = company_info["currentPrice"]
market_cap = current_price * shares_outstanding

#Weighted Average Cost of Capital data

equity_weight = market_cap / (market_cap + latest_debt)
debt_weight = latest_debt / (market_cap + latest_debt)

#Cost of equity

risk_free_rate = 0.043
market_risk_premium = 0.055

cost_of_equity = risk_free_rate + beta * market_risk_premium

#Cost of debt Rd

interest_expense = income_statement.loc["Interest Expense"]
average_interest_expense = interest_expense.dropna().mean()
cost_of_debt = abs(average_interest_expense / latest_debt)

#WACC Calculation

wacc = (equity_weight * cost_of_equity) + (debt_weight * cost_of_debt * (1-tax_rate))

#Discount the projected DCFs

discounted_fcf_1 = projected_fcf_1 / (1 + wacc) ** 1
discounted_fcf_2 = projected_fcf_2 / (1 + wacc) ** 2
discounted_fcf_3 = projected_fcf_3 / (1 + wacc) ** 3
discounted_fcf_4 = projected_fcf_4 / (1 + wacc) ** 4
discounted_fcf_5 = projected_fcf_5 / (1 + wacc) ** 5

sum_discounted_fcfs = discounted_fcf_1 + discounted_fcf_2 + discounted_fcf_3 + discounted_fcf_4 + discounted_fcf_5

#Calculating Terminal Value

terminal_value = projected_fcf_5 * (1 + terminal_growth) / (wacc - terminal_growth)

discounted_terminal_value = terminal_value / (1 + wacc) ** 5

#Enterprise value

enterprise_value = sum_discounted_fcfs + discounted_terminal_value

#Equity value

equity_value = enterprise_value + latest_cash - latest_debt

#Implied share price and upside/downside

implied_share_price = equity_value / shares_outstanding

upside_downside = ((implied_share_price - current_price) / current_price) * 100

#Lists for charts

projected_revenues = [projected_revenue_1, projected_revenue_2, projected_revenue_3, projected_revenue_4, projected_revenue_5]

projected_fcfs = [projected_fcf_1, projected_fcf_2, projected_fcf_3, projected_fcf_4, projected_fcf_5]

#Final DCF valuation summary

print("DCF Valuation Summary")
print("----------------------------------------")
print("Company:", full_company_name)
print("Revenue Growth Assumption:", revenue_growth * 100, "%")
print("Terminal Growth Assumption:", terminal_growth * 100, "%")
print("WACC:", round(wacc * 100, 2), "%")
print()
print("Enterprise Value:", round(enterprise_value, 2))
print("Equity Value:", round(equity_value, 2))
print("Current Share Price:", round(current_price, 2))
print("Implied Share Price:", round(implied_share_price, 2))
print("Upside/Downside:", round(upside_downside, 2), "%")
print("----------------------------------------")

print("5-Year Forecast Summary")

forecast_summary = pd.DataFrame({"Year": years,"Projected Revenue": projected_revenues,"Projected FCF": projected_fcfs})
forecast_summary["Projected Revenue"] = forecast_summary["Projected Revenue"] / 1_000_000_000
forecast_summary["Projected FCF"] = forecast_summary["Projected FCF"] / 1_000_000_000

print(forecast_summary.round(2).to_string(index=False))

print("----------------------------------------")

print()

plt.plot(years, [x / 1_000_000_000 for x in projected_revenues])
plt.title("Projected Revenue")
plt.xlabel("Forecast Year")
plt.ylabel("Revenue ($B)")
plt.grid(True)
plt.show()

print()

plt.plot(years, [x / 1_000_000_000 for x in projected_fcfs])
plt.title("Projected Free Cash Flow")
plt.xlabel("Forecast Year")
plt.ylabel("Free Cash Flow ($B)")
plt.grid(True)
plt.show()

print()

plt.bar(["Current Price", "Implied Price"], [current_price, implied_share_price])

plt.title(f"{ticker}: Current Share Price vs Implied Share Price")
plt.ylabel("Share Price")
plt.grid(True)
plt.show()