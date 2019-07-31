x11,y11=map(str,input().split())
z11=0
for i in range(len(x11)):
    if x11[i]==y11:
        z11=z11+1
        
print(z11)
