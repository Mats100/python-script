try:
    number = int(input("Display multiplication table of? "))
    if number:
        for i in range(1, 11):
            print(number, 'x', i, '=', number * i)
except:
    print("It's a string.You must enter an integer")
