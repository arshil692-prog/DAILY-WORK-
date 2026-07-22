# 1///
fruits = {"apple","mango","banana","orange"}
print(fruits)

# 2///
fruits1 = {"apple","mango","banana","orange"}
print("origanal",fruits1)
fruits.add("apple")
print("duplicate",(fruits))

# 3///
set1 = set()
print(type(set1))

#4///
num1 = [1,2,3,4,5]
print("orignal list",num1)
set_num = set(num1)
print("set",set_num)

# 5///
# print(fruits[1])
#TypeError: 'set' object is not subscriptable

# 6///
student = {"arshil","rehan","fazal","vahid","aliyan"}
print("student set;",student)
print(len(student))

#7///
city = {"nashik","niphad","puna","jalgaon"}
if "puna" in city:
    print("city find")
else:
    print("city Not find")

# 8///
#num3 = {11,[22],33}
#print(num3)
#TypeError: unhashable type: 'list'

#9///
registrations = [
    "Rahul",
    "Amit",
    "Rahul",
    "Sneha",
    "Pooja",
    "Amit",
    "Rahul"
]
# 1. Convert the list into a set
unique_students = set(registrations)
# 2. Print all unique student names
print("Unique Student Names:")
print(unique_students)
# 3. Print the total number of unique students
print("\nTotal Unique Students:", len(unique_students))
# 4. Check whether "Sneha" is registered
if "Sneha" in unique_students:
    print("\nSneha is registered.")
else:
    print("\nSneha is not registered.")
# 5. Display the original list count versus the unique student count
print("\nOriginal Student Count:", len(registrations))
print("Unique Student Count:", len(unique_students))



# level 1 
# 1///
student_ids = [101,102,103,102,104,101,105,106,105]
unique_students_ids = set(student_ids)
print("unique student ids:",unique_students_ids)


#2///
student1 = {"Python","sql","Java","c++"}
print("student1 know:",student1)
student2 = {"Python","JavaScript","sql","html"}
print("student2 know:",student2)
print("commen subject student knows:",student1.intersection(student2))


#3///
print("subject known by student1:",student1.symmetric_difference(student2))


#4///
backend = {"Python","Django","sql"}
print("backend skills:",backend)
frontend = {"html","css","JavaScript"}
print("frondend skills:",frontend)
print("combine skiils:",backend.union(frontend))


# lvel 2
# 5///
Company_A = {"Rahul","Sneha","Amit","Pooja"}
Company_B = {"Amit","Pooja","Rohan","Karan"}
both_selected = Company_A.intersection(Company_B)
only_company_A = Company_A.difference(Company_B)
only_company_B = Company_B.difference(Company_A)
total_selected = Company_A.union(Company_B)
print("student selected in both companys:")
print(both_selected)
print("\nstudent selected in company A:")
print(only_company_A)
print("\nstudent selected in company B:")
print(only_company_B)
print("\ntotal student selected in both company:")
print(total_selected)
print("\ntotal unique student selcted :")
print(len(total_selected))

#6///
