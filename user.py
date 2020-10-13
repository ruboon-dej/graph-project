import requests
import os

from physics import calculate


LINE_URL = 'https://api.line.me/v2/bot/message/reply'
token = os.environ['LINE_TOKEN']

VALID_VARIABLES = ['v', 'u', 'a', 't', 's']

class User:
    def __init__(self, userId):
        self.userId = userId
        self.reset()
    
    def reset(self):
        self.unknown_variable = None
        self.missing_variable = None
        self.variables_to_ask = VALID_VARIABLES.copy()
        
        # for calculation
        self.variables = {}

    def ask_for_unknown(self, replyToken):
        self.reply(replyToken, 'กรุณาใส่ตัวแปรที่ท่านต้องการหา', VALID_VARIABLES)
    
    def ask_for_missing(self, replyToken):
        self.reply(replyToken, 'กรุณาใส่ตัวแปรที่ไม่มีอยู่ในโจทย์', self.variables_to_ask)
    
    def converse(self, replyToken, text):
        if self.unknown_variable is None:
            if text in VALID_VARIABLES:
                self.unknown_variable = text
                self.variables_to_ask.remove(self.unknown_variable)
            else:
                self.ask_for_unknown(replyToken)
                return

        if self.missing_variable is None:
            if text in self.variables_to_ask:
                self.missing_variable = text
                self.variables_to_ask.remove(self.missing_variable)
            else:
                self.ask_for_missing(replyToken)
                return

        if len(self.variables_to_ask) != 0:
            variable = self.variables_to_ask[0]
            if text.isnumeric():
                value = float(text)
                self.variables_to_ask.remove(variable)
                self.variables[variable] = value

                if len(self.variables_to_ask) != 0:
                    self.reply(replyToken, self.variables_to_ask[0] + ' = ?')
                    return
            else:
                self.reply(replyToken, variable + ' = ?')
                return
        
        try:
            answer = str(calculate(self.unknown_variable, self.missing_variable, self.variables))
            self.reply(replyToken, 'Answer: ' + answer)
        except:
            self.reply(replyToken, 'Something went wrong!')
        self.reset()

    def create_quickReply_item(self, option):
        return {\
            'type': 'action',\
            'action': {\
                'type': 'message',\
                'label': option,\
                'text': option\
            }\
        }

    def reply(self, replyToken, text, options=[]):
        body = {}
        body['replyToken'] = replyToken
        body['messages'] = [{ 'type': 'text', 'text': text }]

        if len(options) != 0:
            quickReply = { 'items': [] }

            for option in options:
                quickReply['items'].append(self.create_quickReply_item(option))

            body['messages'][0]['quickReply'] = quickReply

        headers = { 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + token }
        req = requests.post(LINE_URL, json=body, headers=headers)
        print(req.text)