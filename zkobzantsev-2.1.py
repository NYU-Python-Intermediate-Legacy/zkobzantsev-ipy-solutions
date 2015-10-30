#!/usr/bin/python

import os
import sys

sendmail_prog = '/usr/sbin/sendmail'

required_args = set(['to', 'from'])
valid_args = set(['to', 'from', 'subject', 'body'])

#print sys.argv

args = sys.argv[1:]
#print args

email_dict = {}
for el in args:
   key = el.split('=')[0]
   val = el.split('=')[1]
   #print key, val
   email_dict[key] = val

print email_dict

set_field_input = set(email_dict.keys())
#print set_field_input

required_valid = required_args.intersection(set_field_input)
#print required_valid

for el in required_args:
   if el in email_dict:
      print 'required argument provided'
   else:
      print 'required argument ' + el + ' is missing'

for key in email_dict:
   if key in valid_args:
      print 'key is valid'
   else:
      print 'key is not valid'

header = """{}: {from}
{}: {to}
{}: {subject}"""

#new_header = header.format(**email_dict) 
#print new_header
      
