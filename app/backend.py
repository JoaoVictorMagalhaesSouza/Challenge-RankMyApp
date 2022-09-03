import pandas as pd

class BackEndDashboard():
    def __init__(self):
        self.data = pd.read_csv('../data/final_data.csv')
    
    def get_app_views(self, start_date='2019-08-01', end_date='2019-10-30'):
        aux_data = self.data.loc[:,['Date','Store Listing Visitors']]
        aux_data = aux_data[(aux_data['Date']>start_date)&(aux_data['Date']<end_date)]
        total_views = aux_data['Store Listing Visitors'].sum()
        
        return total_views
    
    def get_app_installations(self, start_date='2019-08-01', end_date='2019-10-30'):
        aux_data = self.data.loc[:,['Date','Installers']]
        aux_data = aux_data[(aux_data['Date']>start_date)&(aux_data['Date']<end_date)]
        total_installers = aux_data['Installers'].sum()
        
        return total_installers    
    
    def get_average_installer_visitor_rate(self, start_date='2019-08-01', end_date='2019-10-30'):
        aux_data = self.data.loc[:,['Date','Visitor-to-Installer conversion rate']]
        aux_data = aux_data[(aux_data['Date']>start_date)&(aux_data['Date']<end_date)]
        average_installers = aux_data['Visitor-to-Installer conversion rate'].mean()
        
        return average_installers 