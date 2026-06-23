for i in range(1, 11):
    row = []
    for j in range(1, 11):
        value = i * j
        if value % 5 == 0:
            continue
        row.append(str(value))
    print("\t".join(row))
