# -*- coding: utf-8 -*-

import os
import json
import requests
import datetime
import logging
from collections import defaultdict
from scrapy.exceptions import DropItem


class APIPipeline(object):
    report = {
        'total': 0,
        'invalid': 0,
        'valid': 0,
        'status': defaultdict(int),
        'status_text': defaultdict(int)
    }

    def process_item(self, item, spider):
        if os.environ.get('ENV_NAME') == 'prod':
            host = 'powerful-fjord-44213.herokuapp.com'
            port = 80
        else:
            host = 'localhost'
            port = 8000
        outlet_id = 1
        APIPipeline.report['total'] += 1

        valid = True
        for data in item:
            if not data:
                valid = False
                APIPipeline.report['invalid'] += 1
                raise DropItem("Missing {0}!".format(data))
        if valid:
            APIPipeline.report['valid'] += 1

            data = dict(item)

            url = 'http://{host}:{port}/v1/outlets/{outlet_id}/articles/'.format(
                host=host, port=port, outlet_id=outlet_id)
            payload = {
                'title': data['title'],
                'link': data['link'],
                'content': data['description'],
                'publication_date': APIPipeline.format_date(data['publish_date']),
                'tags': data['categories'],
                'outlet_id': outlet_id,
                'author': data['author']
            }
            headers = {'content-type': 'application/json'}
            response = requests.post(url, data=json.dumps(payload), headers=headers)

            APIPipeline.report['status'][response.status_code] += 1
            if response.status_code != 201:
                APIPipeline.report['status_text'][response.text] += 1

            logging.debug('Data sent to API, response {0}'.format(str(response)))

        logging.debug('\n\n\nAPI report: {0}\n\n\n'.format(str(APIPipeline.report)))
        return item

    @staticmethod
    def format_date(original_date):
        simple_date = ' '.join(original_date.split()[1:4])
        formatted_date = datetime.datetime.strptime(simple_date, "%d %b %Y")
        return formatted_date.strftime("%Y-%m-%d")
