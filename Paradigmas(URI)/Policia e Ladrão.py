import sys
def pos_valida(i, j):

    if i >= 5 or j >= 5 or i < 0 or j < 0: return False
    return not vis[i][j] and matriz[i][j] != '1'

def dfs(i, j):

    if not pos_valida(i, j):
        return

    vis[i][j] = 1
    dfs(i+1, j)
    dfs(i-1, j)
    dfs(i, j+1)
    dfs(i, j-1)

for z in xrange(int(raw_input())):
    matriz = []
    while len(matriz) < 5:
        data = raw_input()
        if len(data) >= 9:
            matriz.append(data.split())
    vis = [[0 for i in xrange(5)] for j in xrange(5)]
    dfs(0,0)

    if vis[4][4] == 1:
        sys.stdout.write('COPS\n')
    else:
        sys.stdout.write('ROBBERS\n')
