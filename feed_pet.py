import globals


# Feed our pet
def feed_pet():
    # handle negative edge cases
    new_hunger = globals.pet["hunger"] - 10
    if new_hunger < 0:
        new_hunger = 0
    globals.pet["hunger"] -= new_hunger
    print("Fed your pet, decreasing hunger by 10")
