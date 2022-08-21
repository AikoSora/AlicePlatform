from bot.message import Message
from bot.messages.first_message import first_message_alice_skill
from bot.messages.command_not_found_message import command_not_found

from utils.search_matches import search_matches

from database.engine.engine import db_sa_open_session


async def message_handler(request):
    """Function for handling requests"""

    msg = Message(request.json)

    if not request.json["request"]["original_utterance"]:
        return await first_message_alice_skill(msg)

    for cmd in request.ctx.commands:
        if search_matches(
                cmd.names, request.json["request"]["command"]
                ):

            return await cmd.handle(
                msg, await db_sa_open_session(request)
            )

    return await command_not_found(msg)
