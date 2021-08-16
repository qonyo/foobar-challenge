import time
import copy

LENGTH = 0
WIDTH = 0

def explore(maps, breaker, x, y):
    
    if x < 0 or y < 0 or x >= WIDTH or y >= LENGTH:
        return 1000
    
    if x == WIDTH-1 and y == LENGTH-1:
        return 1
    
    val = maps[y][x]
    journal = copy.deepcopy(maps)
    journal[y][x] = -1
    
    if val == 1 :
        if breaker :
            new_breaker = False
            return min(1 + explore(journal, new_breaker, x-1, y),
                       1 + explore(journal, new_breaker, x+1, y),
                       1 + explore(journal, new_breaker, x, y-1),
                       1 + explore(journal, new_breaker, x, y+1),)
        
        return 1000
        
    elif val == -1:
        return 1000
        
    else:
        return min(1 + explore(journal, breaker, x-1, y),
                   1 + explore(journal, breaker, x+1, y),
                   1 + explore(journal, breaker, x, y-1),
                   1 + explore(journal, breaker, x, y+1),)

def solution(maps):
    global LENGTH, WIDTH
    breaker = True
    x,y = (0,0)
    LENGTH = len(maps)
    WIDTH = len(maps[0])
    count = explore(maps ,breaker, x, y)
    return count

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