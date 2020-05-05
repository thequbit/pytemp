
import sys
import requests

def _get_text(lat, lng):
    url = 'https://forecast.weather.gov/MapClick.php?lat=%s&lon=%s' % (str(lat), str(lng))
    text = None
    try:
        r = requests.get(url, json={})
        text = r.text
        #print(r.text)
        #raise Exception('debug')
    except Exception as ex:
        print("[ERRPR] request error: %s", str(ex))
    return text

def _parse_text(text):
    parts = text.split('<p class="myforecast-current-lrg">')
    temp = parts[1].split('</p>')[0]
    current_temp = temp.split('&')[0]
    return current_temp

def get_temp_in_f(lat, lng):
    text = _get_text(lat, lng)
    current_temp = _parse_text(text)
    return int(float(current_temp))

def get_temp_in_c(lat, lng):
    text = _get_text(lat, lng)
    current_temp = _parse_text(text)
    temp = int(float(current_temp))
    return int( (temp - 32) * (5.0/9.0) )

if __name__ == '__main__':

    if len( sys.argv ) != 3:
        print("Usage:\n\n\tpython pytemp.py <lat> <lng>\n\n")
    else:

        lat = sys.argv[1]
        lng = sys.argv[2]

        f = get_temp_in_f(lat, lng)
        c = get_temp_in_c(lat, lng)
        
        print("Temp: %i\xb0F ( %i\xb0C )" % (f, c))