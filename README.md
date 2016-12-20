# ripecheck
A short python status check for your RIPE Atlas probe

##Requirements
The script needs Python 3.x, it won't work with Python 2.x

##Usage
Crontab entry to run the script every hour at xx:00:
0 * * * * /usr/bin/python3.4 /home/markus/coding/ripecheck/ripecheck.py

Run the script manually, just replace the python version with your version number and the path with your path
python3.4 /path-to-script/ripecheck.py
