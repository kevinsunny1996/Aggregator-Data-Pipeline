import pytest
import hydra
from omegaconf import DictConfig, OmegaConf

from src.pricing_aggregator import QueryParamsLocations

location_query = QueryParamsLocations()

@hydra.main(config_path='configs/urls.yaml')
def test_location_url_configs(cfg: DictConfig) -> None:
    url_retrieved = location_query.get_url()
    assert url_retrieved == cfg.urls.location_url

def test_location_url_status() -> None:
    test_response = location_query.run_query()
    assert test_response.status_code == 200

def test_location_url_response() -> None:
    test_response = location_query.run_query()
    # deepcode ignore change_to_is/test: <please specify a reason of ignoring this>
    assert test_response.json() is not None