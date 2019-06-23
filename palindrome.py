n=input()
w=""
for i in n:
  w=i+w
  if(n==w):
    print("yes")
    break
else:
    print("no")
