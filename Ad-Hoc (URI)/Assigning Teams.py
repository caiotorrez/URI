
dados = map(int, raw_input().split())
dados.sort()
print abs((dados[0] + dados[3]) - (dados[1] + dados[2]))
