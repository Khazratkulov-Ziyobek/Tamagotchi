from globals import Globals


# Get new toys
def get_toys():
    print("Yay! Let's get some new toys!")
    toy_options = Globals.pet_toys[Globals.pet["type"]]

    # specific toy number to select from the list
    toy_num = -1
    # get a valid toy to input
    while toy_num < 0 or toy_num > len(toy_options) - 1:
        for i in range(len(toy_options)):
            print(f"{str(i)}: {toy_options[i]}")
        toy_num = int(input("Input the number of the toy you would like: "))

    # get the selected toy option from our list
    chosen_toy = toy_options[toy_num]
    print(f"Nice! You selected the {chosen_toy} !")
    Globals.pet["toys"].append(chosen_toy)
