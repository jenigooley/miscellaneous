mport random
def num_guess_game():

    print "Hello, lets play a game."
    num_guess = 0
    right_answer = random.randint(1,10)


    while num_guess < 6:

        guess = raw_input("Guess a number between 1 and 10:")
        guess = int(guess)
        num_guess += 1

        if guess < right_answer:
            print "Your guess is too low"

        if guess > right_answer:
            print "Your guess is too high"

        if guess == right_answer:
            print "You are correct! you guess the answer in", num_guess, "try. Great job."
            break




print num_guess_game()
