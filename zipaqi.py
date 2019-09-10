#!/usr/bin/python
# AQI for zipcode CLI. ./zipaqi.py 90210 
# Gets AQI data from Airnow API. 

from __future__ import print_function
from datetime import date
from datetime import datetime
import calendar
import urllib, json
import sys, getopt

AIRNOWAPIKEY =""

def showaqi():
	aqiurl ="http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode="+zipcode+"&distance=10&API_KEY="+AIRNOWAPIKEY
	response = urllib.urlopen(aqiurl)
	data = json.loads(response.read())
	ResetText  = '\033[0m'
	
	for item in data:
        	if item['Category']['Number'] == 1:
                	TextColor = '\033[92m'
        	elif item ['Category']['Number'] == 2:
                	TextColor = '\033[93m'
        	elif item ['Category']['Number'] == 3:
                	TextColor = '\033[91m'
        	elif item ['Category']['Number'] == 4:
               		TextColor = '\033[91m'
        	elif item ['Category']['Number'] == 5:
                	TextColor = '\033[41m'
        	elif item ['Category']['Number'] == 6:
                	TextColor = '\033[41m'
        	else:
                	TextColor = ResetText
		print(TextColor + "{}\t{}\t{}".format(item['ParameterName'],item['AQI'],item['Category']['Name']) + ResetText)
	print ("Observed in {} aroud {}:00 on {}".format(item['ReportingArea'],item['HourObserved'],item['DateObserved']))

if len(sys.argv) == 1:
	print ("Please provide zip code 5 digit zip code ex: {} 90210".format(sys.argv[0]))
else:
	zipcode = sys.argv[1]
	showaqi()
