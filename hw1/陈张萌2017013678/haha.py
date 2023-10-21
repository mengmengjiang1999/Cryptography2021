my_input = '''A cryptocurrency, crypto-currency, or crypto is a digital currency designed to work as a medium of exchange through a computer network that is not reliant on any central authority, such as a government or bank, to uphold or maintain it.

Individual coin ownership records are stored in a digital ledger, which is a computerized database using strong cryptography to secure transaction records, to control the creation of additional coins, and to verify the transfer of coin ownership.[1][2][3] Despite their name, cryptocurrencies are not necessarily considered to be currencies in the traditional sense and while varying categorical treatments have been applied to them, including classification as commodities, securities, as well as currencies, cryptocurrencies are generally viewed as a distinct asset class in practice.[4][5][6] Some crypto schemes use validators to maintain the cryptocurrency. In a proof-of-stake model, owners put up their tokens as collateral. In return, they get authority over the token in proportion to the amount they stake. Generally, these token stakers get additional ownership in the token over time via network fees, newly minted tokens or other such reward mechanisms.[7]

Cryptocurrency does not exist in physical form (like paper money) and is typically not issued by a central authority. Cryptocurrencies typically use decentralized control as opposed to a central bank digital currency (CBDC).[8] When a cryptocurrency is minted or created prior to issuance or issued by a single issuer, it is generally considered centralized. When implemented with decentralized control, each cryptocurrency works through distributed ledger technology, typically a blockchain, that serves as a public financial transaction database.[9]

A cryptocurrency is a tradable digital asset or digital form of money, built on blockchain technology that only exists online. Cryptocurrencies use encryption to authenticate and protect transactions, hence their name. There are currently over a thousand different cryptocurrencies in the world.[10]

Bitcoin, first released as open-source software in 2009, is the first decentralized cryptocurrency. Since the release of bitcoin, many other cryptocurrencies have been created.'''

my_input2 = '''
Computer science is the study of computation, automation, and information.[1] Computer science spans theoretical disciplines (such as algorithms, theory of computation, and information theory) to practical disciplines (including the design and implementation of hardware and software).[2][3] Computer science is generally considered an area of academic research and distinct from computer programming.[4]
Algorithms and data structures are central to computer science.[5] 
The theory of computation concerns abstract models of computation and general classes of problems that can be solved using them. The fields of cryptography and computer security involve studying the means for secure communication and for preventing security vulnerabilities. Computer graphics and computational geometry address the generation of images. Programming language theory considers approaches to the description of computational processes, and database theory concerns the management of repositories of data. Human–computer interaction investigates the interfaces through which humans and computers interact, and software engineering focuses on the design and principles behind developing software. Areas such as operating systems, networks and embedded systems investigate the principles and design behind complex systems. Computer architecture describes the construction of computer components and computer-operated equipment. Artificial intelligence and machine learning aim to synthesize goal-orientated processes such as problem-solving, decision-making, environmental adaptation, planning and learning found in humans and animals. Within artificial intelligence, computer vision aims to understand and process image and video data, while natural-language processing aims to understand and process textual and linguistic data.
'''

def shrip(my_input:str):
    my_list = []

    for item in my_input.upper():
        if ord(item)>=ord('A') and ord(item)<=ord('Z'):
            my_list.append(item)

    my_output = "".join(my_list)
    print(my_output)
    return my_output

my_output2 = shrip(my_input2)

from copy import deepcopy
import random

chars = [chr(item+ord("A")) for item in range(26)]
print(chars)
# chars_rand = deepcopy(chars)
# random.shuffle(chars_rand)
chars_rand = ['Q', 'I', 'O', 'B', 'T', 'U', 'Z', 'L', 'F', 'R', 'V', 'G', 'J', 'S', 'W', 'E', 'Y', 'H', 'K', 'A', 'P', 'M', 'X', 'C', 'N', 'D']
print(chars_rand)

def index(item: str)->int:
    assert(len(item)==1)
    assert(ord(item)>=ord('A'))
    assert(ord(item)<=ord('Z'))
    return ord(item)-ord('A')

my_output2 = list(my_output2)
for i in range(len(my_output2)):
    my_output2[i] = chars_rand[index(my_output2[i])]
print(''.join(my_output2))