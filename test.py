import googlemaps
from datetime import datetime
import json

gmaps = googlemaps.Client(key='AIzaSyDH_Ti9v2RXaHg3On8Tnbsqakijpw5Vdpc')


# Request directions via public transit
now = datetime.now()
result = gmaps.distance_matrix("lergravsvej",
                                     "lyngbyvej",
                                     mode="driving",
                                     departure_time=now)
#print(result)

print(result["rows"][0]["elements"][0]["duration"]["text"])

