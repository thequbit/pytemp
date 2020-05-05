# pytemp
Gets the temperature based on US location information

Dependencies:

    pip install requests

CLI Usage:

    python3 pytemp.py <lat> <lng>

From code:

    from pytemp import get_temp_in_f

    lat = 43.0374
    lng = -77.7038
    temp_f = get_temp_in_f(lat, lng)
    if temp_f > 80:
        print("Getting hot!)
    else:
        print("Still cool.)

This uses the weather.gov html web end point.  Please use it responsibly.