import  datetime
groccerroy = [{"id":10001 ,"product_name":"oil","Available":10,"price":200,"original_price":150 },
            {"id":10002 ,"product_name":"aata","Available":10,"price":100,"original_price":90 },
            {"id":10003 ,"product_name":"chawmin","Available":10,"price":50,"original_price":40 },
            ]
groccerroy1 = groccerroy
def AdminLogin():
        print("*********************")
        print("1.Display Menu")
        print("2.Add item")
        print("3.Remove item")
        print("4.Total goods available")
        print("5.Income and Loss")
        print("6.Logout")
        print("*********************")

def DisplayMenu():
    print("Id\tName\tAvailable\tPrice\tOriginal Price")
    print("*****************************************")
    for groccerroyss in groccerroy :
        print(f'{groccerroyss["id"]}  \t{groccerroyss["product_name"]}  \t{groccerroyss["Available"]}  \t{groccerroyss["price"]}\t{groccerroyss["original_price"]}')


def AddItems():
    n=int(input("Enter the number of items you need to added:"))
    for i in range(n):
        new_id=int(input("Enter your new id:"))
        new_product_name=input("Enter your new_product_name: ")
        new_Available=int(input("Enter your new_Available Qua: "))
        new_price=int(input("Enter your new new_price:"))
        new_original = int(input("Enter the original price : "))
        add_items = [{"id":new_id,"product_name":new_product_name,"Available":new_Available,"price":new_price,"original_price":new_original}]
        print(type(add_items))
        groccerroy.extend(add_items)

        DisplayMenu()
    #while True:
        ab = input("you wants to add more item Yes/No")
        if ab  == "yes":
            AddItems()
        else:
            print("Thank you")
        break




temp=[]
def RemoveItems():
    removeId = int(input("remove your id:"))
    for x in groccerroy:
        found = x["id"] == removeId
        if  found == False:
            temp.append(x)
        if found == True:
            x["Available"] -= 10
    print("Deleating Itme")
    if len(temp) == x:
        print(f"{removeId} not found")
    else:
        print(f"{removeId}s one available is removed from the list")
    DisplayMenu()


def Goods():
    AddItems()
    total = 0
    for goods in groccerroy:
        print(f'{goods["product_name"]}: {goods["Available"]}')
        total = total + (goods["Available"])
    print(f'{total} Number of Your items')


def Income():
    total_income = 0
    for income  in  groccerroy:
        total_income = total_income + ((income["Available"] * income["price"]) - (income["Available"] * income["original_price"]))
    print(f'{total_income}  your total income')

def Logout():
    login()

def AdminChoice():
    choice = int(input("Enter your choice in number:"))
    if choice == 1 :
        DisplayMenu()
        print("************************")
        #login()
        print("************************")
        AdminChoice()
    if choice == 2:
        AddItems()
        print("************************")
        #login()
        print("************************")
        AdminChoice()
    if choice == 3:
        RemoveItems()
        print("************************")
        #login()
        print("************************")
        AdminChoice()
    if choice == 4:
        Goods()
        print("************************")
        #login()
        print("************************")
        AdminChoice()
    if choice == 5:
        Income()
        print("************************")
        #login()
        print("************************")
        AdminChoice()
    if choice == 6:
        Logout()

        print("************************")
        AdminChoice()


def userLogin():
    print("User")
    pass



def login():
    now = datetime.datetime.now()

    bn = input("Enter you are admin or user A/U:")

    if bn == 'A' or bn == 'a':
        xy = input("Enter the name of admin:")
        password = input("Enter your password:")
        if password == "abc" and xy == "Vikas" :
            x = now.strftime("\t%Y-%m-%d\t   %H:%M:%S\t")
            print(f'Hi {xy} Welcome {x}' )


            AdminLogin()
            AdminChoice()
        else:
            print("Invalid password. Please enter valid password or admin name")
            xy = input("Enter the name of admin:")
            password = input("Enter your password:")
            while True:

                if password == "abc" and xy == "Vikas":
                    print(f'Hi {xy} Welcome')
                    AdminLogin()
                    AdminChoice()
                    break
                else:
                    xy = input("Enter the name of admin:")
                    password = input("Enter your password:")
            pass
    elif bn == "U" or bn == "u":
        password = input("Enter your password:")
        if password == "123":
            userLogin()
        else:
            print("Please Enter the valid user password")
            password = input("Enter your password:")
            while True:

                if password == "123":
                    userLogin()
                    break
                else:
                    password = input("Enter your password:")



            #AdminChoice()



    else:
        print("Invalid user type. Enter valid user type")
#DisplayMenu()
login()
#Income()