import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 1, 100)
y = np.linspace(0,100,1000)
y = abs((1/x)*(1-1/2.87))
fig = plt.figure(figsize= (5,5))
plt.plot(x,y)
plt.ylim(0,1)
plt.title("Estimation of population to be vaccinated")
plt.xlabel("Efficacy of Vaccine")
plt.ylabel("Percentage population to be vaccinated")

plt.show()