import pytest
from app.main import app as flask_app
from app.redis_helper import RedisHelper


@pytest.fixture
def app():
    return flask_app


@pytest.fixture
def redis_helper():
    return RedisHelper()


@pytest.fixture(autouse=True)
def clear_redis_data():
    redis_helper = RedisHelper()
    redis_helper.get_connection().flushdb()
    yield
