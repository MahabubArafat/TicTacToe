
def taking_input():
    position = []
    for _ in range(1 ,20):
        num =int(input("enter a number between 1 to 9:"))
        if num >= 1 and num <= 9:
            position.append(num)
            if len(position)==9:
                break
        else:
            print("invalid input,plz enter again")

    print(position)
taking_input()