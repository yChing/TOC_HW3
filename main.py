# coding=utf-8
import urllib
import json
import sys # command line input | python main.py arg1 arg2 arg3
import re

#print 'Number of arguments: ',len(sys.argv),'arguments'
url = sys.argv[1]
section=sys.argv[2] 
road=sys.argv[3]
year=sys.argv[4]

page = urllib.urlopen(url)
#print page.read()

localpage = json.load(page,"utf-8")  #json into python list(dictionary)
#print json.dumps(localpage,ensure_ascii=False, indent=1)
#print localpage
m = re.search("楊梅市", localpage) 
if m:  
    print m.group(0), m.group(1)  
else:  
    print 'not search' 
