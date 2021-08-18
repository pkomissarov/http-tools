# httptools

Usage: ```httpreq.py <url> [<sleeptime>] [<limit>]```

Usage example: ```httpreq.py https://google.com 0.1 1000```  
That means - send 1000 GET requests to https://google.com, sleeping 0.1 seconds beetween requests  
Default values: sleeptime = 1 sec, limit = 0 (unlimited)

Example of requests, with responses returning page with 200 code:
```
$ python3 httpreq.py https://www.google.com
200:[https://www.google.com/]
200:[https://www.google.com/]
```
Example of requests with all intermediate redirects (request and responses) before final 200 response (e.g. 301, 302 codes):
```
$ python3 httpreq.py https://www.google.com/mail
301:[https://www.google.com/mail] Location:[https://mail.google.com/mail/]
 `-> 302:[https://mail.google.com/mail/] Location:[https://accounts.google.com/ServiceLogin?service=mail&passive=true&rm=false&continue=https://mail.google.com/mail/&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1#]
      `-> 200:[https://accounts.google.com/ServiceLogin?service=mail&passive=true&rm=false&continue=https://mail.google.com/mail/&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1]
301:[https://www.google.com/mail] Location:[https://mail.google.com/mail/]
 `-> 302:[https://mail.google.com/mail/] Location:[https://accounts.google.com/ServiceLogin?service=mail&passive=true&rm=false&continue=https://mail.google.com/mail/&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1#]
      `-> 200:[https://accounts.google.com/ServiceLogin?service=mail&passive=true&rm=false&continue=https://mail.google.com/mail/&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1]
```
