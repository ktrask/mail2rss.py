#!/usr/bin/env python


__license__ = """
Copyright (C) 2012 <Heinrich Schmidt>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""


__version__ = "0.02"

import sys
import email
import rss #http://znasibov.info/blog/post/rss-py.html
from datetime import datetime
import pickle
import poplib
import re
#import unicode

mailBox = poplib.POP3('pop3.example.com')
mailBox.user('user')
mailBox.pass_('password')

feedTitle = "Testfeed"
feedURL   = "http://example.com/test.rss"
feedDiscr = "This is my simple test feed"
feedLang  = "de-DE"

numMessages = len(mailBox.list()[1])
#ll = 0
#ss = ""
#  for j in ll:
#    #ss = re.sub("xb'","",j.toString)
#    ss += j.decode("utf-8")
#    print(j)

#print(ll)
f = sys.stdin
#msg = email.message_from_file(f)]
f.close()

#try:
#  pickleFile = open("object.dump", 'rb')
#except: 
channel = rss.Channel(feedTitle, feedURL, feedDiscr, generator = 'rss.py', pubdate = datetime.now(), language = feedLang)
#else:
#  channel = pickle.load(pickleFile)
#  pickleFile.close()

for i in range(numMessages):
  mailbytes = mailBox.retr(i+1)[1]
  mail = b'\n'.join(mailbytes)
  msg = email.message_from_bytes(mail)
  mail_content = msg.get_payload(decode=1)
  subject = msg.get('Subject')
  item = rss.Item(channel, subject, '', mail_content.decode(), pubdate = datetime.now())
  channel.additem(item)


mailBox.quit()

print(channel.toprettyxml())

pickleFile = open("object.dump", 'wb')
ll = pickle.dumps(channel)
pickleFile.write(ll)
pickleFile.close()
