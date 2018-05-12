class File():
#1 класс
    def __init__(self,name, num):
#конструктор класса 
        self.name=name
        self.number=num
    def __str__(self):
        s = '\n Файл: '+ self.name + ' № ' + str(self.number)
        return s
class Catalogsfile():
#Каталог файлов ( взяла виды дел) ;2 класс
    def __init__(self,name, num):
#конструктор класса 
        self.number=num
        self.name=name
        self.listFile=[]
    def __str__(self):
         s = ' \n Каталог: '+ self.name + '  '
         for i in (self.listFile):
             s = s+ " " + str(i)
         return s
    def ADD(self, File):
#добавление 
        self.listFile.append(File)



a=File('Сидоров',1)
b=File('Клименко 8',2)
c=File('Аксель',3)
d=File('Муромский',4)
e=File('Лопин',5)
f=File('Михальчук',6)
g=File('Алпацкий',7)
h=File('Андоров',8)
i=File('Кошкин',9)
j=File('Акимов',10)
k=File('Армон',11)
l=File('Шпитонюк',12)
m=File('Агутин',13)
n=File('Кокорин',14)
o=File('Антонов',15)
p=File('Стрюков',16)
r=File('Пандронов',17)


a1=Catalogsfile("Административные дела",1)
b1=Catalogsfile("Административно-процессуальные ",2)
c1=Catalogsfile("Уголовные дела",3)
d1=Catalogsfile("Заявления от пострадавших",4)
e1=Catalogsfile("Гражданские дела",5)

a1.ADD(a)
a1.ADD(g)
a1.ADD(l)
a1.ADD(m)
b1.ADD(b)
b1.ADD(h)
b1.ADD(k)
c1.ADD(c)
c1.ADD(r) 
c1.ADD(j)
d1.ADD(i)
d1.ADD(e)
e1.ADD(d)
e1.ADD(f)
e1.ADD(n)
e1.ADD(o)
e1.ADD(p)
list_c=[a1,b1,c1,d1,e1]


z=0

print('\t\t\t Список фпйлов отсортированный по каталогам дел\n')
for i in list_c:
    print(i)

print("\n\t\t\t Список всех файлов, у которых название начинается с буквы «А»\n")
for i in list_c:
    for j in i.listFile:
        if j.name[0]=="А":
            print(j)

print('\n\t\t\t Список всех каталогов дел и количество файлов в каждом из них\n')
for i in list_c:
    z=0
    for j in i.listFile:
            z=z+1
    print( i, '\n количество файлов в каталоге:', z)

print('\n\t\t\t Список каталогов дел, в которых названия всех файлов начинаются с буквы "А"\n')
for i in list_c:
    z=0
    t=0
    for j in i.listFile:
        if j.name[0]=="А":
            t=t+1
        z=z+1
    if z==t:
        print(i)
else:
    print ('таких не существует')
   

print('\n\t\t\t Список каталогов дел, на которых названия хотябы одной файл начинаются с буквы «А»\n')
for i in list_c:
    t=0
    for j in i.listFile:
        if j.name[0]=="А":
            t+=1
    if t!=0:
        print(i)


