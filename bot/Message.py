from sanic.response import json


class Message:

    def __init__(self, data):
        self.data = data
        self.censored = "<censored>" in self.data["request"]["command"].split()

    def __call__(self, text, end_session=False):
        """Function for creating a json response"""
        
        assert text, "Text for Message class must not by empty!"

        message_answer = {
                            "response": {"end_session": end_session},
                            "session": {}, "version": ""
                        }

        message_answer["session"] = self.data["session"]
        message_answer["version"] = self.data["version"]
        message_answer["response"]["text"] = text

        return json(message_answer)
