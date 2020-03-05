from pandas_datareader import data as pdr

import yfinance as yf
yf.pdr_override() # <== that's all it takes :-)

# download dataframe
data = pdr.get_data_yahoo("AMZN GOOGL MSFT", start="2020-02-01", end="2020-03-01")
print(data)
data.to_csv('./test2.csv')