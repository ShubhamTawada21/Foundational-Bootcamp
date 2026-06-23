A = [15, 25, 8, 22, 19, 30]
B = [5, 12, 13, 18, 3, 20]
greater_than_10 = [x for x in B if x > 10]
result = [x for x in A if x > max(greater_than_10)]
print("Elements from A greater than", max(greater_than_10), ":", result)
