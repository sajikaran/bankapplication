#deposite#
def deposite():
    
  try:
        deposite=float(input('enter the amounrt') )      
        if deposite>=Balance
            Balance+=deposite
            print("Balance")

    except ("value error"):
        print('enter the number only')  

#withdrawal# 
def withdraw():  

  withdraw=int(input('enter the withdrw amount'))
  if withdraw<=Balance:
    print('money transcation sucussfully')
  else:
    ptint('insufficient funds') 
 
#create the account#

def user_personal():

  name=input('enter the user_name') 
  password=int(input('enter the pasword'))  
  contract=int(input('enter the contract number'))
  address=input('enter the address')
  user_id=name+str(password)
  return name,password,contract,address,user_id

userinfo=user_personal()
print(userinfo)  
with open('user.txt','w')as user:
    user.write(f'{userinfo}')  


   
#check the balance#
def check_balance():
      amount={}

#create the menu#
print(/n====='bank menu deatils====')

print('1.Create the account')
print('2.deposite the money')
print('3.withraw money')
print('4.check the balance')
print('5.tarnscations history')
print('6.Exit')

choice=int(input('enter the user choice(1-6) '))
if choice==1
print(f"{user_personal()}")

if choice==3
print(f'{withdraw()}')
if choice==4
print(f'{check_balance()}')
