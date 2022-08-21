import sys
import traceback

from bot.messages.error_message import error_message


class Command:
    def __init__(self, **kwargs):
        if not kwargs.keys() & {'names', 'handler'}:
            raise Exception('Not enough arguments to create command object')

        self.names = kwargs['names']
        self.__handler = kwargs['handler']

    async def handle(self, msg, database):
        """Error catching function, wrapper over the command"""
        
        try:
            return await self.__handler(msg, database)

        except Exception:
            ex_type, ex, tb = sys.exc_info()
            print(ex, traceback.format_tb(tb))

            return await error_message(msg)
