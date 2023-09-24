'''x = int(input("Please give a number for x: "))
y = int(input("Please give a number for y: "))

if x>y:
    print("x is bigger than y")
elif y>x:
    print("y is bigger than x")
else:
    print("x equals y")
#-------------------------------------------------------------
age = int(input("enter your age: "))
graduation = input("enter your graduation: ")
if age >= 18:
    if graduation.upper() == "university".upper() or graduation.upper() == "high school".upper():
        print("You are eligible to have Licance")
    else:
        print("You are NOT eligible to have Licance. Because your degree is not efficient")
else:
    print("You are NOT eligible to have Licance. Because your age is not efficient")
#-------------------------------------------------------------
written1 = int(input("Enter your first written exam note: "))
written2 = int(input("Enter your second written exam note: "))
oral = int(input("Enter your second oral exam note: "))
avarage = (written1+written2+oral)/3
if avarage>=0 and avarage<=24:
    print(("Your avarage is " + str(avarage)))
    print("Your rate is 0")
elif avarage>=25 and avarage<=44:
    print(("Your avarage is " + str(avarage)))
    print("Your rate is 1")
elif avarage >= 45 and avarage <= 54:
    print(("Your avarage is " + str(avarage)))
    print("Your rate is 2")
elif avarage >= 55 and avarage <= 69:
    print(("Your avarage is " + str(avarage)))
    print("Your rate is 3")
elif avarage >= 70 and avarage <= 84:
    print(("Your avarage is " + str(avarage)))
    print("Your rate is 4")
elif avarage >= 85 and avarage <= 100:
    print(("Your avarage is " + str(avarage)))
    print("Your rate is 5")
else:
    print("Your entrance is wrong")'''


