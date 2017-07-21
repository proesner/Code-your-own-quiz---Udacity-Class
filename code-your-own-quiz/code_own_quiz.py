from data import game_dict # import data from data.py
import re # import built-in python libs


def GuessAttempts():
	try:
		guess_choice = int(raw_input('\nPlease choice number of choices you\'d like to have. (1-3) -> '))
	except ValueError:
		print 'That is not a number.'
		return GuessAttempts() # restart guessAttempts
	else:
		if 1 <= guess_choice <= 3: # interval comparison
			print '\nYou\'ve entered to have ' + str(guess_choice) + ' guess(es)'
			return guess_choice # return value
		else:
			print '\nChoose again. A number between 1 and 3.'
			return GuessAttempts() # restart guessAttempts

def CheckAnswer(i, user_guess, answers):
	if user_guess == answers[i]:
		return True
	return False

def SelectDifficulty():
	user_lvl = str(raw_input('\nPlease select a difficulty (e)asy, (m)edium, (h)ard) -> '))
	if user_lvl == 'e': # easy level
		easy_phrase = re.sub('\s\s+', ' ', game_dict['phrases']['easy'])
		easy_answers = game_dict['answers']['easy']
		return PlayGame(easy_phrase, easy_answers, GuessAttempts())
	elif user_lvl == 'm': # medium level
		medium_phrase = re.sub('\s\s+', ' ', game_dict['phrases']['medium'])
		medium_answers = game_dict['answers']['medium']
		return PlayGame(medium_phrase, medium_answers, GuessAttempts())
	elif user_lvl == 'h': # hard level
		hard_phrase = re.sub('\s\s+', ' ', game_dict['phrases']['hard'])
		hard_answers = game_dict['answers']['hard']
		return PlayGame(hard_phrase, hard_answers, GuessAttempts())
	else:
		print '\nPlease choose one of the options provided. Clue: It\'s one letter.'
		return SelectDifficulty() # restart

def PlayGame(phrase, answers, guesses):
	i, guesses = 0, guesses
	blank = game_dict['blanks']

	while i <= len(blank):
		print '\n------------------------------\n' + phrase + '\n------------------------------\n'
		user_guess = str(raw_input('What is your guess for ' + blank[i] + ' ? -> '))
		if CheckAnswer(i, user_guess, answers):
			print '\nCorrect.'
			phrase = phrase.replace(blank[i], '__' + user_guess + '__')
			i = i + 1
		else:
			if guesses == 1:
				print '\nGame over! Thank you for playing.'
				break
			guesses = guesses - 1
			print '\nIncorrect. You have (' + str(guesses) + ') guesses left.'
			continue
		
SelectDifficulty() # let the games begin
