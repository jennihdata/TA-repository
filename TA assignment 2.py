def number_one():
    name = input("Please enter a name(Jennifer-Ihdata-Blabla): ")
    name_replace = name.replace("-", " ")
    name_list = name_replace.split()

    def shorten(name_list):
        for i in name_list:
            print(i[0].upper(), end="")

    (shorten(name_list))

def number_two():
    rounds = int(input("How many rounds do you want to play? "))
    for i in range(rounds):
        num_of_stones = int(input("How many stones do you want to play with: "))

        def winners():
            if num_of_stones % 2 == 1:
                print("The winner is Alice!")
            elif num_of_stones % 2 != 1:
                print("The winner is Bob!")

        winners()

def number_three():

    def modulus():
        num = []
        x = []
        for i in range(0, 10):
            num.append(int(input("enter a number:")))
        for j in range(0, 10):
            x.append(num[j] % 42)
        x = set(x)
        print(len(x))
    modulus()

def number_four():
    moves = input("Enter the moves(abc): ")
    lists = ["ball", " ", " "]
    for i in (moves):
        if i == "a":
            new = lists[0]
            lists[0] = lists[1]
            lists[1] = new
        elif i == "b":
            new = lists[1]
            lists[1] = lists[2]
            lists[2] = new
        elif i == "c":
            new = lists[2]
            lists[2] = lists[0]
            lists[0] = new

    if lists[0] == "ball":
        print("The ball is in the left!")
    elif lists[1] == "ball":
        print("The ball is in the middle!")
    elif lists[2] == "ball":
        print("The ball is in the right!")

while True:
    question = int(input("Please choose a question(1/2/3/4): "))

    if question == 1:
        number_one()
        print("\n")
    elif question == 2:
        number_two()
        print("\n")
    elif question == 3:
        number_three()
        print("\n")
    elif question == 4:
        number_four()
        print("\n")
    else:
        continue
