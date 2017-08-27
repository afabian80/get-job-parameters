import argparse
import urllib2
import json

class UrlReader():
    def read(self, url):
        request = urllib2.Request(url)
        result = urllib2.urlopen(request)
        return result.getcode(), result.read()

# parser = argparse.ArgumentParser(description='Get build parameters from a Jenkins build URL.')
# parser.add_argument('url', metavar='BUILD_URL',  help='A specific Jenkins build url, like http://<jenkins>/job/<jobname>/42')
# args = parser.parse_args()

if __name__ == '__main__':
    url_reader = UrlReader()
    code, result = url_reader.read('http://localhost:8080/job/stagingjob/1/api/json')
    print code
    print result
