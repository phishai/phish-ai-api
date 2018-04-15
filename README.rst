phish-ai-api
============
.. image:: https://img.shields.io/badge/License-MIT-blue.svg 
.. image:: https://img.shields.io/badge/python-2.7%2B%203.5%2B-blue.svg

Summary
-------
Official python API for Phish.AI public and private API to detect zero-day phishing websites

How it Works (TLDR)
-------------------
Essentially we have a very big computer vision database of known websites and their legitimate domains.
The API surf to a given website takes a screenshots of the website and then compare it with our database and if we detect that it is similar to a known website but hosted we classify it as malicious and classify the targeted brand (which website this site tries to mimic).

The Engine is in beta and doesn't protect all brands yet. we make the database bigger every day, if you believe your brand is not in our database and you want us to crawl it, just drop me a line at yp@phish.ai

Privacy Policy
--------------
The full privacy policy is at: https://www.phish.ai/phish-ai-privacy-policy/. By using the Public API you agree to our Privacy Policy and allow us to share your submission with the security community. If you want a Private API Key please contact us at info@phish.ai.

Useful resources
----------------
* UI Version: https://app.phish.ai
* Raw API Documentation: https://app.phish.ai/ (under documentation, "Thanks PyPi for not allowing minimum-cash sign")
* Official website: https://www.phish.ai
* Blog: https://www.phish.ai/blog

Installation
------------


.. code-block:: bash

   $ pip install phish-ai-api


Usage
-----


.. code-block:: python

 from __future__ import print_function
 from phish_ai_api import API

 ph = API(api_key='None or private api key you can request at info@phish.ai')
 res = ph.scan_url('https://google.com')
 print(res)
 print(ph.get_report(res['scan_id']))


Output
------


.. code-block:: json

 {"scan_id": "pQz7bGMwxgzGboNyX8cy"}


.. code-block:: json

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

Issues & Contributing
---------------------
Found a Bug/Have a feature request feel free to open an Issue and we will look into it. Cheers.
