import h5py
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

matplotlib.use('TkAgg')

hf = h5py.File('GOLD_XYZ_OSC.0001_1024.hdf5', 'r')

print("Getting the XYZ files")
nx = hf.get('X')
ny = hf.get('Y')
nz = hf.get('Z')

print("Making the arrays")
print("z")
z = np.array(nz)
print("y")
y = np.array(ny)
# print( len(np.array(nx)))
print("x")
x = np.array(nx)

print("Shape of the files")
print("X", x.shape)
print("Y", y.shape)
print("Z", z.shape)

print("The array")
print("Z", z)
print("Y", y)
print("X", x)


xplot = np.arange(1, (len(z) + 1))
plt.plot(xplot, z, color="red")
plt.show()

xplot = np.arange(1, (len(y) + 1))
plt.plot(xplot, y, color="blue")
plt.show()

# print("X")
# xplot = np.arange(1, (len(x) + 1))
# plt.plot(xplot, x, color="green")
# plt.show()

# fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
# surf = ax.plot_surface(x, cmap=cm.coolwarm, linewidth=0, antialiased=False)
# plt.show()
# path = '/home/wabaker/WORKYBOY/'
# x_train = np.load(path + 'GOLD_XYZ_OSC.0001_1024.hdf5')
