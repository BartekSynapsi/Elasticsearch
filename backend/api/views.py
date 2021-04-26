from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
import requests
import json
from elasticsearch import Elasticsearch
from copy import deepcopy

elastic_client = Elasticsearch(hosts=['elasticsearch'])

base_search_param = {
  "from": 0,
  "size": 10,
  "query": {
    "match": {"title": ""}
  },
  "highlight" : {
    "pre_tags" : ["<b>"], "post_tags" : ["</b>"],
    "fields": {
      "*": {"number_of_fragments": 0}
    },
      "require_field_match" : False
    },
}

def select_search_param(data, base):
  search_param = deepcopy(base)
  search_param["from"] = data['from']
  search_param["query"]["match"]["title"] = data['query']
  
  if data['sort_by'] != 'elasticsearch':
    search_param['sort'] = [
      {
        "score": {
          "order": "desc"
        }
      }
    ]
  if data['fields'] == True:
    search_param['query'] = {"multi_match": {
      "query": data["query"],
      "fields": ["body", "title"]}}

  print(search_param)
  return search_param


@api_view(['POST'])
def elastisearch_query(request):
    data = request.data
    search_param = select_search_param(data, base_search_param)
    search_param = json.dumps(search_param, indent=3)
    response = elastic_client.search(search_param)
    return Response(response, status=status.HTTP_200_OK)



# def select_search_param(data):
#   if data['sort_by'] == 'elasticsearch':
#     search_param = {
#         "from": data['from'],
#         "size": 10,
#     "query" : {
#       "match": { "title": data['query'] }
#     },
#     "highlight" : {
#     "pre_tags" : ["<b>"], "post_tags" : ["</b>"],
#     "fields": {
#       "*": {"number_of_fragments": 0}
#     },
#     "require_field_match" : False
#     }
#   }
#   else:
#     search_param = {
#     "from": data['from'],
#     "size": 10, 
  #     "sort": [
  #       {
  #         "score": {
  #           "order": "desc"
  #         }
  #       }
  #     ], 
#     "query" : {
#       "match": { "title": data['query'] }
#     },
#     "highlight" : {
#     "pre_tags" : ["<b>"], "post_tags" : ["</b>"],
#     "fields": {
#       "*": {"number_of_fragments": 0}
#     },
#     "require_field_match" : False
#   }}
#   if data['fields'] == True:
#       query = {"multi_match": {
#       "query": data["query"],
#       "fields": ["body", "title"]
#     }}
#       search_param['query'] = query
#   return search_param
