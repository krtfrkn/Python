'''
def myFunction(name):
    print(name+"'s function is very good")
myFunction('Furkan')
#-------------------------------------------------
def addition(num1,num2):
    return num1+num2
total = addition(400,576)
print(total)
#-------------------------------------------------
def displayWord(word,x):
    itr=0
    while itr<x:
        print(word)
        itr+=1
displayWord("furkan",5)
#-------------------------------------------------
def createList(*item):
    list=[]
    for x in item:
        list.append(x)
    return list
print(createList("furkan", True, 5))
#-------------------------------------------------
def findPrimeNumbers(num1,num2):
    list=[]
    primeNumbers=[]
    x=num1+1
    while x<num2:
        list.append(x)
        x=x+1
    for x in list:
        itr = 1
        total = 0
        while itr <= x:
            if x % itr == 0:
                total += 1
            itr += 1
        if total == 2:
            primeNumbers.append(x)
    return primeNumbers

num1 = int(input('pls enter first number: '))
num2 = int(input('pls enter second number: '))

print(findPrimeNumbers(num1, num2))
#-------------------------------------------------
'''
def subMultiple(num):
    itr=1
    listSubMultiple=[]
    while itr<=num:
        if num%itr==0:
            listSubMultiple.append(itr)
        itr+=1
    return listSubMultiple

num=int(input("pls enter the number: "))
print(subMultiple(num))