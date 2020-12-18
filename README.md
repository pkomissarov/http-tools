# httptools

Usage: ```httpreq.py <url> [<sleeptime>] [<limit>]```

Example: ```httpreq.py https://google.com 0.1 1000```  
which means send 1000 GET requests to https://google.com, sleeping 0.1 sec beetween requests

Defaults: sleeptime = 1 sec, limit = 0 (unlimited)
