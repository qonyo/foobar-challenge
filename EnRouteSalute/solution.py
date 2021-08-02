def data_iter(file = "testcases.txt"):
    with open(file, "r") as f:
        cases = f.read()
        for case in cases.split("\n"):
            result = solution(case)
            print(case, result)
MUL = 2           
def solution(s):
    result = 0
    rstring, lstring = convert_string(s)
    rstring = rstring >> 1
    while(not(lstring ==0 or rstring ==0)):
        result += bin(rstring & lstring).count("1")
        rstring = rstring >> 1
    return result*2

def convert_string(s):
    rstring = s.replace("<", "-").replace("-","0").replace(">","1")
    lstring = s.replace(">", "-").replace("-","0").replace("<","1")
    rstring = int(rstring, 2)
    lstring = int(lstring, 2)
    return rstring, lstring


data_iter()