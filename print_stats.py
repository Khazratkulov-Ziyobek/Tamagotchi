import globals


# print out stats about the current status of the pet
def print_stats():
    print("Your " + globals.pet["type"] + " " + globals.pet["name"] + " is doing great!")
    if len(globals.pet["toys"]) == 0:
        print("Your pet currently has not toys")
    else:
        print("Your pet currently has: " + str(len(globals.pet["toys"])) + " toys, which are: ")
    for toy in globals.pet["toys"]:
        print(toy)
    print("Your pet is currently at hunger of " + str(globals.pet["hunger"]) + " of a max of 100.")
    print("Your pet is " + str(globals.pet["age"]) + " days old.")
