import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.style.use('bmh')
df = pd.read_csv('UTs_Vaccine.csv')

state = df['State']
first_dose = df['Dose 1']
second_dose = df['Dose 2']
total = df['Total Vaccination Doses']

ind = np.arange(len(df))
width = 0.4

fig, ax = plt.subplots()
ax.barh(ind,first_dose,width,color='red',label="First Dose")
ax.barh(ind+width,second_dose,width,color='blue',label="Second Dose")

ax.set(yticks=ind + width, yticklabels=state, ylim=[2*width - 1, len(df)])
ax.legend()
plt.xlabel('Vaccinations')
plt.ylabel('Union Territory')
# plt.barh(state,first_dose,label='First Dose',color='red')
# plt.barh(state,second_dose,label = 'Second Dose',color='blue')
plt.grid(False)
# # plt.barh(state,total, label = 'Total Doses',color='red')
plt.show()