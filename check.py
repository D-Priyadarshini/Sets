'''

 Write a program to delete the given element in the given set values. If the given element is not in the set values, then print "Given value is not present in the set list.".
Sample Input:
1 2 3 4
2
Sample Output:
1 3 4 
Note: There is a trailing space at the end of the list.'''

s = set(map(int,input().split()))
n = int(input())
d = ()
if n in s:
  for i in s:
    if i == n:
      d.add(i)
  for i in d:
    print(i,end = " ")
else:
  print("Given value is not present in the set list.")
      


