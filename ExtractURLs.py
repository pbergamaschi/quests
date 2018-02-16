import re
import linkGrabber
import pprint

links = linkGrabber.Links('http://www.xkcd.com/')
gb = links.find(limit=4,duplicates=False,pretty=True)

# I think i need some regular expressions under here but I'm still trying to
# learn them... But this works to get the URLs
