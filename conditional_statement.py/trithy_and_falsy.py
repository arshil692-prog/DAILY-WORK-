"""=================================================
ASS _1  using Truthy & Falsy – Employee Database 
=================================================

empolyee = { 
     "name" : "arshil", 
     "age" : 19
}
bool(empolyee)

========================================
ASS_2 Trafic signal using match case 
=======================================

color = input ("siganl color:-")
match color:
    case "red":
        print("stop")
    case "yellow":
        print("get redy")
    case "green":
        print("go")
    case _:
        print ("invalid signal")   

==================================        
ASS_3 calcuator using match case 
================================== 

print("1. Additon ")
print ("2. Subtraction")
print ("3. Division")
print ("4. Multiplication")
choise = int (input("Enter your choise number:"))
num1 = float (input("Enter your num1:"))
num2 = float (input("Enter your second num2:"))
match choise :
    case 1:
        print("answer =", num1 + num2)
    case 2:
        print("answer =", num1 - num2)
    case 3:
        print("answer =", num1 * num2)
    case 4:
        if num2 != 0:
            print("answer =", num1 / num2)
        else:
            print("cannot divide by zero")
    case _:
        print("invalid choise") 



===============================
ASS_4 ATM MENU USING 
===============================

print("1.menu")
print("2.deposit")
print ("3.withdrow")
print("4.cheak_balence")
print("5.exit")
choise = int (input("Enter choise:"))
match choise :
    case 1:
        print ("deposit selected")
    case 2:
        print("withdrow selected")
    case 3:
        print("balence = $5000")
    case 4:
        print("thank you")
    case _:
        print("invalid choise")


==================================
 food ordering system 
==================================

print("1. menu")
print("2. pasta")
print("3. burger")
print ("4. sandwich")
print("5. pizza")
choise = int (input("Enter choise:"))
match choise:
    case 1:
        print("pasta ordered")
    case 2:
        print("burger ordered")
    case 3:
        print("sandwich ordered")
    case 4:
        print("pizza ordered")
    case _:
        print("invalid menu")

===================================
student grade syteam 
===================================

grade = (input("Enter your grade"))
match grade:
    case "A":
        print("excellent")
    case "B":
        print("very good")
    case "C":
        print("good")
    case "D":
        print("pass")
    case "F":
        print("fail")
    case _:
        print("invalid grade")



================================
banking deposit system
================================

active = input ("account_active (True/False):" ) == "True"
kyc = input ("kyc completed (True/False):") == True
amount = float (input("deposit amount"))
if not active :
    print("deposit rejected")
elif not kyc :
    print("compelete kyc frist")
elif amount <=0:
    print("invalid deposit amount")
elif amount > 200000:
    print("meneger permission required")
elif amount >= 500000:
    print ("pan verification required")
else:
    print ("deposit successful")


====================================
secure login system 
====================================

username = input("Enter your username")
password = input ("Enter your password")
otp = ("otp verfired (True/False)")== "True"
if not username:
    print("username cannot be empty")
elif not password:
    print("password cannot be empty")
elif not otp:
    print("otp verification failled")
else:
    print("login sucssecfully")

================================================
 online course caertificate eligibility system 
 ===============================================

course = input ("course completed (True/False)") == "True"
project = input ("final project submitted(True/False)")
exam = input ("final exam passed (True/ FAlse)")
if course and project and exam :
    print ("certificate issued")
else:
    print("certificate not issued")


=============================================
airline bordiing system 
============================================
ticket = input ("ticket confirmed(True/False)")== "True"
passport = input ("passport valid(True/False)")== "True"
security = input ("security check completed (True/False)")=="True"
if ticket and passport and security :
    print("allow bording")
else:
    print("deny bording ")


=================================================
mini banking application 
================================================="""
balence = 10000

print ("MENU")
print("1. DEPOSIT")
print ("2. WITHDROW")
print ("3. BALENCE ENQIRY")
print ("4. EXIT")
choise = int(input("Enter your choise"))
match choise :
    case 1:
        amount = float(input("Enter deposit amount"))
        if amount > 0:
            balence += amount
            print("deposit seccessful")
            print ("Balence =", balence)
        else:
            print ("invalid deposit amount ")
    case 2:
        withdrow =float (input("Enter deposit amount"))
        if amount >= 0:
            print("invalid withdrow amount ")
        elif amount > balence:
            print("insuffient balence")
        else:
            balence -= amount
            print ("withrowal successful")
            print ("balence=", balence)
    case 3:
        if balence:
            print("current balence=", balence)
        else:
            print("zero balence")
    case 4:
        print("thank you for banking with us")
    case 5:
        print("invalid menu choise")




