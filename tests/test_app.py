import json
from unittest.mock import MagicMock
from app.utils import generate_random_string, simulate_requests


def test_api_endpoint(client, redis_helper):
    path = f"/api/{generate_random_string()}/{generate_random_string()}/"
    response = client.get(path)
    assert response.status_code == 200
    assert redis_helper.get_request_stats()[path] == "1"


def test_stats_endpoint(client):
    response = client.get("/stats/")
    assert response.status_code == 200
    stats = json.loads(response.data)
    assert isinstance(stats, dict)


def test_test_endpoint(client, redis_helper):
    num_requests = 10
    response = client.post(f"/test/{num_requests}/")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == '{"message":"Simulated requests successfully sent"}\n'
    stats = redis_helper.get_request_stats()
    assert sum(map(int, stats.values())) >= num_requests
