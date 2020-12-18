import sys
import requests
import time

def str_response(r):
    #if 'Set-Cookie' in r.headers:
    #    r_cookies = " Cookies:[" + r.headers['Set-Cookie'] + "]"
    #else:
    r_cookies = ""
    if 'Location' in r.headers:
        r_location = " Location:[" + r.headers['Location'] + "]"
    else:
        r_location = ""
    return f"{r.status_code}:[{r.request.url}]{r_location}{r_cookies}"


# parse arguments or print usage help
if len(sys.argv) > 1:
    url = sys.argv[1]
else:
    print("   Usage: httpreq.py <url> [<sleeptime>] [<limit>]")
    print("   Example: httpreq.py https://google.com 0.1 1000")
    print("   means 1000 GET requests to https://google.com, waiting 0.1 sec beetween requests")
    print("   default sleeptime = 1 sec, default limit = 0 (unlimited)")
    exit()
if len(sys.argv) > 2:
    sleeptime = float(sys.argv[2])
else:
    sleeptime = 1
if len(sys.argv) > 3:
    limit = int(sys.argv[3])
    if limit > 0:
        nolimit = False
    else:
        nolimit = True
else:
    nolimit = True


# main cycle
c = 0
while nolimit or c < limit:
    r = requests.get(url)
    indent = ""
    if r.history:
        for h in r.history:
            print(f"{indent}{str_response(h)}")
            if indent == "":
                indent = " `-> "
            else:
                indent = "     " + indent
    print(f"{indent}{str_response(r)}")
    time.sleep(sleeptime)
    c = c + 1
