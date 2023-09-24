square = lambda x: x ** 2
numbers = [2,3,4,5,6,7,8,9,10]
#-------------------------------------------------
result1 = square(3)
print(result1)
#-------------------------------------------------
result2 = list(map(square,numbers))
print(result2)
#-------------------------------------------------
def check_even(num) : return num%2 == 0
result3 = list(filter(check_even,numbers))
print(result3)
#-------------------------------------------------
result4 = list(filter(lambda num: num%2==0,numbers))
print(result4)