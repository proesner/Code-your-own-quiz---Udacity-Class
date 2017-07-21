from data import game_dict
import re

easy_answers = game_dict['answers']['easy']

# def matchBlanksInPhrase(blanks, phrase):
# 	for blank in blanks:
# 		if blank in phrase:
# 			return blank
# 	return None

def checkCorrectAnswer(i, answer):
	if answer == easy_answers[i]:
		print 'Correct.'
		return True
	else:
		if guesses:
			guesses -= 1
			print 'Try again. You have ' + str(guesses) + ' choice(s) left'
			return False
		else:
			print 'You are out of guesses. GAME OVER!'

def guessAttempts():
	try:
		guess_choice = int(raw_input('Please choice number of choices you\'d like to have. (1-3) -> '))

	except ValueError:
		print 'That is not a number.'
		return guessAttempts()

	else:
		if guess_choice == 1 or guess_choice == 2 or guess_choice == 3:
			print 'You\'ve entered to have ' + str(guess_choice) + ' choice(s) to guess'

		else:
			print 'Choose again. A number between 1 and 3.'
			return guessAttempts()

		return guess_choice

def playGame(phrase, answer):
	i = 0
	blank = game_dict['blanks']

	while i <= len(blank):
		print phrase + '\n'
		user_guess = str(raw_input('What is your guess for ' + blank[i] + ' ? -> '))
		checkCorrectAnswer(i, user_guess)

	# print 'Playing game now ' + phrase, attempts
	

def start():
	guesses = guessAttempts() # run guess attempt
	user_lvl = str(raw_input('Please select a difficulty (e)asy, (m)edium, (h)ard) -> '))

	if user_lvl == 'e': # easy level
		easy_phrase = re.sub('\s\s+', ' ', game_dict['phrases']['easy'])
		print 'You\'ve choosen and easy way out. Get ready to start.'
		return playGame(easy_phrase, easy_answers)

	elif user_lvl == 'm': # medium level
		medium_phrase = re.sub('\s\s+', ' ', game_dict['phrases']['medium'])
		print 'You\'ve choosen a fair route. Get ready to start.'
		return playGame(medium_phrase, game_dict['answers']['medium'])

	elif user_lvl == 'h': # hard level
		hard_phrase = re.sub('\s\s+', ' ', game_dict['phrases']['hard'])
		print 'You like challenges. Get ready to start.'
		return playGame(hard_phrase, game_dict['answers']['hard'])

	else:
		print 'Please choose one of the options provided. Clue: It\'s one letter.'
		return start() # restart game


start() # let the games begin