from sanic.response import json


class Message:
	
	def __init__(self, data):
		self.data = data
		self.censored = "<censored>" in self.data["request"]["command"].split()

	def __call__(self, text, end_session = False):
		assert text, "Text for Message class must not by empty!"

		messageAnswer = {"response": {"end_session": end_session}, "session": {}, "version": ""}
		messageAnswer["session"] = self.data["session"]
		messageAnswer["version"] = self.data["version"]
		messageAnswer["response"]["text"] = text

		return json(messageAnswer)
