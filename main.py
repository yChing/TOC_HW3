import urllib
from sgmllib import SGMLParser

url = 'http://myweb.ncku.edu.tw/~f74002086/a.json'
fileobj = urllib.urlopen(url)
print fileobj.read()