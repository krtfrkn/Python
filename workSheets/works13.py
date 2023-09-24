num = int(input("pls enter your number: "))
itr = 1
total = 0
while itr<=num:
    if num%itr==0:
        total+=1
    itr+=1
if total==2:
    print("it is prime number")
else:
    print("it is NOT prime number")