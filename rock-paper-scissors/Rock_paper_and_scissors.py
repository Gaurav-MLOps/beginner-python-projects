import random

gestures = ("r", "p", "s")

while True:
    user_input1 = input("Want to play rock, paper or scissors, y/n?: ").lower()
    if user_input1 == "y":
        user_input2 = input("Rock, Paper or Scissors (r/p/s)?: ").lower()

        if user_input2 not in gestures:
            print("INVALID choice!")
            continue

        comp_random = random.choice(gestures)
        print(f"You: {user_input2}, Comp: {comp_random}")

        if user_input2 == comp_random:
            print("Tie!")
        elif (comp_random == "r" and user_input2 == "s") or \
             (comp_random == "s" and user_input2 == "p") or \
             (comp_random == "p" and user_input2 == "r"):
            print("Computer Wins!")
        else:
            print("You Won!")

    elif user_input1 == "n":
        print("Thank you for playing")
        break
    else:
        print("INVALID!")