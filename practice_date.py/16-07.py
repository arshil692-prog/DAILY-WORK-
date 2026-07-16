#section A 
l1 = []
print(l1)

l2 = ["arshil","rohit","rohan","rushi","sekhar"]
print(l2)

marks = [99,23,77,89,57,]
print(marks)

intro = ["arshil","ugaon",20, "%87"]
print (intro)

num = [[1,2,3],[4,5,6,],[7,8,9]]
print( num [0:3])

num1 = [[1,2,2],[3,4,5]]
print (num1[0:2:2])

#using lenth method
print(len(l1))

programmers = ["python","java","c++","c+","javascript"]
print("favorite programming languages",programmers)

#section B

city_name = ["nagpur","bombay","puna","nashik","niphad"]
print(city_name[2])

print(city_name[-1])

print(city_name[0:5:3])

print(city_name[::-1])

print (city_name[::2])

print(city_name[0:6:2])


name = [["hello"],["hiii"],["heyyy"],["whtasapp"],["yepp"]]
print(name[2])

#diffrence between (=) and copy() 
#1////  (=)

list1 = [1,2,3]
list2 = list1

list2.append(4)

print (list1,list2)
print(id(l1))
print(id(l2))
#2/// copy()

l1 = [1,2,3]
l2 = l1.copy()

l2.append(4)
print(l1,l2)
print(id(l1))
print(id(l2))


# section c 
l3 = [1,2,3,4,5]
l3[2] = 4
print(l3)

city = ["ugaon","niphad","nashik","maharastra","india"]
city.append("asia")
print(city)


student = ["rohan","roit","anam"]
student.insert(0,"arshil")
print(student)

student1 = ["arshil","rohan"]
marks = [89,76]
student1.extend(marks)
print(student1)

# section D 

name = ["arshil","rohit","viki","darshan"]
name[::-2] = ["sohel","vikas"]
print(name)

shopping_list = ["fruits","tech product","grosary","sea food"]
shopping_list [0]= "milk"
print(shopping_list)

#append we use for add the item in list 
name4 = ["shaikh","pathan"]
name4.append("shah")
print(name4)

#extend we use for merge to list in one or add elements to anoter colleation
name5 = [1,2,3]
name6 = [9,8,7]
name5.extend(name6)
print(name5)

#that is diffrence is append is use for add one item in list
# and extend is merge two list in one 

empolyee1 = ["gita","soham","roshan"]
empolyee2 = ["vina","nadim","sarthak"]
empolyee1.extend(empolyee2)
print(empolyee1)