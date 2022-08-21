from bot.message import Message

async def error_message(msg: Message) -> Message:
    """Function for sending a error message"""
    
    return msg("Произошла ошибка, попробуйте позже!")
