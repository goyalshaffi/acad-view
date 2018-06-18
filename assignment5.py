# q1

a=input("enter no")
if(a%4==0):
    print("leap year")
else:
    print("not a leap year")


# q2

b=input("enter length")
c=input("enter breath")
if(b==c):
    print("the dimensions are of square")
else:
    print("the dimensions are of rectangle")


# q3

d=input("enter age of person 1")
e=input("enter age of person 2")
f=input("enter age of person 3")
if(d>e):
    if(d>f):
        print("d is oldest")
    else:
        print("f is oldest")
elif(e<f and e<d):
     print("e is youngest")
elif(f<e and f<d):
    print("f is youngest")
elif(e>d and e>f):
    print("e is oldest")
else:
    if(d<f):
        print("d is youngest")


# q4


g=input("enter no")
if(g>=0 and g<=50):
    print("sorry")
    print("no prize")
elif(g>=51 and g<=200):
    print("congratulations!")
    if(g>=51 and g<150):
        print("wooden dog")
    elif(g<=151 and g>=180):
        print("book")
    else:
         print("chocolates")
else:
    print("no is out of range")


# q5

k=input("enter units")
print k
if(k<=10):
    cost=k*100
    print(cost)
else:
    cost=k*100-10*k
    print(cost)







