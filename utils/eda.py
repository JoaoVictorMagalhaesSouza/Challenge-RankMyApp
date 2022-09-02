import logging
import pandas as pd
from copy import deepcopy

class ExploratoryDataAnalisys():
    def __init__(self, input_data: pd.DataFrame):
        self.data = deepcopy(input_data)
        self.log_step = '[EDA]'
        
    def view_inconsistencies(self):
        print(f'{self.log_step} - Checking Inconsistencies into Input Data...')
        '''
            Objective: overview of missing values from input data.
            Result: no inconsistencies found
        '''
        self.data.info()
    
    def filter_data(self):
        print(f'{self.log_step} - Filtering only records that are Organic...')
        '''
            Objective: filter data that is only from the Organic Channel
        '''
        print(f"    => {len(self.data[self.data['Acquisition Channel']=='Organic'])} of {len(self.data)} are Organic records...")
        self.data = self.data[self.data['Acquisition Channel']=='Organic']
        
    def remove_trap(self):
        print(f'{self.log_step} - Removing 31/09/2019 from the data...')
        '''
            Objective: I found day 31/09/2019 but September don't have 31 days my brother.
        '''
        
        self.data = self.data.drop(index=196)
    
    def apply_pipeline_eda(self):
        self.filter_data()
        self.view_inconsistencies()
        self.remove_trap()
        return self.data
        