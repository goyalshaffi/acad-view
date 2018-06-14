#question 1
a=input("enter no")
c=input("enter no")
b=[]
b.append(a)
print(b)
b.append(c)
print(b)

#question2
d=['google','facebool','apple','tesla','tesla']
b.extend(d)
print(b)

#question 3
print(b.count('tesla'))

#question 4
f=[5,2,8,4,1]
f.sort()
print(f)

#question 5
g=[3,7,8,9]
h=[2,4,5,8]
#k=g+h
#print(k)
#k.sort()
#print(k)
# second method
for i in h:
    g.append(i)
g.sort()
print(g)

#question 6

stackk=[]
while(True):
    resp = input("What would you like do with stack??\n 1. Push\n 2. Pop\n 3. Display \n 4.Exit\nYour Response: ")

    if resp==1:
     item = input("\n\nEnter item that you want to add to stack:")
     stackk.append(item)

    elif resp==2:
     if(len(stackk)==0):
      print("\n\nStack is empty.... You can't pop\n\n")
     else:
      item = stackk.pop()
    elif resp==3:
     print(stackk)
     print("\n\n")
    elif resp==4:
     break
    else:
     print("\n\nPlease Enter a valid input!!\n\n")


 # queue
queue = []
while (True):
    resp = input("What would you like do with que??\n 1. queue\n 2. dequeue\n 3. Display \n 4.Exit\nYour Response: ")

    if resp == 1:
        item = input("\n\nEnter item that you want to add to que:")
        queue.append(item)

    elif resp == 2:
        if (len(queue) == 0):
            print("\n\nque is empty.... You can't pop\n\n")
        else:
            item = queue._delitem_(0)
    elif resp == 3:
        print(queue)
        print("\n\n")
    elif resp == 4:
        break
    else:
        print("\n\nPlease Enter a valid input!!\n\n")

#optional question
s=[1,2,3,4,5,6,7,8,9]
oddno=[]
evenno=[]
count=0
for x in s:
    if (x%2==0):
        evenno.append(x)
    else:
        oddno.append(x)
print(evenno,len(evenno))
print(oddno,len(oddno))










