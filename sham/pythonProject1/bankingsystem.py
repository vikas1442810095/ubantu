#Admin
#if u are admin show all user
#user  (user do only acti)
#1--check blance
#2--add money
#3--withdrawmoney
#4--total amount

account_holders = [{"name" : "vikas" ,"age" : 28 ,"address": "rohaniya" ,"amount" : 6000000 }
                   ,{"name" : "prakash" ,"age" : 25 ,"address": "rohaniya" ,"amount" : 600000},
                    {"name" : "akash" ,"age" : 21 ,"address": "varanasi" ,"amount" : 60000.220}
                   ]
def Admin_display():
    print("Name \t Age \t Address \t Amount")
    for x in account_holders:
        print(f'{x["name"]} \t {x["age"]} \t  {x["address"]} \t {x["amount"]}')

def forloop():
    for i in account_holders:
        print(f'{i["name"]}')
def check_blance():
    x = print(type(account_holders.append()))
    print(x)
    if account_holders[0].get("name") == "vikas":
        print(account_holders[0])
    elif account_holders[0].get("name") == "prakash":
        print(account_holders[1])
    elif account_holders[0].get("name") == "akash":
        print(account_holders[1])


check_blance()
#forloop()
def login():
    xy = input("You are demin or user if admin click A otherwise U:")
    if xy == "A" or xy  == "a":
        ab= input("enter your username:")
        rm = int(input("enter your password:"))
        if ab == "admin" and rm == 123:
            print(f'Hi {ab} Your welcome' )
            Admin_display()
        else:
            print("please entered wight usr/Pass")
    elif xy == "U" or xy == "u":
        av = input("Enter your name:")
        #print(account_holders[0].get("name"))

        if av == account_holders[0].get("name") or av == account_holders[1].get("name") or av == account_holders[2].get("name"):
            #print(account_holders[0])
            print(f'hi {av} enjoy your day')
            check_blance()
        else:
            print("Please enter valid name")
    else:
        print("Please entered Correct word")


login()