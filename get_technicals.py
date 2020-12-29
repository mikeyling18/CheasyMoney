import FundamentalAnalysis as fa
import pandas as pd
import numpy as np


def get_technicals(ticker) -> pd.DataFrame:
    weekly_stock_data = fa.stock_data(ticker, period='1y', interval='1wk')
    daily_stock_data = fa.stock_data(ticker, period='1y', interval='1d')
    daily_stock_data.index = pd.to_datetime(daily_stock_data.index)

    weekly_stock_data = weekly_stock_data[['close', 'open']]
    weekly_stock_data['next_week_gain'] = (weekly_stock_data.loc[:, 'close'].shift(-1) / weekly_stock_data.loc[:,'close']) - 1
    weekly_stock_data.dropna(inplace=True)

    wks_of_interest = weekly_stock_data[abs(weekly_stock_data['next_week_gain']) > 0.10]
    wks_of_interest.index = pd.to_datetime(wks_of_interest.index)
    wks_of_interest = wks_of_interest[wks_of_interest.index.year == 2020]
    wks_of_interest['int_idx'] = np.linspace(1, len(wks_of_interest), num=len(wks_of_interest))

    return wks_of_interest


if __name__ == '__main__':
    print(get_technicals('TSLA'))
