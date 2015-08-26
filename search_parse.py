#!/usr/bin/python

import sys
#sys.path.append('./Lib')

import re
#import ast
#from json import load, dumps
# Custom parser for search results


#@outputSchema("user_id: chararray, posted_time: double, query_string: chararray")
@outputSchema("user_id: chararray, posted_time: double")
def parse_search(search_result):

    #search_stringified = '%s' % search_result

    temp = json.loads(search_result)

    user_id = temp['user_id']
    posted_time = temp['posted_time']

    #search_dict = dict(search_result)
    #user_id = str(search_dict['user_id'])
    #posted_time = float(search_dict['posted_time'])

    #search_cleaned = search_stringified.replace('false', '"false"')
    #search_dict_2 = ast.literal_eval(search_cleaned)
    #query_string = search_dict_2['query']['query']['bool']['must'][0]['query_string']['query']

    return user_id, posted_time


