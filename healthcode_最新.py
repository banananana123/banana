import turtle
import numpy as np
import time
pen = turtle.Pen()
pen.speed(0)
pen.hideturtle()
l = np.load('number.npy')
list = l.tolist()
g_t = int(list[1])
y_t = int(list[3])
r_t = int(list[5])
while True:
    a = input(":")#读取
    list = (a.split('"'))#分割
    if list[0] == "{":
        c_d = list.index("c")#第一个c
        color = list[c_d+2]
        n_d = list.index("name")
        name = list[n_d+2]
        idnum_d = list.index("cid")
        idnum = list[idnum_d+2]
        t_d = list.index("t")#第一个
        tm1 = list[t_d+1].split(':')
        tm = tm1[1].split(',')
        a = time.gmtime(int(tm[0]))
        tim2 = str(a[0])+'-'+str(a[1])+'-'+str(a[2])+' '+str(a[3])+':'+str(a[4])+':'+str(a[5])
        print(color)
        if color == "G":
            g_t += 1
            print("Green health code")
            pen.color("green")
            pen.write("绿码",align="center",font=("楷体",72,"normal"))
            pen.up()
            pen.goto(0,-100)
            pen.down()
            pen.write(name + idnum,align="center",font=("楷体",72,"normal"))
            pen.up()
            pen.goto(0,-200)
            pen.down()
            pen.write(tim2,align="center",font=("楷体",72,"normal"))
            time.sleep(2)
        elif color == "Y":
            y_t += 1
            print("Yellow health code")
            pen.color("yellow")
            pen.write("黄码",align="center",font=("楷体",72,"normal"))
            pen.up()
            pen.goto(0,-100)
            pen.down()
            pen.write(name + idnum,align="center",font=("楷体",72,"normal"))
            pen.up()
            pen.goto(0,-200)
            pen.down()
            pen.write(tim2,align="center",font=("楷体",72,"normal"))
            time.sleep(2)
        elif color == "R":
            r_t += 1
            print("Red health code")
            pen.color("red")
            pen.write("红码",align="center",font=("楷体",72,"normal"))
            pen.up()
            pen.goto(0,-100)
            pen.down()
            pen.write(name + idnum,align="center",font=("楷体",72,"normal"))
            pen.up()
            pen.goto(0,-200)
            pen.down()
            pen.write(tim2,align="center",font=("楷体",72,"normal"))
            time.sleep(2)
        list = [
            'Green scan time:', g_t,
            'Yellow scan time:', y_t,
            'Red scan time:', r_t
            ]
        m = np.array(list)
        np.save('number', m)
    else:
        print("QR error")

    pen.reset()
    pen.hideturtle()
    pen.speed(0)