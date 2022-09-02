import pandas as pd

class BackEndDashboard():
    def __init__(self):
        self.data = pd.read_csv('../data/final_data.csv')
    
    def get_start_and_end_dates(self):
        pass
    