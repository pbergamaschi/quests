import re
import linkGrabber
import pprint

links = linkGrabber.Links('http://www.xkcd.com/')
gb = links.find(limit=4,duplicates=False,pretty=True)
print(gb)
