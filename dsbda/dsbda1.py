import pandas as pd
df = pd.read_csv(r'C:\dsbda\employees.csv')
#print(df)
#finding mean
#print(df['Salary'].mean())
# using isnull() function  
'''null_data = pd.isnull(df['Team']) 
print(df[null_data])''' 

#print(df.dtypes)   
print(df.describe())