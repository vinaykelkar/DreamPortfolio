import requests
import yfinance as yf
import pandas as pd
import numpy as np
from nselib import capital_market

data = capital_market.equity_list()
print(data)

# symbol='SBIN.NS'
# stock = yf.Ticker(symbol)
# info = stock.info

high_low_52w = capital_market.week_52_high_low_report(trade_date='11-12-2024',symbol='SBIN')
print(high_low_52w)