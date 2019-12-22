from tkinter import *
from random import *

class row:

    def __init__(self,rowNum):
        self.row = rowNum
        self.object = Canvas(tiles_canvas, width = 400, height = 100, bg = "#ff6f00")
        self.object.pack(side=self.row)
        self.left = tile(self,LEFT)
        self.right = tile(self,RIGHT)
        self.middle = tile(self,LEFT)

class tile():

    def __init__(self,master,col):
        self.row = master
        self.col = col
        self.value = ""
        self.object = Canvas(master.object, height = 95, width = 95, bg = self.color, highlightbackground = "#ff6f00")
        self.object.pack(side=self.col)
        txt = self.object.create_text(40,40, fill = "#000", text = self.value)

    @property
    def color(self):
        if self.value == "":
            return "#ffc942" # more cases are to be made...
        return "#ffc942"

    def alter(self):
        self.object.config(bg = self.color)
        self.object.delete(txt)
        txt = self.object.create_text(40,40, fill = "#000", text = self.value)

def right(*args):
    pass
    

window = Tk()
window.geometry("400x500")
window.resizable(0,0)
window.title("2048 by Divyam")

score = Canvas(window, width = 400, height = 100, bg = "#ffd042", highlightbackground = "#ff6f00")
score.pack()

tiles_canvas = Canvas(window, width = 400, height = 400, highlightbackground = "#fff")
tiles_canvas.pack()

top = row(TOP)
bottom = row(BOTTOM)
middle = row(TOP)

window.mainloop()
