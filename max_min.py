'''
 Write a program to find the maximum and minimum value of given set values.
Sample Input:
1 2 3 4 5
Sample Output:
Maximum: 5
Minimum: 1
'''
s = set(map(int,input().split()))
print("Maximum:",max(s))
print("Minimum:",min(s))
