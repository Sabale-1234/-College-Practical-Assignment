import pandas as pd
import numpy as np
import csv
from scipy import stats
from scipy.stats import boxcox
data = pd.read_csv(r'C:\dsbda\employees.csv')
#print(data)

# check for missing values
# if data.isnull().values.any():
    # print("There are missing values in the DataFrame.")
# else:
    #  print("No")
    
# replace missing values with mean or median
# for col in data.columns:
# replace missing values with mean or median
    for col in data.columns:
        if data[col].isnull().values.any():
            if data[col].dtype != 'object':
                median = data[col].median()
                data[col].fillna(median, inplace=True)
            else:
                mode = data[col].mode().iloc[0]
                data[col].fillna(mode, inplace=True)
print(data)