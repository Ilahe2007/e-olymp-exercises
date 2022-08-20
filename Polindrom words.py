a=str(input())
a=a.replace(' ','')
a=list(a)
b=list(reversed(a))
if a.count(' ')!=0:
  while a.count(' ')!=0:
    b.remove(' ')
    break
    print(a)
    print(b)
if a==b:
  print('YES')
else:
  print('NO')
