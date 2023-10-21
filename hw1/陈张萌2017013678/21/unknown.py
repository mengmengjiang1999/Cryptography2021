input_unknown = '''BNVSNSIHQCEELSSKKYERIFJKXUMBGYKAMQLJTYAVFBKVTDVBPVVRJYYLAOKYMPQSCGDLFSRLLPROYGESEBUUALRWXMMASAZLGLEDFJBZAVVPXWICGJXASCBYEHOSNMULKCEAHTQOKMFLEBKFXLRRFDTZXCIWBJSICBGAWDVYDHAVFJXZIBKC GJIWEAHTTOEWTUHKRQVVRGZBXYIREMMASCSPBHLHJMBLRFFJELHWEYLWISTFVVYEJCMHYUYRUFSFMGESIGRLWALSWMNUHSIMYYITCCOPZSICEHBCCMZFEGVJYOCDEMMPGHVAAUMELCMOEHVLTIPSUYILVGFLMVWDVYDBTHFRAYISYSGKVSUUHYHGGCKTMBLRX'''

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

def calculate(input: str):
    result = {}
    for item in range(ord("A"), ord("Z")+1, 1):
        result[chr(item)] = 0
    for i in range(len(input)):
        if(ord(input[i])>=ord("A") and ord(input[i])<=ord("Z")):
            result[input[i]] = result.get(input[i], 0) + 1
    result = dict(sorted(result.items(), key=lambda item: item[1], reverse=True))
    return result

def chonghezhishu(input: str):
    result = calculate(input)
    n = len(input)
    sum_fi = 0
    for key in result.keys():
        sum_fi += result[key]*(result[key]-1)
    return sum_fi/(n*(n-1))

def calculate_chonghezhishu(input:str, m:int):
    print(input)
    y = cut(input,m)
    f = []
    for item in y:
        f.append(chonghezhishu(''.join(item)))
    print("m="+str(m)+"时重合指数为")
    print(f)
    # 到这里时，y里面有m个list，每个list都是分割后的字符串


for m in range(1,10):
    calculate_chonghezhishu(input_unknown, m)