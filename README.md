# Algorithmic Trading

A Python-based algorithmic trading project.

## Description

This project aims to develop and backtest algorithmic trading strategies using Python. The project includes functionality for fetching stock data, applying trading strategies, backtesting the performance of those strategies, and visualizing the results through various plots.

## Project Structure

```
algorithmic-trading/
├── main.py
├── .gitignore
├── README.md
└── requirements.txt
```

More files and directories will be added as the project develops.

## Getting Started

1. Clone the repository:
```bash
git clone https://github.com/yourusername/algorithmic-trading.git
cd algorithmic-trading
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate # On Windows use `.venv\Scripts\activate`
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

**Note:** The `backtesting` library is installed directly from its GitHub repository.

4. Run the backtest script:
```bash
python main.py
```

This will apply a moving average crossover strategy using Google stock data and generate several plots.

## Requirements

- Python 3.x
- Virtual environment (`venv`)
- Packages listed in `requirements.txt`

## Backtest Example

The current strategy implemented in `main.py` is a simple moving average crossover strategy. It uses two simple moving averages (10-day and 20-day) and generates buy and sell signals based on the crossover of these two moving averages.

## License

This project is licensed under the MIT License.
