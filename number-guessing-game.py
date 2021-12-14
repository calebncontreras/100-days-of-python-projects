import random
from art import logo
from replit import clear
import time
#Number Guessing Game Objectives:
EASY_TURNS = 10
HARD_TURNS = 5

def get_difficulty():
  difficulty = input("choose a difficulty. 'easy' or 'hard': ")

  if difficulty == "hard":
    return EASY_TURNS
  elif difficulty == "easy":
    return HARD_TURNS

def check_guess(guess, answer):
  if guess < correct_number:
      print("Too Low")
      print("Guess Again")
      return attempts - 1
  elif guess > correct_number:
      print("Too High")
      print("Guess Again")
      return attempts - 1  

continue_game = 0

while continue_game == 0:
  print(logo)
  print("Welcome to the guessing game!")
  print("Im thinking of a number between 1 and 100")
  correct_number = random.randint(1, 101)

  attempts = get_difficulty()

  game_over = False
  while game_over == False:
    print(f"you have {attempts} attempts remaining to guess the number")

    guess = int(input("Make a guess: "))

    if guess == correct_number:
      print("That's correct you guessed the number ")
      game_over = True    
    
    attempts = check_guess(guess, correct_number)
    
    if attempts == 0:
      print("Sorry, You ran out of attempts :(")
      game_over = True
  
  continue_game = int(input("would you like to play again? 0=yes, 1=no "))
