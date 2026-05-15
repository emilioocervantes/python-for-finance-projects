#By Emilio Ortiz Cervantes, feel free to connect with me on LinkedIn : https://www.linkedin.com/in/emilioortizcervantes/

# What if you had invested in a certain company many years ago? This project calculates how much that investment would be worth today so you can regret it.

import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

ticker = "NVDA"
investment_amount = 1000000
formatted_investmentamount = f"{investment_amount:,}"
start_date = "1999-01-02"
end_date = "2026-05-15"
#Please follow Year-Month-Day format

stock = yf.download(ticker, start=start_date, end=end_date, auto_adjust=True, multi_level_index=False)

ticker_info = yf.Ticker(ticker)
company_name = ticker_info.info['longName']

prices = pd.DataFrame()
prices[ticker] = stock["Close"]

start_price = prices[ticker].iloc[0]
end_price = prices[ticker].iloc[-1]

shares_bought = investment_amount / start_price

final_value = shares_bought * end_price

profit = final_value - investment_amount

total_return = profit / investment_amount

total_return_percentage = total_return * 100

prices["Investment value"] = prices[ticker] * shares_bought

print(f"Stock's first Price, in {start_date} was {round(start_price,2)} USD")
print(f"Stock's latest price, in {end_date} was {round(end_price, 2)} USD")
print(f"You bought {round(shares_bought, 2)} shares in {start_date}")
print(f"The final value was {final_value:,.2f} USD")
print(f"The profit was {profit:,.2f} USD")
print(f"Getting an ROI of {total_return_percentage:,.2f} %")

plt.figure(figsize=(10, 5))

plt.plot(prices["Investment value"], label=f"{company_name} Investment Value", color='green')

plt.title(f"Growth of ${formatted_investmentamount} Invested in {company_name}")
plt.xlabel("Date")
plt.ylabel("Investment Value in USD")

plt.legend()
plt.show()