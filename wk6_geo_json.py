# Chapter 13 Assignment: Calling a JSON API

#Welcome Luai Ghazali from Using Python to Access Web Data

# In this assignment you will write a Python program somewhat similar to
# http://www.pythonlearn.com/code/geojson.py. The program will prompt for a
# location, contact a web service and retrieve JSON for the web service and
# parse that data, and retrieve the first place_id from the JSON. A place ID is
# a textual identifier that uniquely identifies a place as within Google Maps.

# API End Points

# To complete this assignment, you should use this API endpoint that has a
# static subset of the Google Data:

# http://py4e-data.dr-chuck.net/geojson?

# This API uses the same parameters (sensor and address) as the Google API.
# This API also has no rate limit so you can test as often as you like. If you
# visit the URL with no parameters, you get a list of all of the address values
# which can be used with this API.

# To call the API, you need to provide a sensor=false parameter and the address
# that you are requesting as the address= parameter that is properly URL encoded
# using the urllib.urlencode() fuction as shown in
# http://www.pythonlearn.com/code/geojson.py

# Test Data / Sample Execution

# You can test to see if your program is working with a location of "South
# Federal University" which will have a place_id of
# "ChIJJ8oO7_B_bIcR2AlhC8nKlok".
'''
$ python solution.py
Enter location: South Federal University
Retrieving http://...
Retrieved 2101 characters
Place id ChIJJ8oO7_B_bIcR2AlhC8nKlok
'''
# Turn In

# Please run your program to find the place_id for this location:
'University of Mumbai'
# Make sure to enter the name and case exactly as above and enter the place_id
# and your Python code below. Hint: The first seven characters of the place_id
# are "ChIJERx ..."

# Make sure to retreive the data from the URL specified above and not the normal
# Google API. Your program should work with the Google API - but the place_id
# may not match for this assignment.

from urllib.parse import urlencode
from urllib.request import urlopen
import json

# serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
serviceurl = 'http://py4e-data.dr-chuck.net/geojson?'

while True:
    address = input('Enter location: ')
    if len(address) < 1: break
    url = serviceurl + urlencode({'address': address})
    print('Retrieving ',url)
    url_handle = urlopen(url)
    data = url_handle.read()
    print('Retrieved',len(data),'characters')
    json_data = json.loads(data)    
    print('Place id',json_data['results'][0]['place_id'])