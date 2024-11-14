# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

# (green, yellow, *red) = fruits

# print(green)
# print(yellow)
# print(red)


# fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

# (green, *tropic, red) = fruits

# print(green)
# print(tropic)
# print(red)


# thistuple = ("apple", "banana", "cherry")
# for x in thistuple:
#   print(x)


# thistuple = ("apple", "banana", "cherry")
# for i in range(len(thistuple)):
#   print(thistuple[i])


# thistuple = ("apple", "banana", "cherry")
# i = 0
# while i < len(thistuple):
#   print(thistuple[i])
#   i = i + 1

# thistuple = ["apple",]
# thistuple = ("apple",)
# print(type(thistuple))


# tuple1 = ("apple", "banana", "cherry")
# print(type(tuple1))

# tuple2 = (1, 5, 7, 9, 3)
# print(type(tuple2))

# tuple3 = (True, False, False)
# print(type(tuple3))
# tuple1 = ("abc", 34, True, 40, "male")


#tuple constructor
# thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
# print(thistuple)

#access Tuple
# thistuple = ("apple", "banana", "cherry")
# print(thistuple[1])

# thistuple = ("apple", "banana", "cherry")
# print(thistuple[-1])

# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[2:5])

# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[:4])


# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[2:])

# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[-4:-1])

# thistuple = ("apple", "banana", "cherry")
# if "apple" in thistuple:
#   print("Yes, 'apple' is in the fruits tuple")



#Convert the tuple into a list to be able to change it:
# x = ("apple", "banana", "cherry")
# y = list(x)
# y[1] = "kiwi"
# x = tuple(y)

# print(x)

#Convert the tuple into a list, add "orange", and convert it back into a tuple:
# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.append("orange")
# thistuple = tuple(y)
# print(thistuple)


# thistuple = ("apple", "banana", "cherry")
# y = ("orange",)
# thistuple += y

# print(thistuple)

#Convert the tuple into a list, remove "apple", and convert it back into a tuple:
# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.remove("apple")
# thistuple = tuple(y)
# print(thistuple)

#The del keyword can delete the tuple completely:
# thistuple = ("apple", "banana", "cherry")
# del thistuple
# print(thistuple) #this will raise an error because the tuple no longer exists

#Packing a tuple:
fruits = ("apple", "banana", "cherry")

#Unpacking a tuple:
# fruits = ("apple", "banana", "cherry")

# (green, yellow, red) = fruits

# print(green)
# print(yellow)
# print(red)


#dd a list of values the "tropic" variable:
# fruits = ("apple", "mango", "papaya", "pineapple", "pineapple1", "pineapple2", "cherry")

# (green, *tropic, red) = fruits

# print(green)
# print(tropic)
# print(red)