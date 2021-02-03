import h5py
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

matplotlib.use('TkAgg')

hf = h5py.File('GOLD_XYZ_OSC.0001_1024.hdf5', 'r')
ny = hf.get('Y')
x = np.array(ny)


fig, ax = plt.subplots()
ax.set(xlabel='Types of radio Modulation', ylabel='Active or Not',
       title='Different types of radio modulation')

ax.grid()
y = np.arange(1, (len(x) + 1))
ax.plot(y, x)
fig.canvas.draw()
plt.show()

listofradiotypes = ["Loot1", "Loot2", "Loot3", "Loot4", "Loot5", "Loot6", "Loot7", "Loot8", "Loot9", "Loot10",
                    "Loot11", "Loot12", "Loot13", "Loot14", "Loot15", "Loot16", "Loot17", "Loot18", "Loot19", "Loot20",
                    "Loot21", "Loot22", "Loot23", "Loot24"]


def findmodtype(index: int = 0) -> str:
    currentrow = x[index]
    for i in range(0, len(currentrow)):
        if currentrow[i] == 1:
            return listofradiotypes[i]


print("", findmodtype(2111111))