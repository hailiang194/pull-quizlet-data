# set between term and definition as \n#END_TERM#\n
# set between rows as \n#END_CARD#\n
import quizlet_func
import quizlet_card
import sys

if(len(sys.argv) < 2):
	quizletPath = str(input("path>> "))
else:
	quizletPath = sys.argv[1]

print("Loading... %s" %(quizletPath))
print("make sure you set between term and definition as \\n#END_TERM#\\n")
print("make sure you set between rows as \\n#END_CARD#\\n")
lstQuizlet = quizlet_func.get_quizlet_data(quizletPath)

print("Loaded successfully! n = %d" %(len(lstQuizlet)))

if(len(sys.argv) < 3):
	key = str(input("key>> "))
else:
	key = sys.argv[2]

print("Finding... %s" %(key))
lstMatch = quizlet_func.find_quizlet(lstQuizlet, key)
print("RESULT: n = %d" %(len(lstMatch)))

for quizlet in lstMatch:
	print("Term:")
	print("%s" % quizlet.get_term())
	print("def:")
	print("%s" % quizlet.get_definition())
	input()