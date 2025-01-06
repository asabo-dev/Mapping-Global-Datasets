from pathlib import Path
import json

# Read data as a string and convert to a Python object.
path = Path('/Users/quanefiom/desktop/developer/python_work/chapters/chp16_Downloading_Data/eq_data/eq_data_1_day_m1.geojson')
contents = path.read_text(encoding='utf-8')
all_eq_data = json.loads(contents)

# Create a more readable version of the data file.
path = Path('/Users/quanefiom/desktop/developer/python_work/chapters/chp16_Downloading_Data/eq_data/readable_eq_data.geojson')
readable_contents = json.dumps(all_eq_data, indent=4)
path.write_text(readable_contents)

# Examine all earthquakes in the dataset.
all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))

# Extract the magnitude of each earthquake.
mags = []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    mags.append(mag)

print(mags[:10]) 