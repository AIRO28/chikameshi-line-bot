from flask import request, abort
from bot import app, web_handler

from linebot.exceptions import InvalidSignatureError

@app.post("/callback")
def callback() -> str:
    """署名検証の実施"""

    sig = request.headers["X-Line-Signature"]
    body = request.get_data(as_text=True)

    try:
        web_handler.handle(body, sig)
    except InvalidSignatureError:
        abort(400)
    return "OK"


