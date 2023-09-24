import sys

numbers = [1,3,5,7,9,12,19,21]
num=0
'''
list = []
x=1
while x<100:
    if x%2==1:
        list.append(x)
    x+=1
print(list)
#-------------------------------------------------------------
while num< len(numbers):
    print(numbers[num])
    num+=1
#-------------------------------------------------------------
start = int(input("Enter start num: "))
if start not in numbers: print("There is no such this number in the list") , sys.exit()
end = int(input("Enter end number: "))
if end not in numbers: print("There is no such this number in the list"), sys.exit()
newList = []
startIndex=numbers.index(start)
lastIndex=numbers.index(end)
while num< len(numbers):
    if num>=startIndex and num<=lastIndex:
        newList.append(numbers[num])
    num+=1
print(newList)
#-------------------------------------------------------------
list=[]
x=0
while x<=100:
    list.append(x)
    x+=1
print(list.sort(reverse=True))
print(list)
#-------------------------------------------------------------
x=0
list=[]
while x<5:
    list.append(input(f"Pls enter num {x+1}: "))
    x+=1
list.sort()
print(list)
#-------------------------------------------------------------
x=0
times = int(input("pls enter number of items: "))
list={}
while x<times:
    list[input("pls enter name of item: ")] = int(input("pls enter the price of item: "))
    x+=1
print(list)
#-------------------------------------------------------------
x=0
times = int(input("pls enter number of items: "))
list=[]
while x<times:
    name = input("pls enter name of item: ")
    price = int(input("pls enter price of item: "))
    list.append({
        'name':name,
        'price':price
    })
    x+=1
for item in list:
    print(f"item name: {item['name']} item price: {item['price']} ")
    '''
#-------------------------------------------------------------


