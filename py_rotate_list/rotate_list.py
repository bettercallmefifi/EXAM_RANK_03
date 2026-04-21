from collections import deque
from typing import List

def rotate_list(lst: List[int], n: int):
    tolist = []
    dq = deque(lst)
    dq.rotate(n)
    return list(dq)

def main():
    print(rotate_list([1, 2, 3, 4, 5], 2))
    print(rotate_list([4,2,1,-1,'a'], 4))
    print(rotate_list([] , 3))
    print(rotate_list([1], 10))


main()