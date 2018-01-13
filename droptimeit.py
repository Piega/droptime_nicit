#! /usr/bin/python
import time
import datetime
import sys
import os
import urllib.request
import re

tomorrow = datetime.date.today() + datetime.timedelta(days=1)

nove = "http://www.nic.it/droptime/files/{0}".format(tomorrow.strftime('%Y%m%d09.txt')) 
sedici = "http://www.nic.it/droptime/files/{0}".format(tomorrow.strftime('%Y%m%d16.txt'))


i = [ nove, sedici ]
for c in i:
	txt = urllib.request.urlopen( c )
	txt = txt.read()
	txt = txt.decode()
	txt = txt.split()
	r = re.compile(".{3,6}\.it")  # domini da 3 a 6 caratteri
	txt = filter(r.match, txt)
	txt = list(txt)
	print ("--- dropfile "+ c )
	print ('\n'.join(list(sorted(txt))))
	print ("---------------------------------------------------------------------------")


