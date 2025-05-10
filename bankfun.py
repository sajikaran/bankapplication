
import random
Balance=0
def generate_userid():
  UserIds=[]
  #get alluserid from user.txt and store it in userIds
  while True:
    userid= f"U{random.randint(1,100)}"

    if userid not in UserIds:
        return userid

#cereate the account to customers#
def customer_create():
      global Balance
      first_Name=input('enter Your first name:')
      last_Name=input('enter the your last name:')
      Address=input('enter your Address')
      password=int(input('enter your password:'))
      new_userid=generate_userid()
      Initial_Balance=int(input('enetr the  amount'))
      Balance+=Initial_Balance
  #save the customers deatils on File#   
      with open('userspersonal','a')as users_personal:
          users_personal.write(f'{new_userid},{first_Name},{last_Name},{Address}\n')

      with open('userssecure.txt','a')as Users_secure:
          Users_secure.write(f' {new_userid},{password},{new_userid},{Balance}\n')
     
      with open('save the Balance.txt','a')as balancefile:
            balancefile.write(f'{new_userid}, initial_balance:{Balance}')
      print(f" Helloo {first_Name} sucessfully created your account and this is your {new_userid} ") 
      
#Deposite#
def deposite():
  global Balance
  while True:
      newuser_id=generate_userid()
      usersid =int(input('enter the your id number'))
      if usersid==newuser_id:
        try:
            amount=int(input('enter the amount') )      
            if amount>0:
                  Balance+=amount
                  print(f'sucessfully deposited :{amount}')
                  break
            else:
                    print(f"invalid deposite try again")
                    
        except ValueError:
                  print('enter the number only')     
        else:
          print(f"check your id number")
          
        with open('save the balance.txt','a')as balancefile:
              balancefile.write(f"{newuser_id},{Balance},deposited:-{amount}")    
        return Balance




#withdrawal# 
def withdraw():  
   global balance
   while True:
      newuser_id=generate_userid()
      usersid=input('enter the yourid')
      if newuser_id==usersid:
        try:
            cash=int(input('enter the cash') )      
            if cash>0:
                  Balance+=cash
                  print(f'sucessfully withdrawal:{cash}')
                  break
            else:
                    print(f" cheack the Balance ")
                    
        except ValueError:
                  print('enter the number only')     
        else:
          print(f"check your id number")
          
        with open('save the balance.txt','a')as balancefile:
                balancefile.write(f"{newuser_id},{Balance}withdrawal amount:-{cash}") 

#Check the balance#
def check_balance():
      global Balance
      Userid=generateuser_id()
      userid=int(input('enter the yourid'))
      if userid==Userid
          print('currently balance is:-')

#choose the option for admin#
def choose_option()

print(f'\n==== choosing your options=====\n')
print('1.Create the account')
print('2.deposite the money')
print('3.withraw money')
print('4.check the balance')
print('5.tarnscations history')
print('6.Exit')

choice=int(input('enter the user choice(1 to 6) '))
try:
    if choice=='1':
        customer_create()
    elif choice=='2':
        deposite()
    elif choice=='3':
        withdraw()
    elif choice=='4':
        check_balance()  
    # elif choice=='5':
    #     Transcations_historty
    elif choice=='6':
        print("Thanks For Using  Minibanking")   
    else:
        print('invalid number')
except ValueError:
            print("enter the numbers only")


Admin_singin():
    Username=Kanna
    Userid=3102
    user_name=input('enter the name')
    user_id=int(input('enter your id'))
    if Username==user_name and Userid==user_id:
        print("sucessfully created ")

    choose_option()

    else:
        print("unvalid name and id ")
#choose the option for customer#
def choose_customeroption():

print(f'\n===choosetheoption===\n')
print('1.Deposite Money')
print('2.withdrawal')
print('3.check the Balance')
|
choose=int(input('enetr the option 1to 3'))
try:
    if choose=='1':
       deposite()
    elif choose=='2':
        withdrawal()
    elif choose=='3':
        check_balance()
    else:
        print('invalid choose')

except ValueError:
       print("only enter the numbers only ")


def customers_sigin():
    userid=input('enter the  your id')
    User_id=generate_userid()
    if userid==User_id:
        print('choose your options')
    
    choose_customeroption()
    else:
        print("You need to create the account ")
    