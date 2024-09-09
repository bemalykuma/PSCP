'''Cat Parade'''
import copy
def parade():
    '''Cat Parade'''
    animal_list = []
    ans_list = []
    name = input()
    while name != 'END':
        name = name.split(', ')
        animal_list += name
        if "IT'S A DOG" in animal_list:
            animal_list.remove("IT'S A DOG")
        name = input()
        if name == "IT'S A DOG":
            animal_list.pop()
    animal_list_sort = copy.copy(animal_list)
    animal_list_sort.sort()
    only_one = []
    result = []
    for i in animal_list_sort:
        if not i in only_one:
            only_one.append(i)
    for i in only_one:
        position = animal_list.index(i)
        count_num = animal_list.count(i)
        ans_list.append(i)
        ans_list.append(str(position+1))
        ans_list.append(str(count_num))
        result.append(ans_list)
        ans_list = []
    for i in result:
        print(' '.join(i))
parade()
