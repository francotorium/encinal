# Instructions:
# Erase the placeholder text (number_one, number_two, etc.) and replace it with your own text.

class Hangman():

	# initialization function
	def __init__(self):

		# gives two choices: user promted to enter 1 to play, 2 to exit
		print("Welcome to Hangman, are you ready to play?")
		print("(1) Yes, I am prepared. \n(2) No, get me outta here!")

		# retrieves user input
		user_choice_1 = input("-> ")

		# if user types in "1", start the game with start_game() function
		if(user_choice_1 == "1"):
			print("Loading game...")
			self.start_game()

		# if user types in "2", exit the game with exit() function
		elif(user_choice_1 == "2"):
			print("Bye bye now...")
			exit()

		# error handling for invalid user input
		else:
			print("Sorry, that wasn't a valid choice! Try again.")
			self.__init__()

	# runs core_game()
	def start_game(self):
		self.core_game()

	def core_game(self):
		# NUMBER_ONE = what you should initialize wrong_guesses (an INT) to
		wrong_guesses = NUMBER_ONE
		# letters used = an empty string to keep track of letters guessed; we will add to this!
		letters_used = ""
		# NUMBER_TWO = the word the user should guess (a STRING)
		the_word = NUMBER_TWO
		# NUMBER_THREE = a list of "_" strings; there should be as many "_"s as there are letters in your word
		progress = [NUMBER_THREE]

		# NUMBER FOUR = the condition under which we want to keep playing; HINT: how many wrong guesses
		# are we allowed to make before hangman is complete?
		while(NUMBER_FOUR):

			# User's guess
			guess = input("Guess a letter -> ")

			# NUMBER_FIVE and NUMBER_SIX: replace these with two of our variables (wrong_guesses, letters_used,
			# the_word, or progress) such that the code within the if statement is run for a CORRECT guess
			if(guess in NUMBER_FIVE and not (guess in NUMBER_SIX):
				# NUMBER_SEVEN: print a statement congratulating the user on a correct guess
				print(NUMBER_SEVEN)

				# NUMBER_EIGHT = what we should CONCATENATE to the letters_used variable given a correct guess
				letters_used += NUMBER_EIGHT + " "

				self.hangman_graphic(wrong_guesses)
				print("Progress: " + self.progress_updater(guess, the_word, progress))

				# NUMBER_NINE: print out a string telling us which letters we used
				print(NUMBER_NINE)

			# NUMBER_TEN and NUMBER_ELEVEN: replace these with two of our variables (wrong_guesses, letters_used,
			# the_word, or progress) such that the code within the elif statement is run for an INCORRECT guess
			elif(guess not in NUMBER_TEN and not (guess in NUMBER_ELEVEN)):

				# NUMBER_TWELVE = value we should add to wrong_guesses to update the counte
				wrong_guesses += NUMBER_TWELVE

				# NUMBER_THIRTEEN: print a statement telling the user their guess was incorrect
				print(NUMBER_THIRTEEN)

				letters_used += NUMBER_EIGHT + " "

				self.hangman_graphic(wrong_guesses)
				print("Progress: " + "".join(progress))

				print(NUMBER_NINE)

			else:
				# NUMBER_FOURTEEN: print a statement telling the user their guess was INVALID
				print(NUMBER_FOURTEEN)

			if ("".join(progress) == the_word):
				# NUMBER_FIFTEEN: print a statement telling the user what happens if PROGRESS == THE_WORD
				# Hint: have we won or lost the game?
				print(NUMBER_FIFTEEN)

	def progress_updater(self, guess, the_word, progress):
		i = 0
		while(i < len(the_word)):
			if guess == the_word[i]:
				progress[i] = guess
				i += 1
			else:
				i += 1
		return "".join(progress)

	def hangman_graphic(self, guesses):
		if(guesses == 0):
			print("________      ")
			print("|      |      ")
			print("|             ")
			print("|             ")
			print("|             ")
			print("|             ")
		elif(guesses == 1):
			print("________      ")
			print("|      |      ")
			print("|      0      ")
			print("|             ")
			print("|             ")
			print("|             ")
		elif(guesses == 2):
			print("________      ")
			print("|      |      ")
			print("|      0      ")
			print("|     /       ")
			print("|             ")
			print("|             ")
		elif(guesses == 3):
			print("________      ")
			print("|      |      ")
			print("|      0      ")
			print("|     /|      ")
			print("|             ")
			print("|             ")
		elif(guesses == 4):
			print("________      ")
			print("|      |      ")
			print("|      0      ")
			print("|     /|\     ")
			print("|             ")
			print("|             ")
		elif(guesses == 5):
			print("________      ")
			print("|      |      ")
			print("|      0      ")
			print("|     /|\     ")
			print("|     /       ")
			print("|             ")
		else:
			print("________      ")
			print("|      |      ")
			print("|      0      ")
			print("|     /|\     ")
			print("|     / \     ")
			print("|             ")
			print("GAME OVER!")
			self.__init__()

game = Hangman()