# input function and escape characters , type casting  , printing multiple values with sep , and end 

name = input ("Enter your name : ")
print ("hello" , name )

age = input ("Enter your age : ")
print (type (age))

name = "arshil"
age = 20
print (name , age )

# printing multiple values with sep parameter 

print ("apple","banana", "mango" , sep = " ")


#using sep parameter with - 
print ("student1", "student2", "student3", sep = "-")

#using end parameter
#normaly 
print ("hii")
print ("hello")

# using end parameter
print ("hii",end = "_")
print ("hello") 

# escape characters

# \n - new line for new line 
print ("hello \nword")

# \t tab space for tab space 
print ("hello \tword")

# \\ for bakshlash 
print ('hello \\ arshil')

# \' for singal quote 
print("hello \'arshil\'")

# for duble qoute 
print ("hello \"asrshil\"")

# \b for backspace 
print ("hello \bword") 

# \r for carriage return
print ("hello \rword")


# print (--------------)
#type casting 
# print (--------------)

# implicit type casting 
a = 10 
b = 2.5
print (a +b )

# explicit type casting
# in int  
a = "100"
b = int (a)
print(b)
print (type(b))

# in float 
x= "15"
print (float(x)) 

# in str 
num = 10
text = str(num)
print (text)
print (type(text))

# bool ()
print (bool(10))
print (bool(0))
print ((""))
print (bool("python"))

#print (---------)
#string formating 
# print (---------)

# by using comma 
name = "arshil"
age = 20 
print ("name",name)
print ("age",age)


# concatenation
name = "arshil"
print("hello"+name)

#  %formating in older stayle
name = "arshil"
age = 20 
print ("my name is %s and i am %d years old" %(name,age))
 

# %s for sting
# %d for integer
# %f for float


# string formating by use format method 

name = "arshil"
age = 20 
print ("my name is {} and i am {} years old ".format(name,age))
 
# f-string formating
name = "arshil"
age = 20 
print (f"my name is {name} and i am {age} years old.")

 
