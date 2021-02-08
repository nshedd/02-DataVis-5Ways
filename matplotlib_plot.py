import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import pandas as pd
import math

cars = pd.read_csv("cars-sample.csv")
cars = cars.dropna()

legend_label = ["bmw", "ford", "honda", "mercedes", "toyota"]
color = []
for i in cars.Manufacturer:
    if i == "bmw" :
        color.append(1)
    elif i == "ford" :
        color.append(2)
    elif i == "honda" :
        color.append(3)
    elif i == "mercedes" :
        color.append(4)
    elif i == "toyota" :
        color.append(5)
color_dict = {1:"bmw", 2:"ford", 3:"honda", 4:"mercedes", 5:"toyota"}

print(cars)


fig, ax = plt.subplots()

scatter = ax.scatter(cars.Weight, cars.MPG, c=color, s=cars.Weight**3.5/1000**3.5, alpha=0.5, cmap = mcolors.ListedColormap(["lightcoral", "olivedrab", "teal", "deepskyblue", "violet"]), label=cars.Manufacturer)

# produce a legend with the unique colors from the scatter
handles1, labels1 = scatter.legend_elements(prop="colors")
labels1 = ["bmw", "ford", "honda", "mercedes", "toyota"]
legend1 = ax.legend(handles1, labels1, loc="lower left", title="Manufacturer")
ax.add_artist(legend1)


# produce a legend with a cross section of sizes from the scatter
handles2, labels2 = scatter.legend_elements(prop="sizes", num=4, alpha=0.5)
labels2 = [3500, 4250, 4750]
legend2 = ax.legend(handles2, labels2, loc="upper right", title="Weight")

plt.xlabel("Weight")
plt.ylabel("MPG")

plt.savefig("matplotlib_plot.png")


