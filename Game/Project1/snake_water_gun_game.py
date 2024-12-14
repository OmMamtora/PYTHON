import random

'''
1 for snake
-1 for water
0 for gun
'''
def snake_game(uservalue):
    
    lst= [-1,0,1]
    computer_dict = {1:"Snake",-1:"Water",0:"Gun"}
    computer = random.choice(lst)

    userDic = {"snake":1,"water":-1,"gun":0}
    userNum = userDic[uservalue]

    print("Computer enter : ",computer_dict[computer])
    print("User enter :",user)
    print()

    if computer == userNum:
        print("Match draw..")
    else:
        if computer == -1 and userNum == 1:
            print("You Win..")
        elif computer == -1 and userNum == 0:
            print("Computer Win..")
        elif computer == 0 and userNum == -1:
            print("You Win..")
        elif computer == 0 and userNum == 1:
            print("Computer Win..")
        elif computer == 1 and userNum == -1:
            print("Computer Win..")
        elif computer == 1 and userNum == 0:
            print("User Win..")
        else:
            print("Something went wrong..")

user = input("Enter your choices(snake,water,gun):->")

snake_game(user)