import pandas as pd
import datetime
from datetime import timedelta

class BackEndDashboard():
    def __init__(self):
        self.data = pd.read_csv('final_data.csv')
    #Periodic analisys
    def get_app_views(self, start_date='2019-08-01', end_date='2019-10-30'):
        end_date = datetime.datetime.strptime(end_date[0:10],'%Y-%m-%d')+timedelta(days=1)
        end_date = end_date.strftime('%Y-%m-%d')
        aux_data = self.data.loc[:,['Date','Store Listing Visitors']]
        aux_data = aux_data[(aux_data['Date']>=start_date)&(aux_data['Date']<=end_date)]
        total_views = aux_data['Store Listing Visitors'].sum()
        
        return total_views
    
    def get_app_installations(self, start_date='2019-08-01', end_date='2019-10-30'):
        end_date = datetime.datetime.strptime(end_date[0:10],'%Y-%m-%d')+timedelta(days=1)
        end_date = end_date.strftime('%Y-%m-%d')
        aux_data = self.data.loc[:,['Date','Installers']]
        aux_data = aux_data[(aux_data['Date']>=start_date)&(aux_data['Date']<=end_date)]
        total_installers = aux_data['Installers'].sum()
        
        return total_installers    
    
    def get_average_installer_visitor_rate(self, start_date='2019-08-01', end_date='2019-10-30'):
        end_date = datetime.datetime.strptime(end_date[0:10],'%Y-%m-%d')+timedelta(days=1)
        end_date = end_date.strftime('%Y-%m-%d')
        aux_data = self.data.loc[:,['Date','Visitor-to-Installer conversion rate']]
        aux_data = aux_data[(aux_data['Date']>=start_date)&(aux_data['Date']<=end_date)]
        average_installers = aux_data['Visitor-to-Installer conversion rate'].mean()
        
        return average_installers
    
    def get_weekday_with_more_views(self, start_date='2019-08-01', end_date='2019-10-30'):
        end_date = datetime.datetime.strptime(end_date[0:10],'%Y-%m-%d')+timedelta(days=1)
        end_date = end_date.strftime('%Y-%m-%d')
        aux_data = self.data.loc[:,['Date','Store Listing Visitors','Referent Week Day']]
        aux_data = aux_data[(aux_data['Date']>=start_date)&(aux_data['Date']<=end_date)]
        aux_data = aux_data.loc[:,['Store Listing Visitors','Referent Week Day']]
        group_by_day = aux_data.groupby('Referent Week Day').sum().sort_values(by='Store Listing Visitors',ascending=False)

        return group_by_day.head(1).index[0], group_by_day.head(1).values[0][0]
    
    def get_weekday_with_less_views(self, start_date='2019-08-01', end_date='2019-10-30'):
        end_date = datetime.datetime.strptime(end_date[0:10],'%Y-%m-%d')+timedelta(days=1)
        end_date = end_date.strftime('%Y-%m-%d')
        aux_data = self.data.loc[:,['Date','Store Listing Visitors','Referent Week Day']]
        aux_data = aux_data[(aux_data['Date']>=start_date)&(aux_data['Date']<=end_date)]
        aux_data = aux_data.loc[:,['Store Listing Visitors','Referent Week Day']]
        group_by_day = aux_data.groupby('Referent Week Day').sum().sort_values(by='Store Listing Visitors',ascending=True)

        return group_by_day.head(1).index[0], group_by_day.head(1).values[0][0]
    
    def get_weekday_with_more_installers(self, start_date='2019-08-01', end_date='2019-10-30'):
        end_date = datetime.datetime.strptime(end_date[0:10],'%Y-%m-%d')+timedelta(days=1)
        end_date = end_date.strftime('%Y-%m-%d')
        aux_data = self.data.loc[:,['Date','Installers','Referent Week Day']]
        aux_data = aux_data[(aux_data['Date']>=start_date)&(aux_data['Date']<=end_date)]
        aux_data = aux_data.loc[:,['Installers','Referent Week Day']]
        group_by_day = aux_data.groupby('Referent Week Day').sum().sort_values(by='Installers',ascending=False)

        return group_by_day.head(1).index[0], group_by_day.head(1).values[0][0]
    
    def get_weekday_with_less_installers(self, start_date='2019-08-01', end_date='2019-10-30'):
        end_date = datetime.datetime.strptime(end_date[0:10],'%Y-%m-%d')+timedelta(days=1)
        end_date = end_date.strftime('%Y-%m-%d')
        aux_data = self.data.loc[:,['Date','Installers','Referent Week Day']]
        aux_data = aux_data[(aux_data['Date']>=start_date)&(aux_data['Date']<=end_date)]
        aux_data = aux_data.loc[:,['Installers','Referent Week Day']]
        group_by_day = aux_data.groupby('Referent Week Day').sum().sort_values(by='Installers',ascending=True)

        return group_by_day.head(1).index[0], group_by_day.head(1).values[0][0]
    
    def get_total_days(self, start_date='2019-08-01', end_date='2019-10-30'):
        end_date = datetime.datetime.strptime(end_date[0:10],'%Y-%m-%d')+timedelta(days=1)
        end_date = end_date.strftime('%Y-%m-%d')
        aux_data = self.data[(self.data['Date']>=start_date)&(self.data['Date']<=end_date)]
        print(aux_data)
        return len(aux_data)

    def get_number_of_days_with_above_average_views(self, start_date='2019-08-01', end_date='2019-10-30'):
        end_date = datetime.datetime.strptime(end_date[0:10],'%Y-%m-%d')+timedelta(days=1)
        end_date = end_date.strftime('%Y-%m-%d')
        aux_data = self.data.loc[:,['Date','Store Listing Visitors']]
        aux_data = aux_data[(aux_data['Date']>=start_date)&(aux_data['Date']<=end_date)]
        mean_views = aux_data['Store Listing Visitors'].mean()
        return aux_data['Store Listing Visitors'][aux_data['Store Listing Visitors']>=mean_views].count()
    
    def get_number_of_days_with_above_average_installs(self, start_date='2019-08-01', end_date='2019-10-30'):
        end_date = datetime.datetime.strptime(end_date[0:10],'%Y-%m-%d')+timedelta(days=1)
        end_date = end_date.strftime('%Y-%m-%d')
        aux_data = self.data.loc[:,['Date','Installers']]
        aux_data = aux_data[(aux_data['Date']>=start_date)&(aux_data['Date']<=end_date)]
        mean_views = aux_data['Installers'].mean()
        return aux_data['Installers'][aux_data['Installers']>=mean_views].count()
    
    def get_best_view_day(self, start_date='2019-08-01', end_date='2019-10-30'):
        end_date = datetime.datetime.strptime(end_date[0:10],'%Y-%m-%d')+timedelta(days=1)
        end_date = end_date.strftime('%Y-%m-%d')
        aux_data = self.data.loc[:,['Date','Store Listing Visitors']]
        aux_data = aux_data[(aux_data['Date']>=start_date)&(aux_data['Date']<=end_date)]
        maxx = aux_data['Store Listing Visitors'].max()
        aux_data = aux_data[aux_data['Store Listing Visitors']==maxx]
        return aux_data['Date'].values[0][0:10], aux_data['Store Listing Visitors'].values[0]

    def get_worst_view_day(self, start_date='2019-08-01', end_date='2019-10-30'):
        end_date = datetime.datetime.strptime(end_date[0:10],'%Y-%m-%d')+timedelta(days=1)
        end_date = end_date.strftime('%Y-%m-%d')
        aux_data = self.data.loc[:,['Date','Store Listing Visitors']]
        aux_data = aux_data[(aux_data['Date']>=start_date)&(aux_data['Date']<=end_date)]
        minn = aux_data['Store Listing Visitors'].min()
        aux_data = aux_data[aux_data['Store Listing Visitors']==minn]
        return aux_data['Date'].values[0][0:10], aux_data['Store Listing Visitors'].values[0]

    def get_best_installs_day(self, start_date='2019-08-01', end_date='2019-10-30'):
        end_date = datetime.datetime.strptime(end_date[0:10],'%Y-%m-%d')+timedelta(days=1)
        end_date = end_date.strftime('%Y-%m-%d')
        aux_data = self.data.loc[:,['Date','Installers']]
        aux_data = aux_data[(aux_data['Date']>=start_date)&(aux_data['Date']<=end_date)]
        
        maxx = aux_data['Installers'].max()
        aux_data = aux_data[aux_data['Installers']==maxx]
        return aux_data['Date'].values[0][0:10], aux_data['Installers'].values[0]

    def get_worst_installs_day(self, start_date='2019-08-01', end_date='2019-10-30'):
        end_date = datetime.datetime.strptime(end_date[0:10],'%Y-%m-%d')+timedelta(days=1)
        end_date = end_date.strftime('%Y-%m-%d')
        aux_data = self.data.loc[:,['Date','Installers']]
        aux_data = aux_data[(aux_data['Date']>=start_date)&(aux_data['Date']<=end_date)]
        minn = aux_data['Installers'].min()
        aux_data = aux_data[aux_data['Installers']==minn]
        return aux_data['Date'].values[0][0:10], aux_data['Installers'].values[0]

    def get_dataframe_graph1(self, start_date='2019-08-01', end_date='2019-10-30'):
        end_date = datetime.datetime.strptime(end_date[0:10],'%Y-%m-%d')+timedelta(days=1)
        end_date = end_date.strftime('%Y-%m-%d')
        aux_data = self.data.loc[:,['Date','Store Listing Visitors','Installers','Referent Week Day']]
        aux_data = aux_data[(aux_data['Date']>=start_date)&(aux_data['Date']<=end_date)]
        return aux_data
    
    def get_dataframe_graph2(self, start_date='2019-08-01', end_date='2019-10-30'):
        end_date = datetime.datetime.strptime(end_date[0:10],'%Y-%m-%d')+timedelta(days=1)
        end_date = end_date.strftime('%Y-%m-%d')
        aux_data = self.data.loc[:,['Date','Store Listing Visitors','Referent Week Day']]
        aux_data = aux_data[(aux_data['Date']>=start_date)&(aux_data['Date']<=end_date)]
        aux_data = aux_data.drop(columns={'Date'})
        group_day = aux_data.groupby('Referent Week Day').sum()
        group_day = group_day.sort_values(by='Store Listing Visitors',ascending=False)
        return group_day
    
    def get_dataframe_graph3(self, start_date='2019-08-01', end_date='2019-10-30'):
        end_date = datetime.datetime.strptime(end_date[0:10],'%Y-%m-%d')+timedelta(days=1)
        end_date = end_date.strftime('%Y-%m-%d')
        aux_data = self.data.loc[:,['Date','Installers','Referent Week Day']]
        aux_data = aux_data[(aux_data['Date']>=start_date)&(aux_data['Date']<=end_date)]
        aux_data = aux_data.drop(columns={'Date'})
        group_day = aux_data.groupby('Referent Week Day').sum()
        group_day = group_day.sort_values(by='Installers',ascending=False)
        return group_day
    


    #Individual analisys
    def get_visitors_day(self, date='2019-08-01'):
        date = date+' 00:00:00'
        return self.data['Store Listing Visitors'][self.data['Date']==date].values[0]

    def get_installs_day(self, date='2019-08-01'):
        date = date+' 00:00:00'
        return self.data['Installers'][self.data['Date']==date].values[0]
    
    def get_percentage_visitors_installs(self, date='2019-08-01'):
        date = date+' 00:00:00'
        return self.data['Visitor-to-Installer conversion rate'][self.data['Date']==date].values[0]*100
    
    def get_retained_1d(self, date='2019-08-01'):
        date = date+' 00:00:00'
        return self.data['Installers retained for 1 day'][self.data['Date']==date].values[0]
    
    def get_retained_1d_rate(self, date='2019-08-01'):
        date = date+' 00:00:00'
        return self.data['Installer-to-1 day retention rate'][self.data['Date']==date].values[0]*100
    
    def get_retained_7d(self, date='2019-08-01'):
        date = date+' 00:00:00'
        return self.data['Installers retained for 7 days'][self.data['Date']==date].values[0]
    
    def get_retained_7d_rate(self, date='2019-08-01'):
        date = date+' 00:00:00'
        return self.data['Installer-to-7 days retention rate'][self.data['Date']==date].values[0]*100
    
    def get_retained_30d(self, date='2019-08-01'):
        date = date+' 00:00:00'
        return self.data['Installers retained for 30 days'][self.data['Date']==date].values[0]
    
    def get_retained_30d_rate(self, date='2019-08-01'):
        date = date+' 00:00:00'
        return self.data['Installer-to-30 days retention rate'][self.data['Date']==date].values[0]*100
    
    def get_referent_week_day(self, date='2019-08-01'):
        date = date+' 00:00:00'
        return self.data['Referent Week Day'][self.data['Date']==date].values[0]
