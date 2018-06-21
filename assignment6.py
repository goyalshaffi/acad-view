# q1
'''
for i in range(1,11):
  print(int(input("enter no")))


# q2


while(True):
  print(int(input("enter no")))





# q3

l=[1,5,3,4]
for i in l:
  x=i*i
  print(x)




# q4

l=[1,"sakshi",3.6,2,"uro",5.9,3,"kansal",8.9]
l1=[]
l2=[]
l3=[]
for i in l:
  if(isinstance(i,int)):
    l1.append(i)
  elif (isinstance(i, str)):
    l2.append(i)
  else:
    l3.append(i)
print(l3)
print(l2)
print(l1)



# Q5


l1=[]
l2=[]
for i in range(1,101):
  if(i%2==0):
    l1.append(i)
  else:
    l2.append(i)
print(l1)
print(l2)


 #q6

for i in range(0,4):
  for j in range(0,i+1):
    print("*",end-" ")
  print("\r")

'''

# q7

d1={}
for i in range(1,4):
    value=input("enter value")
    key=input("enter key")
    d1[key]=value

print(d1)
for i in d1:
    print(i)

'''
# q8


l=[]
l1=input("enter value")
l.extend(l1)
print(l)
j=input("enter no")
for i in l:
  if(i==j):
    l.remove(i)
print(l)

'''