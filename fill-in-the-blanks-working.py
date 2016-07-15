
import sys

easy_quiz = '''\nA ___1___ is created with the def keyword. You specify the inputs a ___1___ 
takes by adding ___2___ separated by commas between the parentheses. ___1___s by default 
return ___3___ if you don't specify the value to return. ___2___ can be standard data types 
such as string, number, dictionary, tuple, and ___4___ or can be more complicated such as 
objects and lambda functions.'''

medium_quiz = '''\nThere are several ___1___s we can use on lists in Python. One example is the
"append" ___1___. Users can add an ___2___ to an existing list by typing <list>.append(<___2___>). 
Another ___1___ is "index". With "index", we can search a list for a certain ___3___ by typing 
<list>.index(<___3___>). This won't find all ___3___s in a list, just the ___4___ occurence. 
We can also use certain mathematical operators on lists. For example, we can ___5___ lists 
together to create a single new list, but we can't multiply them.'''

jedi_master_quiz = '''\nDarth ___1___ was the ___2___ Lord who created the Rule of Two. His 
apprentice was a girl named Darth ___3___. Together, they roamed the galaxy in search of 
___2___ Holocrons. These Holocrons held vast amounts of information passed down from ancient 
___2___ Lords. During one of Darth ___1___'s searches for a Holocron, he was attacked by 
crustaceous parasites called ___4___. These parasites kept spreading over the surface of his 
skin until they covered everything but his face, hands, and feet. Their shells were impervious 
to blaster fire and ___5___ strikes, and because of this, his apprentice Darth ___3___ didn't 
want to face him until the parasites were removed. She knew she was bound to face him because of 
the Rule of Two: One master and one apprentice. One to embody the power, the other to ___6___ it.'''

question_number  = ["___1___", "___2___", "___3___", "___4___", "___5___", "___6___"]

easy_answers = ["function", "arguments", "None", "list"]

medium_answers = ["operation", "element", "value", "first", "add"]

jedi_master_answers = ["Bane", "Sith", "Zannah", "Orbalisks", "lightsaber", "crave"]

difficulties = ["easy", "medium", "jedi master"]

try_list = ["still have 5 more tries.", "still have 4 more tries.", "still have 3 more tries.", 
"still have 2 more tries. Concentrate!", "only have 1 more try! Good luck!"]

def quiz_difficulty(choices): 
	"""
	start here. user inputs a choice to determine difficulty of quiz. 
	prints error message if choice not in list
	the last part could be simpler, but I wanted different opening statements to go with the difficulties
	"""
	user_choice = raw_input("\nFirst, choose your difficulty: " + ", ".join(choices) + "\n")
	while user_choice.lower() not in choices:
		user_choice = raw_input("\nNo way, Jose!\nTry typing your selection from these difficulties: " + ", ".join(choices) + "\n")
	if user_choice.lower() == choices[0]:
		print "\nYou've chosen the " + choices[0] + " quiz! You have 5 attempts for each question."
		play_game(easy_quiz, easy_answers)
	elif user_choice.lower() == choices[1]:
		print "\nYou've chosen the " + choices[1] + " quiz! You have 5 attempts for each question."
		play_game(medium_quiz, medium_answers)
	elif user_choice.lower() == choices[2]:
		print "\nYou've chosen the " + choices[2] + " quiz! You have 5 attempts to bullseye these womprats."
		play_game(jedi_master_quiz, jedi_master_answers)

# inputs are quiz and answers from quiz_difficulty function. returns first empty quiz string.
def play_game(quiz_string, answers):    
	print quiz_string
	blank = 0
	while blank < len(answers):
		if correct_answers(blank, answers, quiz_string):
			print updated_quiz(answers, blank, quiz_string)
			blank += 1
		else:
			attempt = 0
			while attempt <= len(try_list):
				if incorrect_answers(attempt, blank, answers, quiz_string):
					print updated_quiz(answers, blank, quiz_string)
					blank += 1
					break
				else:
					attempt += 1
	sys.exit("\nGreat job!! You must be a brainiac.")

# inputs: user answers. prints "correct" for each correct answer, and the current updated quiz after any answer
def correct_answers(blank, answers, quiz_string):  	
	user_answer = raw_input("\nWhat's your answer for " + question_number[blank] + "? ")
	if user_answer.lower() == answers[blank].lower():
		print "\nCorrect!!"
		return True
	else:
		return False

# inputs: user answers. returns error messages according to attempt number after each incorrect answer
def incorrect_answers(attempt, blank, answers, quiz_string): 
	if attempt == len(try_list):
		sys.exit("\nYa done messed up!! Come back when you're ready.")
	else:
		blank -= 1
		print updated_quiz(answers, blank, quiz_string)
		print "\nSorry, that's not the right answer! You " + try_list[attempt]
		blank += 1
		return correct_answers(blank, answers, quiz_string)

# prints out an updated quiz each time it's called
def updated_quiz(answers, blank, quiz_string): 
	while blank >= 0:
			quiz_string = quiz_string.replace(question_number[blank], answers[blank])
			blank -= 1
	return quiz_string

quiz_difficulty(difficulties)