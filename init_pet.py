import globals


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
    globals.pet["type"] = pet_type
    # name our pet
    globals.pet["name"] = input("What would you like to name your " + pet["type"] + "? ")

