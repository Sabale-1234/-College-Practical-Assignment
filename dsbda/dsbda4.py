import pandas as pd;
#df =pd.read_csv(r'C:\dsbda\boston.csv')
#print(df)
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
df =pd.read_csv(r'C:\dsbda\Regression.csv')
#print(df)
lr=LinearRegression()
x=df.iloc[:,0].values.reshape(-1,1)
y=df.iloc[:,1].values.reshape(-1,1)
lr.fit(x,y)
y_predict=lr.predict(x)

plt.scatter(x,y)
plt.plot(x,y_predict,color='r')
plt.xlabel("SAT")
plt.ylabel("GPA")
plt.title("SAT,GPA Prediction Model")
plt.plot()
plt.show()


