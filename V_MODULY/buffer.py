from shapely.geometry import Point
from shapely.geometry import mapping, shape

def udelej_buffer(geometry, velikost):
    """Vráti buffer vo formáte GeoJSON pre zadanú geometriu
    """

    geometrie = shape(geometry)
    buffer = geometrie.buffer(velikost)
    return  mapping(buffer)