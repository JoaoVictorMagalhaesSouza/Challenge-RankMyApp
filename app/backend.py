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
    
    def get_weekday_with_more_views(self, start_date='2019-08-01', end_date='2019-10-30'):
        aux_data = self.data.loc[:,['Date','Store Listing Visitors','Referent Week Day']]
        aux_data = aux_data[(aux_data['Date']>start_date)&(aux_data['Date']<end_date)]
        aux_data = aux_data.loc[:,['Store Listing Visitors','Referent Week Day']]
        group_by_day = aux_data.groupby('Referent Week Day').sum().sort_values(by='Store Listing Visitors',ascending=False)

        return group_by_day.head(1).index[0], group_by_day.head(1).values[0][0]
    
    def get_weekday_with_less_views(self, start_date='2019-08-01', end_date='2019-10-30'):
        aux_data = self.data.loc[:,['Date','Store Listing Visitors','Referent Week Day']]
        aux_data = aux_data[(aux_data['Date']>start_date)&(aux_data['Date']<end_date)]
        aux_data = aux_data.loc[:,['Store Listing Visitors','Referent Week Day']]
        group_by_day = aux_data.groupby('Referent Week Day').sum().sort_values(by='Store Listing Visitors',ascending=True)

        return group_by_day.head(1).index[0], group_by_day.head(1).values[0][0]
    
    def get_weekday_with_more_installers(self, start_date='2019-08-01', end_date='2019-10-30'):
        aux_data = self.data.loc[:,['Date','Installers','Referent Week Day']]
        aux_data = aux_data[(aux_data['Date']>start_date)&(aux_data['Date']<end_date)]
        aux_data = aux_data.loc[:,['Installers','Referent Week Day']]
        group_by_day = aux_data.groupby('Referent Week Day').sum().sort_values(by='Installers',ascending=False)

        return group_by_day.head(1).index[0], group_by_day.head(1).values[0][0]
    
    def get_weekday_with_less_installers(self, start_date='2019-08-01', end_date='2019-10-30'):
        aux_data = self.data.loc[:,['Date','Installers','Referent Week Day']]
        aux_data = aux_data[(aux_data['Date']>start_date)&(aux_data['Date']<end_date)]
        aux_data = aux_data.loc[:,['Installers','Referent Week Day']]
        group_by_day = aux_data.groupby('Referent Week Day').sum().sort_values(by='Installers',ascending=True)

        return group_by_day.head(1).index[0], group_by_day.head(1).values[0][0]
    