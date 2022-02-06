from asyncio.log import logger
from flask import request, abort
from bot import app, web_handler

from linebot.exceptions import InvalidSignatureError

@app.post("/callback")
def callback() -> str:
    """Perform signature verification"""

    sig = request.headers["X-Line-Signature"]
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    try:
        web_handler.handle(body, sig)
    except InvalidSignatureError:
        app.logger.exception("Signature Error.")
        abort(400)
    
    return "OK"
