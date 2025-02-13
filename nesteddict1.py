# nested dict for states

d1={}
print("total no. of items")
n=int(input())
for i in range (n):
    print("enter the key")
    k=input()
    print("enter the value")
    l1=[]
    
    cap=input()
    l1.append(cap)        
    pop=int(input())
    l1.append(pop)
    area=float(input())
    l1.append(area)
    temp=float(input())
    l1.append(temp)
    print(l1)
    
    d1[k]=l1
print("dictionary formed is ")
print(d1)