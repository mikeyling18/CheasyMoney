import matplotlib.pyplot as plt
import pandas as pd
import datetime as dt
import plotly.plotly as py


def create_graph(ax):
    ax.plot
    # plt.title(f'{ticker} Analysis')
    # plt.legend()
    # plt.xlabel('Date')
    # plt.ylabel('Dollars [USD]')
    # plt.show()



def get_linegraph_with_fundamentals(wks_of_interest, wkly_stock_data, fmtls_df):
    qtr_dates = [pd.to_datetime('2020-01-01'),
                 pd.to_datetime('2020-03-31'),
                 pd.to_datetime('2020-06-30'),
                 pd.to_datetime('2020-09-30')]

    ylim_max = max(wks_of_interest['close']) * 1.75
    fig, ax1 = plt.subplots(figsize=(20, 10), sharex='True')

    ax1.set_ylim(0, ylim_max)

    # Graph 1
    ax1.plot(wkly_stock_data['close'], label=f'Weekly Close Price')
    ax1.scatter(wks_of_interest.index, wks_of_interest['close'][wks_of_interest.index], color='r')
    for i, y in enumerate(wks_of_interest.index):
        ax1.annotate(f'{i + 1}\n', (y, wks_of_interest['close'][y]), fontsize=15)
    # insert fundamentals
    for date in qtr_dates[1:]:
        ax1.axvline(date)
    qtr_count = 0
    for idx, row in fmtls_df[fmtls_df.index.year >= 2020].iterrows():
        qrty_funda_str = f'===Q{qtr_count} FUNDAMENTALS===\n\n' + '\n'.join(
            f'{colname}:{row[colname]:.5f}' for colname in row.index)
        ax1.annotate(qrty_funda_str,
                     xy=(qtr_dates[qtr_count] + dt.timedelta(days=20), 0.7 * ylim_max),
                     xycoords='data')
        qtr_count += 1
    return ax1
