# encoding: utf-8
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('ayYuB7D/BnzwTQOmqMQPCH/RfyB735vpXiYN+ruRYZS/ab1w1HG1WOrtov1pRs2hyHM+KiOaFTEL9VXvky74SdxJGx9N1ymXGW5Yhs4nDT8x+GRvcSmM+MAzGNRyZHy2+Q7fM38Ma0jLu3pJoJYt5AdB04t89/1O/w1cDnyilFU=') #Your Channel Access Token
handler = WebhookHandler('ecb818d08de8d62b520dc12c1eb77ec3') #Your Channel Secret

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    text = event.message.text #message from user

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=text)) #reply the same message from user
    

import os
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=os.environ['PORT'])
