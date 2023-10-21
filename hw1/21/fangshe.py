
import numpy as np
from daihuan import calculate
from virginia import pro_alpha

input_fangshe = '''KQEREJEBCPPCJCRKIEACUZBKRVPKRBCIBQCARBJCVFCUPKRIOFKPACUZQEPBKRXPEIIEABDKPBCPFCDCCAFIEABDKPBCPFEQPKAZBKRHAIBKAPCCIBURCCDKDCCJCIDFUIXPAFFERBICZDFKABICBBENEFCUPJCVKABPCYDCCDPKBCOCPERKIVKSCPICBRKIJPKABI'''

freq = calculate(input_fangshe)

print(freq)

def find_reverse(a:int):
    if a==1:
        return 1
    elif a==3:
        return 9
    elif a==5:
        return 21
    elif a==7:
        return 15
    elif a==11:
        return 19
    elif a==17:
        return 23
    elif a==25:
        return 25
    else:
        return -1

def get(guess1:int, guess2:int, ans1:int, ans2:int):
    pass

def jiami(input:str,a:int,b:int):
    input_list = list(input)
    for i in range(len(input_list)):
        id = (a * (ord(input_list[i]) - ord("A")) + b + 26)%26
        input_list[i] = chr(id+ord("A"))
    return "".join(input_list)

def jiemi(input:str, a:int, b:int):
    input_list = list(input)
    for i in range(len(input_list)):
        id = (  find_reverse(a) * ( (ord(input_list[i]) - ord("A")) - b + 26) )%26
        input_list[i] = chr( id +ord("A"))
    return "".join(input_list)


# 验证加密解密函数正确
for a in range(1,26):
    for b in range(0,26):
        if(find_reverse(a)>=0):
            assert(input_fangshe==jiami(jiemi(input_fangshe, a, b), a, b))
            assert(input_fangshe==jiemi(jiami(input_fangshe, a, b), a, b))


def get_pro(input:str):
    fi = calculate(input)
    n0 = len(input)
    pro_sum = 0
    for item in pro_alpha.keys():
        pro_sum += pro_alpha[item] * fi[item]
    return pro_sum/n0


loss = 10
ans_a = -1
ans_b = -1
ans_string = ""
for a in range(26):
    for b in range(26):
        if(find_reverse(a)>=0):
            string = jiemi(input_fangshe, a, b)
            pro = get_pro(string)
            if abs(pro-0.065)<loss:
                loss = abs(pro-0.065)
                ans_a = a
                ans_b = b
                print("loss=",loss)
                ans_string = string
                print(ans_string)

print(loss, ans_a, ans_b)
print(ans_string)

