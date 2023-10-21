input = 'MYAMRARUYIQTENCTORAHROYWDSOYEOUARRGDERNOGW'
# input = 'CTAROPYGHPRY'
LEN = len(input)

for l in range(1, LEN +1):
    for n in range(1, LEN + 1):
        if l % n == 0:
            m = l // n

            text = ''
            for k in range(0, LEN, l):
                for i in range(n):
                    for j in range(m):
                        if k + i + j * n < LEN:
                            text += input[k + i + j * n]
            print(l, n, m, text.lower())
