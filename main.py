#%%
import pandas as pd
from utils import eda
from utils import data_inputation

%load_ext autoreload
%autoreload 2
data_path = './data/'
#%% 1) Read the data
input_data = pd.read_excel(f'{data_path}b4bank.xlsx',sheet_name='Retained_Bank')
#%% 2) EDA and Data Filtering/Treatment
filtered_data = eda.ExploratoryDataAnalisys(input_data).apply_pipeline_eda()
#%% 3) Data Inputation
final_data = data_inputation.DataInputation(filtered_data).apply_pipeline_data_inputation()
#%% 4) Saving data
final_data.to_csv(f"{data_path}final_data.csv")

# %% 5) Load data
data = pd.read_csv(f'{data_path}final_data.csv')

# %%
