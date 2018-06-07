

sentence = "$GPRMC,122721.166,A,5231.506,N,01325.425,E,4018.3,090.0,030518,000.0,W*46"


def parse(sentence):
	arr = sentence.split(",")
	print get_latitudeInDegree(arr)
	print get_longitudeInDegree(arr)
	print get_Compass(arr)

def get_latitudeInDegree(arr):
	lat = arr[3].split(".")
	minutes = lat[0][-2:]+'.'+lat[1]
	deg = lat[0][:-2]
	minutes = float(minutes) / 60
	return float(float(deg)+minutes)

def get_longitudeInDegree(arr):
	lat = arr[5].split(".")
	minutes = lat[0][-2:]+'.'+lat[1]
	deg = lat[0][:-2]
	minutes = float(minutes) / 60
	return float(float(deg)+minutes)

def get_Compass(arr):
	return float(arr[8])

parse(sentence)