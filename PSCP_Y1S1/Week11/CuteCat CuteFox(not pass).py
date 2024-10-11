'''CuteCat CuteFox'''
import json
def cat_fox(num):
    '''CuteCat CuteFox'''
    animal = {}
    for _ in range(num):
        dict_animal = input()
        if not animal:
            animal = json.loads(dict_animal)
        else:
            animal.update(json.loads(dict_animal))
    animal_sort = sorted(animal.items(), key = lambda x : x[1])
    animal.clear()
    count_cat, count_fox = 0, 0
    for i in animal_sort:
        if "Cat" in i[1]:
            count_cat += 1
        if "Fox" in i[1]:
            count_fox += 1
        animal["Cat"], animal["Fox"] = count_cat, count_fox
        animal[i[0]] = i[1]
    for x, y in animal.items():
        print(x, ":", y)
cat_fox(int(input()))
