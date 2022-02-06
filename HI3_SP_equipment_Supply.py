import random
import copy
import winsound as sd


def gacha_defin() :
    r = random.randrange(1,1000+1)

    result = 1

    if(r<=200):
        result = 2
    elif(r<=300):
        result = 3
    elif(r<=400):
        result = 5
    elif (r <= 500):
        result = 7

    return result
def gacha_defin_2(result) :

    select=[]


    if (result % 2 != 0):
        select.append(2)
    if(result % 3 != 0):
        select.append(3)
    if (result % 5 != 0):
        select.append(5)
    if (result % 7 != 0):
        select.append(7)

    r = random.randrange(0,len(select))

    result = select[r]

    return result

def gacha_normal() :
    r = random.randrange(1, 1000000+1)

    result=1

    if(r<=74000):
        result = 11

        if(r<=14800):
            result = 2
        elif(r<=22200):
            result = 3
        elif(r<=29600):
            result =5
        elif(r<=37000):
            result = 7

    return result

# num 2 is pick-up weapon , num 3,5,7 are pick-up stigmatas 
pass_condition_result0 =\
    [2]#무기만

pass_condition_result1 = \
    [3,5,7]#성흔 1개

pass_condition_result2 =\
    [3*5, 3*7, 5*7]# 성흔2개

pass_condition_result3 =\
    [3*5*7]#성흔종결

pass_condition_result4 =\
    [2 * 3, 2*5, 2*7]# 무기 + 성흔1부위

pass_condition_result5 =\
    [2*3*5, 2*3*7, 2*5*7]# 무기 + 성흔 2부위

pass_condition_complete =\
    [2*3*5*7] # 여기까지종결


R0=0
R1=0
R2=0
R3=0
R4=0
R5=0
R6=0

repeat = 10000000#The total number of simulations = Accuracy 
retry =29#The number of pulls in one simulation

for k in range(0,repeat):
    temp_arr0 = copy.deepcopy(pass_condition_result0)
    temp_arr1 = copy.deepcopy(pass_condition_result1)
    temp_arr2 = copy.deepcopy(pass_condition_result2)
    temp_arr3 = copy.deepcopy(pass_condition_result3)
    temp_arr4 = copy.deepcopy(pass_condition_result4)
    temp_arr5 = copy.deepcopy(pass_condition_result5)
    temp_arr6 = copy.deepcopy(pass_condition_complete)

    stack = 0
    result =1

    for i in range(1, retry+1):

        gacha_num=1

        if(i % 30==0):
            if (result % 210 != 0): # 2*3*5*7= 210
                gacha_num = gacha_defin_2(result)
            stack =0

        elif(stack ==9):
            gacha_num=gacha_defin()
            if(gacha_num==11):
                gacha_num=1
            stack =0

        elif(stack != 9):
            gacha_num=gacha_normal()

            if(gacha_num == 1):
                stack = stack+1
            else:
                stack = 0
                if(gacha_num ==11):
                    gacha_num=1

        result = result * gacha_num

    for j in range(0, len(temp_arr0)):
        temp = temp_arr0[j]

        if(result % temp ==0):
            R0=R0+1
            break

    for j in range(0, len(temp_arr1)):
        temp = temp_arr1[j]

        if (result % temp == 0):
            R1 = R1 + 1
            break

    for j in range(0, len(temp_arr2)):
        temp = temp_arr2[j]

        if (result % temp == 0):
            R2 = R2 + 1
            break

    for j in range(0, len(temp_arr3)):
        temp = temp_arr3[j]

        if (result % temp == 0):
            R3 = R3 + 1
            break

    for j in range(0, len(temp_arr4)):
        temp = temp_arr4[j]

        if (result % temp == 0):
            R4 = R4 + 1
            break

    for j in range(0, len(temp_arr5)):
        temp = temp_arr5[j]

        if (result % temp == 0):
            R5 = R5 + 1
            break

    for j in range(0, len(temp_arr6)):
        temp = temp_arr6[j]

        if (result % temp == 0):
            R6 = R6 + 1
            break

print("무기만 : "+ str(R0))
print("성흔 1부위 : "+ str(R1))
print("성흔 2부위 : "+ str(R2))
print("성흔 종결 : "+ str(R3))
print("무기 + 성흔 1부위 : "+ str(R4))
print("무기 + 성흔 2부위 : "+ str(R5))
print("종결 : "+ str(R6))
