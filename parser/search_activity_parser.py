from utils import *
from lxml import etree
import logging

import csv


tree = etree.parse(SEARCH_ACTIVITY_HTML_PATH, parser=etree.HTMLParser(encoding='UTF-8'))
root = tree.getroot()

a1 = tree.xpath('//div[@class="content-cell mdl-cell mdl-cell--6-col mdl-typography--body-1"]')


def parse_one_record(record):
    try:
        record_action = record.text
        record_url = record[0].get('href')
        record_info = record[0].text
        record_time = record[1].tail
        # print(record_action, record_url)
        # print("%s | %s | %s " % (record[0].tag, record[0].text, record[0].tail))
        # print("%s | %s | %s " % (record[1].tag, record[1].text, record[1].tail))

        # if "Visited" in record_action:
        #     return "Visited"
        # elif "Searched for" in record_action:
        #     return "Search"
        # else:
        #     logging.error("Wrong record_action : "+record_action)
        #     return ""
        return record_time, record_action, record_info
    except Exception as err:
        logging.error(err)
        # return None


counter = 0
result = [["TIME","ACTION","INFO"]]
for ele in a1:
    counter += 1
    try:
        time, action, info = parse_one_record(ele)
        result.append([time,action,info])
    except Exception as err:
        logging.error(err)
        continue

with open(SEARCH_ACTIVITY_CSV_PATH, 'w',encoding='utf_8_sig', newline='') as output_file:
    writer = csv.writer(output_file)
    writer.writerows(result)
    # output_file.writelines(result)
