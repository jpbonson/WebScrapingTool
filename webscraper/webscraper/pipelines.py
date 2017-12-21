# -*- coding: utf-8 -*-

import json
import requests
import datetime
import logging
from scrapy.exceptions import DropItem


class APIPipeline(object):
    def process_item(self, item, spider):
        host = 'localhost'
        port = 8000
        outlet_id = 1

        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:
            data = dict(item)

            url = 'http://{host}:{port}/outlets/{outlet_id}/articles/'.format(
                host=host, port=port, outlet_id=outlet_id)
            payload = {
                'title': data['title'].encode('utf-8'),
                'content': data['description'].encode('utf-8'),
                'publication_date': APIPipeline.format_date(data['publish_date']),
                'outlet_id': outlet_id,
                'author_id': 1  # TODO
            }  # TODO: add more fields
            headers = {'content-type': 'application/json'}

            response = requests.post(url, data=json.dumps(payload), headers=headers)

            logging.debug('Data sent to API, response {r}'.format(r=str(response)))
        return item

    @staticmethod
    def format_date(original_date):
        simple_date = ' '.join(original_date.split()[1:4])
        formatted_date = datetime.datetime.strptime(simple_date, "%d %b %Y")
        return formatted_date.strftime("%Y-%m-%d")
