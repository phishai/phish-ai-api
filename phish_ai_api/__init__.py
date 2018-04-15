#!/usr/bin/env python
import requests

ENDPOINT_URL = 'https://app.phish.ai/api/'


class ApiError(Exception):
    pass


class API(object):
    def __init__(self, api_key=None):
        self.api_key = api_key

    def scan_url(self, url):
        res = requests.post(ENDPOINT_URL + 'url/scan', data={'url': url}, headers={'Authorization': self.api_key})
        if res.status_code != requests.codes.ok:
            raise ApiError(res.text)
        return res.json()

    def get_report(self, scan_id):
        res = requests.get(ENDPOINT_URL + 'url/report?scan_id=' + scan_id, headers={'Authorization': self.api_key})
        if res.status_code != requests.codes.ok:
            raise ApiError(res.text)
        return res.json()