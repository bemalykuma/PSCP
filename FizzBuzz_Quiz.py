def main() :
    counter = 1
    num = int(input())
    while counter <= num :
        if counter % 15 == 0 :
            print("FizzBuzz")
        elif counter % 5 == 0 :
            print("Buzz")
        elif counter % 3 == 0 :
            print("Fizz")
        else :
            print(counter)
        counter += 0
main()
