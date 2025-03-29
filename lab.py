import json
import requests
import pandas as pd

destination = [
    'Boston, MA',
    'Toronto, ON'
]

api_key = 'AIzaSyDnIEIsZ9ZJSJCKCC39ZsWzYpZR5iqleXk'
origin = "Washington, DC"


def travel_time(origin, dest, api_key):
       
    url = "https://maps.googleapis.com/maps/api/distancematrix/json"
    url += f"?destinations={dest}"
    url += f"&origins={origin}"
    url += f"&units=imperial"
    url += f"&key={api_key}"

    results = requests.get(url).text
    results_json = json.loads(results)

    travel_time = results_json['rows'][0]['elements'][0]['duration']['value']
    return travel_time

def travel_table(origin,destination):
    api_key =  'AIzaSyDnIEIsZ9ZJSJCKCC39ZsWzYpZR5iqleXk'
    data = []
    for location in destination:
        row = []
        row.append(location)
        row.append(travel_time(origin,location,api_key))
        data.append(row)

    data = pd.DataFrame(data, columns=['destination','travel_time'])
    return data

data = travel_table(origin,destination)