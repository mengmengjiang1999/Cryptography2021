
virginia = "KCCPKBGUFDPHQTYAVINRRTMVGRKDNBVFDETDGILTXRGUDDKOTFMBPVGEGLTGCKQRACQCWDNAWCRXIZAKFTLEWRPTYCQKYVXCHKFTPONCOQRHJVAJUWETMCMSPKQDYHJVDAHCTRLSVSKCGCZQQDZXGSFRLSWCWSJTBHAFSIASPRJAHKJRJUMV GKMITZHFPDISPZLVLGWTFPLKKEBDPGCEBSHCTURWXBAFSPEZQNRWXCVYCGAONWDDKACKAWBBIKFTIOVKCGGHJVLNHIFFSQESVYCLACNVRWBBIREPBBVFEXOSCDYGZWPFDTKFQIYCWHJVLNHIQIBTKHJVNPIST"

from traceback import print_tb
from cv2 import RNG_NORMAL
from daihuan import calculate,calculate2,calculate3

# calculate(virginia)
# calculate2(virginia)
# calculate3(virginia)

pro_alpha = {
        "A":0.082,
        "B":0.015,
        "C":0.028,
        "D":0.043,
        "E":0.127,
        "F":0.022,
        "G":0.020,
        "H":0.061,
        "I":0.070,
        "J":0.002,
        "K":0.008,
        "L":0.040,
        "M":0.024,
        "N":0.067,
        "O":0.075,
        "P":0.019,
        "Q":0.001,
        "R":0.060,
        "S":0.063,
        "T":0.091,
        "U":0.028,
        "V":0.010,
        "W":0.023,
        "X":0.001,
        "Y":0.020,
        "Z":0.001,
}

input_virginia = '''KCCPKBGUFDPHQTYAVINRRTMVGRKDNBVFDETDGILTXRGUDDKOTFMBPVGEGLTGCKQRACQCWDNAWCRXIZAKFTLEWRPTYCQKYVXCHKFTPONCQQRHJVAJUWETMCMSPKQDYHJVDAHCTRLSVSKCGCZQQDZXGSFRLSWCWSJTBHAFSIASPRJAHKJRJUMVGKMITZHFPDISPZLVLGWTFPLKKEBDPGCEBSHCTURWXBAFSPEZQNRWXCVYCGAONWDDKACKAWBBIKFTIOVKCGGHJVLNHIFFSQESVYCLACNVRWBBIREPBBVFEXOSCDYGZWPFDTKFQIYCWHJVLNHIQIBTKHJVNPIST'''

def chonghezhishu(input: str):
    result = calculate(input)
    n = len(input)
    sum_fi = 0
    for key in result.keys():
        sum_fi += result[key]*(result[key]-1)
    return sum_fi/(n*(n-1))

def cut(input:str,m:int):
    n = len(input)
    n = n - (n%m) #使得n能够整除m
    y = []
    for j in range(m):
        yj = []
        y.append(yj)
    for i in range(int(n/m)):
        for j in range(m):
            y[j].append(input[i*m+j])
    return y

def calculate_chonghezhishu(input:str, m:int):
    print(input)
    y = cut(input,m)
    f = []
    for item in y:
        f.append(chonghezhishu(''.join(item)))
    print("m="+str(m)+"时重合指数为")
    print(f)
    # 到这里时，y里面有m个list，每个list都是分割后的字符串

def get_key(input:str, m:int, index:int, shift:int):
    y = cut(input, m)
    # print(input)
    # print(y)
    fi = calculate(y[index])
    # print(fi)
    n0 = len(y[index])
    pro_sum = 0
    for item in pro_alpha.keys():
        # print(item)
        pro_sum += pro_alpha[item] * fi[chr(((ord(item)-ord("A")+26-shift)%26)+ord("A"))]
        # print(pro_alpha[item],fi[chr(((ord(item)-ord("A")+26-shift)%26)+ord("A"))]/n0)
    return pro_sum/n0

def run():
    m = 6
    # for i in range(26):
    #     print(get_key(input_virginia, 5, 1, i))

    strings = []

    keys = []

    for index in range(0,m):
        loss = 10
        key = -1
        # print("index="+str(index))
        for i in range(26):
            # print("i=",i)
            pi = get_key(input_virginia, m, index, i)
            if(abs(pi-0.065)<loss):
                loss = abs(pi-0.065)
                key=i
        print("key="+str(key)+"\tloss="+str(loss))
        print(chr(ord("A")+26-key))
        keys.append(key)
        string = []
        y = cut(input_virginia, m)
        for item in y[index]:
            string.append(chr( (ord(item)-ord("A") + 26 - key)%26 + ord("A")))
        strings.append(string)


    mingwen = []

    print(keys)

    for i in range(len(input_virginia)):
        # print(i%m)
        # print(input_virginia[i])
        # print(chr(((ord(input_virginia[i])-ord("A")+26+keys[i%m])%26)+ord("A")))
        mingwen.append(chr(((ord(input_virginia[i])-ord("A")+26+keys[i%m])%26)+ord("A")))

    print("".join(mingwen))



    # pro_sum=0
    # for item in pro_alpha.keys():
    #     # print(item)
    #     # print(chr(((ord(item)-ord("A")+shift)%26)+ord("A")))
    #     pro_sum += pro_alpha[item] * pro_alpha[item]
    # print(pro_sum)

    # for i in range(1,10,1):
    #     calculate_chonghezhishu(input_virginia, i)

