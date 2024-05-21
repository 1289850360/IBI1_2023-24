import numpy as np  
import matplotlib.pyplot as plt  
  
beta = 0.3  # Infection probability  
gamma = 0.05  # Recovery probability  
population = np.zeros((100, 100), dtype=int)  
  
# Randomly choose a point for the initial outbreak  
# Note: np.random.choice should not have a space between np and random  
outbreak = np.random.choice(range(100), 2, replace=False)  # Use replace=False to ensure unique points  
population[outbreak[0], outbreak[1]] = 1  
  
plt.figure(figsize=(6, 4), dpi=150)  # Draw the initial state  
plt.imshow(population, cmap='viridis', vmin=0, vmax=2, interpolation='nearest')  
plt.title('Initial State')  
plt.colorbar(ticks=[0, 1, 2], label='Status')  # Add colorbar with labels  
plt.show()  
  
for t in range(100):  
    # Find infected points  
    infectedIndex = np.where(population == 1)  
      
    # Loop through all infected points  
    for i in range(len(infectedIndex[0])):  
        x = infectedIndex[0][i]  
        y = infectedIndex[1][i]  
          
        # infect each neighbour with probability beta  
        # infect all 8 neighbours  
        for x_neighbour in range(max(0, x-1), min(x+2, 100)):  # Ensure indices don't go out of bounds  
            for y_neighbour in range(max(0, y-1), min(y+2, 100)):  
                if (x_neighbour, y_neighbour) != (x, y):  # Don't infect yourself  
                    if population[x_neighbour, y_neighbour] == 0:  # Only infect neighbours that are not already infected  
                        population[x_neighbour, y_neighbour] = np.random.choice([0, 1], p=[1-beta, beta])  # No need for np.array  
      
    # Recover individuals with probability gamma  
    for i in range(len(infectedIndex[0])):  
        x, y = infectedIndex[0][i], infectedIndex[1][i]  
        if np.random.rand() < gamma:  
            population[x, y] = 2  # Mark recovered individuals as 2  
      
    # Plot the current time step's heatmap  
    plt.figure(figsize=(6, 4), dpi=150)  
    plt.imshow(population, cmap='viridis', vmin=0, vmax=2, interpolation='nearest')  
    plt.title(f'Time step {t}')  
    plt.colorbar(ticks=[0, 1, 2], label='Status')  # Add colorbar with labels  
    plt.show()  
  
