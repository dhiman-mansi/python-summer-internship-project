from random import randint


EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
#Functions to check user's guess against actual answer.
def check_answer(guess, answer,  turns):
    """checks answer against guess. Returns the number of turns remaining."""
    if guess > answer:
        print("Too high.")
        return turns-1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was{answer}.")

# make function to set difficulty.
def set_difficulty():
    level = input("choose a difficulty. Type 'easy' or 'hard':")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    answer = randint(1,100)

    turns = set_difficulty()
     #Repeat the guessing functionality if they get it wrong.
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")

     #Let the user guess a number.
        guess = int(input("Make a guess: "))

     #Track the number of turns and reduce by 1 if they get it wrong.
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print(" you have run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")

game()