import tkinter as tk
from tkinter import *
from tkinter import messagebox
import random

def tlacitka(event):
    if event.keysym == 'Up':
        posun()
        gen()
        vykresli()
        vyhra()
    elif event.keysym == 'Down':
        otoc()
        otoc()
        posun()
        otoc()
        otoc()
        gen()
        vykresli()
        vyhra()
    elif event.keysym == 'Left':
        otoc()
        posun()
        otoc()
        otoc()
        otoc()
        gen()
        vykresli()
        vyhra()
    elif event.keysym == 'Right':
        otoc()
        otoc()
        otoc()
        posun()
        otoc()
        gen()
        vykresli()
        vyhra()
    else:
        pass

root = Tk() #jako podložka
m =[[1024,1024,0,0],   #      x
    [0,0,0,0],   #    ####
    [0,0,0,0],   # y  ####
    [0,0,0,0]]   #    ####

barvy = {
    "nic": "#b6b0a0",
    0: "#cbc2b3",
    2: "#eee6db",
    4: "#ece0c8",
    8: "#efb27c",
    16: "#f39768",
    32: "#f37c64",
    64: "#f2623e",
    128: "#eacf76",
    256: "#edcb67",
    512: "#ecc85a",
    1024: "#e7c257",
    2048: "#e8bd4d",
}
root.configure(bg=barvy["nic"])

txt00 = StringVar()
txt01 = StringVar()
txt02 = StringVar()
txt03 = StringVar()
txt10 = StringVar()
txt11 = StringVar()
txt12 = StringVar()
txt13 = StringVar()
txt20 = StringVar()
txt21 = StringVar()
txt22 = StringVar()
txt23 = StringVar()
txt30 = StringVar()
txt31 = StringVar()
txt32 = StringVar()
txt33 = StringVar()

b00 = Button(root,textvariable=txt00,width=10,height=5,state=DISABLED,fg="blue",font="5",relief=SOLID,borderwidth=1)
b00.grid(column=0,row=0,padx=(8,0),pady=(8,0))
b01 = Button(root,textvariable=txt01,width=10,height=5,state=DISABLED,fg="blue",font="5",relief=SOLID,borderwidth=1)
b01.grid(column=0,row=1,padx=(8,0),pady=(8,0))
b02 = Button(root,textvariable=txt02,width=10,height=5,state=DISABLED,fg="blue",font="5",relief=SOLID,borderwidth=1)
b02.grid(column=0,row=2,padx=(8,0),pady=(8,0))
b03 = Button(root,textvariable=txt03,width=10,height=5,state=DISABLED,fg="blue",font="5",relief=SOLID,borderwidth=1)
b03.grid(column=0,row=3,padx=(8,0),pady=(8,8))
b10 = Button(root,textvariable=txt10,width=10,height=5,state=DISABLED,fg="blue",font="5",relief=SOLID,borderwidth=1)
b10.grid(column=1,row=0,padx=(8,0),pady=(8,0))
b11 = Button(root,textvariable=txt11,width=10,height=5,state=DISABLED,fg="blue",font="5",relief=SOLID,borderwidth=1)
b11.grid(column=1,row=1,padx=(8,0),pady=(8,0))
b12 = Button(root,textvariable=txt12,width=10,height=5,state=DISABLED,fg="blue",font="5",relief=SOLID,borderwidth=1)
b12.grid(column=1,row=2,padx=(8,0),pady=(8,0))
b13 = Button(root,textvariable=txt13,width=10,height=5,state=DISABLED,fg="blue",font="5",relief=SOLID,borderwidth=1)
b13.grid(column=1,row=3,padx=(8,0),pady=(0,0))
b20 = Button(root,textvariable=txt20,width=10,height=5,state=DISABLED,fg="blue",font="5",relief=SOLID,borderwidth=1)
b20.grid(column=2,row=0,padx=(8,0),pady=(8,0))
b21 = Button(root,textvariable=txt21,width=10,height=5,state=DISABLED,fg="blue",font="5",relief=SOLID,borderwidth=1)
b21.grid(column=2,row=1,padx=(8,0),pady=(8,0))
b22 = Button(root,textvariable=txt22,width=10,height=5,state=DISABLED,fg="blue",font="5",relief=SOLID,borderwidth=1)
b22.grid(column=2,row=2,padx=(8,0),pady=(8,0))
b23 = Button(root,textvariable=txt23,width=10,height=5,state=DISABLED,fg="blue",font="5",relief=SOLID,borderwidth=1)
b23.grid(column=2,row=3,padx=(8,0),pady=(0,0))
b30 = Button(root,textvariable=txt30,width=10,height=5,state=DISABLED,fg="blue",font="5",relief=SOLID,borderwidth=1)
b30.grid(column=3,row=0,padx=(8,8),pady=(8,0))
b31 = Button(root,textvariable=txt31,width=10,height=5,state=DISABLED,fg="blue",font="5",relief=SOLID,borderwidth=1)
b31.grid(column=3,row=1,padx=(8,8),pady=(8,0))
b32 = Button(root,textvariable=txt32,width=10,height=5,state=DISABLED,fg="blue",font="5",relief=SOLID,borderwidth=1)
b32.grid(column=3,row=2,padx=(8,8),pady=(8,0))
b33 = Button(root,textvariable=txt33,width=10,height=5,state=DISABLED,fg="blue",font="5",relief=SOLID,borderwidth=1)
b33.grid(column=3,row=3,padx=(8,8),pady=(0,0))

def vykresli():
    if m[0][0] == 0:
        txt00.set("")
        b00.configure(bg = barvy[0])
    else:
        txt00.set(m[0][0])
        b00.configure(bg = barvy[m[0][0]])
    if m[0][1] == 0:
        txt10.set("")
        b10.configure(bg = barvy[0])
    else:
        txt10.set(m[0][1])
        b10.configure(bg = barvy[m[0][1]])
    if m[0][2] == 0:
        txt20.set("")
        b20.configure(bg = barvy[0])
    else:
        txt20.set(m[0][2])
        b20.configure(bg = barvy[m[0][2]])
    if m[0][3] == 0:
        txt30.set("")
        b30.configure(bg = barvy[0])
    else:
        txt30.set(m[0][3])
        b30.configure(bg = barvy[m[0][3]])
    if m[1][0] == 0:
        txt01.set("")
        b01.configure(bg = barvy[0])
    else:
        txt01.set(m[1][0])
        b01.configure(bg = barvy[m[1][0]])
    if m[1][1] == 0:
        txt11.set("")
        b11.configure(bg = barvy[0])
    else:
        txt11.set(m[1][1])
        b11.configure(bg = barvy[m[1][1]])
    if m[1][2] == 0:
        txt21.set("")
        b21.configure(bg = barvy[0])
    else:
        txt21.set(m[1][2])
        b21.configure(bg = barvy[m[1][2]])
    if m[1][3] == 0:
        txt31.set("")
        b31.configure(bg = barvy[0])
    else:
        txt31.set(m[1][3])
        b31.configure(bg = barvy[m[1][3]])
    if m[2][0] == 0:
        txt02.set("")
        b02.configure(bg = barvy[0])
    else:
        txt02.set(m[2][0])
        b02.configure(bg = barvy[m[2][0]])
    if m[2][1] == 0:
        txt12.set("")
        b12.configure(bg = barvy[0])
    else:
        txt12.set(m[2][1])
        b12.configure(bg = barvy[m[2][1]])
    if m[2][2] == 0:
        txt22.set("")
        b22.configure(bg = barvy[0])
    else:
        txt22.set(m[2][2])
        b22.configure(bg = barvy[m[2][2]])
    if m[2][3] == 0:
        txt32.set("")
        b32.configure(bg = barvy[0])
    else:
        txt32.set(m[2][3])
        b32.configure(bg = barvy[m[2][3]])
    if m[3][0] == 0:
        txt03.set("")
        b03.configure(bg = barvy[0])
    else:
        txt03.set(m[3][0])
        b03.configure(bg = barvy[m[3][0]])
    if m[3][1] == 0:
        txt13.set("")
        b13.configure(bg = barvy[0])
    else:
        txt13.set(m[3][1])
        b13.configure(bg = barvy[m[3][1]])
    if m[3][2] == 0:
        txt23.set("")
        b23.configure(bg = barvy[0])
    else:
        txt23.set(m[3][2])
        b23.configure(bg = barvy[m[3][2]])
    if m[3][3] == 0:
        txt33.set("")
        b33.configure(bg = barvy[0])
    else:
        txt33.set(m[3][3])
        b33.configure(bg = barvy[m[3][3]])

vykresli()
bylo = False
def vyhra():
    global bylo
    for x in range(4):
        for y in range(4):
            if m[y][x] == 2048 and not bylo:
                bylo = True
                odpoved = messagebox.askquestion("Vyhrál jsi!", "Chceš pokračovat?")
                if odpoved == "yes":
                    pass
                else:
                    root.quit()

def konec():
    global m
    jde = False
    for x in range(4):
        for y in range(3):
            if m[y][x] == m[y+1][x]:
                jde = True
    for x in range(3):
        for y in range(4):
            if m[y][x] == m[y][x+1]:
                jde = True
    if jde == False:
        odpoved = messagebox.askquestion("Konec hry!", "Chceš to zkusit znovu?")
        if odpoved == "yes":
            m =[[0,0,0,0],
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0]]
            gen()
            gen()
            vykresli()
        else:
            root.quit()

root.bind('<Key>', tlacitka)
root.focus()

def gen():
    xka = []
    yka = []
    for x in range(4):
        for y in range(4):
            if m[y][x] == 0:
                xka.append(x)
                yka.append(y)
    if len(xka) != 0:
        index = random.randint(0,(len(xka)-1))
        cislo = random.randint(1,10)
        if cislo == 1:
            m[yka[index]][xka[index]] = 4
        else:
            m[yka[index]][xka[index]] = 2
    else:
        konec()
gen()
gen()
vykresli()
def tisk(m):
    print("\n"+'\n'.join([''.join(['{:4}'.format(item) for item in row])for row in m]))

def otoc():
    N = len(m[0])
    for i in range(N // 2):
        for j in range(i, N - i - 1):
            temp = m[i][j]
            m[i][j] = m[N - 1 - j][i]
            m[N - 1 - j][i] = m[N - 1 - i][N - 1 - j]
            m[N - 1 - i][N - 1 - j] = m[j][N - 1 - i]
            m[j][N - 1 - i] = temp

def posun(): #nahoru
    def secti(x,y):
        #print("secti")
        if m[y][x] == m[y+1][x]:
            m[y][x] = m[y][x]*2
            m[y+1][x] = 0
            #print("1")
        elif y<=1 and m[y][x] == m[y+2][x] and m[y+1][x] == 0:
            m[y][x] = m[y][x]*2
            m[y+2][x] = 0
            #print("2")
        elif y==0 and m[y][x] == m[y+3][x] and m[y+1][x] == 0 and m[y+2][x] == 0:
            m[y][x] = m[y][x]*2
            m[y+3][x] = 0
            #print("3")

    for x in range(4):
        for y in range(3):
            #tisk(m)
            #print(str(x) + "x" + str(y) + " - " + str(m[y][x]))

            if m[y][x] == 0:
                #print("je nula")
                if m[y+1][x] == 0:
                    if y<=1 and m[y+2][x] != 0:
                        m[y][x] = m[y+2][x]
                        m[y+2][x] = 0
                        secti(x,y)
                    elif y<=1 and m[y+2][x] == 0:
                        if y==0 and m[y+3][x] == 0:
                            pass
                        elif y==0 and m[y+3][x] != 0:
                            m[y][x] = m[y+3][x]
                            m[y+3][x] = 0
                            secti(x,y)
                elif m[y+1][x] != 0:
                    m[y][x] = m[y+1][x]
                    m[y+1][x] = 0
                    secti(x,y)

            elif m[y][x] != 0:
                #print("neni nula")
                secti(x,y)

root.mainloop()
