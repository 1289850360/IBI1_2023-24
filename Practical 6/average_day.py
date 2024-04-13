#import somes tools in Python for making graphs
#In this session, since we want to change the time freely, so we need a variable to save values
#In the list, each string represents a variable
import numpy as py #inport python tools
import matplotlib.pyplot as plt #import python tools

time = {'sleeping' : 8 , 'classes' : 6 , 'studying' : 3.5 , 'TV' : 2 , 'music' : 1 } #input the data
time['other']= 24 - sum(time.values()) #get the time
print(time) #output
print(time['sleeping'])

plt.figure()
plt.pie(time.values(), labels= time.keys()) 
plt.show()
plt.clf()