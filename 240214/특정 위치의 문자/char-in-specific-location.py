chars = ['L', 'E', 'B', 'R', 'O', 'S']
char = input()
idx = "None"

for i, cha in enumerate(chars):
    if chars[i] == char:
        idx = i
        break

print(idx)