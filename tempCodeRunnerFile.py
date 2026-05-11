
name = ["hitesh" ,"aakash","vipul"]
height = [180,160,162]
d={}
for i in range(len(name)):
    d[height[i]]=name[i]

d=sorted (d.items() , key=lambda x:x[0] , reverse = True)

for i in range (len(d)):
    names[i] = d[i][1]

print(names)    