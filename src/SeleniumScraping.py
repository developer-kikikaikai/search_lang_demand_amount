# coding: UTF-8
#�Q�l:https://qiita.com/Azunyan1111/items/b161b998790b1db2ff7a
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class SeleniumScraping:

	#singleton instance
	_instance = None

	def __init__(self):
		# �u���E�U�̃I�v�V�������i�[����ϐ���������Ă��܂��B
		options = Options()
		# Headless���[�h��L���ɂ���i�R�����g�A�E�g����ƃu���E�U�����ۂɗ����オ��܂��j
		options.set_headless(True)
		# �u���E�U���N������
		self._driver = webdriver.Chrome(chrome_options=options)

	@classmethod
	def get_instance(self):
		if not self._instance:
			self._instance = self()
		return self._instance

	def scraping(self, url, id):
		try:
			# �u���E�U�ŃA�N�Z�X
			self._driver.get(url)
			# HTML�𕶎��R�[�h��UTF-8�ɕϊ����Ă���擾
			html = self._driver.page_source.encode('utf-8')
			# BeautifulSoup�ň�����悤�Ƀp�[�X���܂�
			soup = BeautifulSoup(html, "html.parser")
			# id�̗v�f��\��
			return soup.select_one(f"#{id}").text
		except:
			return ""
