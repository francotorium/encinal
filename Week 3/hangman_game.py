class Hangman():
	def __init__(self):
		print("Welcome to Hangman, are you ready to play?")
		print("(1) Yes, I am prepared. \n(2) No, get me outta here!")
		user_choice_1 = input("-> ")

		if(user_choice_1 == "1"):
			print("Loading game...")
			self.start_game()
		elif(user_choice_1 == "2"):
			print("Bye bye now...")
			exit()
		else:
			print("Sorry, that wasn't a valid choice! Try again.")
			self.__init__()

	def start_game(self):
		self.core_game()

	def core_game(self):
		wrong_guesses = 0
		letters_used = ""
		the_word = "pizza"
		progress = ["_","_","_","_","_"]

		while(wrong_guesses < 6):
			guess = input("Guess a letter -> ")

			if(guess in the_word and not (guess in letters_used)):
				print("Good job! You were right!")
				letters_used += guess + " "
				self.hangman_graphic(wrong_guesses)
				print("Progress: " + self.progress_updater(guess, the_word, progress))
				print("Letters used: " + letters_used)
			elif(guess not in the_word and not (guess in letters_used)):
				wrong_guesses += 1
				print("Oh no! That guess was wrong!")
				letters_used += guess + " "
				self.hangman_graphic(wrong_guesses)
				print("Progress: " + "".join(progress))
				print("Letters used: " + letters_used)
			else:
				print("That's invalid! Try again.")
			print(progress)
			print(the_word)
			if ("".join(progress) == the_word):
				print("Congrats! You won!")

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

	def progress_updater(self, guess, the_word, progress):
		i = 0
		while(i < len(the_word)):
			if guess == the_word[i]:
				progress[i] = guess
				i += 1
			else:
				i += 1
		return "".join(progress)

game = Hangman()