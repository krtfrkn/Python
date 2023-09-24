list1 = ["BMW","Mercedes","Opel","Mazda"]
result1 = len(list1)
print(result1)

result2 = [list1[0],list1[-1]]
print(result2)

empty = list1[1]
list1[1] = list1[-1]
list1[-1] = empty
result3 = list1.__contains__("Mercedes")
print(result3)

result4 = "Mercedes" in list1
print(result4)

result5 = list1 + ["Audi", "Nissan"]
print(result5)

del list1[0]
result6= list1
print(result6)

result7 = list1[::-1]
print(result7)