#############################################
#   Menus for all operations                #
#   Beef Erikson Studios                    #
#   v2020.0.1                               #
#############################################

from recipes import alchemy, armor, cooking, weapons


def title_screen():
    print()
    print("********************************")
    print("*    BDO Crafting Assistant    *")
    print("*    Beef Erikson Studios      *")
    print("*    v2020.0.1                 *")
    print("********************************")
    print()


def main_menu():
    print("****** Main Menu ******")
    print("(S)earch recipes")
    print("(A)dmin screen")
    print("(E(X)it")
    print()
    argument = input("Choose option: ")

    switcher = {
        "s": cooking,
        "a": alchemy,
        "x": weapons,
        "armor": armor,
    }

    # Get the function from switcher dictionary and execute
    func = switcher.get(argument.lower(), lambda: print("Invalid selection.\n"))
    return func()
