# Use this script to print out the actual parameters
# of a specific Jenkins build.
# Pass the build URL as a parameter.

import urllib2
import json
import argparse
import re
import sys

parser = argparse.ArgumentParser(description='Get build parameters from a Jenkins build URL.')
parser.add_argument('build_url', metavar='URL',
    help='a specific Jenkins job build url, like http://<jenkins>/job/<jobname>/42')
args = parser.parse_args()

m = re.match(".*/\d+/?", args.build_url)
if not m:
    print "Build URL must end in a number. It must be a link to a specific build!"
    sys.exit(-1)

print 'Jenkins build URL: {}'.format(args.build_url)

try:
    json_response = urllib2.urlopen('{}/api/json'.format(args.build_url))
    build_api_json = json.load(json_response)
    build_action = build_api_json[u'actions'][0]

    if u'parameters' in build_action:
        for param in build_action[u'parameters']:
            print "{} = {}".format(param[u'name'], param[u'value'])
    else:
        print "No parameters"

except urllib2.HTTPError as e:
    print 'Build URL not found: {}'.format(args.build_url)
    print e
except Exception as e:
    print type(e)
    print e.args
    print e
