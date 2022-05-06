# Write a python script to get price listing of hotels from hotels api
# and save it to a file.
import requests
from abc import ABC, abstractmethod
import hydra 

# Logger factory class import
from src.logger.logger import LoggerFactory

# TODO 1: Move all these variables to YAML configs
url = "https://hotels4.p.rapidapi.com/locations/v2/search"

querystring = {"query":"new york","locale":"en_US","currency":"USD"}

headers = {
	"X-RapidAPI-Host": "hotels4.p.rapidapi.com",
	"X-RapidAPI-Key": "16fff31242msh84d1a94fb4afb12p1430a4jsnadfa2e122da5"
}

class QueryParams(ABC):
	@abstractmethod
	def get_params_query_string(self):
		pass

	@abstractmethod
	def get_url(self):
		pass

	@abstractmethod
	def get_headers(self):
		pass

	@abstractmethod
	def run_query(self):
		pass

class QueryParamsLocations(QueryParams):
	def __init__(self, query, locale, currency, url, headers):
		self.query = query
		self.locale = locale
		self.currency = currency
		self.url = url
		self.headers = headers

	def get_params_query_string(self):
		return {
			'query': self.query,
			'locale': self.locale,
			'currency': self.currency
		}
	
	def get_url(self):
		return self.url

	def get_headers(self):
		return self.headers

	def run_query(self):
		try:
			response = requests.request("GET", self.url, headers=self.headers, params=self.get_params_query_string())
			return response.json()
		except Exception as e:
			LoggerFactory.get_logger('logs/logger.log',
			                         'ERROR').error(f'Error in running query: {e}')
			
