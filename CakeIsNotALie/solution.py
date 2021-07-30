def data_iter(file = "testcases.txt"):
    with open(file, "r") as f:
        cases = f.read()
        for case in cases.split("\n"):
            result = solution(case)
            print(case, result)
            
def solution(s):
    if len(s) < 4:
        return 1
    if set(s) ==1 :
        return 1
    pattern_length = len(s)/2
    for i in range(len(s)):
        init_pattern = s[i:i+pattern_length]
        j = pattern_length
        
            compare_pattern = s[j : i+half_length*2]
            
        pattern_length -= 1
    return(len(s)/2)
data_iter()