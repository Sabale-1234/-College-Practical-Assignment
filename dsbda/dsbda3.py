import pandas as pd
df = pd.read_csv(r'C:\dsbda\Salary_Data.csv')
#print(df)

#mean of salary column
#print("Mean of the salary column is" ,df['Salary'].mean())

#median of salary column

#print("Median of salary column is" ,df['Salary'].median()) 

#maximum value present in salary column

#print("Maximum value in Salary is" ,df['Salary'].max()) 

#minimum value present in salary column

#print("Minimum value in Salary is" ,df['Salary'].min()) 

#Standard deviation of salary column

#print("Standard deviation of Salary column is" ,df['Salary'].std()) 

#percentile

#print("percentile value in Salary is" ,df['Salary'].quantile(0.5))


#groupby the salary column

#gk = df.groupby('Salary') 
#print(gk.first())

gk = df.groupby('Salary') 
print(gk.last())
