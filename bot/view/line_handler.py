from bot import app, linebot_api, web_handler, hotpepper
from linebot.models.events import Event, MessageEvent
from linebot.models.messages import TextMessage
from linebot.models.send_messages import TextSendMessage

@web_handler.default()
def default_handler(event: Event):
    """デフォルトハンドラ"""

    text = "未対応の操作"

    linebot_api.reply_message(event.reply_token, TextSendMessage(text=text))

@web_handler.add(MessageEvent, message=TextMessage)
def message_event_handler(event: Event):
    """メッセージイベントに対するハンドラ"""

    # debugコード
    ret = hotpepper.search_shop_list("35.6895014", "139.6917337")

    linebot_api.reply_message(event.reply_token, messages=TextSendMessage(text=ret)


