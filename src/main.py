import sys, json
from WebSearchGenerator import WebSearchGenerator

def main(args):
	apis=WebSearchGenerator.get_web_search_apis()
	result={}
	for api in apis:
		result[api.get_search_name()]=api.get_search_result(["Python"])
	print(json.dumps(result))

if __name__ == '__main__':
	main(sys.argv)
