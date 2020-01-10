import tkinter as tk

def find(tx,ty,pos_x,pos_y):
    for i in range(len(pos_x)):
        if tx==pos_x[i] and ty==pos_y[i]:
            return i

pos_x1=0
pos_y1 = 0
pos_x2 = 0 
pos_y2 = 0
pos_x = []
pos_y = []
pos_x0 = []
pos_y0 = []
window=tk.Tk()

def click(event):
    global pos_x1, pos_y1 , pos_x2, pos_y2
    pos_x1=event.x
    pos_y1=event.y
    pos_x0.append(pos_x1)
    pos_y0.append(pos_y1)


canvas=tk.Canvas(window,width=800,height=800,bg='white')

def undo(event):
    print( "High" )
    global pos_x, pos_x0, pos_y, pos_y0
    tx = pos_x0[len(pos_x0)-1]
    ty = pos_y0[len(pos_y0)-1]
    pos_x0.pop()
    pos_y0.pop()
 
    i=find(tx,ty,pos_x,pos_y)
    for j in range(i,len(pos_x)-1):
        canvas.create_line(pos_x[j],pos_y[j],pos_x[j+1],pos_y[j+1],fill='white')
    for j in range(i,len(pos_x)-1):
        pos_x.pop()
        pos_y.pop()

def left(event):
    global pos_x,pos_y,pos_x1, pos_y1 , pos_x2, pos_y2
    print(event.x)
    pos_x2 = (event.x)
    pos_y2 = (event.y)
    pos_x.append(pos_x1)
    pos_y.append(pos_y1)
    canvas.create_line(pos_x1,pos_y1,pos_x2,pos_y2)
    pos_x1 = pos_x2
    pos_y1 = pos_y2

canvas.bind('<B1-Motion>',left)
canvas.bind('<1>',click)
canvas.bind('<3>',undo)

canvas.pack()

window.mainloop()