list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = [11,12,13,14,15,16,17,18,19,20]
result = list1+[33]
list2.append(55)
result = list2
list1.insert(0,55)
result = list1
list1.pop()
list1.pop(0)
list1.remove(1)

names = ["furkan", "emine", "sude", "ceyda"]
ages = [35, 34, 10, 5]
names.append("ali")
names.insert(0,"veli")
names.pop(0)
names.remove("ali")
result = names.index("furkan")
result = "ali" in names
names.reverse()
names.sort()
result = names

list3 = ["y","e","a","r","s"]
list3.sort()
min = min(list3)
list3.clear()

str1 = "Chevrolet,Dacia"
list4 = str1.split(",")

result=list4
print(list3)

