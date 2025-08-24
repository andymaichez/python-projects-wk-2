# This code demonstrates various list operations in Python.
my_list = []

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)


my_list.insert(1, 15)
print(my_list)

new_list =[50, 60, 70]
my_list.extend(new_list)
print(my_list)

my_list.pop()
print(my_list)

my_list.sort()
print(my_list)

index_30 = my_list.index(30)
print("index of 30:", index_30)
