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
parser.add_argument('user', metavar="JENKINS_USER", help='your Jenkins username')
parser.add_argument('api_key', metavar='JENKINS_APIKEY', help='your Jenkins APIKEY')
parser.add_argument('url', metavar='BUILD_URL',  help='A specific Jenkins build url, like http://<jenkins>/job/<jobname>/42')
args = parser.parse_args()

build_url = args.url
username = args.user
api_key = args.api_key
build_api_url = '{}/api/json'.format(build_url)

m = re.match(".*/\d+/?", build_url)
if not m:
    print "Build URL must end in a number. It must be a link to a specific build!"
    sys.exit(-1)

print 'Jenkins build URL: {}'.format(build_url)

try:
    request = urllib2.Request(build_api_url)
    request.add_header('Authorization', b'Basic ' + base64.b64encode(username + b':' + api_key))
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
