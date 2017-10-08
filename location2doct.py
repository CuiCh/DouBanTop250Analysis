locationdict = {}
filepath = './location.txt'
with open(filepath) as f:
	for line in f.readlines():
		country,location = line.split(":")
		lng,lat = location[2:-3].split(",")
		lng = float(lng)
		lat = float(lat)
		locationdict[country] = {'lng':lng,'lat':lat}
print(locationdict)