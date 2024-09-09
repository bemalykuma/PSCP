'''Align'''
def main():
    '''Align'''
    size = int(input())
    option = input()
    text = input()
    lenght = len(text)
    if option == 'left':
        print(text + " " * (size-lenght))
    elif option == 'center':
        space = size - lenght
        if space%2 == 1:
            left = (space // 2) + 1
            right = space // 2
            print(f"{' '*left}{text}{' '*right}")
        else:
            abc = int(space/2)
            print(f"{' '*(abc)}{text}{' '*(abc)}")
    elif option == 'right':
        print(" " * (size-lenght) + text)
main()
