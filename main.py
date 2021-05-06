from globals import Globals
import init_pet
import quit
import feed_pet
import play_toys
import get_toys
import print_menu
import print_stats


# Main game loop
def main():
    # initialize our pet
    init_pet.init_pet()

    # menu options for printing and access
    quit_dict = {"function": quit.quit_simulator, "text": "Quit the game"}
    feed_dict = {"function": feed_pet.feed_pet, "text": "Feed " + pet["name"]}
    play_dict = {"function": play_toys.play_toys, "text": "Play with " + pet["name"]}
    game_dict = {"function": get_toys.get_toys, "text": "Get new toys for " + pet["name"] + "!"}
    menu_options = {"Q": quit_dict, "F": feed_dict, "P": play_dict, "G": game_dict}
    keep_playing = True
    while keep_playing:
        # print the menu
        menu_selection = ""
        # validate the input
        while menu_selection not in menu_options.keys():
            print_menu.print_menu(menu_options)
            menu_selection = input("Which of these new options would you like to use? ").upper()

        if menu_selection == "Q":
            keep_playing = False

        # invoke the function corresponding to the selected menu option
        menu_options[menu_selection]["function"]()

        # increase pet's hunger
        pet["hunger"] += HUNGER_DECREASE
        pet["age"] += AGE_DECREASE
        print_stats.print_stats()
        # print out at extra line between options
        print()
