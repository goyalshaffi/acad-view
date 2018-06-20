
# q1

r=float(input("enter radius"))
def fn(r):
    area=3.14*r*r
    return area
g=fn(r)
print(g)


# q2

n=6
def perfect(n):
    sum=0
    for i in range(1,n):
        if(n%i==0):
            sum=sum+i
    if(sum==n):
        return True
    else:
        return False
print(perfect(n))
for i in range(1,1001):
    if(perfect(i)==True):
      print(i)



# q3
n=input("enter value")
def recur_multi(n,i=1):
    print(n*i)
    if(i!=10):
        recur_multi(n,i=i+1)
recur_multi(n)






# q4
a=input("enter no")
b=input("enter no")

def recur_power(a,b):
    if(b==1):
        return a
    else:
        return(a*recur_power(a,b-1))
print(recur_power(a,b))





# q5

a=input("enter no")
def recur_fact(a):
    if(a==1):
        return 1
    else:
        return(a*recur_fact(a-1))
print(recur_fact(a))

