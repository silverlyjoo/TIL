import sys
from pprint import pprint
sys.stdin = open("tree_prac.txt")


def preorder(node):
    if node != 0:
        print("{}".format(node), end=" ")
        preorder(L[node][0])
        preorder(L[node][1])


def inorder(node):
    if node != 0:
        inorder(L[node][0])
        print("{}".format(node), end=" ")
        inorder(L[node][1])


def postorder(node):
    if node != 0:
        postorder(L[node][0])
        postorder(L[node][1])
        print("{}".format(node), end=" ")


V, G = map(int, input().split())
data = list(map(int, input().split()))

L = [[0 for _ in range(3)] for _ in range(V+1)]

for i in range(0, len(data), 2):
    if L[data[i]][0]:
        L[data[i]][1] = data[i+1]
    else:
        L[data[i]][0] = data[i+1]
    L[data[i+1]][2] = data[i]

for idx, val in enumerate(L):
    print('{:3d} {:3d} {:3d} {:3d}'.format(idx, *val))

print('preorder')
preorder(1)
print('\ninorder')
inorder(1)
print('\npostorder')
postorder(1)