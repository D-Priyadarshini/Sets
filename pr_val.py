'''
Write a program to get n number of values in separate line for set and print the values with space separation.
Sample Input:
5
3
1
4
5
2
Sample Output:
1 2 3 4 5 
Note: There is trailing space at the end of output
'''
n = int(input())
for i in range(n):
  s = int(input())
  print(s,end = " ")
