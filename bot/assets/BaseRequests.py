import traceback, sys
from sanic.response import text
from bot.messages.errorMessage import errorMessage

class Command:
	def __init__(self, **kwargs):
		if not kwargs.keys() & {'names', 'handler'}:
			raise Exception('Not enough arguments to create command object')

		self.names = kwargs['names']
		self.__handler = kwargs['handler']


	async def handle(self, msg, database):
		try:
			return await self.__handler(msg, database)

		except Exception:
			ex_type, ex, tb = sys.exc_info()
			print(ex, traceback.format_tb(tb))

			return await errorMessage(msg)