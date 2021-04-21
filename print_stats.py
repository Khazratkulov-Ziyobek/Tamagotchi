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