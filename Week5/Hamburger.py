'''Hamburger'''
def main():
    '''Hamburger'''
    left = int(input())
    right = int(input())
    middle = '*' * ((left+right)*2)
    left = '|' * left
    right = '|' * right
    print(f'{left}{middle}{right}')
main()
