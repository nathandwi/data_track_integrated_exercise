import requests
import json
import os
import s3

def get_stations_info():
        url = f'https://geo.irceline.be/sos/api/v1/stations/?expanded=true'
        stations_data = requests.get(url).json()
        s3.write_to_s3()
        return stations_data

def get_categories_info():
        url = f'https://geo.irceline.be/sos/api/v1/categories/'
        categories_data = requests.get(url).json()
        s3.write_to_s3()

def get_timeseries_info(stations_data):
       for stat
       url = f"https://geo.irceline.be/sos/api/v1/timeseries/{timeseries_id}/getData?timespan=PT24H/{date}"

        
