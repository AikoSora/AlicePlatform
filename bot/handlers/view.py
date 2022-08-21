from sanic.response import json, text
from sanic.views import HTTPMethodView

from .message_handler import message_handler
from utils.assertions import request_check


class AliceView(HTTPMethodView):
    """Alice skill View"""

    async def post(self, request):
        if request_check(request.json):
            return await message_handler(request)
        else:
            return json({"Error": "this method allowed only for alice!"})

    async def get(self, request):
        return text("Hi bro!")
