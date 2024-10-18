import numpy as np # math
import matplotlib.pyplot as plt # plotting
import matplotlib.image as mpimg # loading images
import pandas # handling csv data

fig = plt.figure(figsize=(8, 7))

# loading a table with pandas
data_frame = pandas.read_csv("spread_data.csv")
print(data_frame)

# loading the image with matplotlib
img_germany = mpimg.imread("germany.png")

# add a subplot to the figure at pos. 1. The grid is 2x2.
axs1 = fig.add_subplot(1, 2, 1)
axs1.set_title("Fälle in 7 Tagen = Punktgröße (Fläche)")
axs1.xaxis.set_visible(False)
axs1.yaxis.set_visible(False)
image1 = axs1.imshow(img_germany)

axs2 = fig.add_subplot(1, 2, 2)
axs2.set_title("Fälle in 7 Tagen = Punktgröße (Steven)")
axs2.xaxis.set_visible(False)
axs2.yaxis.set_visible(False)
image2 = axs2.imshow(img_germany)

infected = data_frame["Anzahl Inf. 7T"]
population = data_frame["Einwohner"]
x_pos = data_frame["x_pos"]
y_pos = data_frame["y_pos"]

alpha = 300
radii = (infected/alpha)**(1/1.4)
areas = np.pi*(radii**2)

relative_infections = 100000*infected/population

scatter1 = axs1.scatter(x_pos, y_pos, s=infected*0.05)
scatter2 = axs2.scatter(x_pos, y_pos, s=areas, cmap="magma", c=relative_infections, vmin=0, vmax=250)
fig.colorbar(scatter2, label="Fälle je 100.000 Einwohner (7 Tage)", ax=axs2, orientation="horizontal", pad=0.02)


# Run show, to make sure everything is displayed.
plt.show()
