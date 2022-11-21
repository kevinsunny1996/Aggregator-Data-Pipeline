import requests
import json

# Logger factory class import
from logger.logger import LoggerFactory

def get_metadata() -> []:

    metadata_dict = open('configs/metadata_query.json', 'r')
    metadata = json.load(metadata_dict)

    metadata_url = f"https://{metadata['headers']['x_rapidapi_host']}/{metadata['endpoints']['metadata_url']}"

    metadata_headers = {
        "X-RapidAPI-Key": metadata['headers']['x_rapidapi_key'],
        "X-RapidAPI-Host": metadata['headers']['x_rapidapi_host']
    }

    hotel_metadata = requests.request("GET", metadata_url, headers=metadata_headers).json()

    site_ids = []
    language_codes = []
    locales = []

    for key in hotel_metadata.keys():
        site_ids.append(hotel_metadata[key]['siteId'])
        language_codes.append(hotel_metadata[key]['supportedLocales'][0]['languageIdentifier'])
        locales.append(hotel_metadata[key]['supportedLocales'][0]['localeIdentifier'])
    
    try:
        LoggerFactory.get_logger('./logs/info.log', 'INFO').info(f'Retrieved {len(site_ids)} site IDs , {len(language_codes)} language codes, {len(locales)} locales from given metadata url {metadata_url}')
    
    except Exception as e:
        LoggerFactory.get_logger('./logs/error.log', 'ERROR').error(f'Error in invoking query : {metadata_url} , recieved the following error : {e}')

    return site_ids, language_codes, locales

if __name__ == '__main__':
    get_metadata()