# ripecheck
A short python status check for your RIPE Atlas probe

##Requirements
* Python >= 3.x, it won't work with Python 2.x
* Telepot (pip install telepot)

##Usage
Crontab entry to run the script every hour at xx:00:

0 * * * * /usr/bin/python3.4 <path-to-script>/ripecheck.py

Run the script manually, just replace the python version with your version number and the path with your path

python3.4 /<path-to-script>/ripecheck.py

or
 
python3.4 /<path-to-script>/ripecheck.py 2>&1> /dev/null

if you don't want to see the output of the script
