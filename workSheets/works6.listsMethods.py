list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = [11,12,13,14,15,16,17,18,19,20]
list1 = list1+[33]
print(list1)
list2.append(55)
print(list2)

list1.insert(0,55)
print(list1)
list1.pop()
print(list1)
list1.pop(0)
print(list1)
list1.remove(6)
print(list1)
names = ["furkan", "emine", "sude", "ceyda"]
print(names)
ages = [35, 34, 10, 5]
print(ages)
names.append("ali")
print(names)
names.insert(0,"veli")
print(names)
names.pop(0)
print(names)
names.remove("ali")
print(names.index("furkan"))
print("ali" in names)
print(names.reverse())
print(names.sort())

list3 = ["y","e","a","r","s"]
list3.sort()
print(list3)
list3.reverse()
print(list3)
min = min(list3)
print(list3)
list3.clear()
print(list3)

str1 = "Chevrolet,Dacia"
list4 = str1.split(",")

result=list4
print(list4)

