from recipes import recipe_list
from menus import main_menu, title_screen


def main():
    selection = "Invalid selection"
    while not (recipe_list(selection) == "Invalid selection"):
        title_screen()
        main_menu()


if __name__ == "__main__":
    main()
