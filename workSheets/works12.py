import math
import random

number = random.randint(0, 100)
#print(number)
totalScore=100
enteeNumber = int(input("pls enter the number of entee: "))
scorePerEntee=totalScore/enteeNumber
itr = 0
resultFlag = False
while itr<enteeNumber:
    estimation = int(input("pls estimate the number: "))
    if estimation>=0 and estimation<=100:
        if estimation==number:
            print(f'You won and your score is {math.ceil(totalScore)}')
            resultFlag=True
            break
        elif estimation<number:
            print(f'<UP> => You have {enteeNumber - (itr + 1)}')
            totalScore-=scorePerEntee
        elif estimation>number:
            print(f'<DOWN> => You have {enteeNumber - (itr + 1)}')
            totalScore -= scorePerEntee
        itr+=1
    else:
        print('Your estimation should be 0-100')
if resultFlag==False:
    print(f'You lost, the number was {number}')