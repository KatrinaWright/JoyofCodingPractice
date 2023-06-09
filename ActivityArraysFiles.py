
#Create an array
Array = []
file = open("turing.txt")
for line in file:
    Array.append(line.rstrip())
file.close()
print(Array[0])
print(Array[-2], Array[-1])
print(len(Array))