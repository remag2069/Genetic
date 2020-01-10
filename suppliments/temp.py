import tkinter as tk


pos_x1=0
pos_y1 = 0
pos_x2 = 0 
pos_y2 = 0
pos_x = []
pos_y = []
pos_x0 = []
pos_y0 = []
color = ['black','red','cyan','blue','pink','magenta']
color_code=0
bg_color = ['white','red','black','cyan','blue','green','yellow']
bg_code=0
window=tk.Tk()

def t_b():
    global color_code
    color_code=0
def t_r():
    global color_code
    color_code=1
def t_c():
    global color_code
    color_code=2
def t_bl():
    global color_code
    color_code=3
def t_p():
    global color_code
    color_code=4
def t_m():
    global color_code
    color_code=5

menubar = tk.Menu(window)
t_color=tk.Menu(menubar,tearoff=0)
t_color.add_command(label='black',command=t_b)
t_color.add_command(label='red',command=t_r)
t_color.add_command(label='cyan',command=t_c)
t_color.add_command(label='blue',command=t_bl)
t_color.add_command(label='pink',command=t_p)
t_color.add_command(label='magenta',command=t_m)
menubar.add_cascade(label="Tool colour", menu=t_color)
# f.add_command(label="text colours", command=toggle_color_m)
# filemenu.add_command(label="New", command=donothing)


window.config(menu=menubar)


def find(tx,ty,pos_x,pos_y):
    for i in range(len(pos_x)):
        if tx==pos_x[i] and ty==pos_y[i]:
            return i

def toggle_color(event):
    print ("Low")
    global color_code
    if color_code ==len(color)-1:
        color_code=0
    else:
        color_code=color_code+1

'''left click'''
def click(event):
    global pos_x1, pos_y1 , pos_x2, pos_y2
    pos_x1=event.x
    pos_y1=event.y
    pos_x0.append(pos_x1)
    pos_y0.append(pos_y1)


canvas=tk.Canvas(window,width=800,height=800,bg=bg_color[bg_code])
canvas.focus_set()

def clear(event):
    canvas.destroy()

def toggle_bg_color(event):
    print('Google')
    global bg_code
    if bg_code ==len(bg_color)-1:
        bg_code=0
    else:
        bg_code=bg_code+1
    canvas.configure(bg=bg_color[bg_code])
    window.update()


def undo(event):
    print( "High" )
    global pos_x, pos_x0, pos_y, pos_y0,bg_code
    tx = pos_x0[len(pos_x0)-1]
    ty = pos_y0[len(pos_y0)-1]
    pos_x0.pop()
    pos_y0.pop()
 
    i=find(tx,ty,pos_x,pos_y)
    for j in range(i,len(pos_x)-1):
        canvas.create_line(pos_x[j],pos_y[j],pos_x[j+1],pos_y[j+1],fill=bg_color[bg_code])
    for j in range(i,len(pos_x)-1):
        pos_x.pop()
        pos_y.pop()

'''left click and drag'''

def left(event):
    global pos_x,pos_y,pos_x1, pos_y1 , pos_x2, pos_y2, color_code
    print(event.x)
    pos_x2 = (event.x)
    pos_y2 = (event.y)
    pos_x.append(pos_x1)
    pos_y.append(pos_y1)
    canvas.create_line(pos_x1,pos_y1,pos_x2,pos_y2, fill=color[color_code])
    pos_x1 = pos_x2
    pos_y1 = pos_y2

canvas.bind('<B1-Motion>',left)
canvas.bind('<1>',click)
canvas.bind('<3>',undo)
canvas.bind("<Right>",toggle_color)
canvas.bind("<Tab>",toggle_bg_color)
canvas.bind("<BackSpace>",clear)

canvas.pack()

window.mainloop()