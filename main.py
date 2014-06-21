import urllib
url = 'http://www.datagarage.io/api/5365dee31bc6e9d9463a0057'
fileobj = urllib.urlopen(url)
print fileobj.read()