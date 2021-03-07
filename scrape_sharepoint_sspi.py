"""
    Web scrape a SharePoint to get a List.

    Combine the authentication from 'requests_negotiate_sspi' and the scraping tools of 'shareplum'
        - requests-negotiate-sspi allows for Single-Sign On HTTP Negotiate authentication using the requests library on Windows.
        - SharePlum is an easier way to work with SharePoint services.

    The authorization only works on Windows machines.
    It does not try to defeat the security. If you don't have authorization for the SharePoint, this won't help.
"""

import json
import csv
from pprint import pprint
from shareplum import Site
from requests_negotiate_sspi import HttpNegotiateAuth

server_root = 'https://hpi11.sharepoint.hp.com/teams/powercords'   # replace with URL for SharePoint

auth = HttpNegotiateAuth()
site = Site(server_root, auth=auth)

# show all lists on the site
sp_lists = site.GetListCollection()
pprint(sp_lists)
print()


# show the structure of a list.
example_sp_list = site.List(sp_lists[0]['Title'])
pprint(example_sp_list.views)
"""
Looks like this...
{'All Items': {'BaseViewID': '1',
               'ContentTypeID': '0x',
               'DefaultView': 'TRUE',
               'DisplayName': 'All Items',
               'ImageUrl': '/_layouts/15/images/generic.png?rev=23',
               'Level': '1',
               'Name': '{34E76D0C-2C54-4496-BE8B-6325B263F4D2}',
               'Type': 'HTML',
               'Url': '/teams/powercords/Lists/Country/AllItems.aspx'}}
"""


# # Below here is example code that is site specific.
# # Highly recommended to read the SharePlum documentation to write the queries.
#
# query = {"Where": [("Neq", "Conductors", "2")]}
# data = sp_list.GetListItems('All Items', query=query, row_limit=400)
# pprint(data, width=120)

# # dump to a json file
# with open('countries_3wire_db.json', 'w') as file:
#     json.dump(data, file)

# # dump to a csv file
# fn = []
# for row in data:
#     fn += row
# fieldnames = list(set(fn))

# with open('countries_3wire_db.csv', 'w', newline='') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#     writer.writeheader()
#     for row in data:
#         writer.writerow(row)