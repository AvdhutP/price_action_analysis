import yfinance as yf





# Set the ticker
ticker = "TCS"

print(ticker)

# Set the start and end date
start_date = '2021-01-01'
end_date = '2021-12-31'

# Get the data
data = yf.download(ticker, start_date, end_date)

# Print 5 rows
data.tail()


