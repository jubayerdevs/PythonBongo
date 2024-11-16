<<<<<<< HEAD

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:])
# print(thislist[-4:-1])

# if "apple" in thislist:
#   print("Yes, 'apple' is in the fruits list")


# thislist[1] = "blackcurrant"
# print(thislist)


# thislist[1:3] = ["blackcurrant", "watermelon"]
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# thislist[1:2] = ["blackcurrant", "watermelon"]
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist[1:3] = ["watermelon"]
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.insert(2, "watermelon")
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange")
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.insert(1, "orange")
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# thistuple = ("kiwi", "orange")
# thislist.extend(thistuple)
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# thislist.remove("banana")
# print(thislist)


# thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
# thislist.remove("banana")
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# thislist.pop(1)
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# thislist.pop()
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# del thislist[0]
# print(thislist)

#Delete the list
# thislist = ["apple", "banana", "cherry"]
# del thislist


#Clear the list
# thislist = ["apple", "banana", "cherry"]
# thislist.clear()
# print(thislist)


#For Loop
# thislist = ["apple", "banana", "cherry"]
# for i in range(len(thislist)):
#   print(thislist[i])


#While Loop
# thislist = ["apple", "banana", "cherry"]
# i = 0
# while i < len(thislist):
#   print(thislist[i])
#   i = i + 1


# thislist = ["apple", "banana", "cherry"]
# [print(x) for x in thislist]


# List Comprehension
# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.


# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []

# for x in fruits:
#   if "a" in x:
#     newlist.append(x)

# print(newlist)


# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newlist = [x for x in fruits if "a" in x]

# print(newlist)


# newlist = [expression for item in iterable if condition == True]
# The return value is a new list, leaving the old list unchanged.

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x for x in fruits if x != "apple"]

# print(newlist)

# newlist = [x for x in fruits]
# print(newlist)


# newlist = [x for x in range(10)]
# print(newlist)

# newlist = [x for x in range(10) if x < 5]

# newlist = [x.upper() for x in fruits]
# newlist = ['hello' for x in fruits]

# newlist = [x if x != "banana" else "orange" for x in fruits]


# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort()
# print(thislist)



# thislist = [100, 50, 65, 82, 23]
# thislist.sort()
# print(thislist)


# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort(reverse = True)
# print(thislist)


# def myfunc(n):
#   return abs(n - 50)

# thislist = [100, 50, 65, 82, 23]
# thislist.sort(key = myfunc)
# print(thislist)

# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort()
# print(thislist)


# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort(key = str.lower)
# print(thislist)

# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.reverse()
# print(thislist)

# Copy a List
# You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.


# thislist = ["apple", "banana", "cherry"]
# mylist = thislist.copy()
# print(mylist)


# thislist = ["apple", "banana", "cherry"]
# mylist = list(thislist)
# print(mylist)


# thislist = ["apple", "banana", "cherry"]
# mylist = thislist[:]
# print(mylist)


# Join Two Lists
# There are several ways to join, or concatenate, two or more lists in Python.

# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]

# list3 = list1 + list2
# print(list3)


# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]

# for x in list2:
#   list1.append(x)

# print(list1)


# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]

# list1.extend(list2)
# print(list1)
=======

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:])
# print(thislist[-4:-1])

# if "apple" in thislist:
#   print("Yes, 'apple' is in the fruits list")


# thislist[1] = "blackcurrant"
# print(thislist)


# thislist[1:3] = ["blackcurrant", "watermelon"]
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# thislist[1:2] = ["blackcurrant", "watermelon"]
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist[1:3] = ["watermelon"]
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.insert(2, "watermelon")
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange")
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.insert(1, "orange")
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# thistuple = ("kiwi", "orange")
# thislist.extend(thistuple)
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# thislist.remove("banana")
# print(thislist)


# thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
# thislist.remove("banana")
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# thislist.pop(1)
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# thislist.pop()
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# del thislist[0]
# print(thislist)

#Delete the list
# thislist = ["apple", "banana", "cherry"]
# del thislist


#Clear the list
# thislist = ["apple", "banana", "cherry"]
# thislist.clear()
# print(thislist)


#For Loop
# thislist = ["apple", "banana", "cherry"]
# for i in range(len(thislist)):
#   print(thislist[i])


#While Loop
# thislist = ["apple", "banana", "cherry"]
# i = 0
# while i < len(thislist):
#   print(thislist[i])
#   i = i + 1


# thislist = ["apple", "banana", "cherry"]
# [print(x) for x in thislist]


# List Comprehension
# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.


# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []

# for x in fruits:
#   if "a" in x:
#     newlist.append(x)

# print(newlist)


# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newlist = [x for x in fruits if "a" in x]

# print(newlist)


# newlist = [expression for item in iterable if condition == True]
# The return value is a new list, leaving the old list unchanged.

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x for x in fruits if x != "apple"]

# print(newlist)

# newlist = [x for x in fruits]
# print(newlist)


# newlist = [x for x in range(10)]
# print(newlist)

# newlist = [x for x in range(10) if x < 5]

# newlist = [x.upper() for x in fruits]
# newlist = ['hello' for x in fruits]

# newlist = [x if x != "banana" else "orange" for x in fruits]


# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort()
# print(thislist)



# thislist = [100, 50, 65, 82, 23]
# thislist.sort()
# print(thislist)


# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort(reverse = True)
# print(thislist)


# def myfunc(n):
#   return abs(n - 50)

# thislist = [100, 50, 65, 82, 23]
# thislist.sort(key = myfunc)
# print(thislist)

# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort()
# print(thislist)


# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort(key = str.lower)
# print(thislist)

# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.reverse()
# print(thislist)

# Copy a List
# You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.


# thislist = ["apple", "banana", "cherry"]
# mylist = thislist.copy()
# print(mylist)


# thislist = ["apple", "banana", "cherry"]
# mylist = list(thislist)
# print(mylist)


# thislist = ["apple", "banana", "cherry"]
# mylist = thislist[:]
# print(mylist)


# Join Two Lists
# There are several ways to join, or concatenate, two or more lists in Python.

# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]

# list3 = list1 + list2
# print(list3)


# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]

# for x in list2:
#   list1.append(x)

# print(list1)


<<<<<<< HEAD
# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]

<<<<<<< HEAD
list1.extend(list2)
print(list1)
>>>>>>> 657e2788b26a3df40cebc51677301887003e8f72
=======
# list1.extend(list2)
# print(list1)
>>>>>>> 1d1871b (commit test)
=======
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)
>>>>>>> 657e2788b26a3df40cebc51677301887003e8f72
>>>>>>> 6e7bb9b (commit conflict)
