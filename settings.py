# This settings file for AlicePlatform

# skill access page, format:
# in - "alice" | out - (https://example.com/alice)
# in - ""      | out - (https://example.com/)
# in - "api"   | out - (https://example.com/api)
url = "alice"

# secret key for nginx proxy (necessarily!)
secretKey = "AbobusTeam"

# IP and Port for access to alice skill
host = "127.0.0.1"
port = "8000"

# Debug mode (Development mode)
debug = True

# Sanic app name
appName = "Alice"