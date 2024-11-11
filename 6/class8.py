#0 based index
my_list = [1, 2, 3, 4]
print(type(my_list))
print(len(my_list)) #length
print(my_list[2]) 
print(my_list[-1]) #get last element
print(my_list[::-1]) #reverse element
#add element
my_list.append(5)
print(my_list) #add element

my_list.insert(2,5) #index 2, item 5
my_list.remove(2)
my_list.insert(2, 'Nure')
#my_list.sort()
my_list.reverse() #

#add list
my_list2=[1, 4, 5]
my_list.extend(my_list2)
print(my_list)
x = my_list + my_list2
print(x)

#x = my_list+ 5 #error
#x = my_list+[5]

my_list3 = [1, 2, 2, 1, 4]
print(set(my_list3))#Unique data
#out put {1, 2, 4}
print(list(set(my_list3)))

#loop> for, while
my_list4 = [1, 2, 2, 0, 4]
#indentation-> space before print
for item in my_list4:
    print(item)
total = 0
for num in my_list4:
    total += num

print(total)


names = ['Nure', 'Taher', 'Anis']

for name in names:
    if name == 'Anis':
        print('Paisi')
        break
    else:
        print('Paini')


nums = [1, 2, 3]
#list comprehention
new_list = [num*2 for num in nums]


nums = [2, 5, 6]
nums.sort()
print(nums)


numsWhile = [3, 5, 4]
count = 0
while count < len(numsWhile):
    count = count + 1
    print('Hello there')
    
print(count)