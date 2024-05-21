import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm #use it to let the plot beautiful

N = 10000
beta = 0.3
gamma = 0.05

plt.figure(figsize=(10, 6), dpi=100)
# Loop over different vaccination rates  
for r in range(0, 101, 10):
    S = N - int(r*N/100)# Convert percentage to a decimal  
    I = 1                     
    R = 0                     
# Initialize an empty list to store I_arr for each vaccination rate     
    I_arr = [I]               
# SIR model simulation  
    for i in range(1, 1000):
        new_I = np.random.choice([0, 1], size=S, p=[1 - beta * I / N, beta * I / N]).sum()
        I += new_I
        S -= new_I

        new_R = np.random.choice([0, 1], size=I, p=[1 - gamma, gamma]).sum()
        I -= new_R
        R += new_R
        I_arr.append(I)

    plt.plot(range(1000), I_arr, label=f'{r}% Vaccination Rate')

plt.xlabel('Time')
plt.ylabel('Number of Infected People')
plt.title('SIR Model with Different Vaccination Rates')
plt.legend()


plt.show()
plt.savefig("SIR_Model_Different_Vaccination_Rates.png")