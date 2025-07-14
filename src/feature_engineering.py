def create_lag_features(df, target_col, lags=[1, 2, 3, 24]):
    for lag in lags:
        df[f"{target_col}_lag_{lag}"] = df[target_col].shift(lag)
    return df


def add_time_features(df):
    df = df.copy()
    df['hour'] = df.index.hour
    df['day'] = df.index.day
    df['dayofweek'] = df.index.dayofweek
    df['month'] = df.index.month
    df['year'] = df.index.year
    df['is_weekend'] = (df['dayofweek'] >= 5).astype(int)
    return df


def add_rolling_features(df, col='t2m', windows=[3, 24]):
    for window in windows:
        df[f"{col}_rollmean_{window}"] = df[col].rolling(window=window).mean()
    return df


def prepare_features(df, lags=None):
    df = create_lag_features(df.copy(), 't2m', lags=[1, 2, 3, 24])
    df = create_lag_features(df.copy(), 'tp', lags=[1, 24])
    df = add_time_features(df)
    df = add_rolling_features(df, col='t2m', windows=[3, 24])
    if lags is None:
        lags = list(range(1, 25))  # Default: lags 1 to 24

    for lag in lags:
        df[f't2m_lag_{lag}'] = df['t2m'].shift(lag)

    return df.dropna()
