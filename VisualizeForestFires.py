import csv
from plotly.graph_objs import Layout
from plotly import offline, colors

lats, lons, brightness, daytime, confidence, dates = [], [], [], [], [], []

filename = "data/MODIS_C6_1_South_America_7d.csv"

# Open the file and look at the header
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

# Define the indices of the headers and columns
    for index, header in enumerate(header_row):
        print(index, header)

    for row in reader:

        try:
            if row[8] == "nominal":
                confidence.append(50)
            elif row[8] == "high":
                confidence.append(90)
            elif row[8] == "low":
                confidence.append(20)
            else:
                confidence.append(float(row[8]))
            if row[12] == "D":
                daytime.append("Daytime capture")
            else:
                daytime.append("Nightime capture")
        except IndexError:
            continue
        else:
            lats.append(float(row[0]))
            lons.append(float(row[1]))
            brightness.append(float(row[2]))
            dates.append(row[5])


print(len(lats), len(lons), len(brightness), len(daytime), len(confidence))
# print(lats[:10])
# print(lons[:10])
# print(brightness[:10])
# print(daytime[:10])
# print(confidence[:10])
number_points= 50000
lons = lons[:number_points]
lats = lats[:number_points]
brightness = brightness[:number_points]
dates = dates[:number_points]
confidence = confidence[:number_points]
daytime = daytime[:number_points]

# print(len(lats), len(lons), len(brightness), len(daytime), len(confidence))
# print(confidence)
#Creating the visualization
data = [{
    "type": "scattergeo",
    "lon": lons,
    "lat": lats,
    "text": dates,
    "marker": {
        "color": confidence,  # This determines which values are used for color-coding
        "colorscale": "Electric",  # This selects the range of colors we want to use
        "reversescale": True,  # We invert the order of the color scale
        "colorbar": {"title": "Confidence"}  # Customise the color scale bar on the map
    }
}]

my_layout = Layout(title="Possible forest fires")

fig = {"data": data, "layout": my_layout}
offline.plot(fig, filename="global_fires.html")

