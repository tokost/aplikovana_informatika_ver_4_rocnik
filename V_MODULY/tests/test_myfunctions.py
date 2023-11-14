# test_myfunctions.py or test_mynewfunctions.py

from mypythonlib import myfunctions
# from mypythonlib import mynewfunctions

def test_haversine():
    assert myfunctions.haversine(52.370216, 4.895168, 52.520008, 13.404954) == 945793.4375088713


# print(distance)