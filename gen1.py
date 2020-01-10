from suppliments import tk
import random
buff=10
class dna:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

f=dna(100,50)
s=dna(45,100)

def same(a,b):
    a.length=b.length
    a.breadth=b.breadth

def mutate(dna):
    l_r=random.random()
    b_r=random.random()
    l_m=random.randint(-1,1)
    b_m=random.randint(-1,1)
    dna.length=dna.length+l_m*buff*l_r
    dna.breadth=dna.breadth+b_m*buff*b_r
    return dna

mutate(f)
mutate(s)

k=tk.create_tk(f,s)
# print(str(f.length)+' '+str(f.breadth)+' '+ str(s.length)+' '+str(s.breadth))
# print('k'+str(k))
while(True):
    file=open('D:\\python projects\\genetic algorithm\\suppliments\\f.txt','r')
    ch=int(file.read())
    file.close()
    # print(ch+'s')
    if ch == 1:
        same(s,f)
        mutate(f)
        mutate(s)
    else:
        same(f,s)
        mutate(f)
        mutate(s)
    k=tk.create_tk(f,s)
    print(str(f.length)+' '+str(f.breadth)+' '+ str(s.length)+' '+str(s.breadth))