import matplotlib.pyplot as plt
import pandas as pd
import datetime as dt
import numpy as np
import time
from nltk.sentiment.vader import SentimentIntensityAnalyzer

from get_fundamentals import get_fundamentals
from get_technicals import get_technicals

TICKER = 'TSLA'
subreddits = ['teslainvestorsclub']


def main():
    fundamentals = get_fundamentals(TICKER)
    technicals = get_technicals(TICKER)
    


if '__name__' == '__main__':
    main()