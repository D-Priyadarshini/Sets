'''
Write a program to print only the different values between two given sets.
Sample Input:
1 2 3 4
2 4 6 8
Sample Output:
1 3
Note: There are trailing spaces at the end of output.
'''
s1 = set(map(int,input().split()))
s2 = set(map(int,input().split()))
for i in s1:
  if i not in s2:
    print(i,end= " ")

