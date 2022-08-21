import asyncio
import importlib
import settings

from sanic import Sanic
from pathlib import Path
from typing import Optional

from . import handler
from .handlers.view import AliceView
from database.engine.middleware import Database


class Application:

    __sanic_app: Optional[Sanic] = None

    def __init__(self):
        """Function for start application"""

        self.__read_handlers()  # Load all commands for alice skill
        self.__init_sanic()

    def __init_sanic(self):
        """Function for initialize Sanic"""

        # Sanic settings
        self.__sanic_app = Sanic(settings.APP_NAME)
        self.__sanic_app.config.FORWARDED_SECRET = settings.SECRET_KEY

        @self.__sanic_app.middleware('request')
        async def _(request):
            setattr(request.ctx, "commands", handler.commands)

        @self.__sanic_app.listener("before_server_start")
        async def _(app: Sanic, loop):
            Database(app)

        # Handlers | add your handler own here

        self.__sanic_app.add_route(AliceView.as_view(), f"/{settings.URL}")

        # End handlers

        self.__sanic_app.run(
            host=settings.HOST,
            port=settings.PORT,
            debug=settings.DEBUG
        )

    def __read_handlers(self):
        """Function for load skill commands"""

        path = Path(__file__).resolve().parent.joinpath("commands/")

        for command in path.rglob('**/*.py'):

            spec = importlib.util.spec_from_file_location(
                command.name, command
            )

            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
