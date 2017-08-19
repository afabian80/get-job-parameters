# Use this script to print out the actual parameters
# of a specific Jenkins build.
# Pass the build URL as a parameter.

import urllib2
import json
import argparse
import re
import sys
import base64

parser = argparse.ArgumentParser(description='Get build parameters from a Jenkins build URL.')
parser.add_argument('build_url', metavar='URL',
    help='a specific Jenkins job build url, like http://<jenkins>/job/<jobname>/42')
args = parser.parse_args()

build_url = args.build_url
build_api_url = '{}/api/json'.format(build_url)

m = re.match(".*/\d+/?", build_url)
if not m:
    print "Build URL must end in a number. It must be a link to a specific build!"
    sys.exit(-1)

print 'Jenkins build URL: {}'.format(build_url)

username = 'akos'
password = '9ff85ba6e0beb00208ee84b998650cf8' # only a local api key, no harm commiting it

try:
    request = urllib2.Request(build_api_url)
    request.add_header('Authorization', b'Basic ' + base64.b64encode(username + b':' + password))
    result = urllib2.urlopen(request)
    build_api_json = json.load(result)
    build_action = build_api_json[u'actions'][0]

    if u'parameters' in build_action:
        for param in build_action[u'parameters']:
            print "{} = {}".format(param[u'name'], param[u'value'])
    else:
        print "No parameters"

except urllib2.HTTPError as e:
    print 'Build URL not found: {}'.format(build_url)
    print e
except Exception as e:
    print type(e)
    print e.args
    print e
