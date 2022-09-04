from operator import le
import pandas as pd
from forex_python.converter import CurrencyRates
import datetime

from copy import deepcopy

class DataInputation():
    def __init__(self, filtered_data: pd.DataFrame):
        self.data = deepcopy(filtered_data)
    
    def insert_week_nominal_day(self):
        '''
            Objective: say which day of the week each of the records is
        '''
        label_base = ['Quarta-Feira','Quinta-Feira','Sexta-Feira','Sábado','Domingo','Segunda-Feira','Terça-Feira']
        #Repeating those days to insert into input data...
        i = 0
        while(len(label_base)!=len(self.data)):
            if (i==7):
                i=0
            label_base.append(label_base[i])
            i += 1
        
        self.data['Referent Week Day'] = label_base
        
        
    def insert_dolar_price(self):
        '''
            Objective: check if have a correlation between dolar price and number of instalations. 
        '''
        days = self.data['Date'].values
        c = CurrencyRates()
        dolar_prices = []
        for day in days:
            dolar_prices.append(c.get_rate('USD', 'BRL',day))
        self.data['Dolar Price'] = dolar_prices
    
    def apply_pipeline_data_inputation(self):
        self.insert_week_nominal_day()
        #self.insert_dolar_price()
        return self.data
