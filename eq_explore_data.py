from pathlib import Path
import json

# Read data as a string and convert to a Python object.
path = Path('/Users/quanefiom/desktop/developer/python_work/chapters/chp16_Downloading_Data/eq_data/30days_sig_earthquakes.geojson')
contents = path.read_text(encoding='utf-8')
all_eq_data = json.loads(contents)

# Create a more readable version of the data file.
path = Path('/Users/quanefiom/desktop/developer/python_work/chapters/chp16_Downloading_Data/eq_data/30days_sig_earthquakes.geojson')
readable_contents = json.dumps(all_eq_data, indent=4)
path.write_text(readable_contents)