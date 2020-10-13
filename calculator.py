from flask import Flask, request
import requests

app = Flask(__name__)

LINE_URL = 'https://api.line.me/v2/bot/message/reply'
token = 'CJ9W6jAk1E0N9F79zbuSTyYthxbBAqyrOTRk+uAmobWxQwhJzsn5G55ySm3qGJsfg65JpzuAgg1hcguiR8WrowmalzlNb0kpA6raPlVoW3FneyjwYTUh3LjqCkMUKOZostyMHMSHNNlLsDoe44lXpQdB04t89/1O/w1cDnyilFU='

conversations = {}

def responseWithMessage(replyToken, text):
    body = {}
    body['replyToken'] = replyToken
    body['messages'] = [{ 'type': 'text', 'text': text }]

    headers = { 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + token }
    req = requests.post(LINE_URL, json=body, headers=headers)
    print(req.text)

@app.route('/')
def hello_world():
    print(request)
    return 'Hello, World!'

@app.route('/message', methods=['POST'])
def message():
    body = request.get_json()

    event = body['events'][0]
    replyToken = event['replyToken']
    userId = event['source']['userId']
    text = event['message']['text']

    response = ''

    if userId not in conversations:
        conversations[userId] = { 'state': 0 }
        response = 'Plus or minus?'
    elif conversations[userId]['state'] == 0:
        conversations[userId]['state'] = 1
        response = 'What is the first number?'
        if text == 'plus':
            conversations[userId]['op'] = 'plus'
        elif text == 'minus':
            conversations[userId]['op'] = 'minus'
        else:
            response = 'Invalid Response! Plus or minus?'
            conversations[userId]['state'] = 0
    elif conversations[userId]['state'] == 1:
        conversations[userId]['state'] = 2
        response = 'What is the second number?'
        conversations[userId]['first'] = float(text)
    elif conversations[userId]['state'] == 2:
        first = conversations[userId]['first']
        second = float(text)
        op = conversations[userId]['op']
        if op == 'plus':
            response = 'Answer: ' + str(first + second)
        elif op == 'minus':
            response = 'Answer: ' + str(first - minus)
        del conversations[userId]

    responseWithMessage(replyToken, response)
    return 'Success'