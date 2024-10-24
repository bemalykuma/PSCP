'''[Recommend] Muddled Menu'''
def muddled(menu):
    '''Muddled Menu'''
    ans = []
    while menu != "DONE":
        if "#" in menu:
            menu = menu.split(" #")
            if menu[1] == "N":
                ans.insert(len(ans), menu[0])
            else:
                ans.insert(int(menu[1])-1, menu[0])
        elif menu == "SOMETHING'S WRONG":
            ans = []
        elif "Can't do:" in menu:
            menu = menu.split(": ")
            ans.remove(menu[1])
        elif menu == "CLOSED":
            ans = []
            break
        menu = input()
    reverse_menu = ans.copy()
    reverse_menu.reverse()
    print(f"Full Course: {ans} Reversed: {reverse_menu}")
muddled(input())
