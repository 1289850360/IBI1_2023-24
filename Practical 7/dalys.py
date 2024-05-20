import os 
import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 

os.getcwd()  
os.listdir()  

dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")  
print(dalys_data.loc[0:100:10,"DALYs"]) # Show the forth column from every 10th row, starting from the first row for the first 100 rows

Afghanistan_row = [] # Use Booleans to check Afghanistan data
for i in dalys_data.loc[:,"Entity"]:  
    if i == "Afghanistan": 
        Afghanistan_row.append(True) 
    else:
        Afghanistan_row.append(False)  
print(dalys_data.loc[Afghanistan_row,"DALYs"])  
# Plot showing the DALYs over time in China
china_data = dalys_data.iloc[1140:1170,[0,2,3]] 
print(china_data)  

Mean = np.array(dalys_data.iloc[1140:1170,3])  
print(np.mean(Mean)) 

print("The dalys of 2019 is smaller than the mean")  

plt.plot(china_data.Year, china_data.DALYs, 'y+')  
plt.xticks(china_data.Year, rotation=45)  
plt.show()  
plt.clf()  



# Solutions for the question
In_2019 = []  
for i in dalys_data.loc[:,"Year"]:  
    if i == 2019:  
        In_2019.append(True)  
    else:
        In_2019.append(False)  
plt.boxplot(dalys_data.loc[In_2019,"DALYs"])  
plt.show()  
plt.clf()  
# The high income countries have less DALYs than the low income countries




