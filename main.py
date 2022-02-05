import yfinance as yf
import sys

# Set the ticker
ticker = sys.argv[0]

print(ticker)

# Set the start and end date
start_date = '2021-01-01'
end_date = '2021-12-31'

# Get the data
data = yf.download(ticker, start_date, end_date)

# Print 5 rows
data.tail()
