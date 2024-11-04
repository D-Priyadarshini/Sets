'''
 Write a program to update the given set in another set.
Sample Input:
1 2 3
3 4 5
Sample Output:
1 2 3 4 5
'''

s1 = set(map(int,input().split()))
s2 = set(map(int,input().split()))
print(*s1 | s2)
