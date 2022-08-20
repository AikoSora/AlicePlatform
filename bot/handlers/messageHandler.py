from sanic.response import json, text
from sanic.views import HTTPMethodView
from bot.Message import Message
from bot.messages.firstMessage import firstMessageAliceSkill
from bot.messages.commandNotFoundMessage import commandNotFound
from utils.searchMatches import searchMatches
from utils.assertions import requestCheck
from database.engine.engine import db_sa_open_session

class AliceView(HTTPMethodView):
	"""Alice skill handler and get (web) request handler"""

	async def post(self, request):
		if requestCheck(request.json):
			msg = Message(request.json)

			if not request.json["request"]["original_utterance"]:
				return await firstMessageAliceSkill(msg)

			for cmd in self.commands:
				if searchMatches(cmd.names, request.json["request"]["command"]):
					return await cmd.handle(msg, await db_sa_open_session(request))

			return await commandNotFound(msg)

		else:
			return json({"Error": "this method allowed only for alice!"})


	async def get(self, request):
		return text("Hi bro!")