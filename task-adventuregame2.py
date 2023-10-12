import time

def story_start():
    print("You are in a dark forest.")
    time.sleep(1)
    print("Choose your path:")
    time.sleep(1)
    print("1 - Go left")
    time.sleep(1)
    print("2 - Go right")

    choice = input("Enter your choice: ")
    
    if choice == "1":
        left_path()
    elif choice == "2":
        right_path()
    else:
        print("Invalid choice. Please select 1 or 2.")
        story_start()

def left_path():
    print("You chose to go left.")
    time.sleep(1)
    print("Option 1 - Follow the river")
    time.sleep(1)
    print("Option 2 - Climb a tree")

    choice = input("Enter your choice: ")

    if choice == "1":
        follow_river()
    elif choice == "2":
        climb_tree()
    else:
        print("Invalid choice. Please select 1 or 2.")
        left_path()

def follow_river():
    print("You follow the river and find a boat.")
    time.sleep(1)
    print("Option 1 - Take the boat downstream")
    time.sleep(1)
    print("Option 2 - Continue following the river on foot")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("You take the boat downstream and discover a hidden village.")
        time.sleep(1)
        print("Congratulations, you've successfully completed your adventure!")
    elif choice == "2":
        print("You continue following the river on foot but get lost in the wilderness.")
        time.sleep(1)
        print("Game over.")
    else:
        print("Invalid choice. Please select 1 or 2.")
        follow_river()

def climb_tree():
    print("You climb a tree and see a distant castle in the forest.")
    time.sleep(1)
    print("Option 1 - Head towards the castle")
    time.sleep(1)
    print("Option 2 - Climb down and explore the forest")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("You head towards the castle and discover an enchanted world.")
        time.sleep(1)
        print("Congratulations, you've successfully completed your adventure!")
    elif choice == "2":
        print("You climb down and explore the forest but encounter dangerous creatures.")
        time.sleep(1)
        print("Game over.")
    else:
        print("Invalid choice. Please select 1 or 2.")
        climb_tree()

def right_path():
    print("You chose to go right.")
    time.sleep(1)
    print("You come across a mysterious cave.")
    time.sleep(1)
    print("Do you want to enter the cave or turn back?")
    time.sleep(1)
    print("1 - Enter the cave")
    time.sleep(1)
    print("2 - Turn back")

    choice = input("Enter your choice: ")

    if choice == "1":
        enter_cave()
    elif choice == "2":
        print("You decide not to enter the cave and continue through the forest.")
        time.sleep(1)
        print("Unfortunately, you got lost and couldn't find your way out.")
        time.sleep(1)
        print("Game over.")
    else:
        print("Invalid choice. Please select 1 or 2.")
        right_path()

def enter_cave():
    print("You enter the cave and find a hidden treasure chest.")
    time.sleep(1)
    print("Do you want to open the chest or leave it?")
    time.sleep(1)
    print("1 - Open the chest")
    time.sleep(1)
    print("2 - Leave the chest")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("You open the chest and find a pile of gold coins!")
        time.sleep(1)
        print("Congratulations, you've won the game!")
    elif choice == "2":
        print("You decide to leave the chest and return to the forest.")
        time.sleep(1)
        print("You eventually find your way out of the forest.")
        time.sleep(1)
        print("Congratulations, you've successfully escaped the dark forest!")
    else:
        print("Invalid choice. Please select 1 or 2.")
        enter_cave()

1
story_start()
