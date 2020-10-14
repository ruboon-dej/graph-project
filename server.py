from flask import Flask, request

from user import User

app = Flask(__name__) 

users = {}

def extract_replyToken_from_event(event):
    return event['replyToken']

def extract_userId_from_event(event):
    return event['source']['userId']

def extract_text_from_event(event):
    if event['type'] == 'message':
        try:
            return event['message']['text']
        except:
            return ''
    else:
        return ''

@app.route('/ping', methods=['GET'])
def ping():
    return 'pong'

@app.route('/message', methods=['POST'])
def message():
    body = request.get_json()
    events = body['events']
    for event in events:
        replyToken = extract_replyToken_from_event(event)
        userId = extract_userId_from_event(event)
        text = extract_text_from_event(event)

        if userId not in users:
            users[userId] = User(userId)
        
        user = users[userId]
        user.converse(replyToken, text)
    return 'success'

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
