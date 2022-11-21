import pytest
import sys

sys.path.append('..')

from src.metadata_fetcher import get_metadata
from src.location_fetcher import get_locations


class TestResultLength:
    # Check to confirm that the list size of the metadata method is same and not less than 46 to make sure zip function works in locations module
    def test_metadata_count(self) -> None:
        site_ids, language_codes, locales = get_metadata()
        assert len(site_ids) == len(language_codes) == len(locales) == 46

    # Check to make sure that the hotel listings are not empty and that they are of equal length
    def test_hotel_listings_count(self) -> None:
        city_ids, property_ids = get_locations()
        assert len(city_ids) == len(property_ids) != 0