def data_iter(file = "testcases.txt"):
    with open(file, "r") as f:
        cases = f.read()
        for case in cases.split("\n"):
            result = solution(case)
            #print(case, result)
        
def solution(s):
    if len(s) < 4:
        return 1
    if len(set(s)) ==1 :
        return 1
    pattern_found = 1
    pattern = find_pattern(s)
    if pattern["index"] < 0:
        return pattern_found
    pattern_found = count_pattern(s,pattern)
    return pattern_found

def find_pattern(s):
    half_pattern = len(s)/2
    pattern_length = 2
    while(pattern_length<= half_pattern):
        for index in range(0,len(s)-pattern_length):
            pattern_test = s[index:index+pattern_length]
            string_test = s.replace(pattern_test, "-"*pattern_length, 1)
            pattern_index = string_test.find(pattern_test)
            
            if pattern_index > -1:
                return {"pattern" : pattern_test, "index": pattern_index}
            
        pattern_length += 1
    return {"pattern" : "", "index" : -1}

def count_pattern(s, pattern):
    pattern_found = 0
    while s.find(pattern["pattern"]) > -1:
        s = s.replace(pattern["pattern"], "-"*len(pattern["pattern"]), 1)
        pattern_found+=1
    return pattern_found
data_iter()