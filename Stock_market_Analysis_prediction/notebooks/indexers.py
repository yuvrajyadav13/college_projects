import numpy as np
import pandas as pd
import file_import

class indexer():
        df = pd.DataFrame()
        start_date = 0
        end_date = 0

        def stock_indexers(self,indexers):
                i = 0
                final_indexers = {}
                for name,indexer in indexers.items():
                        x = np.array(indexer.loc[self.start_date:self.end_date])
                        y = np.array(df['Close'])
                        coef = np.corrcoef(x,y)
                if(coef[0][1] > 0.82):
                        final_indexers.update({name : indexer})
                add_indexers_close(final_indexers)

        def add_indexers_close(final_indexers):
        for name,indexer in final_indexers.items():
                close = 'Close_' +name
                self.df[close] = indexer.loc[self.start_date:self.end_date]

        def operate_file(self,data, start_date, end_date):
    
                self.df = data
                self.start_date = start_date
                self.end_date = end_date
                indexer_names = ['dji', 'inx']
                indexers = file_import.indexers(indexer_names)
                stock_indexers(indexers, start_date, end_date)
                return self.df
    
