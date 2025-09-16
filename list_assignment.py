my_list = []
values = [10,20,30,40]
for value in values:
    my_list.append(value)
my_list.insert(1,15)
another_list = [50,60,70]
my_list.extend(another_list)
del my_list[-1]
my_list.sort()
index = my_list.index(30)
print(index)
