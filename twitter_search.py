#!/usr/bin/env python

__version__ = '0.3'

import datetime
import json
import os
import sys
import urllib

path = os.path.realpath(__file__).replace(sys.argv[0], '')
path = '/home/hammertime/hcf/'

keys = ('from_user', 'created_at', 'text', 'to_user')
base_url = 'http://search.twitter.com/search.json'

def strip_unicode(text):
    """Stupid, stupid function to strip non-ascii characters from a unicode string"""
    ascii = [chr(x) for x in range(1, 129)]
    return ''.join([x for x in text if x in ascii])

if __name__ == '__main__':
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
                this_dict = {}
                for key in keys:
                    this_dict[key] = ''
                for key in result.keys():
                    if key in keys:
                        this_dict[key] = result[key].replace('\n', '').replace('\r', '')
                    
                csv.append('\t'.join(
                    [this_dict[k] if this_dict[k] != None else '' for k in keys])
                )
        except:
            print 'Error:\n\n'
            print sys.exc_info()[0]
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
    output = strip_unicode(output)
    # print output # test only
    
    filename = '%stwitter_search_%s_%s.tsv' % (path, '_'.join(args[1:]), unicode(datetime.datetime.now())[:-7])
    
    with open(filename, 'w') as file:
        
        file.write(output)
        
        print 'File saved as %s' % (filename)
    
    print 'Goodbye.'



