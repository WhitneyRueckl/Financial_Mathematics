# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 21:49:08 2022

@author: whitn
"""


import pandas as pd
import numpy as np
import os

from yahoo_fin import stock_info as si
from yahoo_fin import options as op
	
#import yahoo_fin.stock_info as si

os.chdir('C:/Users/whitn/OneDrive/Documents/Data Science Projects')
print(os.getcwd())

ticker = 'NVDA'
start_dt = '2010-06-30'
end_dt = '2020-06-30'


	
stock = si.get_data(ticker, start_date = start_dt, end_date = end_dt)  # returns a dataframe


expiration_dates = op.get_expiration_dates(ticker)

# Get call data for the first available option date:
call_data = op.get_calls(ticker, expiration_dates[0])
print(type(call_data))
call_data.columns

option_chain_data = op.get_options_chain(ticker = ticker, date = expiration_dates[0])
option_chain_data.keys()
