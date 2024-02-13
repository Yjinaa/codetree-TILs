clinic = [0 for _ in range(4)]
for i in range(3):
    symptoms = list(input().split())
    if symptoms[0] == 'Y' and float(symptoms[1]) >= 37:
        clinic[0] += 1
    elif symptoms[0] == 'N' and float(symptoms[1]) >= 37:
        clinic[1] += 1
    elif symptoms[0] == 'Y' and float(symptoms[1]) < 37:
        clinic[2] += 1
    else:
        clinic[3] += 1

if clinic[0] >= 2:
    print(*clinic, 'E')
else:
    print(*clinic)