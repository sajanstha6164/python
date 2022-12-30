name=[["sajan","shrestha"],
["deep","khadka"],
["devraj","silwal"]]
print(name[0][0])
print(name[0][1])
print(name[1][0])
print(name[1][1])
print(name[2][0])
print(name[2][1])

print("By the help of nested loop")
for row in range(len(name)):
    for column in range(len(name[row])):
        print(name[row][column])
