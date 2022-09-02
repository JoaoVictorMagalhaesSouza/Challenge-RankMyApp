from operator import le
import pandas as pd
from copy import deepcopy

class DataInputation():
    def __init__(self, filtered_data: pd.DataFrame):
        self.data = deepcopy(filtered_data)
    
    def insert_week_nominal_day(self):
        '''
            Objective: say which day of the week each of the records is
        '''
        label_base = ['Quinta-Feira','Sexta-Feira','Sábado','Domingo','Segunda-Feira','Terça-Feira','Quarta-Feira']
        #Repeating those days to insert into input data...
        i = 0
        while(len(label_base)!=len(self.data)):
            if (i==7):
                i=0
            label_base.append(label_base[i])
            i += 1
        
        self.data['week_day'] = label_base
        return self.data
        