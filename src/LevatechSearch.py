#レバテック検索
import sys, os, re, nltk
from WebSearchAPI import *
from SeleniumScraping import SeleniumScraping

class LevatechSearch(WebSearchAPI):

	BASEURL="https://freelance.levtech.jp/project/search/"
	BASEID="searchCount"

	#public
	# 検索結果を取得する
	# @ret {'result_denominator', 'result_numerator'}
	def get_search_result(self, key_list):
		result={}
		#全体検索
		result[WebSearchAPI.TAG_DENOMINATOR]=self._search(self.BASEURL)
		
		#キー検索
		query_value=0
		for key in key_list:
			query_value += self._search_with_key(key)
		result[WebSearchAPI.TAG_NUMERATOR] = query_value

		return result

	def _search_with_key(self, key):
		return self._search(self.BASEURL+"?keyword="+key)

	def _search(self, url):
		result = SeleniumScraping.get_instance().scraping(url, self.BASEID)
		return int(result)

	#public
	# 検索を行った対象名を取得する
	# @ret name
	def get_search_name(self):
		return "levatech"
