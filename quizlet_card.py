class QuizletCard(object):
	"""docstring for QuizletCard"""

	def __init__(self, term = "", definition = ""):
		self.__term = term
		self.__definition = definition

	
	def get_term(self):
		"""return the value of term"""
		return self.__term

	def get_definition(self):
		"""return the value of __definition"""
		return self.__definition

	
	def set_term(self, new_term = ""):
		"""set new value for term"""
		self.__term = new_term

	def set_definition(self, new_definition = ""):
		"""set new value for definition"""
		self.__definition = new_definition

