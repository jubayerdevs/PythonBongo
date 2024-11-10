numbers = [1, 2, 3, 4, 5]
list_with_for = []

for i in numbers:
    list_with_for.append(i + 1)
print("with for loop", list_with_for)


list_with_while = []
j = 0

while j < len(numbers):
    list_with_while.append(numbers[j] + 1)
    j = j + 1
print("with while loop", list_with_while)