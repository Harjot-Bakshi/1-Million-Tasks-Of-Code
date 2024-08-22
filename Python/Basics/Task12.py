import random
from hangman_words import word_list # Adding module info in Task12_Extras_1.py
from hangman_art import logo, stages # Adding module info in Task12_Extras_2.py

print(f"{logo}")
chosen_word = random.choice(word_list)
print(f"Hey the correct answer is: {chosen_word}")  # Remove this line in the actual game to avoid revealing the word
correct_answer = list(len(chosen_word) * "_")
chosen_word_list = list(chosen_word)
lives = 6
print(f"Welcome to Hangman Game! {stages[lives]}")
while "_" in correct_answer and lives > 0:
    guess = input("Guess a letter: ").lower()

    if guess in correct_answer:
        print(f"You've already guessed {guess}. Try again.")

    if guess in chosen_word_list:
        for x in range(len(chosen_word_list)):
            if chosen_word_list[x] == guess:
                correct_answer[x] = chosen_word_list[x]
    else:
        lives -= 1
        print(f"Incorrect guess '{guess}'. You lose a life!")
        print(stages[lives])

    print(f"{''.join(correct_answer)}")

if "_" not in correct_answer:
    print("You won!")
else:
    print("You lost! The word was:", chosen_word)
