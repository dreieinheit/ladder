from turtle import *
import random
shape('turtle')
a = 720
l = []
setup(a, a)


def reset():
    pensize(5)
    penup()
    speed(0)
    right(90)
    goto(a/2 - 80, a/2 - 50)
    pendown()
    forward(a-a/4)
    penup()
    goto(-1*a/2 + 80, a/2 - 50)
    pendown()
    forward(a-a/4)
    
    speed(0)
    penup()
    pencolor('red')
    goto(-1*a/2 + 80, a/2 - 50)
    pendown()
    game_start_1()
    penup()
    pencolor('blue')
    goto(a/2 + 80, a/2 - 50)
    pendown()
    

    
def game_start_1():
    S = [10, 20, 30, 40, 50] # 내려갈 크기
    c = a/2 -50 # 끝점 계산기
    i = 0 # 방향을 위한 카운트

    while True: 
        n = random.choice(S)
        l.append(n) # 선발 거리 = 후발 거리 맞추기 

        if c - n > a/2 - 50 - (a - a/4):
            forward(n)

        c -= n
        i += 1

        if c - n <= a/2 - 50 - (a - a/4):
            if i % 2 == 0:
                goto(-1*(a/2 - 80),  c)
            else:
                goto(a/2 - 80, c)
            
            goto(xcor(), a/2 - 50 -(a-a/4))
            break 

        if i %2 == 0:
            right(90)
            forward(2*(a/2- 80))
            left(90)
        else:
            left(90)
            forward(2*(a/2- 80))
            right(90)
    


        

reset()    
mainloop()
