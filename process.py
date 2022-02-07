def get_ma(data=None,period=50):
       return data.rolling(period).mean()
