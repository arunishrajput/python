# Make BMW car logo in python turtle graphics

import turtle
wn=turtle
turtle.bgcolor("#8b8682")
turtle.speed(0)
wn.setup(1530,780)
turtle.penup()
turtle.left(90)
turtle.forward(375)
turtle.left(90)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor("#9ac0cd")
turtle.penup()
turtle.circle(375,-30)
turtle.left(90)
turtle.forward(16)
turtle.pendown()
turtle.right(90)
turtle.penup()
turtle.circle(375-16,200)
turtle.pendown()
turtle.right(90)
turtle.penup()
turtle.forward(16)
turtle.pendown()
turtle.right(90)
turtle.penup()
turtle.circle(-375,200)
turtle.pendown()
turtle.end_fill()
turtle.begin_fill()
turtle.fillcolor("#607b8b")
turtle.penup()
turtle.circle(-375,160)
turtle.right(90)
turtle.forward(16)
turtle.right(90)
turtle.circle(375-16,160)
turtle.right(90)
turtle.forward(16)
turtle.right(90)
turtle.end_fill()
turtle.pendown()
turtle.right(90)
turtle.forward(16)
turtle.right(90)
turtle.circle(359,30)
turtle.circle(359)
turtle.right(-90)
turtle.forward(120)
turtle.right(90)
turtle.begin_fill()
turtle.fillcolor("#0f0f0f")
turtle.circle(239,-240)
turtle.right(90)
turtle.forward(120)
turtle.right(-90)
turtle.circle(359,120*2)
turtle.right(-90)
turtle.forward(120)
turtle.right(-90)
turtle.end_fill()
turtle.left(90)
turtle.forward(120)
turtle.left(90)
for i in range(1):
    for  color0 in ('#1a1a1a','#2b2b2b','#3d3d3d','#4d4d4d','#595959','#737373','#7f7f7f','#a1a1a1','#ababab','#c2c2c2','#cfcfcf','#d9d9d9','#d9d9d9','#cfcfcf','#c2c2c2','#ababab','#a1a1a1','#7f7f7f','#737373','#595959','#4d4d4d','#3d3d3d','#2d2d2d','#1a1a1a',):
        turtle.begin_fill()
        turtle.fillcolor(color0)
        turtle.penup()
        turtle.circle(359,10-5)
        turtle.left(90)
        turtle.penup()
        turtle.forward(120)
        turtle.pendown()
        turtle.left(90)
        turtle.penup()
        turtle.circle(-239,10-5)
        turtle.pendown()
        turtle.left(90)
        turtle.penup()
        turtle.forward(120)
        turtle.pendown()
        turtle.left(90)
        turtle.circle(359,10-5)
        turtle.end_fill()
turtle.left(60+180)
turtle.pencolor("black")
turtle.penup()
turtle.goto(0,228.5)
turtle.pendown()
turtle.pensize(7+3)
turtle.circle(226+1.9)
turtle.left(90)
turtle.forward(228*2+1)
turtle.left(90)
turtle.circle(227.9,90.5)
turtle.left(89.5)
turtle.forward(228*2+1)
turtle.pencolor("black")
turtle.penup()
turtle.goto(0,228.5)
turtle.pendown()
turtle.pensize(5)
turtle.circle(226+1.9)
turtle.left(90)
turtle.forward(228*2+1)
turtle.left(90)
turtle.circle(227.9,90.5)
turtle.left(89.5)
turtle.forward(228*2+1)
turtle.pensize(1)
turtle.pencolor("#7d26cd")
turtle.penup()
turtle.goto(-5-0.5,5-0.2)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor("#3399cc")
turtle.forward(220)
turtle.right(90+0.5)
turtle.circle(-220,90-0.5)
turtle.right(90)
turtle.forward(220)
turtle.end_fill()
turtle.right(90)
turtle.penup()
turtle.goto(5,5)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor("#f7f7f7")
turtle.right(90)
turtle.forward(220)
turtle.right(90.5)
turtle.circle(-220,90-0.5)
turtle.right(90)
turtle.forward(220)
turtle.end_fill()
turtle.penup()
turtle.goto(-5,-5)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor("#f7f7f7")
turtle.forward(220)
turtle.left(90+1)
turtle.circle(220,89)
turtle.right(-90)
turtle.forward(220)
turtle.end_fill()
turtle.penup()
turtle.goto(5,-5)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor("#3399cc")
turtle.right(90)
turtle.forward(220-0.5)
turtle.right(91)
turtle.circle(-220,90-1)
turtle.right(90)
turtle.forward(220)
turtle.end_fill()
# MAKING BORDER'S
turtle.pencolor("black")
turtle.right(90)
turtle.penup()
turtle.goto(6,4)
turtle.pendown()
for i in range(1):
    for color2 in('#575757','#5c5c5c','#6b6b6b','#787878','#8a8a8a','#9c9c9c','#bababa','#adadad','#c9c9c9','#d1d1d1','#d9d9d9'):
        turtle.begin_fill()
        turtle.fillcolor(color2)
        turtle.penup()
        turtle.forward(20)
        turtle.left(90)
        turtle.penup()
        turtle.forward(4)
        turtle.pendown()
        turtle.left(90)
        turtle.forward(20)
        turtle.left(90)
        turtle.penup()
        turtle.forward(4)
        turtle.pendown()
        turtle.left(90)
        turtle.forward(20)
        turtle.pendown()
        turtle.end_fill()
turtle.left(90)
turtle.penup()
turtle.goto(6.5,7)
turtle.pendown()
for i in range(1):
    for color3 in('#575757','#5c5c5c','#6b6b6b','#787878','#8a8a8a','#9c9c9c','#bababa','#adadad','#c9c9c9','#d1d1d1','#d9d9d9'):
        turtle.begin_fill()
        turtle.fillcolor(color3)
        turtle.penup()
        turtle.forward(19.8)
        turtle.left(90)
        turtle.penup()
        turtle.forward(4)
        turtle.pendown()
        turtle.left(90)
        turtle.forward(19.8)
        turtle.left(90)
        turtle.penup()
        turtle.forward(4)
        turtle.pendown()
        turtle.left(90)
        turtle.forward(19.8)
        turtle.pendown()
        turtle.end_fill()
turtle.begin_fill()
turtle.fillcolor("#d9d9d9")
turtle.right(90)
turtle.penup()
turtle.circle(-220,90)
turtle.right(90)
turtle.forward(5-0.5)
turtle.right(90)
turtle.circle(215,90)
turtle.right(90)
turtle.forward(5)
turtle.right(90)
turtle.pendown()
turtle.end_fill()
turtle.penup()
turtle.goto(4,-4)
turtle.pendown()
for i in range(1):
    for color4 in('#575757','#5c5c5c','#6b6b6b','#787878','#8a8a8a','#9c9c9c','#bababa','#adadad','#c9c9c9','#d1d1d1','#d9d9d9'):
        turtle.begin_fill()
        turtle.fillcolor(color4)
        turtle.forward(20)
        turtle.right(90)
        turtle.penup()
        turtle.forward(4)
        turtle.pendown()
        turtle.right(90)
        turtle.forward(20)
        turtle.right(90)
        turtle.penup()
        turtle.forward(4)
        turtle.pendown()
        turtle.right(90)
        turtle.forward(20)
        turtle.end_fill()
turtle.penup()
turtle.goto(4,-4)
turtle.pendown()
turtle.right(90)
for i in range(1):
    for color5 in('#575757','#5c5c5c','#6b6b6b','#787878','#8a8a8a','#9c9c9c','#bababa','#adadad','#c9c9c9','#d1d1d1','#d9d9d9'):
        turtle.begin_fill()
        turtle.fillcolor(color5)
        turtle.forward(20)
        turtle.left(90)
        turtle.penup()
        turtle.forward(4)
        turtle.pendown()
        turtle.left(90)
        turtle.forward(20)
        turtle.left(90)
        turtle.penup()
        turtle.forward(4)
        turtle.pendown()
        turtle.left(90)
        turtle.forward(20)
        turtle.end_fill()
turtle.begin_fill()
turtle.fillcolor("#d9d9d9")
turtle.left(90)
turtle.circle(220,89.1)
turtle.left(90)
turtle.forward(5)
turtle.left(90)
turtle.circle(-215,90-1.1)
turtle.left(90)
turtle.forward(5)
turtle.left(90)
turtle.end_fill()
turtle.right(90)
turtle.penup()
turtle.goto(-5,-4)
turtle.pendown()
for i in range(1):
    for color9 in('#575757','#5c5c5c','#6b6b6b','#787878','#8a8a8a','#9c9c9c','#bababa','#adadad','#c9c9c9','#d1d1d1','#d9d9d9'):
        turtle.begin_fill()
        turtle.fillcolor(color9)

        turtle.forward(20)
        turtle.right(90)
        turtle.penup()
        turtle.forward(4)
        turtle.pendown()
        turtle.right(90)
        turtle.forward(20)
        turtle.right(90)
        turtle.penup()
        turtle.forward(4)
        turtle.pendown()
        turtle.right(90)
        turtle.forward(20)
        turtle.end_fill()
turtle.penup()
turtle.goto(-5+0.4,-4)
turtle.pendown()
turtle.right(90)
for i in range(1):
    for color11 in('#575757','#5c5c5c','#6b6b6b','#787878','#8a8a8a','#9c9c9c','#bababa','#adadad','#c9c9c9','#d1d1d1','#d9d9d9'):
        turtle.begin_fill()
        turtle.fillcolor(color11)
        turtle.penup()
        turtle.forward(20)
        turtle.left(90)
        turtle.penup()
        turtle.forward(4)
        turtle.pendown()
        turtle.left(90)
        turtle.forward(20)
        turtle.left(90)
        turtle.penup()
        turtle.forward(4)
        turtle.pendown()
        turtle.left(90)
        turtle.forward(20)
        turtle.pendown()
        turtle.end_fill()
turtle.begin_fill()
turtle.fillcolor("#d9d9d9")
turtle.left(91-0.5)
turtle.circle(220,89.1)
turtle.left(90)
turtle.forward(5)
turtle.left(90)
turtle.circle(-215,90-1.1)
turtle.left(90)
turtle.forward(5)
turtle.left(90)
turtle.end_fill()
#making left white boarder
turtle.penup()
turtle.goto(-6,5-0.1)
turtle.pendown()
turtle.left(179.5)
for i in range(1):
    for color11 in('#575757','#5c5c5c','#6b6b6b','#787878','#8a8a8a','#9c9c9c','#bababa','#adadad','#c9c9c9','#d1d1d1',):
        turtle.begin_fill()
        turtle.fillcolor(color11)
        turtle.penup()
        turtle.forward(21.3)
        turtle.right(90)
        turtle.penup()
        turtle.forward(4)
        turtle.pendown()
        turtle.right(90)
        turtle.forward(21.3)
        turtle.right(90)
        turtle.penup()
        turtle.forward(4)
        turtle.pendown()
        turtle.right(90)
        turtle.forward(21.3)
        turtle.pendown()
        turtle.end_fill()
turtle.penup()
turtle.goto(-6,5-1)
turtle.pendown()
turtle.left(90)
for i in range(1):
    for color8 in('#575757','#5c5c5c','#6b6b6b','#787878','#8a8a8a','#9c9c9c','#bababa','#adadad','#c9c9c9','#d1d1d1',):
        turtle.begin_fill()
        turtle.fillcolor(color8)
        turtle.forward(21.3)
        turtle.right(90)
        turtle.penup()
        turtle.forward(4)
        turtle.pendown()
        turtle.right(90)
        turtle.forward(21.3)
        turtle.right(90)
        turtle.penup()
        turtle.forward(4)
        turtle.pendown()
        turtle.right(90)
        turtle.forward(21.3)
        turtle.end_fill()
turtle.penup()
turtle.goto(-5.3,5.4)
turtle.forward(220)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor("#d9d9d9")
turtle.right(91-0.6)
turtle.circle(-220,90)
turtle.right(90)
turtle.forward(5)
turtle.right(90)
turtle.circle(215,90)
turtle.right(90)
turtle.forward(5)
turtle.right(90)
turtle.end_fill()
# END BORDER'S
turtle.penup()
turtle.left(-90)
turtle.goto(0,239)
turtle.left(180)
turtle.circle(239,-40)
turtle.pendown()
for i in range(1):
    for  color1 in ('#c7c7c7','#8a8a8a','#7f7f7f','#6e6e6e','#595959','#4d4d4d','#3d3d3d','#242424','#242424','#3d3d3d','#4d4d4d','#595959','#6e6e6e','#7f7f7f','#8a8a8a','#c7c7c7'):
        turtle.begin_fill()
        turtle.fillcolor(color1)
        turtle.circle(239,10)
        turtle.left(90)
        turtle.penup()
        turtle.forward(8)
        turtle.pendown()
        turtle.left(90)
        turtle.circle(-231,10)
        turtle.left(90)
        turtle.penup()
        turtle.forward(8)
        turtle.pendown()
        turtle.left(90)
        turtle.circle(239,10)
        turtle.end_fill()
turtle.right(90+30)
turtle.penup()
turtle.goto(0,239)
turtle.pendown()
turtle.circle(239,-40)
turtle.fillcolor("#a4d3ee")
turtle.begin_fill()
turtle.left(90)
turtle.forward(8)
turtle.left(90)
turtle.circle(-231,200)
turtle.left(90)
turtle.forward(8)
turtle.left(90)
turtle.circle(239,200)
turtle.end_fill()
turtle.left(40)
# making "B"
turtle.penup()
turtle.goto(0,239)
turtle.circle(239,60)
turtle.right(90)
turtle.forward(15)
turtle.right(10)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor("#ffffff")
turtle.forward(95)
turtle.right(90)
turtle.forward(75)
for i in range(8+1):
    turtle.forward(8)
    turtle.right(18)
turtle.left(30+100)
for i in range(8+1):
    turtle.forward(8)
    turtle.right(18)
turtle.left(20-7)
turtle.forward(80)
turtle.end_fill()
turtle.penup()
turtle.back(27)
turtle.right(90)
turtle.forward(17+2)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor("#bfbfbf")
turtle.forward(23)
turtle.right(90)
turtle.forward(45)
for i in range(5):
    turtle.forward(8/3)
    turtle.right(18)
for i in range(5):
    turtle.forward(8/2+0.5)
    turtle.right(18)
turtle.forward(43)
turtle.end_fill()
turtle.penup()
turtle.right(90)
turtle.forward(40)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor("#bfbfbf")
turtle.forward(21)
turtle.right(90)
turtle.forward(40)
for i in range(10):
    turtle.forward(7/2)
    turtle.right(18)
turtle.forward(40)
turtle.end_fill()
#making "m" letter
turtle.penup()
turtle.goto(-50-5,239)
turtle.left(42-1+180)
turtle.forward(10)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor("#ffffff")
turtle.forward(93)
turtle.right(90)
turtle.forward(30-1)
turtle.right(68)
turtle.forward(70)
turtle.left(140)
turtle.forward(70)
turtle.right(74-0.3)
turtle.forward(33)
turtle.right(90)
turtle.forward(95)
turtle.right(90)
turtle.forward(20-1)
turtle.right(90)
turtle.forward(70-5)
turtle.left(160)
turtle.forward(70)
turtle.right(70)
turtle.forward(20)
turtle.right(70-3)
turtle.forward(70)
turtle.left(160)
turtle.forward(60+5)
turtle.right(90)
turtle.forward(20)
turtle.end_fill()
# MAKING LETTER "W"
turtle.penup()
turtle.goto(0,239)
turtle.circle(239,-59-0.7)
turtle.right(90+5)
turtle.forward(14)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor("#ffffff")
turtle.forward(87)
turtle.left(100+3)
turtle.forward(21)
turtle.left(80-5)
turtle.forward(55)
turtle.right(150)
turtle.forward(55)
turtle.left(77)
turtle.forward(25-1)
turtle.left(80-7)
turtle.forward(55)
turtle.right(150)
turtle.forward(55)
turtle.left(76)
turtle.forward(22)
turtle.left(103)
turtle.forward(89)
turtle.left(90-13)
turtle.forward(24)
turtle.left(70+1)
turtle.forward(55+2)
turtle.right(140+5+0.5)
turtle.forward(57-0.5)
turtle.left(70+4)
turtle.hideturtle()
turtle.forward(25)
turtle.end_fill()
turtle.done()
