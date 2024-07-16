'''
Write a program using WHILE LOOP WITH ELSE to Implement a simple guessing game. 
Description: A simple guessing game where the user tries to guess a secret number. The loop runs as long as the guess is not equal to the secret number. Inside the loop, we ask the user for a guess and increment the number of tries. If the guess is correct, we print a congratulatory message and break out of the loop. If the guess is incorrect, we print a message indicating that the guess was wrong. After the loop completes, we print a message indicating that the game is over.
'''
guess = int(input("Enter your guess: "))
secret_num = 57
while guess != secret_num:
    print("wrong guess")
    guess = int(input("Enter your guess: "))
if guess == secret_num:
    print("Congratulation Your Guess is Correct")
    print("Game Is Over")