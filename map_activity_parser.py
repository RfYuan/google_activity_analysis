from utils import *
from lxml import etree
import re

tree = etree.parse(MAP_ACTIVITY_HTML_PATH, parser=etree.HTMLParser(encoding='UTF-8'))
root = tree.getroot()

a1 = tree.xpath('//div[@class="content-cell mdl-cell mdl-cell--6-col mdl-typography--body-1"]')


# for a in a1:
#     print(''.join(a.itertext()).strip())


# print(etree.tostring(a1[0]))
def get_location(gmap_url):
    ADDRESS_LOOK_UP_PATTERN = r".*(?<=\/place\/)([^\/]*)\/\@([^\/]*)"
    re_match = re.match(ADDRESS_LOOK_UP_PATTERN, gmap_url)
    if re_match:
        return re_match.group(1), re_match.group(2)
    else:
        return "Not found place", "0,0"


# TODO: finish this method
def parse_one_record(record):
    try:
        # record action
        record_action = record.text
        address_url = record[0].get('href')
        print(record_action)
        # action = record[0].text
        # print(action)
        # print(''.join(record[0].itertext()).strip())
        # print(record[0].tag, record[0].text, record[0].tail)
        print(address_url)
        # for i in record:
        print("%s | %s | %s " % (record[0].tag, record[0].text, record[0].tail))

        if record_action is None:
            # view somewhere
            view_action = record[0].text
            if "Viewed area" in view_action:
                # viewed
                return "Viewed Area"
            else:
                place_name, place_location = get_location(address_url)
                print(place_name, place_location)
                return "Viewed Place"
        elif "Searched" in record_action:
            # searched for a place
            pass
        elif "Directions to" in record_action:
            # search direction
            pass
        elif "Used Maps" in record_action:
            # use map, do nothing
            pass

    except RuntimeError as err:
        print(err)
        # return None


counter = 0
for ele in a1:
    counter += 1
    parse_one_record(ele)

    print()
    if counter > 50:
        break
