
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import pandas as pd

#gets the values
data = pd.read_csv("crime.csv", encoding = "ISO-8859-1")

lon = np.array(data["Long"].head(35))
lat = np.array(data["Lat"].head(35))

fig = plt.figure(figsize=(8, 8))
m = Basemap(llcrnrlon=-71.25, llcrnrlat=42.2, urcrnrlon=-70.85, urcrnrlat=42.5, epsg=4269)
m.arcgisimage(service="ESRI_Imagery_World_2D", xpixels = 2000, verbose= True)

x, y = m(lon, lat)
plt.scatter(x, y, 5, marker="o", color="Red")

plt.show()