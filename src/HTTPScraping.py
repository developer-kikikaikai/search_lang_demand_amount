# coding: UTF-8
#参考:https://qiita.com/Azunyan1111/items/b161b998790b1db2ff7a
from bs4 import BeautifulSoup
import requests

class HTTPScraping:

	#singleton instance
	_instance = None

	@classmethod
	def get_instance(self):
		if not self._instance:
			self._instance = self()
		return self._instance

	def scraping(self, url, id):
		try:
			# get url
			html = requests.get(url).text.encode('utf-8')
			# BeautifulSoupで扱えるようにパースします
			soup = BeautifulSoup(html, "html.parser")
			# idの要素を表示
			return soup.select_one(f"#{id}").text
		except:
			return ""
