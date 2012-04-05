
# mail2rss.py

this is a simple mail2rss script, written in python3.
You can use it with procmail to generate a simple rss-feed with incoming mails.

## usage:
cat mail|./mail2rss.py > rssfeed.xml

## note:
this first version actually only creates an rss-file with the content of only one email.
