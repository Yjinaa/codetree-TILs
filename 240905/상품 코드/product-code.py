class Product:
    def __init__(self, name=None, code=None):
        self.name = name
        self.code = code

p1 = Product()
p2 = Product()

p1.name = 'codetree'
p1.code = '50'

n, c = input().split()
p2.name = n
p2.code = c

print(f'product {p1.code} is {p1.name}')
print(f'product {p2.code} is {p2.name}')