from bot.Message import Message

async def commandNotFound(msg: Message) -> Message:
	return msg("Команда не найдена!")