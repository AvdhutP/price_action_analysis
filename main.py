import yfinance as yf
import download as d
import process as p
import notify as n
import seggragate as s
import storageservice 

# Set the ticker
ticker = "INFY.NS"

print(ticker)

# Set the start and end date
moving_averages_tf = [20,50,100,200]
moving_averages = []
start_date = '2020-01-01'
end_date = '2022-02-10'
interval = '1d'
period = "max"
min_diff_to_get_notified = 10

# Get the data
data = d.download_data_yfinance(ticker, start_date, end_date,period,interval)

current_price =  data['Close'].iloc[-1]
ma20 = p.get_ma(data['Close'],20)
ma50 = p.get_ma(data['Close'],50)
ma100 = p.get_ma(data['Close'],100)
ma200 = p.get_ma(data['Close'],200)

for ma in moving_averages_tf:
    moving_averages.append(p.get_ma(data['Close'],ma))

ma_dict = dict(zip(moving_averages_tf,moving_averages))

for k,v in ma_dict.items():
    price_diff = p.get_diff_current_price_ma(current_price,v)
    if(min_diff_to_get_notified <= price_diff >= 0):
        n.send_notification(k)

s.get_avg_volumn(data=data['Volume'])     

mongo_connection = storageservice.get_database_connection()

dbs = mongo_connection['tradedata']

db_collecions = dbs.get_collection('ticker_interval_price')
data.insert(0,"Ticker Name", [ticker]*data['Close'].count())
data.insert(1,"Interval", [interval]*data['Close'].count())
data.reset_index(inplace=True)
data_dict = data.to_dict("records")

db_collecions.insert_many(data_dict)

db_collecions.find_one()

last_row = storageservice.get_last_row_for_ticker_and_interval(ticker,interval)

print(last_row)









