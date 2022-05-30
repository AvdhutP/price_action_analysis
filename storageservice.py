from asyncio.windows_events import NULL
from http import client
from numpy import sort
from pymongo import MongoClient

client = NULL

def get_database_connection():
    if client == NULL:
        client = MongoClient("localhost",27017)
    return client

def get_last_row_for_ticker_and_interval(ticker,interval):
    db_connection = get_database_connection()
    dbs = db_connection['tradedata']
    db_collecions = dbs.get_collection('ticker_interval_price')
    return db_collecions.find(
        filter={"Ticker Name":ticker,"Interval": interval} 
        ).sort([('$natural', -1)]).limit(1)

