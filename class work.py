a=5
b=6.8
c=6+7j
print(type(a))
print(type(b))
print(type(c))
print(isinstance(a,int))
g="hello world"#space is also a string
print(g[1])
print(g[1:9:2])
#print(g[1]=c)#error
#string is immutable
print(g[-1])
a="good"
#a.#press ctrl+space
print(a.upper())
print(a.capitalize())
print(len(a))
#a.is#ctrl+space
print(a.isalpha())
k=[1,[1,2,3],"hello"]
print(k[1][1])
print(k[2][1])
k.insert(1, " hlo")
print(k)
k.pop(1)
print(k)
k.remove(3)
print(k)
s=[1, 7, 9, 8]
s.reverse()
print(s)