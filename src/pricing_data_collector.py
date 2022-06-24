import requests
import hydra 
from hydra import initialize, compose
from omegaconf import OmegaConf, DictConfig

# Logger factory class import
from logger.logger import LoggerFactory

location_url = "https://hotels4.p.rapidapi.com/locations/v2/search"

location_querystring = {"query":"new york","locale":"en_US","currency":"USD"}

headers = {
	"X-RapidAPI-Key": "16fff31242msh84d1a94fb4afb12p1430a4jsnadfa2e122da5",
	"X-RapidAPI-Host": "hotels4.p.rapidapi.com"
}

pricing_url = "https://hotels4.p.rapidapi.com/properties/list"

def get_locations() -> list():
    response = requests.request("GET", location_url, headers=headers, params=location_querystring).json()
    entity_idx = 0

    locations = []

    for suggestion_idx in range(len(response['suggestions'])):
        while (entity_idx < len(response['suggestions'][suggestion_idx]['entities'])):
            locations.append(response['suggestions'][suggestion_idx]['entities'][entity_idx]['destinationId'])
            entity_idx += 1

    return locations

def get_pricing_details(locations) -> dict():
    for location_id in locations:
        pricing_querystring = {
            "destinationId":location_id,
            "pageNumber":"1",
            "pageSize":"25",
            "checkIn":"2020-01-08",
            "checkOut":"2020-01-15",
            "adults1":"1",
            "sortOrder":"PRICE",
            "locale":"en_US",
            "currency":"USD"}
        pricing_response = requests.request("GET", pricing_url, headers=headers, params=pricing_querystring).json()

    return pricing_response

def main() -> None:
    location_results = get_locations()
    pricing_results = get_pricing_details(location_results)
    print(pricing_results)

if __name__ == '__main__':
    main()