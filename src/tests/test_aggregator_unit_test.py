import pytest
import sys
import json

sys.path.append('..')

from src.scope_fetcher import ScopeGenerator


# Check to confirm that the list size of the metadata method is same and not less than 46 to make sure zip function works in locations module
def test_scope_fetching() -> None:
    test_scope = ScopeGenerator.get_scopes_per_request("urpp")        
    assert test_scope == "user-read-playback-position"