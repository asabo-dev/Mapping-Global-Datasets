from pathlib import Path
import json

import plotly.express as px

# Read data as a string and convert to a Python object.
path = Path('/Users/quanefiom/desktop/developer/python_work/chapters/chp16_Downloading_Data/eq_data/eq_data_30_day_m1.geojson')
contents = path.read_text(encoding='utf-8')
all_eq_data = json.loads(contents)

# Create a more readable version of the data file.
path = Path('/Users/quanefiom/desktop/developer/python_work/chapters/chp16_Downloading_Data/eq_data/readable_eq_data2.geojson')
readable_contents = json.dumps(all_eq_data, indent=4)
path.write_text(readable_contents)

# Examine all earthquakes in the dataset.
all_eq_dicts = all_eq_data['features']
#print(len(all_eq_dicts))

# Extract the magnitude and location data of each earthquake.
mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

# Map the earthquakes.
title = 'Global Earthquakes'
fig = px.scatter_geo(lon=lons, lat=lats, size=mags, title=title, color=mags, color_continuous_scale='Viridis', labels={'color': 'Magnitude'}, projection='natural earth',)
fig.show()