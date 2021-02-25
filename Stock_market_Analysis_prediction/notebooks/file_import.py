# for importing and giving the dataframe of the file
import pandas as pd
from ast import literal_eval
import call_api

# Empty Dataframe object
data = pd.DataFrame()


# For importing file from the kaggle dataset folder
def file_importing(a):
    pref = '/home/yuvraj/PycharmProjects/SMAP/data/Stocks/'
    file_name = pref + a + ".us.txt"
    read_data(file_name, a)
    return file_name


# For reading the dataset into dataframe object
def read_data(file_name, a):
    global data
    data = pd.read_csv(file_name, index_col=0, header=0)


# For using the file_import.py
def operate_file():
    f = open('var.txt','r')
    lis = literal_eval(f.readline())
    file_name = file_importing(lis[0])
    return data, lis, file_name


def indexers(indexer_names):
    indexers = {}
    for name in indexer_names:
        file_name = file_importing(name)
        indexers.update({name : data['Close']})
    return indexers
    
def update_indexers(indexer_names):
    for name in indexer_names:
        try:
                data, file_name = file_importing(name)
                call_api.data_update(data, file_name, name)
        except:
                continue
