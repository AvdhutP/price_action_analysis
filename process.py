def get_ma(data=None,period=50):
    return data.rolling(period).mean()[-1]

def get_diff_current_price_ma(cp,ma):
    return cp-ma

