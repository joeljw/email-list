#!/usr/bin/env python


import csv
import sys
import os
import time

filename = sys.argv[1]
SENDMAIL = "/usr/sbin/sendmail" # sendmail location
FROM = "joeljw@mail.com"
SUBJECT = "New Login Info!"

with open(filename, 'rb') as csvfile:
     listreader = csv.reader(csvfile, delimiter=',')
     for row in listreader:
         TO = row[0]
         FNAME = row[2]
         PWD = row[3]
         TEXT = 'Hi '+ FNAME +'!\nVoting System errors, please use this new login information:\nWebsite = http://vote.ripplesolutions.com\nUsername = ' + TO +'\nPassword = ' + PWD

         # Prepare actual message

         message = """\
From: %s
To: %s
Subject: %s

%s
""" % (FROM,TO, SUBJECT, TEXT)
         print message
         # Send the mail

         p = os.popen("%s -t -i" % SENDMAIL, "w")
         p.write(message)
         status = p.close()
         time.sleep(2)
         if status:
             print "Sendmail exit status", status
