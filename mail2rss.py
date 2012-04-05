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


__verion__ = "0.01"

import sys
import email
import rss #http://znasibov.info/blog/post/rss-py.html
from datetime import datetime

f = sys.stdin
msg = email.message_from_file(f)
mail_content = msg.get_payload()
subject = msg.get('Subject')
f.close()


channel = rss.Channel('Testfeed', 'http://ktrask.de/test.rss', 'This is my simple test feed', generator = 'rss.py', pubdate = datetime.now(), language = 'de-DE')

item1 = rss.Item(channel, subject, '', mail_content, pubdate = datetime.now())

channel.additem(item1)
print(channel.toprettyxml())


