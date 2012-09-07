#!/usr/bin/env python

__version__ = 0.1

import datetime
import json
import os
import sys
import urllib

keys = ('from_user', 'from_user_name', 'created_at', 'text', 'to_user')
base_url = 'http://search.twitter.com/search.json'

def timestamp_string():
    return str(datetime.datetime.now())[:-7].replace(' ', '_').replace(':', '_')

if __name__ == '__main__':

    filename = sys.argv[0]
    if filename[:2] == './': filename = filename[2:]
    path = os.path.realpath(__file__).replace(filename, '')
    
    if path[-1] != '/': path = '%s/' % (path)

    args = sys.argv
    if len(args) < 2:
        print 'Keyword needed.'
        sys.exit()
        
    q = urllib.quote_plus(' '.join(args[1:]))
    
    url = '%s?q=%s' % (base_url, q)

    csv = []
    csv.append('\t'.join(keys))
    
    keep_going = True
    while keep_going == True:
    
        print 'Fetching %s...' % (url)
    
        response = urllib.urlopen(url)
        page = unicode(response.read(), 'utf8')
        obj = json.loads(page)
        
        try:
            results = obj['results']
            for result in results:
                csv.append('\t'.join(
                    [unicode(result[k]) if result[k] != None else '' for k in keys])
                )
        except:
            print 'HTTP request failed:\n\n'
            print page
            keep_going = False

        try:
            url = '%s%s' % (base_url, obj['next_page'])
        except:
            print 'Last page'
            print
            keep_going = False
            
    output = '\n'.join(csv)
    output = output.encode('utf8')
    
    filename = '%stwitter_search_%s_%s.tsv' % (path, '_'.join(args[1:]), timestamp_string())
    
    with open(filename, 'w') as file:
        file.write(output)
        print 'File saved as %s' % (filename)
    
    print 'Goodbye.'
