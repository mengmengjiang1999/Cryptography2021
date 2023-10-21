import numpy as np

def index(item: str)->int:
    assert(len(item)==1)
    assert(ord(item)>=ord('A'))
    assert(ord(item)<=ord('Z'))
    return ord(item)-ord('A')

def calculate(input: str):
    # result = np.zeros((26,)).tolist()
    # for item in input.upper():
    #     result[index(item)] = result[index(item)] + 1
    # for i in range(len(result)):
    #     print(chr(i+ord('A'))+"\t"+str(int(result[i]))+"\t"+str(int(result[i])/len(input)))
    result = {}
    for item in range(ord("A"), ord("Z")+1, 1):
        result[chr(item)] = 0
    for i in range(len(input)):
        if(ord(input[i])>=ord("A") and ord(input[i])<=ord("Z")):
            result[input[i]] = result.get(input[i], 0) + 1
    result = dict(sorted(result.items(), key=lambda item: item[1], reverse=True))
    # print(result)
    return result

def calculate2(input: str):
    result = {}
    for i in range(len(input)-1):
        result[input[i]+input[i+1]] = result.get(input[i]+input[i+1], 0) + 1
    result = dict(sorted(result.items(), key=lambda item: item[1], reverse=True))
    # print(result)
    return result

def calculate3(input: str):
    result = {}
    for i in range(len(input)-3):
        result[input[i]+input[i+1]+input[i+2]] = result.get(input[i]+input[i+1]+input[i+2], 0) + 1
    result = dict(sorted(result.items(), key=lambda item: item[1], reverse=True))
    # print(result)
    return result

def tihuan(input:str, howto: list):
    upinput = list(input.upper())
    answer = ['-']*len(upinput)
    print(upinput)
    for i in range(len(upinput)):
        if howto[index(upinput[i])] !=0:
            upinput[i]=howto[index(upinput[i])]
            answer[i]=upinput[i]
    print(''.join(input))
    # print(''.join(upinput))
    print(''.join(answer))

input_daihuan = "EMGLOSUDCGDNCUSWYSFHNSFCYKDPUMLWGYICOXYSIPJCKQPKUGKMGOLICGINCGACKSNISACYKZSCKXECJCKSHYSXCGOIDPKZCNKSHICGIWYGKKGKGOLDSILKGOIUSIGLEDSPWZUGFZCCNDGYYSFUSZCNXEOJNCGYEOWEUPXEZGACGNFGLKNSACIGOIYCKXCJUCIUZCFZCCNDGYYSFEUERUZCSOCFZCCNOIACZEJNCSHFZEJZEGMXCYHCJUMGKUCY"


def run():
    calculate(input_daihuan)
    calculate2(input_daihuan)
    calculate3(input_daihuan)

    how_daihuan = np.zeros((26,)).tolist()
    print(how_daihuan)
    how_daihuan[index("C")]="E"
    how_daihuan[index("Z")]="H"
    how_daihuan[index("F")]="W"
    # ===
    how_daihuan[index("N")]="L"
    # D=B,G=A,Y=R,S=O
    how_daihuan[index("G")]="A"
    how_daihuan[index("D")]="B"
    how_daihuan[index("Y")]="R"
    how_daihuan[index("S")]="O"
    # --A--O-BEABLE-O一
    how_daihuan[index("U")]="T"
    how_daihuan[index("W")]="G"
    how_daihuan[index("H")]="F"
    how_daihuan[index("O")]="N"
    how_daihuan[index("I")]="D"

    how_daihuan[index("P")]="U"

    how_daihuan[index("X")]="P"
    how_daihuan[index("J")]="C"
    # GROWFLOWER-
    how_daihuan[index("K")]="S"
    how_daihuan[index("Q")]="J"
    how_daihuan[index("E")]="I"

    how_daihuan[index("A")]="V"
    how_daihuan[index("R")]="S"

    how_daihuan[index("M")]="M"
    how_daihuan[index("L")]="Y"

    tihuan(input_daihuan, how_daihuan)

    for i in range(26):
        print(str(i)+"\t"+chr(ord("A")+i))