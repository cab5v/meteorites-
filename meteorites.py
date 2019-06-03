import os
import sys
import requests
import math

#print(sys.platform)
#print(sys.version)
#path = '.'
#print(os.path,os.listdir(path))
#print new line

def get_distance(lat1, lon1):
    lat2 = 37.5407
    lon2 = -77.4360
    # approximate radius of earth in km
    radius = 6373.0
   
    dlat = math.radians(lat1 - lat2)
    dlon = math.radians(lon1 - lon2)
    a = (math.sin(dlat / 2) * math.sin(dlat / 2) +
         math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
         math.sin(dlon / 2) * math.sin(dlon / 2))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = radius * c
    return d


meteor_resp = requests.get('https://data.nasa.gov/resource/gh4g-9sfh.json')
#print (meteor_resp.text)
meteor_data = meteor_resp.json()
leastdis = 100000
error = 0
for x in meteor_data:
    try:
        looplat = float(x['geolocation']['latitude'])
        looplon = float(x['geolocation']['latitude'])
        dis = get_distance(looplat, looplon)
        if dis < leastdis:
            leastdis = dis
            short = x
    except:
        error = error +1
        continue
        
print ("Least distance to RVA is " + str(dis))
print(short)
print(error)