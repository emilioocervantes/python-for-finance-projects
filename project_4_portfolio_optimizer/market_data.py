import yfinance as yf

def download_prices(tickers, start_date):
    data = yf.download(tickers, start=start_date)
    close_prices = data["Close"]
    return close_prices