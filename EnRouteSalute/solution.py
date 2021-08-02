MUL = 2

def data_iter(file = "testcases.txt"):
    with open(file, "r") as f:
        cases = f.read()
        for case in cases.split("\n"):
            result = solution(case)
            print(case, result)
            
def solution(s):
    result = 0
    print(MUL)
    return result

data_iter()