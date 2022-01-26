import os
from flask import Flask
from linebot import LineBotApi, WebhookHandler

app_config = {"default": "bot.app_config.DevelopmentConfig",
              "development": "bot.app_config.DevelopmentConfig",
              "production": "bot.app_config.ProductionConfig"
}

app = Flask(__name__)
app.config.from_object(app_config[os.getenv("EXECUTION_ENV", "default")])

linebot_api = LineBotApi(app.config.get("CHANNEL_ACCESS_TOKEN"))
web_handler = WebhookHandler(app.config.get("CHANNEL_SECRET_KEY"))