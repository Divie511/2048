from tkinter import *
GameState=0
l=[['','','',],['','',''],['','','']]
i=0
def CheckWin():
    global i
    # X Row win
    if (l[0])[0]==(l[0])[1] and (l[0])[1]==(l[0])[2] and (l[0])[1]!="":
        print((l[0])[1],"Won!")
        frame.destroy()
    elif (l[1])[0]==(l[1])[1] and (l[1])[1]==(l[1])[2] and (l[1])[1]!="":
        print((l[1])[1],"Won!")
        frame.destroy()
    elif (l[2])[1]==(l[2])[0] and (l[2])[1]==(l[2])[2] and (l[2])[2]!="":
        print((l[2])[1],"Won!")
        frame.destroy()

    # X Column win
    elif (l[0])[0]==(l[1])[0] and (l[2])[0]==(l[1])[0] and (l[2])[0]!="":
        print((l[0])[0],"Won!")
        frame.destroy()
    elif (l[0])[1]==(l[1])[1] and (l[2])[1]==(l[1])[1] and (l[2])[1]!="":
        print((l[0])[1],"Won!")
        frame.destroy()
    elif (l[0])[2]==(l[1])[2] and (l[2])[2]==(l[1])[2] and (l[2])[2]!="":
        print((l[0])[2],"Won!")
        frame.destroy()

    #X Diagonal win
    elif (l[0])[0]==(l[1])[1] and (l[0])[0]==(l[2])[2] and (l[2])[2]!="":
        print((l[0])[0],"Won!")
        frame.destroy()
    elif (l[2])[0]==(l[1])[1] and (l[1])[1]==(l[0])[2] and (l[2])[0]!="":
        print((l[1])[1],"Won!")
        frame.destroy()

    #O Row win
    if (l[0])[0]==(l[0])[1] and (l[0])[1]==(l[0])[2] and (l[0])[1]!="":
        print((l[0])[1],"Won!")
        frame.destroy()
    elif (l[1])[0]==(l[1])[1] and (l[1])[1]==(l[1])[2] and (l[1])[1]!="":
        print((l[1])[1],"Won!")
        frame.destroy()
    elif (l[2])[1]==(l[2])[0] and (l[2])[1]==(l[2])[2] and (l[2])[2]!="":
        print((l[2])[1],"Won!")
        frame.destroy()

    #O Column win
    elif (l[0])[0]==(l[1])[0] and (l[2])[0]==(l[1])[0] and (l[2])[0]!="":
        print((l[0])[0],"Won!")
        frame.destroy()
    elif (l[0])[1]==(l[1])[1] and (l[2])[1]==(l[1])[1] and (l[2])[1]!="":
        print((l[0])[1],"Won!")
        frame.destroy()
    elif (l[0])[2]==(l[1])[2] and (l[2])[2]==(l[1])[2] and (l[2])[2]!="":
        print((l[0])[2],"Won!")
        frame.destroy()

    #O Diagonal win
    elif (l[0])[0]==(l[1])[1] and (l[0])[0]==(l[2])[2] and (l[2])[2]!="":
        print((l[0])[0],"Won!")
        frame.destroy()
    elif (l[2])[0]==(l[1])[1] and (l[1])[1]==(l[0])[2] and (l[2])[0]!="":
        print((l[1])[1],"Won!")
        frame.destroy()

    #DRAW
    elif i==8:
        print("It is a draw")
    i+=1

def doNothing():
    return
def ChangeGameState():
    global GameState
    if GameState==0:
        GameState=1
    else:
        GameState=0
    print(GameState)
def ChangeBoard(lab):
    if GameState==0:
        if l[0][0]=='' and lab=='button1_1':
            buttonText1_1.set("X")
            l[0][0]='X'
        elif l[0][1]=='' and lab=='button1_2':
            buttonText1_2.set("X")
            l[0][1]='X'
        elif l[0][2]=='' and lab=='button1_3':
            buttonText1_3.set("X")
            l[0][2]='X'
        elif l[1][0]=='' and lab=='button2_1':
            buttonText2_1.set("X")
            l[1][0]='X'
        elif l[1][1]=='' and lab=='button2_2':
            buttonText2_2.set("X")
            l[1][1]='X'
        elif l[1][2]=='' and lab=='button2_3':
            buttonText2_3.set("X")
            l[1][2]='X'
        elif l[2][0]=='' and lab=='button3_1':
            buttonText3_1.set("X")
            l[2][0]='X'
        elif l[2][1]=='' and lab=='button3_2':
            buttonText3_2.set("X")
            l[2][1]='X'
        elif l[2][2]=='' and lab=='button3_3':
            buttonText3_3.set("X")
            l[2][2]='X'
    else:
        if l[0][0]=='' and lab=='button1_1':
            buttonText1_1.set("O")
            l[0][0]='O'
        elif l[0][1]=='' and lab=='button1_2':
            buttonText1_2.set("O")
            l[0][1]='O'
        elif l[0][2]=='' and lab=='button1_3':
            buttonText1_3.set("O")
            l[0][2]='O'
        elif l[1][0]=='' and lab=='button2_1':
            buttonText2_1.set("O")
            l[1][0]='O'
        elif l[1][1]=='' and lab=='button2_2':
            buttonText2_2.set("O")
            l[1][1]='O'
        elif l[1][2]=='' and lab=='button2_3':
            buttonText2_3.set("O")
            l[1][2]='O'
        elif l[2][0]=='' and lab=='button3_1':
            buttonText3_1.set("O")
            l[2][0]='O'
        elif l[2][1]=='' and lab=='button3_2':
            buttonText3_2.set("O")
            l[2][1]='O'
        elif l[2][2]=='' and lab=='button3_3':
            buttonText3_3.set("O")
            l[2][2]='O'
        else:
            pass
    ChangeGameState()
    CheckWin()
root=Tk()
frame=Frame()
frame.pack()
buttonText1_1=StringVar()
buttonText1_2=StringVar()
buttonText1_3=StringVar()
buttonText2_1=StringVar()
buttonText2_2=StringVar()
buttonText2_3=StringVar()
buttonText3_1=StringVar()
buttonText3_2=StringVar()
buttonText3_3=StringVar()
b1_1=Button(frame,textvariable=buttonText1_1,height=5,width=10,font=(None,20),command=lambda: ChangeBoard("button1_1")).grid(row=1,column=1)
b1_2=Button(frame,textvariable=buttonText1_2,height=5,width=10,font=(None,20),command=lambda: ChangeBoard('button1_2')).grid(row=1,column=2)
b1_3=Button(frame,textvariable=buttonText1_3,height=5,width=10,font=(None,20),command=lambda: ChangeBoard('button1_3')).grid(row=1,column=3)
b2_1=Button(frame,textvariable=buttonText2_1,height=5,width=10,font=(None,20),command=lambda: ChangeBoard('button2_1')).grid(row=2,column=1)
b2_2=Button(frame,textvariable=buttonText2_2,height=5,width=10,font=(None,20),command=lambda: ChangeBoard('button2_2')).grid(row=2,column=2)
b2_3=Button(frame,textvariable=buttonText2_3,height=5,width=10,font=(None,20),command=lambda: ChangeBoard('button2_3')).grid(row=2,column=3)
b3_1=Button(frame,textvariable=buttonText3_1,height=5,width=10,font=(None,20),command=lambda: ChangeBoard('button3_1')).grid(row=3,column=1)
b3_2=Button(frame,textvariable=buttonText3_2,height=5,width=10,font=(None,20),command=lambda: ChangeBoard('button3_2')).grid(row=3,column=2)
b3_3=Button(frame,textvariable=buttonText3_3,height=5,width=10,font=(None,20),command=lambda: ChangeBoard('button3_3')).grid(row=3,column=3)
root.mainloop()
