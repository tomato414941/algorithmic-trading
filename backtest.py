import matplotlib.pyplot as plt
import pandas as pd

from strategies.moving_average import moving_average_strategy


def backtest_strategy(data, strategy_function):
    # Apply your strategy to the stock data
    data["signal"] = strategy_function(data)
    # Implement basic logic for profit calculation here
    data["returns"] = data["signal"].shift(1) * (data["Close"].pct_change())
    return data


if __name__ == "__main__":
    from fetch_stock_data import fetch_stock_data

    # Fetch the stock data for AAPL
    data = fetch_stock_data("AAPL", "2023-01-01", "2023-12-31")
    backtested_data = backtest_strategy(data, moving_average_strategy)

    print(backtested_data)

    # Plot 1: Closing prices and moving averages
    plt.figure(figsize=(10, 6))
    backtested_data[["Close", "short_mavg", "long_mavg"]].plot(figsize=(10, 6))
    plt.title("Close Price and Moving Averages")
    plt.show()

    # Plot 2: Trading signals on the closing price
    plt.figure(figsize=(10, 6))
    plt.plot(backtested_data.index, backtested_data["Close"], label="Close Price")
    plt.plot(
        backtested_data.index,
        backtested_data["signal"] * backtested_data["Close"],
        "o",
        label="Buy Signal",
        markersize=5,
        color="green",
    )  # Buy signals
    plt.title("Buy Signals on Close Price")
    plt.legend()
    plt.show()

    # Plot 3: Daily returns
    plt.figure(figsize=(10, 6))
    backtested_data["returns"].plot()
    plt.title("Daily Returns")
    plt.ylabel("Returns")
    plt.show()

    # Plot 4: Cumulative returns
    backtested_data["cumulative_returns"] = (1 + backtested_data["returns"]).cumprod()
    plt.figure(figsize=(10, 6))
    backtested_data["cumulative_returns"].plot()
    plt.title("Cumulative Returns")
    plt.ylabel("Cumulative Returns")
    plt.show()

    # Plot 5: Zoom in on a specific date range (June to August)
    start_date = "2023-06-01"
    end_date = "2023-08-31"
    backtested_data_range = backtested_data.loc[start_date:end_date]

    plt.figure(figsize=(10, 6))
    plt.plot(
        backtested_data_range.index, backtested_data_range["Close"], label="Close Price"
    )
    plt.plot(
        backtested_data_range.index,
        backtested_data_range["short_mavg"],
        label="Short Moving Average",
        linestyle="--",
    )
    plt.plot(
        backtested_data_range.index,
        backtested_data_range["long_mavg"],
        label="Long Moving Average",
        linestyle="--",
    )
    plt.plot(
        backtested_data_range.index,
        backtested_data_range["signal"] * backtested_data_range["Close"],
        "o",
        label="Buy Signal",
        markersize=5,
        color="green",
    )
    plt.title("Moving Averages and Buy Signals (Zoomed In)")
    plt.legend()
    plt.show()
