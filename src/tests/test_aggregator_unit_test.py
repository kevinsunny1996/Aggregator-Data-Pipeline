import pytest
import sys
import json

sys.path.append('..')

from src.scope_token_fetcher import ScopeGenerator


# Check to confirm that the list size of the metadata method is same and not less than 46 to make sure zip function works in locations module
def test_scope_fetching() -> None:
    scope_gen_test = ScopeAndTokenGenerator("urpp")
    test_scope = scope_gen_test.get_scopes_per_request()        
    assert test_scope == "user-read-playback-position"