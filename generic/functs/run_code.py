import sys
from math_functs import s_add , s_sub

def __main__() :
    if len(sys.argv) > 1:
        print(s_add(int(sys.argv[1]) ,int(sys.argv[2])))
        print(s_sub(int(sys.argv[1]) ,int(sys.argv[2])))
    else:
        print(s_add(5,6))
        print(s_sub(7,8))


__main__()
