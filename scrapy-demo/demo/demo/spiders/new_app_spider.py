#coding:utf-8
# !/usr/bin/env python
# -*- coding: UTF-8 -*-
# Author:  chendezhi@chandashi.com
# Purpose:  
# Created: 02/11/2016


from scrapy.http import Request
from scrapy.spiders import Spider
import json
COUNTRY='cn'


class NewAppSpider(Spider):
    name = "new_app"
    start_urls = [
        'https://itunes.apple.com/%s/rss/newapplications/limit=100/json' % COUNTRY
    ]

    def parse(self, response):
        j = json.loads(response.body)
        entry = j['feed']['entry']
        print response.url, entry
