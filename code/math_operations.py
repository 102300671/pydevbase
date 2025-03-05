def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


def mod(a, b):
    return a % b


def pows(a, b):
    return a ** b


def rsa(m):
    flag="CTF{"
    m = int.from_bytes((flag+m+'}').encode(), 'big')
    p_hex="C327A95D8277779B62D41C4773C7C62516997D7777C97777377777977779C77777777777777"
    q_hex="B198D63F45612B3E7F96A54D8C321A76984F3D2B1A7F4E8C5D6B3A9F2C7E1D4A8B3C5F2E7A"
    p=int(p_hex,16)
    q=int(q_hex,16)
    n=p*q
    e=65537
    c=pow(m,e,n)
    c=str.encode(hex(c)[2:])
    return c