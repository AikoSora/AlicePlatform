# This settings file for AlicePlatform

# skill access page, format:
# in - "alice" | out - (https://example.com/alice)
# in - ""      | out - (https://example.com/)
# in - "api"   | out - (https://example.com/api)
URL = "alice"

# secret key for nginx proxy (necessarily!)
SECRET_KEY = "AbobusTeam"

# IP and Port for access to alice skill
HOST = "127.0.0.1"
PORT = "8000"

# Debug mode (Development mode)
DEBUG = True

# Sanic app name
APP_NAME = "Alice"
