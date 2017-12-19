import sys
def pos_valida(i, j):
    
    if i >= m or j >= n or i < 0 or j < 0: return False
    return not vis[i][j] and matriz[i][j] != 'X'

def dfs(i, j):

    if not pos_valida(i, j):
        return

    vis[i][j] = 1
    matriz[i][j] = 'T'
    dfs(i+1, j)
    dfs(i-1, j)
    dfs(i, j+1)
    dfs(i, j-1)

while True:
        
    m, n = map(int, raw_input().split())
    if n + m == 0:
        break
    vis = [[0 for i in xrange(n)] for j in xrange(m)]

    matriz = []
    for k in xrange(m):
        matriz.append(list(raw_input()))


    for i in xrange(m):
        for j in xrange(n):
            if matriz[i][j] == 'T':
                dfs(i, j)

    for i in xrange(m):
        sys.stdout.write(''.join((matriz[i])) + '\n')
    sys.stdout.write('\n')
