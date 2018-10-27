# coding: UTF-8
from GoogleSearch import GoogleSearch
from LevatechSearch import LevatechSearch
from QiitaSearch import QiitaSearch

class WebSearchGenerator:
	_instance = None

	def __init__(self):
		classlist=[
			'GoogleSearch',
			'LevatechSearch',
			'QiitaSearch'
		]

		self.apis=[]
		for classname in classlist:
			self.apis.append(globals()[classname]())

	@classmethod
	def get_web_search_apis(self):
		if not self._instance:
			self._instance = self()
		return self._instance.apis
