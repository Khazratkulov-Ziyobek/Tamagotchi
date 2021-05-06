from globals import Globals
from init_pet import init_pet()
from feed_pet import feed_pet()
from get_toys import get_toys()
from print_stats import print_stats()



# Play with our toys
def play_toys():
    print(pet["name"] + " had a wonderful time playing with the toys!")


# Quit the game
def quit_simulator():
    print("Quit the simulator. Thanks for playing!")


# Print menu
def print_menu(menu_options):
    option_keys = list(menu_options.keys())

    print("Here are your options:")
    print("------")
    for key in option_keys:
        print(key + ":\t" + menu_options[key]["text"])


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
        pet["hunger"] += HUNGER_DECREASE
        pet["age"] += AGE_DECREASE
        print_stats()
        # print out at extra line between options
        print()
