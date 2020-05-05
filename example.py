
from pytemp import get_temp_in_f

lat = 43.0374
lng = -77.7038
temp_f = get_temp_in_f(lat, lng)
if temp_f > 80:
    print("%i: Getting hot!" % temp_f)
else:
    print("%i: Still cool." % temp_f)