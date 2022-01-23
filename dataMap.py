import numpy as np
import pandas as pd
import streamlit as st
import pydeck as pdk

#Page Setup
st.set_page_config(layout="wide")

#DataFrame
dataFrame = pd.DataFrame(np.random.randn(2000, 2) / [10, 10] + [43.65, -79.34], columns=['lat', 'lon'])
dataFrame2 = pd.DataFrame(np.random.randn(2000, 2) / [10, 10] + [43.65, -79.34], columns=['lat', 'lon'])

#Geocode
#import http.client, urllib.parse

#conn = http.client.HTTPConnection('api.positionstack.com')

#params = urllib.parse.urlencode({
#    'access_key': '2936a8a700f59a9f6acf885ae6a0daef',
#    'query': 'king',
#   'limit': 1,
#   'country': 'CA'
#   })
#conn.request('GET', '/v1/forward?{}'.format(params))

#res = conn.getresponse()
#data = res.read()

#print(data.decode('utf-8'))


#Mapping function
def map(data, lat, lon, zoom):
    st.write(pdk.Deck(
        initial_view_state={
            "latitude": lat,
            "longitude": lon,
            "zoom": zoom,
            "pitch": 60,
        },
        layers=[
            pdk.Layer(
                "HexagonLayer",
                data=data,
                get_position=["lon", "lat"],
                radius=200,
                elevation_scale=40,
                elevation_range=[0, 1000],
                pickable=True,
                extruded=True,
                auto_highlight = True,
                get_fill_color=[140,0,155,140]
            ),
        ]
    ))


map(dataFrame, 43.65, -79.34, 10)
print(dataFrame)

#CSV Read

age_cat = {"19 and Younger":"Under 19","20 to 29 Years":"Young Adult","30 to 39 Years":"Adults","40 to 49 Years":"Adult","50 to 59 Years":"Adult","60 to 69 Years":"Senior","70 to 79 Years":"Senior","80 to 89 Years":"Senior"}
postal_loc = {"M2N":}

print("------------CSV Testing---------")
covid_cases = pd.read_csv("/Users/roshanram/Documents/DataMap/DataMap/e5bf35bc-e681-43da-b2ce-0242d00922ad.csv", header=None,low_memory=False,usecols=[3,4,5])[[3,4,5]]
covid_cases.dropna()
print(covid_cases)
covid_cases.insert(3,"Latitude","Fill In")
covid_cases.insert(4,"Longitude","Fill In")
covid_cases.replace(value=None, to_replace=age_cat,inplace=True)
st.write(covid_cases)