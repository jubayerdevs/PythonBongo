import requests
import csv

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    
    with open('users.csv', 'w', newline='') as csvfile:
        fieldnames = ['Name', 'Email', 'City']
        writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
        
        writer.writeheader()
        # print(data[0]['name'])
        # print(data[0]['email'])

else:
    print("Bad request: ", response.status_code)



#numbers = [1,2,3,4,5]
# numList = []
# new_list = [x+1 for x in numbers]
# print(new_list)

# print("Heloo")

# list_with_for=[]

# for i in numbers:
#     list_with_for.append( i+1)
    
#     print("With For loop", list_with_for)

# list_with_while = []

# j=0
    
# while j< len(numbers):
#     list_with_while.append(numbers[j] + 1)
#     j = j+1
    
#     print("with while loop", list_with_while)


# with open("hello.txt") as file:
#     for line in file:
#         if "ERROR" in line:
#             print(line.strip())


