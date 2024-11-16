import requests
import csv

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    
    with open('users.csv', 'w', newline='' ) as csvfile:
        fieldnames = ['Name', 'Email', 'City']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for user in data:
            writer.writerow(
                {
                    'Name': user['name'],
                    'Email': user['email'],
                    'City' : user['address']['city']
                }
            )

    #print(data)
    # print(data[0]['name'])
    # print(data[0]['username'])    
    # print(data[0]['email'])
    # print(data[0]['email'])

else:
    print("Bad request:", response.status_code)


