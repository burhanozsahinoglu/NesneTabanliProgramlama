#https://repl.it/languages/python3 ile olu�turuldu.
print("Merhaba")
a=10
print(a)
a="Merhaba"
print(a)
print(a[0])
print(a[0:3])
print(a[3:5])
print(a[::2])
print(a[::-1])
print(type(a))
b=10
print(type(b))
c=4.5
print(type(c))
d=True
print(type(d))
a="3.5"
a=float(a)
print(type(a))
print(int(a))
print(round(a))
a=5
b=6
x=a
a=b
b=x
print(a,b)
a,b=b,a
print(a,b)
a,b,c,d=1,2,3,4
print(a,b,c,d)
a=[1,2,3,4,5]
print(type(a))
a=["Beykoz","2.3",5,True]
print(a[0])
print(a[0][0])
print(a[1][0])
a={1,2,3,4}
print(a)
a.add(10)
print(a)
a.add("Kavac�k")
print(a)
print(5/3)
print(5//3)
print(5%3)
print(5**3)
print(16**(1/2))
print(16**0.5)
print(8**(1/3))
a=4
print(-a)
a=-a
print(a)
a='G�zde\'nin bug�n dersi var'
print(a)
a='G�zde \t nin bug�n dersi var'
print(a)
print(len(a))
a="Beykoz"
print(a[len(a)-1])
print(a[-1])
print(12,34,23,sep=".")
print(12,34,23,sep=" ")
print(21,2,2019,sep="/")
print(21,2,2019,sep="\n")
print(*"Python")
print(*"123")
print(123,212,331,sep=",")
a,b,c=10,10.5,345.234
print("{2} {0} {1}".format(a,b,c))
print("{:10.2f}".format(a))
print("{:10.2f}".format(b))
print("{:10.2f}".format(c))


