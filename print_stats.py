from globals import Globals


# print out stats about the current status of the pet
def print_stats():
    print(f"Your {Globals.pet['type']} {Globals.pet['name']} is doing great!")
    if len(Globals.pet["toys"]) == 0:
        print("Your pet currently has not toys")
    else:
        print(f"Your pet currently has: {str(len(Globals.pet['toys']))} toys, which are: ")
    for toy in Globals.pet["toys"]:
        print(toy)
    print(f"Your pet is currently at hunger of {str(Globals.pet['hunger'])} of a max of 100.")
    print(f"Your pet is {str(Globals.pet['age'])} days old.")
