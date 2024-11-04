'''
Write a program to get set values in a single line with space(including duplicate values) and 
find the number of duplicate values given during input and print the output set value without duplicate elements.
Sample Input:
6
1
2
1
2
3
1
Sample Output:
Duplicate Values: 3
1 2 3 
'''
n = int(input())
s = set()
count = 0
l = []
for i in range(n):
    s1 = int(input())
    if s1 not in s:
        s.add(s1)
        l+=[s1]
    else:
        count += 1
print("Duplicate Values:",count)
print(*l)

