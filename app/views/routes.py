from flask import Blueprint, current_app, request, jsonify
from app.utils import simulate_requests


routes = Blueprint("routes", __name__)


@routes.route("/api/<path:path>", methods=["GET"])
def api(path):
    """
    Route for handling API requests.

    :param path: The path variable from the request URL.
    :return: A JSON response with a message.
    """
    redis_helper = current_app.redis_helper
    redis_helper.increment_request_count(request.path)
    return jsonify(message="ok")


@routes.route("/stats/", methods=["GET"])
def stats():
    """
    Route for getting request statistics.

    :return: A JSON response containing request statistics.
    """
    redis_helper = current_app.redis_helper
    stats = redis_helper.get_request_stats()
    return stats


@routes.route("/test/<int:num_requests>/", methods=["POST"])
def test(num_requests):
    """
    Route for simulating a given number of requests to the API.

    :param num_requests: The number of requests to simulate.
    :return: A JSON response with a message.
    """
    simulate_requests(num_requests, current_app)
    return jsonify(message="Simulated requests successfully sent")


@routes.route("/", methods=["GET"])
def home():
    return jsonify(hello="world")
