from SeleniumScraping import SeleniumScraping
from HTTPScraping import HTTPScraping

class Scraping:
	_instance = None

	@classmethod
	def scraping(self, url, id):
		#return SeleniumScraping.get_instance().scraping(url, id)
		return HTTPScraping.get_instance().scraping(url, id)
