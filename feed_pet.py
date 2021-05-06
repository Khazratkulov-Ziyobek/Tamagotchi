from globals import Globals


# Feed our pet
def feed_pet():
    # handle negative edge cases
    new_hunger = globals.pet["hunger"] - HUNGER_DECREASE
    pet["hunger"] -= max(0, new_hunger)
    print("Fed your pet, decreasing hunger by 10")
