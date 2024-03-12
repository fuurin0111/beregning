def plus(num:int=0,num2:int=0):
    return num+num2

def mult(num:int=0,num2:int=0):
    henge = max(num,num2)
    liten = min(num,num2)
    return_num = 0 
    for i in range(henge):
        return_num = plus(liten,return_num)
    return round(return_num,5)

def minus(num:int=0,num2:int=0):
    num2 = bitomd(num2)
    return plus(num,num2)

def dele(num:int=0,num2:int=1):
    num = mult(num,100000)
    i = 0
    flag = True
    while flag:
        if num >= num2:
            num = minus(num,num2)
            i = plus(i,1)
        else:
            flag = False
    return round(i/100000,5)

def bitomd(num:int):
    num = list(bin(num))
    if num[0] == "-":
        num.insert(3, '1')
    else:
        num.insert(2, '0')
    num = "".join(num)
    if num[0] == "-":
        num = num[1:]
    pre_num = "0b"

    for i in range(len(num)-2):
        pre_num += str(int(not(int(num[i+2]))))
    
    pre_num = list(pre_num)
    flag = True
    for i in range(len(pre_num)-2):
        if flag:
            if pre_num[len(pre_num)-1-i] == "0":
                pre_num[len(pre_num)-1-i] = "1"
                flag = False
            else:
                pre_num[len(pre_num)-1-i] = "0"
    pre_num = "".join(pre_num)

    max_num = "0b"
    max_num += "1"*(len(pre_num)-3)
    max_num = plus(int(max_num,2),1)

    if pre_num[2] == "1":
        pre_num = list(pre_num)
        pre_num[2] = "0"
        pre_num = "".join(pre_num)
        return plus(int(pre_num,2),mult(-1,max_num))
    else:
        return int(pre_num,2)

# print(plus(10,20))
# print(minus(10,20))
# print(mult(10,20))
# print(dele(10,20))