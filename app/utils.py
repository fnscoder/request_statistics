import random
import string


def generate_random_string():
    """
    Generate a random string of 3 lowercase ASCII characters.

    :return: A random string of 3 lowercase ASCII characters.
    """
    return ''.join(random.choices(string.ascii_lowercase, k=3))


def generate_random_path(pool=None, min_segments=1, max_segments=6):
    """
    Generate a random API path using a pool of string segments.

    :param pool: A list of string segments to use for generating the path.
                 If not provided, a new pool will be generated.
    :param min_segments: The minimum number of segments to include in the path.
    :param max_segments: The maximum number of segments to include in the path.
    :return: A random API path string.
    """
    if pool is None:
        pool = [generate_random_string() for _ in range(3)]

    num_segments = random.randint(min_segments, max_segments)
    path_segments = [random.choice(pool) for _ in range(num_segments)]

    return "/api/" + "/".join(path_segments) + "/"


def simulate_requests(num_requests, app):
    """
    Simulate a given number of requests to a Flask app using randomly generated API paths.

    :param num_requests: The number of requests to simulate.
    :param app: The Flask app to send requests to.
    """
    pool = [generate_random_string() for _ in range(3)]

    with app.test_client() as client:
        for _ in range(num_requests):
            random_path = generate_random_path(pool=pool)
            client.get(random_path)
