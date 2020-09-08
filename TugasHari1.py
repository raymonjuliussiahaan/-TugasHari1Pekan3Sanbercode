# soal no 1

Jelaskan apa itu Figure
Figure, adalah window atau page atau halaman dalam objek visual.

Jelaskan apa itu Axis
Axis adalah suatu area di dalam figure dimana data akan di plot.

# soal no 2

# Buatlah Figure dan Axis kosong tanpa Data

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
plt.show()

# Plot data dengan explicit

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 20, 100)
y = np.cos(x/2)

fig, ax = plt.subplots()

ax.plot(x, y)
plt.show()

# Plot data dengan Implicit

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 20, 100)
y = np.cos(x/2)

plt.plot(x, y)
plt.show()

# soal no 3

import matplotlib.pyplot as plt
from IPython.display import Image
plt.style.use('seaborn')

fig = plt.figure()
ax = fig.add_subplot()

x = np.linspace(0, 20, 100)
y = np.cos(x/2)
y2 = np.sin(x)
y3 = np.sin(2*x)

ax.plot(x, y, x, y2, x, y3)
plt.show()

# save data tersebut dengan nama file bebas
fig.savefig('gambar.png')
Image('gambar.png')