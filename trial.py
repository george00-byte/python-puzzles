#! usr bin python3

a,b=3,4

print(a,b)


print(a*b)


print("\n")



def game():
    i = int(input("Enter 1 to play the game and 3 to exit"))
    while (i != 3):
        def sum():
            x = int(input("Enter a Number "))
            y = int(input("Enter the second number "))
            y = x * y
            print(y)

            for x in range(1, y):
                print(x)
                if (x == 4):
                    print(i)

        sum()

game()







