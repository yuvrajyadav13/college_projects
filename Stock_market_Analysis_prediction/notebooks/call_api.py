from alpha_vantage.timeseries import TimeSeries
from datetime import date
import pandas as pd
import requests

# For getting todays date and in needed format
today = date.today()
current_date = today.strftime("%Y-%m-%d")

# API key for accessing Alpha_Vantage API and ts as TimeSeries Object
api_key = 'GEUPEEGYHGGWM8P5'
ts = TimeSeries(key=api_key, output_format='pandas')


# Function data_updates the data in txt files to current date
def data_update(data, file_name, stock_name):
    up_data, metadata = (ts.get_daily(symbol=stock_name, outputsize='full'))
    up_data.sort_index(inplace = True)
    if data.index[-1] != current_date:
        df = up_data[data.index[-1] :]
        df = df.drop(df.index[0])
        with open(file_name, 'a') as f:
            df.to_csv(f, header=0)
        return df
    else:
        return 0

def current_stats(stock_name):
    stats = str(ts.get_quote_endpoint(symbol=stock_name))
    dict_stats = to_dict(stats)
    return dict_stats


def to_dict(stats):
    stats = stats.replace('\\\nGlobal Quote', '')
    stats = stats.replace('\nGlobal Quote', '')
    stats = stats.replace('\n\n', '')
    string = ''
    lis = []
    for a in stats[:]:
        if (a == ' '):
            lis.append(string)
            string = ''

        else:
            if (a == '(' or a == ','):
                continue
            string = string + a
    while '' in lis:
        lis.remove('')
    keys = ['symbol', 'open', 'high', 'low', 'price', 'volume', 'latest trading day', 'previous close', 'change',
            'change percent']
    values = lis[-10:-1]
    values.append(lis[-1])
    return dict(zip(keys, values))


def stock_title(stock_name):
    url = 'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=' + stock_name + "&apikey=GEUPEEGYHGGWM8P5"
    resp = requests.get(url=url)
    data = resp.json()
    return data['bestMatches'][0]

