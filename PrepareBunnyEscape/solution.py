import time
import queue

D_COL = [-1,0,1,0]
D_ROW = [0,-1,0,1]
VISITED = list()
GRID = list()
ROW_QUE = queue.Queue()
COL_QUE = queue.Queue()
PICKAXE_QUE = queue.Queue()
NODES_NEXT_LAYER = 0
def neighbours_lookup(row_now, col_now, pax_now):
    global NODES_NEXT_LAYER, ROW_QUE, COL_QUE, PICKAXE_QUE, VISITED
    for i in range(4):
        row_next = row_now + D_ROW[i]
        col_next = col_now + D_COL[i]
    
        if row_next < 0 or col_next < 0 or row_next >= HEIGHT or col_next >= WIDTH: continue
        if VISITED[row_next][col_next]: continue
        if GRID[row_next][col_next] == 1 : continue
        
        ROW_QUE.put(row_next)
        COL_QUE.put(col_next)
        PICKAXE_QUE.put(pax_now)
        VISITED[row_next][col_next] += 1
        NODES_NEXT_LAYER += 1
        
def solution(grid):
    global VISITED, WIDTH, HEIGHT, GRID, NODES_NEXT_LAYER
    GRID = grid
    WIDTH = len(GRID[0])
    HEIGHT = len(GRID)
    source = (0,0,True) #third column for breaker
    target = (HEIGHT-1, WIDTH-1) #row, col target
    VISITED = [[False for col in range(WIDTH)] for row in range(HEIGHT)]
    depth = 1
    
    ROW_QUE.put(source[0])
    COL_QUE.put(source[1])
    PICKAXE_QUE.put(source[2])
    nodes_in_layer = 1
    while not(ROW_QUE.empty()):
        row_now = ROW_QUE.get()
        col_now = COL_QUE.get()
        pax_now = PICKAXE_QUE.get()
        VISITED[row_now][col_now] = True
        if row_now == target[0] and col_now == target[1]:
            return depth
        
        neighbours_lookup(row_now, col_now, pax_now)
        nodes_in_layer-=1
        
        if nodes_in_layer == 0:
            nodes_in_layer = NODES_NEXT_LAYER
            NODES_NEXT_LAYER = 0
            depth+=1
    
    return -1


start = time.time()    
print(solution([
[0, 0, 0], 
[0, 0, 0], 
[0, 0, 0], 
[0, 0, 0]
]))
end = time.time()
print(end-start)

start = time.time()    
print(solution([
[0, 1, 1, 0], 
[0, 0, 0, 1], 
[1, 1, 0, 0], 
[1, 1, 1, 0]
]))
end = time.time()
print(end-start)

start = time.time() 
print(solution([
[0, 0, 0, 0, 0, 0], 
[1, 1, 1, 1, 1, 0], 
[0, 0, 0, 0, 0, 0], 
[0, 1, 1, 1, 1, 1], 
[0, 1, 1, 1, 1, 1], 
[0, 0, 0, 0, 0, 0]
]
))
end = time.time()
print(end-start)

start = time.time() 
print(solution([
[0, 1, 0, 0, 0, 0], 
[1, 1, 1, 1, 1, 0], 
[1, 0, 0, 0, 0, 0], 
[0, 0, 1, 1, 1, 1], 
[0, 1, 1, 1, 1, 1], 
[0, 0, 0, 0, 0, 0]
]
))
end = time.time()
print(end-start)

start = time.time() 
print(solution([
[0, 0, 0, 0, 0, 0],
[1, 1, 1, 1, 1, 0],
[1, 1, 1, 1, 1, 1],
[0, 0, 0, 0, 0, 0],
[0, 1, 1, 1, 1, 1],
[0, 0, 0, 0, 0, 0]
] 
))
end = time.time()
print(end-start)

start = time.time() 
print(solution([ 
[0, 1, 1, 0], 
[0, 0, 0, 1], 
[1, 1, 1, 0], 
[1, 1, 1, 0] 
]
))
end = time.time()
print(end-start)

start = time.time() 
print(solution([
[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
[1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
))
end = time.time()
print(end-start)