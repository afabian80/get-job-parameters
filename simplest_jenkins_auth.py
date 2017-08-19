import urllib2
import base64

username = 'akos'
password = '9ff85ba6e0beb00208ee84b998650cf8' # only a local api key, no harm
url = 'http://localhost:8080/job/packjob/4/api/json'

request = urllib2.Request(url)
request.add_header('Authorization', b'Basic ' + base64.b64encode(username + b':' + password))
result = urllib2.urlopen(request)

print result.read()
