n=int(input())
r1,r2=input().split()
r1=int(r1)
r2=int(r2)
if n in range(r1,r2):
  print("yes")
else:
  print("no")
