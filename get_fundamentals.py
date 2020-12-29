import FundamentalAnalysis as fa
import pandas as pd

FA_API_KEY = '0531b0516802b6f762a2fe685575e4f0'


def get_fundamentals(ticker) -> pd.DataFrame:
    # balance_sheet_quarterly = fa.balance_sheet_statement(ticker, FA_API_KEY, period="quarterly")
    # cash_flow_statement_quarterly = fa.cash_flow_statement(ticker, FA_API_KEY, period="quarter")
    # key_metrics = fa.key_metrics(ticker, FA_API_KEY, period="quarter")

    financial_ratios_quarterly = fa.financial_ratios(ticker, FA_API_KEY, period="quarter")
    financial_statement_growth = fa.financial_statement_growth(ticker, FA_API_KEY, period="quarter")

    roe = financial_ratios_quarterly.loc['returnOnEquity']
    gross_profit_margin = financial_ratios_quarterly.loc['grossProfitMargin']
    operating_profit_margin = financial_ratios_quarterly.loc['operatingProfitMargin']
    pretaxProfitMargin = financial_ratios_quarterly.loc['pretaxProfitMargin']
    netProfitMargin = financial_ratios_quarterly.loc['netProfitMargin']

    revenue_growth = financial_statement_growth.loc['revenueGrowth']
    gross_profit_growth = financial_statement_growth.loc['grossProfitGrowth']
    ebit_growth = financial_statement_growth.loc['ebitgrowth']

    fundamentals_df = pd.DataFrame({'roe': roe,
                                    'grossProfitMargin': gross_profit_margin,
                                    'operatingProfitMargin': operating_profit_margin,
                                    'pretaxProfitMargin': pretaxProfitMargin,
                                    'netProfitMargin': netProfitMargin,
                                    'revenueGrowth': revenue_growth,
                                    'ebitGrowth': ebit_growth,
                                    'grossProfitGrowth': gross_profit_growth})

    fundamentals_df.index = pd.to_datetime(pd.Series(fundamentals_df.index))
    fundamentals_df = fundamentals_df[fundamentals_df.index.year >= 2020]
    fundamentals_df = fundamentals_df.sort_index()

    return fundamentals_df


if __name__ == '__main__':
    print(get_fundamentals('TSLA'))
