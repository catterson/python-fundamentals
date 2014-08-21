__author__ = 'adcat'


## scrape the drudge report archives.
from lxml import html
import requests

#r = requests.get('http://www.drudgereportarchives.com/')
#print 'status:', r.status_code
# print 'initial text:', r.text[:4000]
#tree = html.fromstring(r.text)
#print tree.body.text_content()

url_DR = ['http://www.drudgereportarchives.com/data/2014/08/21/20140821_014042.htm',
          'http://www.drudgereportarchives.com/data/2014/08/21/20140821_014223.htm']

def save_web_to_file(url):
    '''Use requests to fetch url, then save to a file'''
    r = requests.get(url)
    strip_url = url.split('//')[1]
    filename = strip_url.replace('/', '_')
    with open(filename, mode = 'w') as outfile:
        outfile.write(r.text)


for curr_url in url_DR
    save_web_to_file(curr_url)
