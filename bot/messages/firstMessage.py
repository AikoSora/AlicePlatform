from bot.Message import Message

async def firstMessageAliceSkill(msg: Message) -> Message:
	return msg("Добро пожаловать в AlicePlatform!\nУдачного кодинга!")
