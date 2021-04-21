# Print menu
def print_menu(menu_options):
    option_keys = list(menu_options.keys())

    print("Here are your options:")
    print("------")
    for key in option_keys:
        print(key + ":\t" + menu_options[key]["text"])