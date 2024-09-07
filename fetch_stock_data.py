import pandas as pd
import yfinance as yf


def fetch_stock_data(ticker, start_date, end_date):
    """
    Fetch stock data for a given ticker and date range.

    :param ticker: Stock symbol (e.g., 'AAPL' for Apple)
    :param start_date: Start date in 'YYYY-MM-DD' format
    :param end_date: End date in 'YYYY-MM-DD' format
    :return: Pandas DataFrame with stock data
    """
    stock = yf.Ticker(ticker)
    data = stock.history(start=start_date, end=end_date)
    return data


if __name__ == "__main__":
    # Example usage
    ticker = "AAPL"
    start_date = "2023-01-01"
    end_date = "2023-12-31"

    df = fetch_stock_data(ticker, start_date, end_date)
    print(df.head())
