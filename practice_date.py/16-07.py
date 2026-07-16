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


