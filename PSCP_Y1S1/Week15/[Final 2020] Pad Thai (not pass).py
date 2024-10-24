'''[Final 2020] Pad Thai'''
def pad_thai():
    '''[Final 2020] Pad Thai'''
    material = [ "Pad Thai Sauce", "Tofu", "Pickle Turnip", "Shrimp", "Bean Sprouts", "Noodle",\
                "Chives", "Lime", "Egg", "Oil", "Peanuts"]
    tasty = ["Sweet", "Sour", "Salty"]
    cooking, add_bad, taste_count, taste_bad, ans = [], 0, [], 0, ""
    mater = input()
    while mater != "Cook":
        add_bad = (1 if not mater in material else 0)
        cooking.append(mater)
        mater = input()

    taste = input()
    while taste != "End":
        taste_bad = (1 if not taste in tasty else 0)
        taste_count.append(taste)
        taste = input()

    no_material = set(material) - set(cooking)
    no_taste = set(tasty) - set(taste_count)
    if add_bad:
        ans = "This is not Pad Thai!!!"
    elif no_material:
        ans = "This is bad!"
    elif not no_material and (no_taste or taste_bad):
        ans = "Not Bad..."
    elif not no_material and not no_taste and not taste_bad and not add_bad:
        ans = "Delicious!"
    print(ans)
pad_thai()
