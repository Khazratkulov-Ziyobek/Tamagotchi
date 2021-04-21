













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

