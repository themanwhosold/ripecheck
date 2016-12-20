#!/usr/bin/python
# Skript um sicherzustellen, dass meine RIPE Probe online ist...
# Script to make sure, your ripe probe is online
# braucht Python Version 3
# requires python >= 3

import configparser
from urllib.request import urlopen
import json
from subprocess import Popen, PIPE 
import os
import argparse #Add User-friendly command line interface

userHome = os.getenv('HOME')
configFile = userHome + '/ripecheck.config'
config = configparser.ConfigParser()
config.read(configFile)
mail = config['Basic']['mail']
probeNr = config['Basic']['probeNr']
probeUrl = 'https://atlas.ripe.net/api/v2/probes/' + probeNr + '?format=json'

# Evtl. machts Sinn JSON zu benutzen https://atlas.ripe.net/api/v2/probes/29535?format=json
response = urlopen(probeUrl).read()
content = response
json_data = json.loads(response.decode('utf-8'))
connectionState = json_data['status']['name']
if connectionState == 'Connected': 
	#print ("OK")
	mail = Popen(["mail","-s","RIPE Atlas verbunden",mail],stdin=PIPE,stdout=PIPE)
	mail.communicate(response)
else:
	#print ("Fehler")
	mail = Popen(["mail","-s","RIPE Atlas nicht mehr verbunden",mail],stdin=PIPE,stdout=PIPE)
	mail.communicate(response)
#print (content)
#print (json_data['status']['name'])
