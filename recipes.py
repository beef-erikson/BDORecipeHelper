

def alchemy():
    # Do stuff
    print("Taking you to alchemy . . .\n")


def armor():
    # Do stuff
    print("Taking you to armor . . .\n")


def cooking():
    # Do stuff
    print("Taking you to cooking . . .\n")


def weapons():
    # Do stuff
    print("Taking you to weapons . . .\n")


def recipe_list(argument):
    switcher = {
        "cooking": cooking,
        "alchemy": alchemy,
        "weapons": weapons,
        "armor": armor,
    }

    # Get the function from switcher dictionary and execute
    func = switcher.get(argument.lower(), lambda: "Invalid selection.\n")
    return func()
