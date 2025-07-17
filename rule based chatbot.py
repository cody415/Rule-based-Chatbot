import random
destination={
    "beaches":["bali","Maldives","Phuket"],
    "mountains":["swiss Alps","rocky mountains","Himalayas"],
    "cities":["Tokyo","paris","New York"]
}

def recommend():
    pref=input("what do you prefer, mountains, beaches or cities")

    if pref in destination:
        suggest=random.choice(destination[pref])
        print("how about",suggest)
        answer=input("do you like it, yes or no")
        if answer=="yes":
            print("awesome")
        elif answer=="no":
            print("let me try again")
            recommend()
        else:
            print("i have suggestion")
            recommend

def tips():
    pass

def jokes():
    pass

def chat():
    name=input("hello, i am travelbot, what is your name?")
    print("nice to meet you",name)
    print("how can i help you --type suggestion, tips, jokes,or quit")
    while True:
        user_input=input()

        if "recommend" in user_input:
            recommend()
        elif "tips" in user_input:
            tips()
        elif "jokes" in user_input:
            jokes()
        elif "exit" in user_input:
            break
        else:
            print("invalid input")
        

if __name__=="__main__":
    chat()