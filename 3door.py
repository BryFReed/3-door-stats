import random
def play():
    print("Happy fathers day! There are 3 doors for you to choose to get your fathers day gift, you can only choose 1 door. ")
    door = int(input("Choose 1, 2, or 3: "))
    print("thank you for selecting", door)
    ans = random.randint(1,3)
    open = ans
    while open == ans or open == door:
        open = random.randint(1,3)
    print("door", open, "will now be opened..... nothing is there!")
    yn = str(input("would you like to switch your door? (yes or no): "))
    if yn == "yes":
        door = 6 - door - open
    if door == ans:
        print("you won! congrats!")
    else:
        print("booo hooo! Try switching doors next time or stop being unlucky!")
def sim(trials):
    right = 0
    wrong = 0
    for i in range(trials):
        ans = random.randint(1,3)
        door = random.randint(1,3)
        open = ans
        while open == ans or open == door:
            open = random.randint(1, 3)
        if ans == 6 - door - open:
            right += 1
        else:
            wrong += 1
    return right/trials

def main():
    pass

if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
