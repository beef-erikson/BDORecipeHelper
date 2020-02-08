def cooking():
    # Do stuff
    return "Taking you to cooking . . .\n"


def alchemy():
    # Do stuff
    return "Taking you to alchemy . . .\n"


def weapons():
    # Do stuff
    return "Taking you to weapons . . .\n"


def armor():
    # Do stuff
    return "Taking you to armor . . .\n"


def recipe_list(argument):
    switcher = {
        "cooking": cooking,
        "alchemy": alchemy,
        "weapons": weapons,
        "armor": armor,
    }

    # Get the function from switcher dictionary
    func = switcher.get(argument.lower(), lambda: "Invalid selection.\n")
    # Execute the function
    return func()
