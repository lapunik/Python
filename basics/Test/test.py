from matplotlib import pyplot as plt
import numpy as np

# Data
data = np.random.randn(1000)

# Průměr
mean = np.mean(data)

# Rozptyl
std = np.std(data)

# Střední odchylka
var = np.var(data)

# Histogram
plt.hist(data, bins=100, density=True)

z = (data-mean)/var

print(z.shape)

# Přímky pro průměr, rozptyl a střední odchylku
plt.axvline(mean, color='r', label='Průměr')
plt.axvline(mean + std, color='g', label='Rozptyl')
plt.axvline(mean - std, color='g')
plt.axvline(mean + np.sqrt(var), color='b', label='Střední odchylka')
plt.axvline(mean - np.sqrt(var), color='b')

plt.legend()
plt.show()