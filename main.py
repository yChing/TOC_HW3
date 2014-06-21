import urllib
url = 'http://api.geonames.org/citiesJSON?north=44.1&south=-9.9&east=-22.4&west=55.2&lang=de&username=demo'
fileobj = urllib.urlopen(url)
print fileobj.read()