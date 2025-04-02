from math_operations import add, sub, mul, div, mod, pows,rsa

while True:
    n = int(input("1:使用模块;2:读取模块文件内容;3:追加模块文件内容;4:逐行读取模块文件内容;5:RSA加密;6:退出:"))
    if n == 1:
        while True:
            a, b = map(int, input("请输入两个数(输入0 0退出):").split())
            if a == 0 and b == 0:
                break
            print("1:加法;2:减法;3:乘法;4:除法;5:取模;6:幂运算:")
            m = int(input("请选择运算:"))
            if m == 1:
                print(add(a, b))
            elif m == 2:
                print(sub(a, b))
            elif m == 3:
                print(mul(a, b))
            elif m == 4:
                print(div(a, b))
            elif m == 5:
                print(mod(a, b))
            elif m == 6:
                print(pows(a, b))
            else:
                break
    elif n == 2:
        with open("math_operations.py", "r") as f:
            print(f.read())
    elif n == 3:
        fun = input("请输入追加内容:\n")
        with open("math_operations.py", "a") as f:
            f.write(fun)
    elif n == 4:
        with open("math_operations.py", "r") as f:
            for line in f:
                print(line)
    elif n == 5:
        m = input("请输入明文:")
        print("密文:", rsa(m))
    else:
        break
