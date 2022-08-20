import random
from bot import handler
from database.models.models import Devices

messages = [
	"Привет!",
	"Привет, как дела?",
	"Давно не виделись!",
	"Я могу быть чем-то полезна?"
]

# names - variable for find text in message
@handler.message(names="Привет")
async def _(msg, database):

	database.add(Devices(name="NewDevice"))
	database.commit()
	
	return msg(random.choice(messages))


@handler.message(names=["пока"])
async def _(msg, database):

	return msg("Прощайте!", end_session=True)


@handler.message(names=["Включить", "свет"])
async def _(msg, database):

	if msg.censored:
		return msg("Не буду!")

	return msg("Сейчас включу!")
