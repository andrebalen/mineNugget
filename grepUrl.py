import re
import urllib2
stuff = urllib2.urlopen('http://python.org').read()  # stuff will contain the *entire* page

# Replace the string Python with your desired regex
results = re.findall('(Python)',stuff)

for i in results:
    print i
