from pykrx import stock
import numpy as np
import pandas as pd
import time

def get_52price(ticker, start_date, end_date):
    # 52주 가격 정보 얻음.
    df = stock.get_market_ohlcv(start_date, end_date, ticker, adjusted = True)
    df.reset_index(inplace=True)
    df['날짜'] = pd.to_datetime(df['날짜'])
    weeks_52 = 52*5
    df['52_week_high'] = df['고가'].rolling(window=weeks_52, min_periods=1).max()
    df['52_week_low'] = df['저가'].rolling(window=weeks_52, min_periods=1).min()
    
    return df


def get_rapid_ticker(start_date, end_date, number=10):
    kosdaq = stock.get_market_price_change(start_date, end_date, market="KOSDAQ")
    if kosdaq.empty:
        time.sleep(2)
        return pd.DataFrame()
    else:
        profit = kosdaq['등락률'].values
        top_profit_index = np.argsort(profit)[(-1)*number:]
        time.sleep(2)
        
        return kosdaq.iloc[top_profit_index] 