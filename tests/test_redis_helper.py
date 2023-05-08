def test_increment_request_count(redis_helper):
    key = "/test/path"
    redis_helper.increment_request_count(key)

    stats = redis_helper.get_request_stats()
    assert stats[key] == "1"


def test_get_request_stats(redis_helper):
    key1 = "/test/path/1"
    key2 = "/test/path/2"
    redis_helper.increment_request_count(key1)
    redis_helper.increment_request_count(key2)
    redis_helper.increment_request_count(key2)

    stats = redis_helper.get_request_stats()

    assert len(stats) >= 2
    assert key1 in stats
    assert key2 in stats
    assert stats[key1] == "1"
    assert stats[key2] == "2"
    assert list(stats.keys())[0] == key2


def test_increment_request_count_invalid_key(redis_helper):
    key = ""
    redis_helper.increment_request_count(key)

    stats = redis_helper.get_request_stats()

    assert key not in stats


def test_increment_request_count_none_key(redis_helper):
    key = None
    redis_helper.increment_request_count(key)

    stats = redis_helper.get_request_stats()

    assert key not in stats
