#By Emilio Ortiz Cervantes, feel free to connect with me on LinkedIn : https://www.linkedin.com/in/emilioortizcervantes/

#Which company has actually had a better run? This dashboard compares stock performance so the data can talk.

import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from numpy import info

ticker1 = "AMD"
ticker2 = "MSFT"
ticker3 = "AAPL"

info1 = yf.Ticker(ticker1).info
info2 = yf.Ticker(ticker2).info
info3 = yf.Ticker(ticker3).info

companyN1 = (info1["longName"])
companyN2 = (info2["longName"])
companyN3 = (info3["longName"])

label1 = (companyN1)
label2 = (companyN2)
label3 = (companyN3)

stock1 = yf.download(ticker1, start="2021-01-01", end="2026-01-01")
stock2 = yf.download(ticker2, start="2021-01-01", end="2026-01-01")
stock3 = yf.download(ticker3, start="2021-01-01", end="2026-01-01")

plt.title("Comparison of stock prices")
plt.xlabel("Date")
plt.ylabel("Opening price")

desired_data = "Low"
#Options: Open, High, Low, Close, Volume

plt.plot(stock1[desired_data], label=(label1))
plt.plot(stock2[desired_data], label=(label2))
plt.plot(stock3[desired_data], label=(label3))
plt.legend()
