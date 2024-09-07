# Algorithmic Trading

A Python-based algorithmic trading project.

## Description

This project aims to develop and backtest algorithmic trading strategies using Python. The project includes functionality for fetching stock data, applying trading strategies, backtesting the performance of those strategies, and visualizing the results through various plots.

## Project Structure

```
algorithmic-trading/
├── fetch_stock_data.py
├── strategies/
│ └── moving_average.py
├── backtest.py
├── .gitignore
├── README.md
└── requirements.txt
```

More files and directories will be added as the project develops.

## Getting Started

1. Clone the repository:
```
git clone https://github.com/yourusername/algorithmic-trading.git
cd algorithmic-trading
```

2. Create and activate a virtual environment:
```
python -m venv .venv
source .venv/bin/activate # On Windows use `.venv\Scripts\activate`
```

3. Install the required packages:
```
pip install -r requirements.txt
```

4. Run the stock data fetching script:
```
python fetch_stock_data.py
```

This will fetch recent stock data for Apple Inc. (AAPL) and display the first few rows.

5. Backtest a trading strategy:
```bash
python backtest.py
```

This will apply the moving average strategy on the stock data and generate several plots:
- Close price and moving averages.
- Buy signals on the close price.
- Daily returns.
- Cumulative returns.
- A zoomed-in view of buy signals for a specific date range.

## License

This project is licensed under the MIT License.
