class Info:
    def __init__(self, idd=None, level=None):
        self.idd = idd
        self.level = level

info1 = Info()
info1.idd = 'codetree'
info1.level = 10

info2 = Info()
_id, _level = input().split()
info2.idd = _id
info2.level = int(_level)

print(f'user {info1.idd} lv {info1.level}')
print(f'user {info2.idd} lv {info2.level}')