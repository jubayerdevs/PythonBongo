# username = input("Enter username:")
# print("Username is: " + username)


txt = f"The price is 49 dollars"
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)


txt = f"The price is {95:.2f} dollars"
print(txt)


txt = f"The price is {20 * 59} dollars"
print(txt)


price = 59
tax = 0.25
txt = f"The price is {price + (price * tax)} dollars"
print(txt)


price = 49
txt = f"It is very {'Expensive' if price>50 else 'Cheap'}"

print(txt)


fruit = "apples"
txt = f"I love {fruit.upper()}"
print(txt)


def myconverter(x):
  return x * 0.3048

txt = f"The plane is flying at a {myconverter(30000)} meter altitude"
print(txt)

# Formatting Types

price = 59000
txt = f"The price is {price:,} dollars"
print(txt)

#To demonstrate, we insert the number 8 to set the available space for the value to 8 characters.

#Use "^" to center-align the value:

txt = f"We have {49:^8} chickens."
print(txt)


#To demonstrate, we insert the number 8 to set the available space for the value to 8 characters.

#Use "<" to left-align the value:

txt = f"We have {49:<8} chickens."
print(txt)


#Use "b" to convert the number into binary format:

txt = f"The binary version of 5 is {5:b}"

print(txt)


#Use "_" to add a underscore character as a thousand separator:

txt = f"The universe is {13800000000:_} years old."

print(txt)



#Use "%" to convert the number into a percentage format:

txt = f"You scored {0.25:%}"
print(txt)

#Or, without any decimals:

txt = f"You scored {0.25:.0%}"
print(txt)



price = 49
txt = "The price is {} dollars"
print(txt.format(price))


txt = "The price is {:.2f} dollars"


quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))


quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))


age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))



myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))