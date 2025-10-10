
first_choice = input("You wake up in a dark forest. There is a path to your left and a cave to your right. Which do you choose? left or right? \n").lower()

if first_choice == "left":
    second_choice = input("You walk down the path and find a river. Do you swim across or walk along the bank? Type swim or walk\n").lower()

    if second_choice == "walk":
        print(" You fell inside a massive hole and now you are stuck. Game over!")

    else:
        print(" You have been attacked by two sharks. Game over !")

else:
    second_choice = input("You are inside the cave. Do you wish to take the wooden aged bridge, or go ahead? Type bridge or ahead\n").lower()
    if second_choice == "bridge":
        print("Congratulations! You have found the treasure chest !")
    else:
        print("You fell inside a trap. Game over!")