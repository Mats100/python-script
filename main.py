is_true = True
while is_true == True:
    try:
        number = int(input("Display multiplication table of? "))
        for i in range(1, 11):
            print(number, 'x', i, '=', number * i)
        break
    except:
        is_true == False
        print("It's a string.You must enter an integer")
