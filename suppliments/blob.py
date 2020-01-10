import tkinter as tk
import time
import random

# def equate(prev,curr):
#     for i in range(len(curr)):
#         prev[i]=curr[]

# buff=25
size=17
def create_blob(size=size):
    frame_rate=100
    # class blob:
    #     dna=random.randint(1,10)

    d=[]
    v_x=[]
    v_y=[]
    for i in range(size):
        d.append(random.randint(1,size)*10/size)
        print(d[i])

    window=tk.Tk()
    window=tk.Tk()
    c=tk.Canvas(width=600,height=600)
    ball=[]
    for i in range(size):
        ball.append(c.create_oval(0,0,10*d[i],10*d[i],fill='magenta'))
    c.grid(row=0,column=0)
    prevpos=[]
    for i in range(size):
        prevpos.append(int(0))
    def run():
        # global v_x,v_y
        for i in range(size):
            v_x.append(300*1.3/(frame_rate*d[i]))
            v_y.append(300*2.8/(frame_rate*d[i]))
        for i in range(size):
            c.move(ball[i],v_x[i],v_y[i])
        for i in range(size):
            pos=c.coords(ball[i])
            # c.create_line(prevpos[0],prevpos[1],pos[0],pos[1])
            if pos[2]>=600:
                v_x[i]=-v_x[i]
            if pos[0]<=0:
                v_x[i]=-v_x[i]
            if pos[3]>=600:
                v_y[i]=-v_y[i]
            if pos[1]<=0:
                v_y[i]=-v_y[i]
            # equate(prevpos,pos)

    while True:
        run()
        window.update()
        time.sleep(1/frame_rate)