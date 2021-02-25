import pandas as pd
import numpy as np
from sklearn import neighbors
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import MinMaxScaler


def simple(data):
        start = float(data[: 1]['Close'] / data[ : 1]['Predictions'])
        end = float(data[-1:]['Close'] / data[-1 :]['Predictions'])
        pred = np.array(data.loc[:,'Predictions'])
        close = np.array(data.loc[:,'Close'])
        print(start,end)
        rms = 10000
        if(start < end):
                temp_pred = pred
                for i in np.arange(start = start ,stop = end, step = 0.01):
                        print(i)
                        temp_pred = pred * i
                        temp_rms = np.sqrt(np.mean(np.power((close-temp_pred),2)))
                        if(temp_rms < rms):
                                rms = temp_rms
                        else:
                                break
                pred = temp_pred
        else:
                temp_pred = pred
                for i in np.arange(start = end ,stop = start , step = 0.01):
                        temp_pred = pred * i
                        temp_rms = np.sqrt(np.mean(np.power((close-temp_pred),2)))
                        if(temp_rms < rms):
                                rms = temp_rms
                        else:
                                break
                pred = temp_pred
        data['New Predictions'] = pred
        return data
        
def full_pred(df,start_date, end_date):
        train = df[ : start_date]
        valid = df[start_date:end_date]
        x_train = train.drop('Close', axis=1)
        y_train = train['Close']
        x_valid = valid.drop('Close', axis=1)
        y_valid = valid['Close']
        scaler = MinMaxScaler(feature_range=(0, 1))
        #scaling data
        x_train_scaled = scaler.fit_transform(x_train)
        x_train = pd.DataFrame(x_train_scaled)
        x_valid_scaled = scaler.fit_transform(x_valid)
        x_valid = pd.DataFrame(x_valid_scaled)

        #using gridsearch to find the best parameter
        params = {'n_neighbors':[2,3,4,5,6,7,8,9]}
        knn = neighbors.KNeighborsRegressor()
        model = GridSearchCV(knn, params, cv=5)

        #fit the model and make predictions
        model.fit(x_train,y_train)
        preds = model.predict(x_valid)
        if('Prediction' in valid.columns):
                valid.drop('Prediction', axis = 1)
    
        #ploting using matplotlib
        valid['Predictions'] = preds
        return valid
        
def additive(data,start_date = 0, end_date = 0):
        data.index = pd.to_datetime(data.index)
        #data = full_pred(new_data, start_date, end_date)
        data['Scaler'] = data['Close'] - data['Predictions']
        li = data.shape
        train = data[ : int(li[0]*0.8)]
        valid = data[int(li[0]*0.8): ]
        x_train = train.drop('Scaler', axis=1)
        y_train = train['Scaler']
        x_valid = valid.drop('Scaler', axis=1)
        y_valid = valid['Scaler']
        
        scaler = MinMaxScaler(feature_range=(0, 1))
        #scaling data
        x_train_scaled = scaler.fit_transform(x_train)
        x_train = pd.DataFrame(x_train_scaled)
        x_valid_scaled = scaler.fit_transform(x_valid)
        x_valid = pd.DataFrame(x_valid_scaled)

        #using gridsearch to find the best parameter
        params = {'n_neighbors':[2,3,4,5,6,7,8,9]}
        knn = neighbors.KNeighborsRegressor()
        model = GridSearchCV(knn, params, cv=5)

        #fit the model and make predictions
        model.fit(x_train,y_train)
        pred_scaler = model.predict(x_valid)
        valid.drop('Scaler', axis = 1, inplace = True)
        valid['Scaler'] = pred_scaler
        data =  pd.concat([train,valid], sort = True)
        data['New Prediction'] = data['Predictions'] + data['Scaler']
        return data
