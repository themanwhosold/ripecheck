# ripecheck
A short python status check for your RIPE Atlas probe

##Requirements
The script needs Python 3.x, it won't work with Python 2.x

##Usage
Crontab entry to run the script every hour
* */1 * * * /usr/bin/python3.4 /home/markus/coding/ripecheck/ripecheck.py

python3.4 ripecheck.py
