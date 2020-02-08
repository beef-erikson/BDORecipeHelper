from recipes import recipe_list


def main():
    selection = "Invalid selection"
    while not (recipe_list(selection) == "Invalid selection"):
        selection = input("What craft? ")
        print(recipe_list(selection))


if __name__ == "__main__":
    main();
