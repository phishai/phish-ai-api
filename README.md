## phish-ai-api
![](https://img.shields.io/badge/License-MIT-blue.svg)
![](https://img.shields.io/badge/python-2.7%2B%203.5%2B-blue.svg)

### Summary
Official python API for Phish.AI public and private API to detect zero-day phishing websites

TLDR of how it works: Essentially we have a very big computer vision database of known websites and their legitimate domains.
The API surf to a given website takes a screenshots of the website and then compare it with our database and if we detect that it is similar to a known website but hosted we classify it as malicious and classify the targeted brand (which website this site tries to mimic).

The Engine is in beta and doesn't protect all brands yet. we make the database bigger every day, if you believe your brand is not in our database and you want us to crawl it, just drop me a line at yp@phish.ai

There is a UI version of this API at [https://app.phish.ai](https://app.phish.ai) and documentation for the raw api at [https://app.phish.ai/#/documentation](https://app.phish.ai/#/documentation)

You can find more info at our [website](https://www.phish.ai) and (blog)[https://www.phish.ai/blog]:


### Installation
```bash
pip install phish-ai-api
```

### Usage
```python
from __future__ import print_function
from phish_ai_api import API

ph = API(api_key='None or private api key you can request at info@phish.ai')
res = ph.scan_url('https://google.com')
print(res)
print(ph.get_report(res['scan_id']))
```

### Output
```json
{"scan_id": "pQz7bGMwxgzGboNyX8cy"}
```
```json
{"domain": "google.com",
 "ip_address": "74.125.124.113",
 "iso_code": "US",
 "status": "completed",
 "target": "Google",
 "time": "2018-04-15T07:27:37.860Z",
 "title": "google",
 "tld": "com",
 "url": "http://google.com",
 "user_agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/67.0.3391.0 Safari/537.36",
 "user_email": "api",
 "verdict": "clean"}
```

### Issues & Contributing

