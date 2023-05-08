from flask import Flask
from app.redis_helper import RedisHelper
from app.views.routes import routes
from config.config import DevelopmentConfig


def create_app(config_object=None):
    """
    Application factory function for creating a new Flask application instance.

    :param config_object: Optional configuration object. If not provided, the DevelopmentConfig is used.
    :return: A Flask application instance with the configured Redis helper and registered blueprints.
    """

    app = Flask(__name__)

    if not config_object:
        config_object = DevelopmentConfig

    app.config.from_object(config_object)

    redis_host = app.config['REDIS_HOST']
    redis_port = app.config['REDIS_PORT']
    redis_helper = RedisHelper(redis_host, redis_port)
    app.redis_helper = redis_helper

    app.register_blueprint(routes)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000)
