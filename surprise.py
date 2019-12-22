from tkinter import *
from random import *

points, win = 0, False

def score(pts):
    global points
    points += pts
    scoreboard.config(text = points)

tile_colors = {
    " ": "#cdc0b4",
    2: "#eee4da",
    4: "#ede0c8",
    8: "#f2b179",
    16: "#f59663",
    32: "#f67d5f",
    64: "#f65d3b",
    128: "#fad177",
    256: "#f7d067",
    512: "#fccb59",
    1024: "#edc540",
    2048: "#f9c62d",
    4096: "#f36775",
    8192: "#f14b61",
    16384: "#eb423f",
    32768: "#74b5db"
    }

class Cell:
    
    def __init__(self,r,c):
        self.row = r
        self.column = c
        self.value = " "
        self.frame = Frame(cells_frame, width = 99, height = 99, bg = self.color, borderwidth = 2, relief="groove")
        self.frame.grid(row = self.row, column = self.column)
        self.frame.pack_propagate(0) # to prevent frame resizing
        self.tile = Label(self.frame, bg = self.color, text = self.value)
        self.tile.pack()

    def update(self, v):
        temp = self.value
        self.value = v
        fontheight = 10* (7 - len(str(self.value)) )
        self.frame.config(bg = self.color)
        self.tile.config(text = self.value, font = ("Helvetica", fontheight), bg = self.color)
        if self.value != " ":
            if self.value > 6: self.tile.config(fg = "#fff")
            else: self.tile.config(fg = "#000")
            if temp != " ": score(self.value)
            if not win and self.value == 2048: victory()

    @property
    def color(self):
        if self.value in tile_colors: return tile_colors[self.value]
        else: return "#ff0000"

step = {
    'Right': [0,1],
    'Left': [0,-1],
    'Up': [-1,0],
    'Down': [1,0]
        }

def select(r,c):
    if r==0:
        if c==0: return cell00
        elif c==1: return cell01
        elif c==2: return cell02
        elif c==3: return cell03
    elif r==1:
        if c==0: return cell10
        elif c==1: return cell11
        elif c==2: return cell12
        elif c==3: return cell13
    elif r==2:
        if c==0: return cell20
        elif c==1: return cell21
        elif c==2: return cell22
        elif c==3: return cell23
    elif r==3:
        if c==0: return cell30
        elif c==1: return cell31
        elif c==2: return cell32
        elif c==3: return cell33

def spawn():
    global last
    r = randint(0,3)
    c = randint(0,3)
    CELL = select(r,c)
    if (CELL.value == " "):
        v = 2 if random() < 0.9 else 4
        CELL.update(v)
    else: spawn()
    
def victory():
    global win
    win = True
    something.config(text = "Congratulations, You Won!")

def move_y(event):
    e = event.keysym
    change = False
    x = 1 if e == 'Down' else -1
    xs = 0 if e == 'Down' else 3
    xe = 3 if e == 'Down' else 0
    for c in range(4):
        r=xe-x
        fixed_tile = 0
        while 0 <= r <=3:
            if r==xe: r=xs+x
            t1, t2 = select(r,c), select(r+x,c)
            if t1.value != " ":
                if t2.value == " ":
                    t2.update(t1.value)
                    t1.update(" ")
                    r += x
                    change = True
                    continue
                elif t1.value == t2.value and fixed_tile != t2:
                    t2.update(2*t2.value)
                    t1.update(" ")
                    fixed_tile = t2
                    change = True
            r -= x
    if change: spawn()

def move_x(event):
    e = event.keysym
    change = False
    x = 1 if e == 'Right' else -1
    xs = 0 if e == 'Right' else 3
    xe = 3 if e == 'Right' else 0
    for r in range(4):
        c=xe-x
        fixed_tile = 0
        while 0 <= c <=3:
            if c==xe: c=xs+x
            t1, t2 = select(r,c), select(r,c+x)
            if t1.value != " ":
                if t2.value == " ":
                    t2.update(t1.value)
                    t1.update(" ")
                    c += x
                    change = True
                    continue
                elif t1.value == t2.value and fixed_tile != t2:
                    t2.update(2*t2.value)
                    t1.update(" ")
                    fixed_tile = t2
                    change = True
            c -= x
    if change: spawn()

window = Tk()
window.geometry("400x500")
window.resizable(0,0)
window.title("2048 by Divyam")

header = Frame(window, width = 400, height = 100, bg = "#f9c62d")
header.pack()
header.pack_propagate(0)
title = Frame(header, width = 200, height = 100, bg = "#f9c62d")
title.pack(side=LEFT)
title.pack_propagate(0)
Label(title, text = "2048", font = ("Helvetica", 50), bg = "#f9c62d", fg = "#fff").pack(side = TOP)
something = Label(title, text = "Made by Divyam Joshi", font = ("Helvetica", 10), bg = "#f9c62d", fg = "#fff")
something.pack(side = BOTTOM)

scores = Frame(header, width = 200, height = 100, bg = "#f9c62d")
scores.pack(side = RIGHT)

Label(scores,text = " SCORE ", bg = "#cdc0b4", fg = "#fff").grid(row = 0, column = 1)
scoreboardframe = Frame(scores, bg = "#cdc0b4", height = 20, width = 48)
scoreboardframe.grid(row = 1, column = 1)
scoreboardframe.pack_propagate(0)
scoreboard = Label(scoreboardframe,text = points, bg = "#cdc0b4", fg = "#fff")
scoreboard.pack()

cells_frame = Frame(window, width = 400, height = 400, highlightbackground = "#fff")
cells_frame.pack_propagate(0)
cells_frame.pack()

cell00 = Cell(0,0)
cell01 = Cell(0,1)
cell02 = Cell(0,2)
cell03 = Cell(0,3)
cell10 = Cell(1,0)
cell11 = Cell(1,1)
cell12 = Cell(1,2)
cell13 = Cell(1,3)
cell20 = Cell(2,0)
cell21 = Cell(2,1)
cell22 = Cell(2,2)
cell23 = Cell(2,3)
cell30 = Cell(3,0)
cell31 = Cell(3,1)
cell32 = Cell(3,2)
cell33 = Cell(3,3)

spawn()
window.bind('<Right>',move_x)
window.bind('<Left>',move_x)
window.bind('<Up>',move_y)
window.bind('<Down>',move_y)

window.mainloop()