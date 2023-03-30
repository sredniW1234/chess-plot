import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as pltc

# notation = input("Chess Notation: ")



Colormap = pltc.LinearSegmentedColormap.from_list("reds2", ["white", "tab:red"])

data = np.random.random((8, 8))
data = np.zeros((8, 8))

plt.imshow(data, cmap=Colormap, interpolation='nearest')
plt.colorbar()
plt.title("2-D Heat Map")
plt.show()