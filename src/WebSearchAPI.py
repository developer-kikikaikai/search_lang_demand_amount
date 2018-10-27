#検索API定義
class WebSearchAPI:
	#item向け
	TAG_DENOMINATOR='result_denominator'
	TAG_NUMERATOR='result_numerator'

	#public
	# 検索結果を取得する
	# @ret {'result_denominator', 'result_numerator'}
	def get_search_result(self, key_list):
		pass

	#public
	# 検索を行った対象名を取得する
	# @ret name
	def get_search_name(self):
		pass
