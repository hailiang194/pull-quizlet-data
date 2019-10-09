import quizlet_card
import os

END_CARD_NOTIFY = "#END_CARD#"
END_TERM_NOTIFY = "#END_TERM#"

def get_quizlet_card(rawQuizletData):
	"""Parse the rawQuizletData to get new QuizletCard"""
	term, definition = rawQuizletData.split(END_TERM_NOTIFY)

	card = quizlet_card.QuizletCard(term.strip(), definition.strip())

	return card

def get_quizlet_data(path):
	"""Get pull the data out of file"""

	lstQuizlet = []
	dataFile = open(path, "r")

	rawQuizletData = ""

	while(True):
		line = dataFile.readline().strip()
		
		if(line == END_CARD_NOTIFY):
			lstQuizlet.append(get_quizlet_card(rawQuizletData.strip()))
			rawQuizletData = ""
		else:
			rawQuizletData = rawQuizletData + line + ' '

		#check end of file
		if dataFile.tell() == os.fstat(dataFile.fileno()).st_size:
			break

	dataFile.close()

	return lstQuizlet

def find_quizlet(lstQuizlet, key):
	"""find all QuizletCard that each of them include key"""
	lstMatch = []

	for quizlet in lstQuizlet:
		if((key.upper() in quizlet.get_term().upper()) or (key.upper() in quizlet.get_definition().upper())):
			lstMatch.append(quizlet)

	return lstMatch
