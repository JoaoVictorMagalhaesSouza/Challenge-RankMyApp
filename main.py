#%%
import pandas as pd
from utils import eda
from utils import data_inputation

%load_ext autoreload
%autoreload 2

#%% 1) Read the data
path = './data/'
input_data = pd.read_excel(f'{path}b4bank.xlsx',sheet_name='Retained_Bank')
#%% 2) EDA
filtered_data = eda.ExploratoryDataAnalisys(input_data).apply_pipeline_eda()
#%% 3) Data Inputation
data_manipulation = data_inputation.DataInputation(filtered_data).insert_week_nominal_day()
# %%
