# Assertions file, write functions and add in main.py

def settings_check(settings):
	"""Functions for check settings"""
	
	error_message = "[Settings] \"%s\" not be empty!"

	assert settings.SECRET_KEY, error_message % "secretKey"
	assert settings.HOST, error_message % "host"
	assert settings.PORT, error_message % "port"
	assert settings.APP_NAME, error_message % "appName"

def request_check(request):
	"""Function for check request"""

	booling_array = [key in request for key in ["request", "session", "version"]]

	if all(booling_array):
		booling_array.append([key in request['request'] for key in ["original_utterance", "command"]])

	return all(booling_array)
