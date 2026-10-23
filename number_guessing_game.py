#Computer will generate randome number and user hadd too remember one number after other number.If the user forgets the number then the game is over.

import random
import time
import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


print("===== NUMBER MEMORY GAME =====")
print("You will get 10 seconds to remember each number.")
print("If you enter it correctly, the next number will have one more digit.")
print("The game continues until you make a mistake.")

input("\nPress Enter to start...")

digits = 1
score = 0

while True:

    # Generate a random number with the required number of digits
    if digits == 1:
        number = random.randint(0, 9)
    else:
        minimum = 10 ** (digits - 1)
        maximum = (10 ** digits) - 1
        number = random.randint(minimum, maximum)

    clear_screen()

    print("===== NUMBER MEMORY GAME =====")
    print(f"\nRemember this {digits}-digit number:")
    print(f"\n              {number}")

    # Wait 10 seconds
    time.sleep(10)

    # Automatically remove the number
    clear_screen()

    print("===== NUMBER MEMORY GAME =====")
    print(f"\nThe {digits}-digit number has disappeared!")

    # Ask the user to enter the number
    user_answer = input("\nEnter the number you remember: ")

    # Check answer
    if user_answer == str(number):
        score += 1
        print("\n✅ Correct!")

        digits += 1

        print(f"Next number will have {digits} digits.")
        time.sleep(2)

    else:
        print("\n❌ Wrong!")
        print(f"The correct number was: {number}")
        print(f"\nGame Over!")
        print(f"Your score: {score}")
        print(f"You reached {digits} digits.")

        break
