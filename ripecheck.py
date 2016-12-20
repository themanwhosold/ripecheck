#!/usr/bin/python
# Skript um sicherzustellen, dass meine RIPE Probe online ist...
# Script to make sure, your ripe probe is online
# benötigt Python >= 3
# requires python >= 3

import configparser
from urllib.request import urlopen
import json
from subprocess import Popen, PIPE 
import os
import argparse #Add User-friendly command line interface

userHome = os.getenv('HOME')

# Parse command line arguments

commandLineParser = argparse.ArgumentParser(description='Script to check status of your Atlas RIPE probe')
commandLineParser.add_argument('-m','--mail',type=str,help='A mail addy to send the status mails to', default = '')
configFile = userHome + '/ripecheck.config'
commandLineParser.add_argument('-c','--config',type=str,help='Path to config file, if this parameter is not given, the config file is ~/ripecheck.config',default = '')

args = commandLineParser.parse_args()

# Do some stuff with the parsed command line arguments
# To do: add some checks if the given config file path is valid
if args.config == '':
	configFile = configFile
else:
	configFile = args.config

# Parse config file 
config = configparser.ConfigParser()
config.read(configFile)

# If there's an command-line argument for mail, don't check the config file 
# To do: Verify format of mail address, given in args.mail and configFile perhaps a function would be a nice way to do so
if args.mail == '':
	mail = config['Basic']['mail']
else:
	mail = args.mail

print (configFile)
print (mail)

probeNr = config['Basic']['probeNr']
probeUrl = 'https://atlas.ripe.net/api/v2/probes/' + probeNr + '?format=json'

# URL for use of Telegram
telegramUrl = 'https://api.telegram.org/' + botID + '/sendMessage?chat_id=' + chatID + '&text="'

#Check the RIPE Atlas probe

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
