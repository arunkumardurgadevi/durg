def print(arr,n):
Min=-1
myset=dict()
for i in range(n,-1,-1,-1):
if arr[i] in myset.keys():
Min=i
myset[arr[i]]=1
if(Min!=-1):
print(arr[Min])
else:
print("unique")
arr=[1,2,3,2,3,4,3]
n=len(arr)
print(arr,n)
