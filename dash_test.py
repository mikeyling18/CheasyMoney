import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from plotly import graph_objs as go
from datetime import datetime as dt
import json
import pandas as pd


def make_dash_table(df):
    ''' Return a dash definitio of an HTML table for a Pandas dataframe '''
    table = []
    for index, row in df.iterrows():
        html_row = []
        for i in range(len(row)):
            html_row.append( html.Td([ row[i] ]) )
        table.append( html.Tr( html_row ) )
    return table


def main():
    df_perf_summary = pd.read_csv('https://plot.ly/~jackp/17530.csv')
    df_fund_data = pd.read_csv('https://plot.ly/~jackp/17534.csv')

    modifed_perf_table = make_dash_table(df_perf_summary)

    app = dash.Dash('Test Report')
    app.layout = html.Div([
        html.Div([
            html.Div([
                html.H6('Fund Data', className = "gs-header gs-text-header padded"),
            ], className = "four columns" ),

            html.Div([
                html.H6("Performance Summary (%)", className = "gs-header gs-table-header padded"),
                html.Table( modifed_perf_table, className = "reversed" ),
            ], className = "eight columns" ),
        ], className = "row ")
    ])
    app.run_server(debug=True)


if __name__ == '__main__':
    main()