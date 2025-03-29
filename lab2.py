#si-exercise

import pandas as pd
import json
import plotly.express as px
import requests
import numpy as np

capitals = pd.DataFrame([["Alabama","Montgomery","AL"],
["Alaska","Juneau","AK"],
["Arizona","Phoenix","AZ"],
["Arkansas","Little Rock","AR"],
["California","Sacramento","CA"],
["Colorado","Denver","CO"],
["Connecticut","Hartford","CT"],
["Delaware","Dover","DE"],
["Florida","Tallahassee","FL"],
["Georgia","Atlanta","GA"],
["Hawaii","Honolulu","HI"],
["Idaho","Boise","ID"],
["Illinois","Springfield","IL"],
["Indiana","Indianapolis","IN"],
["Iowa","Des Moines","IA"],
["Kansas","Topeka","KS"],
["Kentucky","Frankfort","KY"],
["Louisiana","Baton Rouge","LA"],
["Maine","Augusta","ME"],
["Maryland","Annapolis","MD"],
["Massachusetts","Boston","MA"],
["Michigan","Lansing","MI"],
["Minnesota","Saint Paul","MN"],
["Mississippi","Jackson","MS"],
["Missouri","Jefferson City","MO"],
["Montana","Helena","MT"],
["Nebraska","Lincoln","NE"],
["Nevada","Carson City","NV"],
["New Hampshire","Concord","NH"],
["New Jersey","Trenton","NJ"],
["New Mexico","Santa Fe","NM"],
["New York","Albany","NY"],
["North Carolina","Raleigh","NC"],
["North Dakota","Bismarck","ND"],
["Ohio","Columbus","OH"],
["Oklahoma","Oklahoma City","OK"],
["Oregon","Salem","OR"],
["Pennsylvania","Harrisburg","PA"],
["Rhode Island","Providence","RI"],
["South Carolina","Columbia","SC"],
["South Dakota","Pierre","SD"],
["Tennessee","Nashville","TN"],
["Texas","Austin","TX"],
["Utah","Salt Lake City","UT"],
["Vermont","Montpelier","VT"],
["Virginia","Richmond","VA"],
["Washington","Olympia","WA"],
["West Virginia","Charleston","WV"],
["Wisconsin","Madison","WI"],
["Wyoming","Cheyenne","WY"]], columns = ['state', 'capital', 'abbrev'])



def get_cordinates(country, state, city):
       
    url =f"http://api.zippopotam.us/{country}/{state}/{city}"
    results = requests.get(url).text
    results_json = json.loads(results)
    rows = []
    for places in results_json['places']:
        lat = float(places['latitude'])
        long = float(places['longitude'])
        rows.append([lat,long])
    return rows

def map_table(capitals):
    data = []
    for capital_info in np.array(capitals):
        state = capital_info[2].lower()
        capital= capital_info[1].lower()
        #mean_lat,mean_long = np.mean(np.array(get_cordinates('us',state,capital)),axis=0)
        coordinates = get_cordinates('us',state,capital)
        mean_lat = coordinates[0][0]
        mean_long = coordinates[0][1]
        city_info = {
            'capital': capital.title(),
            'abbrev': state.upper(),
            'lat': mean_lat,
            'lon': mean_long
            }
        data.append(city_info)
    return data

coordindates = pd.DataFrame(map_table(capitals))
merged_df = pd.merge(capitals,coordindates, on=['capital','abbrev'], how='left')