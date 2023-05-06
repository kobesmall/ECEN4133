#!/usr/bin/python3

import sys
import urllib.parse
import http.client
from pymd5 import md5, padding

##########################
# Example URL parsing code:
res = urllib.parse.urlparse('https://project1.ecen4133.org/test/lengthextension/api?token=41bd1ccd26a75c282922c2b39cc3bb0a&command=Test1')
# res.query returns everything after '?' in the URL:
assert(res.query == 'token=41bd1ccd26a75c282922c2b39cc3bb0a&command=Test1')

###########################
# Example using URL quoting
# This is URL safe: a URL with %00 will be valid and interpreted as \x00
assert(urllib.parse.quote('\x00\x01\x02') == '%00%01%02')

if __name__ == '__main__':
    if len(sys.argv) < 1:
        print(f"usage: {sys.argv[0]} URL_TO_EXTEND", file=sys.stderr)
        
        sys.exit(-1)

    # Get url from command line argument (argv)
    url = sys.argv[1]

#################################
# Your length extension code here
    
#url = "https://project1.ecen4133.org/kosm1438/lengthextension/api?token=d428efff11f787be7dae0da1821f1155&command=SprinklersPowerOn"

urlList = urllib.parse.urlparse(url).query.split("&")     # creates a list of the url divided by '&'



commands = urlList[1:]

length_of_m = len("&".join(commands)) + 8     # length of m (secret 8-byte password || the portion of the URL starting from the first command= )
token = urlList[0]

MD5ofm = token[6:]

bits = (length_of_m + len(padding(length_of_m*8)))*8 

h = md5(state = bytes.fromhex(MD5ofm), count = bits)     # setting the initial internal state of our MD5 function to MD5(m)
h.update("&command=UnlockSafes")                          # newcommand to unlock safe " x that is appended to m"
   
newtoken = "token=" + h.hexdigest()

#print(urlList[0])
#print(urllib.parse.quote(padding(length_of_m*8)))



url = urllib.parse.urlparse(url).scheme + "://" + urllib.parse.urlparse(url).netloc + urllib.parse.urlparse(url).path + "?" + newtoken + "&"+ "&".join(commands) + urllib.parse.quote(padding(length_of_m*8)) + "&command=UnlockSafes"

print (url)


parsed_url = urllib.parse.urlparse(url)
conn = http.client.HTTPSConnection(parsed_url.hostname, parsed_url.port)
conn.request("GET", parsed_url.path + "?" + parsed_url.query) 
print(conn.getresponse().read())

