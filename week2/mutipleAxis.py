import numpy as np 
import matplotlib.pyplot as plt 




# Make-up data
calories = [380.70, 420.98, 454.91, 406.45, 446.16, 498.08, 504.54, 459.05, 459.55, 484.79]
countries = ['India', 'Japan', 'Korea', 'China', 'Thai', 'Italy', 'France', 'Greece', 'Mexico', 'US']
obesity_rates = [3.9, 4.3, 4.7, 6.2, 10, 19.9, 21.6, 24.9, 28.9, 36.2]

fig, ax1 = plt.subplots(figsize = (8, 5))
ax1.bar(countries, obesity_rates, color='C8')
ax1.set_ylabel('obesity rate(%)', color='C8')
ax1.tick_params(axis='y', labelcolor='C8')

ax2 = ax1.twinx()
ax2.plot(countries, calories, color='C0')
ax2.set_ylabel('calories', color='C0')
ax2.tick_params(axis='y', labelcolor='C0')
plt.show()