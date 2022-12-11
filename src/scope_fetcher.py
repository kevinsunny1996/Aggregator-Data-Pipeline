import json

# Logger factory class import
from logger.logger import LoggerFactory


class ScopeGenerator():
    def __init__(self, scope_id):
        self.scope_id = scope_id
    def get_scopes_per_request(self) -> str:
        api_scopes = open('configs/web_api_scopes.json', 'r')
        scopes     = json.load(api_scopes)
        LoggerFactory.get_logger('./logs/info.log', 'INFO').info(f'Fetching scope : {scopes[self.scope_id]} for scope_id: {self.scope_id}')
        return scopes[self.scope_id]


# def get_locations() -> []:

#     site_ids, language_codes, locales = get_metadata() 

#     location_dict = open('configs/location_query.json', 'r')
#     location = json.load(location_dict)

#     location_url = f"https://{location['headers']['x_rapidapi_host']}/{location['endpoints']['location_url']}"

#     location_headers = {
#         "X-RapidAPI-Key": location['headers']['x_rapidapi_key'],
#         "X-RapidAPI-Host": location['headers']['x_rapidapi_host']
#     }

#     for site_id, lang_id, locale in zip(site_ids, language_codes, locales):
#         try:
#             locations_querystring = {"q":"New York","locale":locale,"langid":lang_id,"siteid":site_id}
#             LoggerFactory.get_logger('./logs/info.log', 'INFO').info(f'Running GET request for locale: {locale}, language ID: {lang_id}, site ID: {site_id}')
#             locations_res = requests.request("GET", location_url, headers=location_headers, params=locations_querystring).json()
#         except Exception as e:
#             LoggerFactory.get_logger('./logs/error.log', 'ERROR').error(f'Error in invoking query : {location_url} , recieved the following error : {e}')    

#     city_ids = []
#     property_ids = []

#     try:
#         for location in range(len(locations_res['sr'])):
#             if locations_res['sr'][location]['type'] == 'HOTEL':
#                 city_ids.append(locations_res['sr'][location]['cityId'])
#                 property_ids.append(locations_res['sr'][location]['hotelId'])
#     except Exception as e:
#         LoggerFactory.get_logger('./logs/error.log', 'ERROR').error(f'Error in iterating json response recieved the following error : {e}')



#     try:
#         LoggerFactory.get_logger('./logs/info.log', 'INFO').info(f'Retrieved {len(city_ids)} city IDs , {len(property_ids)} property IDs from given locations url {location_url}')
#     except Exception as e:
#         LoggerFactory.get_logger('./logs/error.log', 'ERROR').error(f'Error in invoking query : {location_url} , recieved the following error : {e}')

#     return city_ids, property_ids
