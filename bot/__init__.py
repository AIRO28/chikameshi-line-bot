import os
from flask import Flask
from linebot import LineBotApi, WebhookHandler
from bot.libs.hotpepper import HotpepperManager

app_config = {"default": "bot.app_config.DevelopmentConfig",
              "development": "bot.app_config.DevelopmentConfig",
              "production": "bot.app_config.ProductionConfig"
}

app = Flask(__name__)
app.config.from_object(app_config[os.getenv("EXECUTION_ENV", "default")])

# Create various API instances.
try:
    linebot_api = LineBotApi(app.config.get("CHANNEL_ACCESS_TOKEN"))
    web_handler = WebhookHandler(app.config.get("CHANNEL_SECRET_KEY"))
    hotpepper = HotpepperManager(app.config.get("HOTPEPPER_API_KEY"))
except Exception as e:
    app.logger.exception("Failed to create the API instance.")
    app.logger.exception("Please check again if the necessary environment variables are set.")
    exit(1)

from bot.view import line_handler, routing