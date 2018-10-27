#!/usr/bin/python3.6
#QiitaAPIをロード
import sys, os, json
#multi process
import multiprocessing
import threading
from concurrent.futures import *
from WebSearchAPI import *
sys.path.append('../libs/src') 
from QiitaAPIMain import QiitaAPIMain
from QiitaAPI import QiitaAPI

def call_items(obj):
	print("call " + str(obj['data']['show']['item']['page']))
	result=QiitaAPIMain(['dummy',obj,'items']).action()
	return result

class QiitaSearch(WebSearchAPI):

	#public
	# 検索結果を取得する
	# @ret {'result_denominator', 'result_numerator'}
	def get_search_result(self, key_list):
		result={}
		#全体検索
		self._search_qiita()
		len(self.result)

		result[WebSearchAPI.TAG_DENOMINATOR]=len(self.result)

		#キー検索
		query_value=0
		for key in key_list:
			for item_val in self.result.values():
				#tagが{"name":xxx, "versions":[]}のリストなのでめんどい
				for tag_val in item_val[QiitaAPI.ITEM_TAGS]:
					if key in tag_val["name"]:
						query_value+=1
						break

		result[WebSearchAPI.TAG_NUMERATOR]=query_value
		return result

	def _search_qiita(self):
		with open('qiita_setting.json') as f:
			conf=json.loads(f.read())
		self.result={}
		with ThreadPoolExecutor(max_workers=5) as executor:
			future_to_url={}
			#スレッド処理
			for n in range(0,5):
				future_to_url[executor.submit(call_items, conf)] = n
				conf['data']['show']['item']['page']+=10
			#結果格納
			for future in as_completed(future_to_url):
				self.result.update(future.result())

	#public
	# 検索を行った対象名を取得する
	# @ret name
	def get_search_name(self):
		return "qiita"
