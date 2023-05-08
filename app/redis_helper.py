import redis
from collections import Counter


class RedisHelper:
    """
    A helper class to interact with Redis for storing and retrieving request statistics.
    """
    def __init__(self, host, port):
        """
        Initialize the RedisHelper with a connection to a Redis server.

        :param host: The host address of the Redis server.
        :param port: The port number of the Redis server.
        """
        self.redis_connection = redis.StrictRedis(
            host=host,
            port=port,
            decode_responses=True
        )

    def get_connection(self):
        """
        Get the current Redis connection.

        :return: The current Redis connection.
        """
        return self.redis_connection

    def increment_request_count(self, path):
        """
        Increment the request count for a given path.

        :param path: The API path to increment the request count for.
        """
        if not path:
            return
        self.redis_connection.incr(f"request:{path}")

    def get_request_stats(self):
        """
        Get the request statistics for all API paths.

        :return: A dictionary with API paths as keys and request counts as values.
        """
        keys = self.redis_connection.keys("request:*")
        stats = Counter({key[8:]: self.redis_connection.get(key) for key in keys})

        return stats
