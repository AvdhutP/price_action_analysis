from turtle import st
import yfinance as yf

def download_data_yfinance(tickers, start=None, end=None, period="max", interval="1d"):
             data = yf.download(tickers=tickers,start=start,end=end,period=period,interval=interval)
             return data
