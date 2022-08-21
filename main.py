import settings

from utils import assertions
from os import system as system_command
from bot.app import Application


def main():
    """Function for start application"""
    
    # It's funny ^_^
    system_command("clear")

    # Assertions | add your assertion own here
    assertions.settings_check(settings)

    # End Assertions

    # Start app
    Application()


if __name__ == "__main__":
    main()
