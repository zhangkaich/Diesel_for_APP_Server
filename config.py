import yaml

#TODO config
class Configuration(object):
	def __init__(self):
		self.config=None
		self.config_file="config/config.conf"

	def get_configuration(self):
		if self.config is None:
			self.config = yaml.load(file(self.config_file, 'r'))
		return self.config