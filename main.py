# pet dictionary
pet = {"name": "", "type": "", "age": 0, "hunger": 0, "toys": []}
# pet toys data object
cat_toys = ["scratching post", "toy mouse", "ball of yarn"]
dog_toys = ["chew boy", "stick", "frisbee"]
fish_toys = ["undersea castle", "fake coral", "buried treasure"]
pet_toys = {"cat": cat_toys, "dog": dog_toys, "fish": fish_toys}


# Prompt for different options of pet type
def init_pet():
    # get the input of what type pet this is
    pet_type = ""

    pet_options = list(pet_toys.keys())

    # validate the input
    while pet_type not in pet_options:
        print("Please input a type of pet from the following options: ")
        for option in pet_options:
            print(option)
        pet_type = input("Please input one of the pets: ")
    # write in the pet type into the database
    pet["type"] = pet_type
    # name our pet
    pet["name"] = input("What would you like to name your " + pet["type"] + "? ")


# Print menu
def print_menu(menu_options):
    option_keys = list(menu_options.keys())

    print("Here are your options:")
    print("------")
    for key in option_keys:
        print(key + ":\t" + menu_options[key]["text"])


# Play with our toys
def play_toys():
    print(pet["name"] + " had a wonderful time playing with the toys!")


# Get new toys
def get_toys():
    print("Yay! Let's get some new toys!")
    toy_options = pet_toys[pet["type"]]

    # specific toy number to select from the list
    toy_num = -1
    # get a valid toy to input
    while toy_num < 0 or toy_num > len(toy_options) - 1:
        for i in range(len(toy_options)):
            print(str(i) + ": " + toy_options[i])
        toy_num = int(input("Input the number of the toy you would like: "))

    # get the selected toy option from our list
    chosen_toy = toy_options[toy_num]
    print("Nice! You selected the " + chosen_toy + "!")
    pet["toys"].append(chosen_toy)


# Quit the game
def quit_simulator():
    print("Quit the simulator. Thanks for playing!")


# Feed our pet
def feed_pet():
    # handle negative edge cases
    new_hunger = pet["hunger"] - 10
    if new_hunger < 0:
        new_hunger = 0
    pet["hunger"] -= new_hunger
    print("Fed your pet, decreasing hunger by 10")


# print out stats about the current status of the pet
def print_stats():
    print("Your " + pet["type"] + " " + pet["name"] + " is doing great!")
    if len(pet["toys"]) == 0:
        print("Your pet currently has not toys")
    else:
        print("Your pet currently has: " + str(len(pet["toys"])) + " toys, which are: ")
    for toy in pet["toys"]:
        print(toy)
    print("Your pet is currently at hunger of " + str(pet["hunger"]) + " of a max of 100.")
    print("Your pet is " + str(pet["age"]) + " days old.")


# Main game loop
def main():
    # initialize our pet
    init_pet()

    # menu options for printing and access
    quit_dict = {"function": quit_simulator, "text": "Quit the game"}
    feed_dict = {"function": feed_pet, "text": "Feed " + pet["name"]}
    play_dict = {"function": play_toys, "text": "Play with " + pet["name"]}
    game_dict = {"function": get_toys, "text": "Get new toys for " + pet["name"] + "!"}
    menu_options = {"Q": quit_dict, "F": feed_dict, "P": play_dict, "G": game_dict}
    keep_playing = True
    while keep_playing:
        # print the menu
        menu_selection = ""
        # validate the input
        while menu_selection not in menu_options.keys():
            print_menu(menu_options)
            menu_selection = input("Which of these new options would you like to use? ").upper()

        if menu_selection == "Q":
            keep_playing = False

        # invoke the function corresponding to the selected menu option
        menu_options[menu_selection]["function"]()

        # increase pet's hunger
        pet["hunger"] += 10
        pet["age"] += 1
        print_stats()
        # print out at extra line between options
        print()


main()

