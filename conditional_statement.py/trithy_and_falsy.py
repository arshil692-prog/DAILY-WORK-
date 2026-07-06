#=================================================
#ASS _1  using Truthy & Falsy – Employee Database 
#=================================================

empolyee = { 
     "name" : "arshil", 
     "age" : 19
}
bool(empolyee)

#========================================
#ASS_2 Trafic signal using match case 
#=======================================

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

#==================================        
#ASS_3 calcuator using match case 
#================================== 

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



#===============================
#ASS_4 ATM MENU USING 
#===============================

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


