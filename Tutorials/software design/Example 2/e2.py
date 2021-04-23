import random

class GuessNumber:
    def __init__(self,mn=0,mx=100):
        self.guesses = 0
        self.min = int(mn)
        self.max = int(mx)
        self.number = random.randint(self.min,self.max)

    def get_guess(self):
        guess = input(f"Please guess a number ({self.min} - {self.max}): ")

        if self.valid_number(guess):
            return int(guess)
        else:
            print("Please enter a valid number.")
            return self.get_guess()

    def valid_number(self,str_number):
        try:
            number = int(str_number)
        except:
            return False

        return self.min <= number <= self.max

    def play(self):
        while True:
            self.guesses += 1

            guess = self.get_guess()

            if guess < self.number:
                print("Your guess was under")
            elif guess > self.number:
                print("Your guess was over")
            else: #they guessed it
                break

        print(f"You guessed it in {self.guesses} guesses.")

while True:
    min_range = input("Please choose the minium number for your range: ")
    try:
        int(min_range)
    except:
        print("Please enter a valid number!")
        continue     
    max_range = input("Please choose the maximum number for your range: ")
    try:
        int(max_range)
    except:
        print("Please enter a valid number!")
        continue    
    game = GuessNumber(min_range,max_range)
    game.play()