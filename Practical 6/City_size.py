import matplotlib.pyplot as plt
#import tools
import numpy as np
#import tools

UK_cities = [0.56, 0.62, 0.04, 9.7] 
#a list for UK cities
China_cities = [0.58, 8.4, 29.9, 22.2] 
#a list for China cities
UK_labels = ['Edinburgh','Glasgow','Stirling','London'] 
#input name of UK cities
China_labels = ['Haining', 'Hangzhou', 'Shanghai' ,'Beijing'] 
#input name of UK cities
print(UK_cities)
print(China_cities)

index = np.arange(4) # set the index of 4
plt.figure() #create a figure
plt.bar(index, UK_cities, 0.8, yerr = 0) #create a bar chart showing UK
plt.xticks(index, UK_labels) #make xticks' lables UK cities'names 
plt.title("city size of population")#mark the title
plt.show()

plt.figure()#the plan is all same as UK
plt.bar(index, China_cities, 0.8, yerr = 0)
plt.xticks(index, China_labels)
plt.title("city size of population")
plt.show()

plt.clf()