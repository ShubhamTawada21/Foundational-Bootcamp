nested_list = []

for i in range(1, 10, 3):
    temp = []
    for j in range(i, i + 3):
        temp.append(j)
    nested_list.append(temp)

print(nested_list)

mat = [[1,2,3], [4,5,6], [7,8,9]]

for row in mat:
    for var in row:
        print(var)