# Assertions file, write functions and add in main.py

def settingsCheck(settings):
	"""Functions for check settings"""
	
	errorMessage = "[Settings] \"%s\" not be empty!"

	assert settings.secretKey, errorMessage % "secretKey"
	assert settings.host, errorMessage % "host"
	assert settings.port, errorMessage % "port"
	assert settings.appName, errorMessage % "appName"


def requestCheck(request):
	"""Function for check request"""

	keys = request.keys()

	if not keys & {'request'}: return False
	if not keys & {'session'}: return False
	if not keys & {'version'}: return False

	keys = request['request'].keys()

	if not keys & {'original_utterance'}: return False
	if not keys & {'command'}: return False

	return True
	