# -*- coding: utf-8 -*-

from scrapy.exceptions import DropItem
from scrapy import log
import json
import requests


class APIPipeline(object):
    def process_item(self, item, spider):
        outlet_id = 1

        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:
            data = dict(item)

            url = 'http://localhost:8000/outlets/' + str(outlet_id) + '/articles/'  # TODO
            payload = {
                'title': data['title'].encode('utf-8'),
                'content': data['description'].encode('utf-8'),
                'publication_date': '2001-12-30',  # TODO
                'outlet_id': outlet_id,
                'author_id': 1  # TODO
            }  # TODO: add more fields
            headers = {'content-type': 'application/json'}

            response = requests.post(url, data=json.dumps(payload), headers=headers)

            log.msg("Data sent to API, response: " + str(response),
                    level=log.DEBUG, spider=spider)
        return item
