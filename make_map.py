import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from mpl_toolkits.basemap import Basemap
import pandas as pd


#gets the values
data = pd.read_csv("crime.csv", encoding = "ISO-8859-1")

hour_data = data[["HOUR", "Lat", "Long"]]
hour_data.replace(-1, None, inplace=True)
hour_data = hour_data.dropna()

numbers1 = [4,5,6,7,8,9,11]
for n in numbers1:
    hour_data["HOUR"].replace(n, 10, inplace=True)

numbers2 = [12,13,14,15,16,17,19]
for n in numbers2:
    hour_data["HOUR"].replace(n, 18, inplace=True)

numbers3 = [20,21,22,23,1,2,3]
for n in numbers3:
    hour_data["HOUR"].replace(n, 0, inplace=True)



new_data = hour_data.groupby("HOUR")
new_data.get_group(0).Lat


# Store our latitude and longitude
lat1 = new_data.get_group(10).Lat
lon1 = new_data.get_group(10).Long
lat2 = new_data.get_group(18).Lat
lon2 = new_data.get_group(18).Long
lat3 = new_data.get_group(0).Lat
lon3 = new_data.get_group(0).Long

print(lat1.size)
print(lat2.size)
print(lat3.size)

gs = gridspec.GridSpec(1,3)

plt.figure( figsize=(20, 60))
ax1 = plt.subplot(gs[0,0])
ax1.set_title("Morning (04.00-11.59) instances: " + str(lat1.size))
ax2 = plt.subplot(gs[0,1])
ax2.set_title("Afternoon (12.00-19.59) instances: " + str(lat2.size))
ax3 = plt.subplot(gs[0,2])
ax3.set_title("Night (20.00-03.59) instances: " + str(lat3.size))

m1 = Basemap(llcrnrlon=-71.25, llcrnrlat=42.2, urcrnrlon=-70.85, urcrnrlat=42.5, epsg=4269, ax=ax1)
m1.arcgisimage(service="ESRI_Imagery_World_2D", xpixels = 2000, verbose= True)

x, y = m1(lon1, lat1)

ax1.scatter(x, y, 1, marker=".", color="Red")

m2 = Basemap(llcrnrlon=-71.25, llcrnrlat=42.2, urcrnrlon=-70.85, urcrnrlat=42.5, epsg=4269, ax=ax2)
m2.arcgisimage(service="ESRI_Imagery_World_2D", xpixels = 2000, verbose= True)

x, y = m2(lon2, lat2)

ax2.scatter(x, y, 1, marker=".", color="Yellow")

m3 = Basemap(llcrnrlon=-71.25, llcrnrlat=42.2, urcrnrlon=-70.85, urcrnrlat=42.5, epsg=4269, ax=ax3)
m3.arcgisimage(service="ESRI_Imagery_World_2D", xpixels = 2000, verbose= True)

x, y = m3(lon3, lat3)

ax3.scatter(x, y, 1, marker=".", color="Blue")

plt.show()