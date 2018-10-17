import sys, json
from WebSearchGenerator import WebSearchGenerator

def slda_main(args):
	apis=WebSearchGenerator.get_web_search_apis()
	result={}
	for api in apis:
		result[api.get_search_name()]=api.get_search_result(json.loads(args[1]))
	return result
