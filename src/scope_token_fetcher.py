import json
import awswrangler.secretsmanager as sm
import requests
import base64

# Logger factory class import
from logger.logger import LoggerFactory

# URL Encoded Redirect URL needed for getting code to be passed in get_bearer_token
url_encoded_redirect = 'https%3A%2F%2Fjsonurl.org%2F'

# Client ID, Client Secret and Code fetched from Secrets Manager 
client_id = sm.get_secret_json("spotifyClientID").get('spotify_client_id')
client_secret = sm.get_secret_json("spotifyClientSecret").get('spotify_client_secret')
code = sm.get_secret_json("spotifyAuthCode").get('spotify_auth_code')

class ScopeAndTokenGenerator():
    """
    Contains methods to fetch scopes and bearer tokens.
    """
    
    def __init__(self, scope_id):
        self.scope_id = scope_id
    
    """
    Title - Gets scopes based on key passed 
    Description - The method takes in json doc and based on the key passed for each scoped mapped in json file , returns the value for it.

    Returns
    ------------------------------------------
    Bearer Token : str 

    Description - The extracted scopes can then be used to call various Spotify endpoints programatically
    """
    def get_scopes_per_request(self) -> str:
        api_scopes = open('configs/web_api_scopes.json', 'r')
        scopes = json.load(api_scopes)
        LoggerFactory.get_logger('./logs/info.log', 'INFO').info(f'Fetching scope : {scopes[self.scope_id]} for scope_id: {self.scope_id}')
        return scopes[self.scope_id]

    
    """
    Title - Gets Bearer Token 
    Description - The following method takes in encoded client_id and client_secret (Base-64) and fetches bearer and refresh token.

    Returns
    ------------------------------------------
    Bearer Token : str 

    Description - The token can then be used to call Spotify API Programatically
    """
    def get_bearer_token(self) -> str:
        token_url = "https://accounts.spotify.com/api/token"
        encoded_creds = base64.b64encode(client_id.encode() + b':' + client_secret.encode()).decode("utf-8")
        token_headers = {"Authorization": f"Basic {encoded_creds}", "Content-Type": "application/x-www-form-urlencoded"}

        token_data = {
            "grant_type": "authorization_code",
            "code": code,
            "redirect_url": "https://jsonurl.org/"
        }

        token_response = requests.post(token_url, data=token_data, headers=token_headers)

        return token_response.json()["access_token"]




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
