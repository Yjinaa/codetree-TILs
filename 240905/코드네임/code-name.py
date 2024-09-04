class Info:
    def __init__(self, name=None, score=0):
        self.name = name
        self.score = score
agents = []
for i in range(5):
    name, score = input().split()
    agents.append(Info(name, int(score)))

min_idx = 0
for i in range(1,5):
    if agents[min_idx].score > agents[i].score:
        min_idx = i
    
print(agents[min_idx].name, agents[min_idx].score)