from .assets import Command


commands = []


def message(**kwargs):
	def with_args(handler):
		if kwargs.keys() & {'names'}:

			if not isinstance(kwargs['names'], list):
				kwargs['names'] = [kwargs['names']]

			for text in kwargs['names']:
				commands.append(Command(
					names = kwargs['names'],
					handler = handler,
				))

		else:
			return False

	return with_args