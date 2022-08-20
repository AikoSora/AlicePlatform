import uvloop
import importlib

from sanic import Sanic
from pathlib import Path
from . import handler
from .handlers.messageHandler import AliceView
from database.engine.middleware import Database


class AliceSkill:

	def __init__(self):
		uvloop.install()


	def start(self, settings):
		"""Function for start alice skill"""

		# Load all commands for alice skill
		self.read_handlers()

		# Sanic settings
		app = Sanic(settings.appName)
		app.config.FORWARDED_SECRET = settings.secretKey

		# Database init
		Database(app)

		# Handlers | add your handler own here
		setattr(AliceView, "commands", handler.commands)
		app.add_route(AliceView.as_view(), f"/{settings.url}")

		# End handlers

		# Start sanic app
		app.run(host=settings.host, port=settings.port, debug=settings.debug)


	def read_handlers(self):
		"""Function for load skill commands"""

		path = Path(__file__).resolve().parent.joinpath("commands/")

		for command in path.rglob('**/*.py'):
			spec = importlib.util.spec_from_file_location(command.name, command)
			module = importlib.util.module_from_spec(spec)
			spec.loader.exec_module(module)