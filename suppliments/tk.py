from tkinter import *

os1=[150,200]
os2=[470,200]

def create_box(can,l,b,os):
    can.create_line(os[0],os[1],os[0]+l,os[1])
    can.create_line(os[0]+l,os[1],os[0]+l,os[1]+b)
    can.create_line(os[0]+l,os[1]+b,os[0],os[1]+b)
    can.create_line(os[0],os[1]+b,os[0],os[1])


def create_tk(dna1,dna2):
    r=0
    l1=dna1.length
    b1=dna1.breadth
    l2=dna2.length
    b2=dna2.breadth
    window=Tk()
    window.geometry('800x800+0+0')
    def f1():    
        print('1')
        f=open('D:\\python projects\\genetic algorithm\\suppliments\\f.txt','w')
        f.write('1')
        f.close()
        window.destroy()
    def f2():     
        print('2')
        f=open('D:\\python projects\\genetic algorithm\\suppliments\\f.txt','w')
        f.write('2')
        f.close()
        window.destroy()
    but1=Button(window,text='1',command=f1)
    but2=Button(window,text='2',command=f2)
    but1.grid(row=5,column=10)    
    but2.grid(row=15,column=10)
    #print(str(l)+' '+str(b))
    my_canvas=Canvas(window,width=600,height=600)
    create_box(my_canvas,l1,b1,os1)
    create_box(my_canvas,l2,b2,os2)
    my_canvas.grid(row=0,column=0)
    Tk.mainloop(window)
    print('end'+str(r))
    return r