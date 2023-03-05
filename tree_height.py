# python3

import sys
import threading
import numpy


def compute_height(n, parents):
    tree1={}
    def height(i):
        if i in tree1:
            return tree1[i]
        if i==-1:
            return 0
        h=1+height(parents[i])
        tree1[i]=h
        return h

    max_height=0
    for i in range(n):
        max_height=max(max_height, height(i))

    # Your code here
    return max_height


def main():
    inp=input()
    if "I" in inp:
        inp1=int(input())
        put=list(map (int, input().split()))
        print(compute_height(inp1, put))
    if "F" in inp:
        files=input()
        if "a" not in files:
            with open("./test/"+files, "r") as file1:
                calc1=int(file1.readline())
                output=list(map(int,file1.readline().split()))
                print(compute_height(calc1,output))
    pass

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
main()
#print(numpy.array([1,2,3]))
