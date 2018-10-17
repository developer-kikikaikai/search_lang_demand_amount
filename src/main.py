import sys, json
from decimal import Decimal
from search_lang_demand_amount import slda_main
from WebSearchAPI import WebSearchAPI

def main(args):
	LIST={
			"google":"一般目線",
			"levatech":"業界目線",
			"qiita":"趣味目線",
		}
	result=slda_main(args)
	print("あなたのプログラム超人パワーを測定します。")
	for key, value in LIST.items():
		result_val=calculate_power(result[key])
		print(value + ":" +str(result_val) + "万パワー")

def calculate_power(result):
	return Decimal((result[WebSearchAPI.TAG_NUMERATOR]*1000)/result[WebSearchAPI.TAG_DENOMINATOR]).quantize(Decimal('1.00'))

if __name__ == '__main__':
	main(sys.argv)
