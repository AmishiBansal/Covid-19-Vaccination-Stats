import csv
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# style.use('ggplot')
data = pd.read_csv('UTs_Vaccine.csv',delimiter = ',')
x = np.linspace(-5, 5, 10)
state = data['State']
first_dose = data['Dose 1']
second_dose = data['Dose 2']
total = data['Total Vaccination Doses']

x.plot(kind="barh")
fig = plt.figure(figsize= (8,8))
myaxes = fig.add_axes([0.2,0.2,0.7,0.7])
myaxes.plot(state,first_dose,'r',label='First Dose')
myaxes.plot(state,second_dose,'b',label='Second Dose')
myaxes.plot(state,total,'y',label='Total Vaccinations')
myaxes.set_xlabel('Union Territory')
myaxes.set_ylabel('Vaccinations')
myaxes.set_title('Covid-19 Vaccinations in India')
plt.xticks(rotation=30)
myaxes.legend()
plt.show()