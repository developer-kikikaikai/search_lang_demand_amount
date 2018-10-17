#Google検索
import sys, os, re, nltk, urllib.parse
from WebSearchAPI import *
from Scraping import Scraping

class GoogleSearch(WebSearchAPI):

	BASEURL="https://www.google.co.jp/search?tbs=qdr:y&q="+urllib.parse.quote("プログラミング言語")
	BASEID="resultStats"

	#public
	# 検索結果を取得する
	# @ret {'result_denominator', 'result_numerator'}
	def get_search_result(self, key_list):
		result={}
		#全体検索
		result[WebSearchAPI.TAG_DENOMINATOR]=self._search_google("")
		
		#キー検索
		query_value=0
		for key in key_list:
			query_value += self._search_google("+"+key)
		result[WebSearchAPI.TAG_NUMERATOR]=query_value

		return result

	def _search_google(self, key):
		result_text = Scraping.scraping(self.BASEURL+key, self.BASEID)
		num_tokenizer = nltk.RegexpTokenizer(u'([0-9])')
		return int("".join(num_tokenizer.tokenize(result_text)))

	#public
	# 検索を行った対象名を取得する
	# @ret name
	def get_search_name(self):
		return "google"
