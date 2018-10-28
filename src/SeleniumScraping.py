# coding: UTF-8
#参考:https://qiita.com/Azunyan1111/items/b161b998790b1db2ff7a
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class SeleniumScraping:

	#singleton instance
	_instance = None

	def __init__(self):
		# ブラウザのオプションを格納する変数をもらってきます。
		options = Options()
		# Headlessモードを有効にする（コメントアウトするとブラウザが実際に立ち上がります）
		options.set_headless(True)
		# ブラウザを起動する
		self._driver = webdriver.Chrome(chrome_options=options)

	@classmethod
	def get_instance(self):
		if not self._instance:
			self._instance = self()
		return self._instance

	def scraping(self, url, id):
		try:
			# ブラウザでアクセス
			self._driver.get(url)
			# HTMLを文字コードをUTF-8に変換してから取得
			html = self._driver.page_source.encode('utf-8')
			# BeautifulSoupで扱えるようにパースします
			soup = BeautifulSoup(html, "html.parser")
			# idの要素を表示
			return soup.select_one(f"#{id}").text
		except:
			return ""
