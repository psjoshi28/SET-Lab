#!/usr/bin/env python
# coding: utf-8


import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


cars = pd.read_csv('Toyota.csv')

#Scatter plot
plt.scatter(cars['Age'], cars['Price'], c = 'blue')
plt.title('Price vs Age of the Cars')
plt.xlabel('Age in Years')
plt.ylabel('Price(Euros)')
plt.show()

#Histogram
plt.hist(cars['KM'], edgecolor = 'white', bins = 5)
plt.title('Histogram of Kilometer')
plt.xlabel('Kilometer')
plt.ylabel('Frequency')
plt.show()


plt.hist(cars['CC'], edgecolor = 'white', bins = 5)
plt.title('Histogram of CC')
plt.xlabel('CC')
plt.ylabel('Frequency')
plt.show()

#Bar plot
fuel_count = pd.value_counts(cars['FuelType'].values, sort = True)
plt.xlabel('Frequency')
plt.ylabel('Fuel Type')
plt.title('Bar plot of Fuel Type')
fuel_count.plot.barh()
