import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as pltc
import PySimpleGUI as sg
import Functions as f


notation = input("Chess Notation: ")
f.notation_to_data(notation)


Colormap = pltc.LinearSegmentedColormap.from_list("reds2", ["white", "tab:red"])

data = np.random.random((8, 8))

plt.imshow(data, cmap=Colormap, interpolation='nearest')
plt.colorbar()
plt.title("2-D Heat Map")
# plt.show()


layout = [
    [sg.Canvas(size=(400, 400), key="_CANVAS_"),
     ]
]

window = sg.Window("Title", layout)


while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
window.close()
