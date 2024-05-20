import numpy as np  
import matplotlib.pyplot as plt  
  
# Parameters  
N = 10000  # Total population  
S = N - 1  # Initial number of susceptible individuals  
I = 1      # Initial number of infected individuals  
R = 0      # Initial number of recovered individuals  
beta = 0.3  # Infection rate  
gamma = 0.05  # Recovery rate  
  
# Time steps  
t_max = 1000  
dt = 1  # Time step size  
  
# Arrays to store the values of S, I, R  
S_arr = [S]  
I_arr = [I]  
R_arr = [R]  
  
# SIR model simulation  
for t in range(t_max):  
    dS_dt = -beta * S * I / N  # Change in susceptible  
    dI_dt = beta * S * I / N - gamma * I  # Change in infected  
    dR_dt = gamma * I  # Change in recovered  
      
    # Update S, I, R  
    S += dS_dt * dt  
    I += dI_dt * dt  
    R += dR_dt * dt  
      
    # Ensure no negative values and round to integers (optional)  
    S = max(0, int(S))  
    I = max(0, int(I))  
    R = max(0, int(R))  
      
    # Append SIR to the arrays  
    S_arr.append(S)  
    I_arr.append(I)  
    R_arr.append(R)  
  
# Time array  
time = np.arange(t_max + 1) * dt  
  
# Plot the SIR model using Matplotlib  
plt.figure(figsize=(6, 4), dpi=150)  
plt.plot(time, S_arr, label='Susceptible')  
plt.plot(time, I_arr, label='Infected')  
plt.plot(time, R_arr, label='Recovered')  
plt.xlabel('Time')  
plt.ylabel('Number of People')  
plt.title('SIR Model')  
plt.legend()  
plt.show()  
  
plt.savefig("SIR.png")  # Save the figure