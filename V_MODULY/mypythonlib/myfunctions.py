# myfunctions.py

from math import radians, cos, sin, asin, sqrt

def haversine(lon1: float, lat1: float, lon2: float, lat2: float) -> float:
    """
    Vypočítajte dĺžku kruhového výseku medzi dvoma bodmi na
    zemi (uvedenými v desatinách stupňoch), má sa vrátiť 
    vzdialenosť v metroch.
    Všetky argumenty musia byť rovnako dlhé.
    :param lon1: zemepisná dĺžka prvého miesta
    :param lat1: zemepisná šírka prvého miesta

    :param lon2: zemepisná dĺžka druhého miesta
    :param lat2: zemepisná šírka druhého miesta
    
    :return: vzdialenosť v metroch medzi dvoma sadami súradníc

    """
    # Prepočet desiatkovej hohnoty stupnov (uhlov) na radiany (dluzky oblukov)
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # Haversinov vzorec
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371  # Obluk zemi v kilometroch
    return c * r
