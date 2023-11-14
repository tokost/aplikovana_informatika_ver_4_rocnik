# myfnewunctions.py

import math

def haversine(lat1, lon1, lat2, lon2):

    # Radius of the Earth in kilometers

    R = 6371.0

    # Convert latitude and longitude from degrees to radians

    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    # Calculate the differences

    dlat = lat2 - lat1

    dlon = lon2 - lon1

    # Haversine formula

    a = math.sin(dlat / 2)**2 + math.cos(lat1) * \
        math.cos(lat2) * math.sin(dlon / 2)**2

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Calculate the distance

    distance = R * c

    return distance
