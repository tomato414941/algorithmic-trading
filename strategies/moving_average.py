import numpy as np


def moving_average_strategy(data, short_window=40, long_window=100):
    data["short_mavg"] = (
        data["Close"].rolling(window=short_window, min_periods=1).mean()
    )
    data["long_mavg"] = data["Close"].rolling(window=long_window, min_periods=1).mean()
    data["signal"] = 0.0

    # Use .loc[] to avoid chained assignment issues
    data.loc[data.index[short_window:], "signal"] = np.where(
        data.loc[data.index[short_window:], "short_mavg"]
        > data.loc[data.index[short_window:], "long_mavg"],
        1.0,
        0.0,
    )

    return data["signal"]
