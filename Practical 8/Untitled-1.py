import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm #use it to let the plot beautiful

N = 10000
beta = 0.3
gamma = 0.05

plt.figure(figsize=(10, 6), dpi=100)#In order to have all the lines drawn on one graph
for r in range(0, 101, 10):
    S = N - int(r*N/100)#Because r*N/100 is a float, I am going to convert it to int
    I = 1                     
    R = 0                     
    I_arr = [I]               

    for i in range(1, 1000):
        new_I = np.random.choice([0, 1], size=S, p=[1 - beta * I / N, beta * I / N]).sum()#Same as before
        I += new_I
        S -= new_I

        new_R = np.random.choice([0, 1], size=I, p=[1 - gamma, gamma]).sum()
        I -= new_R
        R += new_R
        I_arr.append(I)

    plt.plot(range(1000), I_arr, label=f'{r}% Vaccination Rate')#Plot a plot entitled Vaccination Rate


plt.xlabel('Time')
plt.ylabel('Number of Infected People')
plt.title('SIR Model with Different Vaccination Rates')
plt.legend()


plt.show()
plt.savefig("SIR_Model_Different_Vaccination_Rates.png")






    



    
    





    
    








