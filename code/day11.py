class Titer:
    def __init__(self,data):
        self.data = data

    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.data:
            raise StopIteration
        else:
            item = self.data.pop(0)
            return item
        
def pow(n):
    tpow = (x*x for x in range(1,n+1))
    return tpow

def tgenerator(n):
    for i in range(1,n+1):
        yield i



n = int(input("请输入列表大小:"))
co    