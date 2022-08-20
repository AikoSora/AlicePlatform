from bot.Message import Message

async def errorMessage(msg: Message) -> Message:
	return msg("Произошла ошибка, попробуйте позже!")