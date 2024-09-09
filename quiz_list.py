#correct
list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
print(list1[2:7])

#correct
list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
del list1[7:]
list1.remove('a')
print(list1)

#correct
list1 = [8, 7, 6, 5, 4, 3, 2, 1]
list2 = list1[::-1]
print(list2)
print(list1)

#correct
string1 = "IT@KMITL"
list1 = string1.split("@")
print(list1)

#correct
list1 = ["Pre", "Programming'58"]
string1 = "-".join(list1)
print(string1)

#correct
import random
x = random.randrange(10,10001,5)
print(x)

#correct
x = [7, 3, 2, 7, 8, 1, 2]
del x[2:4]
print(x)

#correct
list1 = [8, 7, 6, 5, 4, 3, 2, 1]
list1.reverse()
print(list1)

#correct
print("It's maybe Illuminati")
