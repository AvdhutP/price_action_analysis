from pandas import Interval
import yfinance as yf

import download as d
import process as p

# Set the ticker
ticker = "SBIN.NS"

print(ticker)

# Set the start and end date
start_date = '2020-01-01'
end_date = '2022-02-07'
interval = '1d'
period="max"

# Get the data
data = d.download_data_yfinance(ticker, start_date, end_date,period,interval)

ma20 = p.get_ma(data['Close'],20)
ma50 = p.get_ma(data['Close'],50)
ma100 = p.get_ma(data['Close'],100)
ma200 = p.get_ma(data['Close'],200)


print(ma20.tail())
print(ma50.tail())
print(ma100.tail())
print(ma200.tail())





