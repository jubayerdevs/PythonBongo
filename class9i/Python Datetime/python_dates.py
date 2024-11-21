import datetime

x = datetime.datetime.now()
print(x)

# import datetime

# x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))


# import datetime
# Display the name of the month:
x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))
print(x.strftime("%j"))
print(x.strftime("%W"))
print(x.strftime("%X"))
print(x.strftime("%G"))
print(x.strftime("%V"))
print(x.strftime("%p"))
print(x.strftime("%Z"))
print(x.strftime("%U"))


