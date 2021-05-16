import cartopy
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import pandas as pd
import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
response = urllib.request.urlopen('https://www.python.org')
fig = plt.figure(figsize=(40, 40))
ax = plt.axes(projection=cartopy.crs.PlateCarree())
ax.add_feature(cartopy.feature.LAND)
ax.add_feature(cartopy.feature.OCEAN)
ax.add_feature(cartopy.feature.COASTLINE)
ax.add_feature(cartopy.feature.BORDERS, linestyle='-', alpha=.5)
ax.add_feature(cartopy.feature.LAKES, alpha=0.95)
ax.add_feature(cartopy.feature.RIVERS)
ax.set_extent([-10, 50, 30, 70])
plt.title("Before COVID-19  Ryo Shiraishi", fontsize="50")
airports = pd.read_table("airports.dat", sep=",",
                         usecols=["ID", "Name", "City", "Country", "IATA", "ICAO", "Latitude", "Longitude", "Altitude",
                                  "Timezone", "DST", "DZ", "Type", "Source"])
print(airports)
before = pd.read_csv("otselennud.csv", sep=";", names=["City", "IATA"])
during = pd.read_csv("flights21.csv", sep=";", names=["City", "IATA"])
airportsDF1 = airports.drop(
    labels=["ID", "Name", "City", "Country", "ICAO", "Altitude", "Timezone", "DST", "DZ", "Type", "Source"], axis=1)
airportBefore = before.merge(airportsDF1, on=["IATA"])
print(airportBefore)
for i in range(1, len(airportBefore)):
    plt.plot([airportBefore["Longitude"].values[0], airportBefore["Longitude"].values[i]],
             [airportBefore["Latitude"].values[0], airportBefore["Latitude"].values[i]], color='blue', linewidth=8,
             marker='o', transform=ccrs.Geodetic())
    plt.text(airportBefore["Longitude"].values[i], airportBefore["Latitude"].values[i], airportBefore["IATA"].values[i],
             fontsize="50", transform=ccrs.Geodetic())
plt.text(airportBefore["Longitude"].values[0], airportBefore["Latitude"].values[0], airportBefore["IATA"].values[0],
         fontsize="50", transform=ccrs.Geodetic())
plt.savefig('airportBefore.png', dpi=250)
plt.cla()

fig = plt.figure(figsize=(40, 40))
ax = plt.axes(projection=cartopy.crs.PlateCarree())
ax.add_feature(cartopy.feature.LAND)
ax.add_feature(cartopy.feature.OCEAN)
ax.add_feature(cartopy.feature.COASTLINE)
ax.add_feature(cartopy.feature.BORDERS, linestyle='-', alpha=.5)
ax.add_feature(cartopy.feature.LAKES, alpha=0.95)
ax.add_feature(cartopy.feature.RIVERS)
ax.set_extent([-10, 50, 30, 70])
plt.title("During COVID-19  Ryo Shiraishi", fontsize="50")
airportDuring = during.merge(airportsDF1, on=["IATA"])
for i in range(1, len(airportDuring)):
    plt.plot([airportDuring["Longitude"].values[0], airportDuring["Longitude"].values[i]],
             [airportDuring["Latitude"].values[0], airportDuring["Latitude"].values[i]], color='blue', linewidth=8,
             marker='o', transform=ccrs.Geodetic())
    plt.text(airportDuring["Longitude"].values[i], airportDuring["Latitude"].values[i], airportDuring["IATA"].values[i],
             fontsize="50", transform=ccrs.Geodetic())
plt.text(airportDuring["Longitude"].values[0], airportDuring["Latitude"].values[0], airportDuring["IATA"].values[0],
         fontsize="50", transform=ccrs.Geodetic())
plt.savefig('airportDuring.png', dpi=250)
