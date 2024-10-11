#correct
# True False False False
print((10, 'hello') > (9, 'moon'),('moon', 10) > ('world', 20),('10', 'world') > ('2', 'world'), (10, 11, 12, 1) > (10, 11, 12, 2))

#correct
# Answer = [3]
numjp = {1:"ichi", 2:"ni", 3:"san", 4:"yon", 5:"go"}
print(numjp[3])

#correct
x = 5
y = 10
x, y = y, x # Answer
print(x)
# 10
print(y)
# 5

#correct
# Answer = list, values()
numjp = {1:"ichi", 2:"ni", 3:"san", 4:"yon", 5:"go"}
jpcount = list(numjp.values())
print(jpcount)
#['ichi', 'ni', 'san', 'yon', 'go']


#correct
#Immutable Type ค่าที่ไม่สามารถเปลี่ยนแปลงได้
#A type is immutable if it is a built-in immutable type: str, int, long, bool, float, tuple
# Answer = 0, (3,), 1.5, "9"


#correct
# Answer = get('100', 'unknown')
numjp2 = {'0':"zero", '6':"roku", '7':"nana", '8':"hachi", '9':"kyuu"}
print(numjp2.get('100', 'unknown'))
#unknown
print(numjp2)
#{'0': 'zero', '6': 'roku', '7': 'nana', '8': 'hachi', '9': 'kyuu'}

#correct
# Answer = False True [10, 2, 3]
a = [1,2,3]
b = [1,2,3]
print(a is b)
a = b
print(a is b)
b[0] = 10
print(b)

#correct
# Answer = *t
def fun(a, b):
    return a+b
t = (1,2)
x = fun(*t)
print(x)

#correct
# Answer = ["0"]
numjp2 = {"0":"zero", 6:"roku", '7':"nana", 8:"hachi", 9:"kyuu"}
print (numjp2["0"])

#correct
#Dictionaries have a method called {items} that returns a sequence of tuples, where each tuple is a key-value pair.

#correct
#{zip} is a built-in function that takes two or more sequences and returns a list of tuples where each tuple contains 
# one element from each sequence.
