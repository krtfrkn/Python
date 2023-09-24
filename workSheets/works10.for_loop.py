'''
numbers = [1,2,3,4,5,6,7]
name = 'furkan'
for x in name:
    print(x)

numbers = [1,3,5,7,9,12,19,21]
#1 which one can be diveded to 3
list3 = []
for x in numbers:
    if (x%3==0):
        list3.append(x)
print(list3)
#2 what is the total of the nums
total = 0;
for x in numbers:
    total+=x
print(total)
#3 what are the squared of odd numbers
list_squared= []
for x in numbers:
    if (x%2==1):
        list_squared.append(x**2)
print(list_squared)

cities = ["kocaeli","istanbul","ankara","izmir","rize"]
#1 which cities have max 5 characters
listCityMax5 = []
for x in cities:
    if (len(x) <=5):
        listCityMax5.append(x)
print(listCityMax5)
'''
items = [
    {'name':'samsung s6' , 'price' : '3000'},
    {'name':'samsung s7' , 'price' : '4000'},
    {'name':'samsung s8' , 'price' : '5000'},
    {'name':'samsung s9' , 'price' : '6000'},
    {'name':'samsung s10', 'price' : '7000'}
]
#1 what is the total of items
total = 0
for x in items:
    total+= int(x['price'])
print(total)

#2 what are the prices are max 5000
listMax5000 = []
for x in items:
    if (int(x['price'])<=5000):
        listMax5000.append(x['name'])
print(listMax5000)