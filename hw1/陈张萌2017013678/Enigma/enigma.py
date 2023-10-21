WIRINGS = [
    "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
    "AJDKSIRUXBLHWTMCQGZNPYFVOE",
    "BDFHJLCPRTXVZNYEIWGAKMUSQO",
]
NOTCHS = ["Q", "E", "V"]
REFLECTOR = "YRUHQSLDPXNGOKMIEBFZCWVJAT"

def index(x):
    if type(x) == str:
        return ord(x.upper()) - 65
    else:
        return x

def alpha(i):
    return chr(i + 65)

def get_diff(a, b):
    s = 0
    for x, y in zip(a, b):
        if x != y:
            s += 1
    return s

class Rotor:
    def __init__(self, wiring: str, notch: int):
        assert len(wiring) == 26
        self.state = []
        self.decode_state = [0] * 26
        self.notch = index(notch)
        self.init_pos = 0
        self.rotate_times = 0
        for i in range(26):
            delta = (index(wiring[i]) - i + 26) % 26
            self.state.append(delta)
            delta = (i - index(wiring[i]) + 26) % 26
            self.decode_state[index(wiring[i])] = delta

    def init(self, ring_set: int, pos: int):
        ring_set = ring_set % 26
        pos = pos % 26
        self.rotate(pos - ring_set)
        self.rotate_times = 0
        self.init_pos = pos

    def __str__(self):
        return "{%d, %s, %s}" % (self.init_pos, self.state, self.decode_state)

    def __repr__(self):
        return self.__str__()

    def reset(self):
        self.rotate(-self.rotate_times)

    def rotate(self, steps: int):
        if steps < 0:
            steps = steps % 26
        advance = steps == 1 and (self.init_pos + self.rotate_times) % 26 == self.notch
        self.rotate_times += steps
        self.state = self.state[steps:] + self.state[:steps]
        self.decode_state = self.decode_state[steps:] + self.decode_state[:steps]
        return advance

    def encode(self, text: str):
        cipher = ""
        for c in text:
            x = index(c)
            y = (x + self.state[x] + 26) % 26
            cipher += chr(y + 65)
        return cipher

    def decode(self, cipher: str):
        text = ""
        for c in cipher:
            x = index(c)
            y = (x + self.decode_state[x] + 26) % 26
            text += chr(y + 65)
        return text


class Enigma:
    def __init__(self, order: tuple[int, int, int], ring_set: tuple[int, int, int],
                init_pos: tuple[int, int, int]):
        self.ref = Rotor(REFLECTOR, 0)
        self.rotors = []
        self.order = order
        self.times = 0
        for i in range(3):
            rotor = Rotor(WIRINGS[order[i]], NOTCHS[order[i]])
            rotor.init(index(ring_set[i]), index(init_pos[i]))
            self.rotors.append(rotor)

    def reset(self):
        self.times = 0
        for r in self.rotors:
            r.reset()

    def encrypt(self, text: str):
        cipher = ""
        for c in text:
            if self.rotors[2].rotate(1):
                if self.rotors[1].rotate(1):
                    self.rotors[0].rotate(1)
            # print(self.times, self.rotors)
            c = self.rotors[2].encode(c)
            c = self.rotors[1].encode(c)
            c = self.rotors[0].encode(c)
            c = self.ref.encode(c)
            c = self.rotors[0].decode(c)
            c = self.rotors[1].decode(c)
            c = self.rotors[2].decode(c)
            cipher += c
        return cipher


def get_loops(perm):
    assert len(perm) == 26
    visited = [False for _ in range(26)]
    loops = []
    lens = []
    for i in range(len(perm)):
        loop = []
        if not visited[i]:
            j = i
            while True:
                visited[j] = True
                loop.append(j)
                j = index(perm[j])
                if j == i:
                    break
            loops.append(loop)
            lens.append(len(loop))
    # print(loops, lens)
    return loops, sorted(lens)

def gen_perms(e: Enigma):
    p = [[0] * 26, [0] * 26, [0] * 26]
    for i in range(26):
        text = alpha(i) * 6
        e.reset()
        cipher = e.encrypt(text)
        # cipher2 = e.encrypt(cipher1)

        for j in range(3):
            idx = index(cipher[j])
            if p[j][idx] != 0:
                assert p[j][idx] == cipher[j + 3]
            p[j][idx] = cipher[j + 3]
    p = ["".join(i) for i in p]
    return p


if __name__ == '__main__':
    print(Rotor(WIRINGS[2], 0))
    P = [
        "OIWNDQRZLYHSGCXTUBFEKJVPAM",
        "ISYGNUKWRXDMQOETVPBZAJHCLF",
        "MYACVNWOIRQEGBLPJUHKTSDFZX",
        # "FQHPLWOGBMVRXUYCZITNJEASDK",
        # "XUYCZITNJEASDKFQHPLWOGBMVR",
        # "GBMVRXFQHPLWOUYCEASDKZITNJ",
    ]
    lens = []
    for i in range(3):
        o, l = get_loops(P[i])
        print(o)
        lens.append(l)
    # lens[1] = [2, 3, 9 ,12]
    # lens[2] = [3, 5, 5, 5, 8]
    print(lens)

    # r = Rotor(WIRINGS[2])
    # for i in range(26):
    #     x = alpha(i)
    #     y = r.encode(x)
    #     z = r.decode(y)

    e = Enigma([0, 2, 1], ['G', 'Y', 'E'], [0, 0, 0])
    text = "AAAMSH"
    cipher = e.encrypt(text)
    print(cipher)
    # exit(0)
    p = gen_perms(e)
    print(p)
    # lens = []
    for i in range(3):
        _, l = get_loops(p[i])
        print(l)
        print(p[i])
        print(P[i])
        print(get_diff(p[i], P[i]))
        # lens.append(l)

    # exit(0)

    for pos in [(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)]:
        for a in range(26):
            # print(pos, a)
            for b in range(26):
                for c in range(26):
                    e = Enigma(pos, (a, b, c), (0, 0, 0))
                    p = gen_perms(e)

                    o1, l1 = get_loops(p[0])
                    o2, l2 = get_loops(p[1])
                    o3, l3 = get_loops(p[2])
                    if l1 == lens[0] and l2 == lens[1] and l3 == lens[2]:
                        e.reset()
                        print(e.encrypt("AAAAAA"))
                        print(pos, (a, b, c), (alpha(a), alpha(b), alpha(c)))
                        print("    ", p)
                        print("    ", o1, l1)
                        print("    ", o2, l2)
                        print("    ", o3, l3)
                        print("")
                        # input()

