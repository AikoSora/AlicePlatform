import settings

from utils import assertions
from os import system as SystemCommand
from bot.app import AliceSkill


def main():
	# It's funny ^_^
	SystemCommand("clear")

	# Assertions | add your assertion own here
	assertions.settingsCheck(settings)

	# End Assertions

	# Start app
	AliceSkill().start(settings)


if __name__ == "__main__":
	main()
