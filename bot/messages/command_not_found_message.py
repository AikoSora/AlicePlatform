from bot.message import Message

async def command_not_found(msg: Message) -> Message:
    """Function for sending a command not found message"""
    
    return msg("Команда не найдена!")
