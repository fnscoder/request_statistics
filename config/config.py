class Config:
    """Common configurations for all environments"""
    pass


class DevelopmentConfig(Config):
    """Development-specific configurations"""
    DEBUG = True
    REDIS_HOST = 'redis'
    REDIS_PORT = 6379


class ProductionConfig(Config):
    """Production-specific configurations"""
    DEBUG = False


class TestingConfig(Config):
    """Testing-specific configurations"""
    TESTING = True
