
import random

def generate_userid():
  UserIds=[]
  #get alluserid from user.txt and store it in userIds
  while True:
    userid= f"U{random.randint(1,100)}"

    if userid not in UserIds:
        return userid

#cereate the account to customers#
def customer_create():
      first_Name=input('enter Your first name:')
      last_Name=input('enter the your last name:')
      Address=input('enter your Address')
      password=int(input('enter your password:'))
      new_userid=generate_userid()
      Balance=int(input('enetr the deposite amount'))
  #save the customers deatils on File#   
      with open('userspersonal','a')as users_personal:
          users_personal.write(f'{new_userid},{first_Name},{last_Name},{Address}\n')

      with open('userssecure.txt','a')as Users_secure:
          Users_secure.write(f' {new_userid},{password},{new_userid},{Balance}\n')
      print(f" Helloo {first_Name} sucessfully created your account and this is your {new_userid} ") 

      with open('save the Balance.txt','a')as balancefile:
            balancefile.write(f'{new_userid}, initial_balance:{Balance}')

      print(f' hello {first_Name} sucessfully create the account')



customer_create()
# # #create the customer Singin#
# # def customer_singin():
# #        singin=
    
#deposite#
def deposite():
  global balance
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
              balancefile.write(f"{newuser_id},deposite:-{amount}")    
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
                balancefile.write(f"{newuser_id},withdrawal amount:-{cash}")    

  
 #check the balance#

# def check_balance():
#      

# print('1.Create the account')
# print('2.deposite the money')
# print('3.withraw money')
# print('4.check the balance')
# print('5.tarnscations history')
# print('6.Exit')

# choice=int(input('enter the user choice(1-6) '))
# try:
#     if choice=='1':
#         customer_create()
#     elif choice=='2':
#         deposite()
#     elif choice=='3':
#         withdraw()
#     elif choice=='4':
#         check_balance()  
#     elif choice=='5':
#         Transcations_history()
#     elif choice=='6':
#         print("Thanks For Using  Minibanking")   
#     else:
#         print('invalid number')
# except ValueError:
#         print('enter the  numbers only')