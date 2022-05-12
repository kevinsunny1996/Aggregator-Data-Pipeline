# Write a python script to get price listing of hotels from hotels api
# and save it to a file.
import requests
from abc import ABC, abstractmethod
import hydra 
from omegaconf import OmegaConf, DictConfig

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

class PricingAggregator(ABC):
	@abstractmethod
	def parse_response(self):
		pass

	@abstractmethod
	def run_pricing_query(self):
		pass
	
class QueryParamsLocations(QueryParams):
	def __init__(self, query: str, locale: str, currency: float, url: str, headers: dict()):
		self.query = query
		self.locale = locale
		self.currency = currency
		self.url = url
		self.headers = headers

	@hydra.main(config_path='configs/query.yaml')
	def get_params_query_string(self, cfg: DictConfig) -> dict():
		return {
			'query': cfg.location_params.query,
			'locale': cfg.location_params.locale,
			'currency': cfg.location_params.currency
		}
	
	@hydra.main(config_path='configs/urls.yaml')
	def get_url(self, cfg: DictConfig) -> str():
		return cfg.urls.location_url

	@hydra.main(config_path='configs/common.yaml')
	def get_headers(self, cfg: DictConfig) -> dict():
		return {
			'X-RapidAPI-Host': cfg.headers.x_rapidapi_host, 
			'X-RapidAPI-Key': cfg.headers.x_rapidapi_key
		}

	def run_query(self) -> None:
		try:
			LoggerFactory.get_logger('logs/logger.log', INFO).info('Running query for location')
			response = requests.request("GET", self.url, headers=self.headers, params=self.get_params_query_string())
			return response.json()
		except Exception as e:
			LoggerFactory.get_logger('logs/logger.log',
			                         'ERROR').error(f'Error in running query: {e}')
			
class QueryParamsPricing(PricingAggregator):
	def __init__(self, response: Dictionary):
		self.response = response

	# TODO 1 : Parse the response and save the whole response to a file and return the list of destination IDs
	def parse_response(self, response: Dictionary):
		pass

	# TODO 2 : Run the pricing query for each destination ID and save the response to a json file to be later used by preprocessing script
	def run_pricing_query(self):
		pass