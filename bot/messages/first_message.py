from bot.message import Message

async def first_message_alice_skill(msg: Message) -> Message:
    """Function for sending a first message"""
    
    return msg("Добро пожаловать в AlicePlatform!\nУдачного кодинга!")
