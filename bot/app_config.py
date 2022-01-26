import os

class Config():
    CHANNEL_ACCESS_TOKEN = os.environ.get("CHANNEL_ACCESS_TOKEN")
    CHANNEL_SECRET_KEY   = os.environ.get("CHANNEL_SECRET_KEY")

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    pass