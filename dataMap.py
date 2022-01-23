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

covid_cases = pd.read_csv("/Users/roshanram/Documents/DataMap/DataMap/e5bf35bc-e681-43da-b2ce-0242d00922ad.csv", header=None,low_memory=False,usecols=[3,4,5])[[3,4,5]]
print(covid_cases)
