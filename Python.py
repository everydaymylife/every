class OS():
    def __init__(self,name, num):
        self.name=name
        self.number=num
    def __str__(self):
        s = '\nOS: '+ self.name + ' № ' + str(self.number)
        return s
class PC():
    def __init__(self,name, num):
        self.number=num
        self.name=name
        self.listos=[]
    def __str__(self):
    def __str__(self):
         for i in (self.listos):
             s = s+ " " + str(i)
         return s
    def ADD(self, OS):
        self.listos.append(OS)



a=OS('Windows 10',1)
b=OS('Windows 8',2)
c=OS('Apple DOS',3)
d=OS('KolibriOS',4)
e=OS('Linux',5)
f=OS('Windows 7',6)
g=OS('Apple macOS High Sierra',7)
h=OS('Apple macOS X 10.6 Snow Leopard',8)
i=OS('Windows 98',9)
j=OS('Apple Darwin',10)


a1=PC("Apple iMac",1)
b1=PC("Acer Aspire E15",2)
c1=PC("iMac G3",3)
d1=PC("Fujitsu Lifebook 520D",4)
e1=PC("Asus ROG GL552VW",5)

a1.ADD(a)
a1.ADD(g)
b1.ADD(b)
b1.ADD(h)
c1.ADD(c)
c1.ADD(j)
d1.ADD(i)
d1.ADD(e)
e1.ADD(d)
e1.ADD(f)
list_c=[a1,b1,c1,d1,e1]


z=0

print('\t\t\tСписок OS отсортированный по компьютерам\n')
for i in list_c:
    print(i)

print("\n\t\t\tСписок всех OS, у которых название начинается с буквы «А»\n")
for i in list_c:
    for j in i.listos:
        if j.name[0]=="A":
            print(j)

print('\n\t\t\tСписок всех компьютеров и количество OS на каждом из них\n')
for i in list_c:
    z=0
    for j in i.listos:
            z=z+1
    print( i, '\n количество OS на компьютере:', z)

print('\n\t\t\tСписок компьютеров, на которых названия всех OS начинаются с буквы "А"\n')
for i in list_c:
    z=0
    t=0
    for j in i.listos:
        if j.name[0]=="A":
            t=t+1
        z=z+1
    if z==t:
        print(i)

print('\n\t\t\tСписок компьютеров, на которых названия хотябы одной OS начинаются с буквы «А»\n')
for i in list_c:
    t=0
    for j in i.listos:
        if j.name[0]=="A":
            t+=1
    if t!=0:
        print(i)

