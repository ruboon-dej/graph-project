from flask import Flask, request
from flask_caching import Cache
import os

from user import User

cache = Cache()

def create_app():
    app = Flask(__name__)
    cache_servers = os.environ.get('MEMCACHIER_SERVERS')
    if cache_servers == None:
        cache.init_app(app, config={'CACHE_TYPE': 'simple'})
    else:
        cache_user = os.environ.get('MEMCACHIER_USERNAME') or ''
        cache_pass = os.environ.get('MEMCACHIER_PASSWORD') or ''
        cache.init_app(app,
            config={'CACHE_TYPE': 'saslmemcached',
                    'CACHE_MEMCACHED_SERVERS': cache_servers.split(','),
                    'CACHE_MEMCACHED_USERNAME': cache_user,
                    'CACHE_MEMCACHED_PASSWORD': cache_pass,
                    'CACHE_OPTIONS': { 'behaviors': {
                        # Faster IO
                        'tcp_nodelay': True,
                        # Keep connection alive
                        'tcp_keepalive': True,
                        # Timeout for set/get requests
                        'connect_timeout': 2000, # ms
                        'send_timeout': 750 * 1000, # us
                        'receive_timeout': 750 * 1000, # us
                        '_poll_timeout': 2000, # ms
                        # Better failover
                        'ketama': True,
                        'remove_failed': 1,
                        'retry_timeout': 2,
                        'dead_timeout': 30}}})
    return app


app = create_app()
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

        user = cache.get(userId)
        if user is None:
            user = User(userId)
            cache.set(userId, user)
        user.converse(replyToken, text)
        cache.set(userId, user)
    return 'success'

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run()