def data_iter(file = "testcases.txt"):
    with open(file, "r") as f:
        cases = f.read()
        for case in cases.split("\n"):
            result = solution(case)
            print(case, result)
        
def solution(s):
    #I read about builtin function being expensive so save this
    length_string = len(s)
    if len(set(s)) == 1:
        return length_string
    if length_string%2 == 1:
        return 1
    else:
        new_string = s*2
        index = new_string.find(s,1,-1)
        if index == -1:
            return 1
        else :
            length_pattern = index
            pattern = s[:length_pattern]
            return (length_string/length_pattern)
        
data_iter()