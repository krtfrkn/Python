list1 = ["BMW","Mercedes","Opel","Mazda"]
result = len(list1)
result = [list1[0],list1[-1]]
empty = list1[1]
list1[1] = list1[-1]
list1[-1] = empty
result = list1.__contains__("mercedes")
result = "Mercedes" in list1
result = list1 + ["Audi", "Nissan"]
del list1[0]
result = list1
result = list1[::-1]
print(result)