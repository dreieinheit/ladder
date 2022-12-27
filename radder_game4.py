from turtle import *
import random

'''----------------------------------------------------------------'''

# 만약 딱히 정할 것이 없다면 알파벳 순서로 진행

shape('turtle')
a = 1920 # 가로
b = 1080 # 세로
setup(a, b) # 화면

S = [50,60,70] # 속도 설정 {Speed}
L = [] # 선따라 거북이 이동하도록 설정 리스트 {List}
P = [] # 확률 {probability}
dp = 50 # 홀 짝 확률 지정 // 지정 값보다 작거나 같으면 홀, 크면 짝 {define probability}
c = 1 # 리스트 적용 
while c <= 100:
    P.append(c) # p 리스트에 c 추가
    c += 1

l = 0 # 줄 따라 거북이 이동 {line}
turtle_x = a/2 - 80 # 거북이 x 위치
turtle_y = b/2 - 120 # 거북이 y 위치
mv = b - b/4 - 30  # 세로 길이 

'''----------------------------------------------------------------'''

def reset(): # 껏다 켰다 안하기 위해서 함수화
    global ranch
    ranch = random.choice(P) # ranch에 P리스트 중 하나 지정 {random choice}
    print(ranch)

    # 기초설정
    L.clear() # 리스트 사용시 필수로 초기화 해야지 연속진행 차질 없음
    penup()
    clear()
    home() # 거북이 위치 0,0
    pensize(5)
    color('black')
    hideturtle()
    speed(0) # 거북이 속도 가장빠름
    
    # 맵 만들기
    right(90) #기본적으로 방향은 오른쪽이기에 아래쪽 향하기 위해서 회전
    goto(-1*turtle_x, turtle_y) # 홀
    forward(-10)
    write("1", move=False, align="center",font=("arial",50,"bold"))
    forward(10)
    pendown()
    forward(mv) # 홀 바텀
    penup()
    forward(90)
    write("홀", move=False, align="center",font=("arial",50,"bold"))
    goto(turtle_x, turtle_y) # 짝
    forward(-10)
    write("2", move=False, align="center",font=("arial",50,"bold"))
    forward(10)
    pendown()
    forward(mv) # 짝 바텀
    penup()
    forward(90)
    write("짝", move=False, align="center",font=("arial",50,"bold"))
    home()

'''----------------------------------------------------------------'''

def first(): # 1 진행
    # 설정
    num1 = len(L)
    f = 1

    pensize(7)
    speed(10) #!@
    pencolor('red')
    goto(-1*turtle_x, turtle_y) # 홀
    right(90)
    pendown()
    showturtle()

    # 진행
    for f in range(num1):
        forward(L[f])
        f = f + 1

        if f % 2 == 0: # 방향전환
            right(90)
            forward(2*turtle_x)
            left(90)
        else:
            left(90)
            forward(2*turtle_x)
            right(90)
    
    print(f)

    if ranch <= dp: # 홀 가도록 설정
        if f % 2 == 0: # 줄 개수가 짝수
            print('홀짝수개')
            goto(-1*turtle_x,  ycor()) # 홀 
        else: # 줄 개수가 홀수
            print('홀홀수개')
            forward(40)
            right(90)
            forward(2*turtle_x)
            left(90) # 홀 방향으로 가도록 줄 하나 추가하고 진행
    else: # 짝으로 가도록 설정
                if f  % 2 == 0: # 줄개수가 짝수
                    print('짝짝수개')
                    forward(40)
                    left(90)
                    forward(2*turtle_x)
                    right(90) # 짝 방향으로 가도록 줄 하나 추가하고 진행
                else:
                    print('짝홀수개') # 줄 개수가 홀수
                    goto(turtle_x,  ycor()) # 짝
    goto(xcor(), turtle_y - mv) # 끝에 깔작

    penup()
    hideturtle()

'''----------------------------------------------------------------'''

def second(): # 2진행
    # 설정
    num2 = len(L)
    g = 1

    pensize(7)
    speed(10) #!@
    pencolor('blue')
    goto(turtle_x, turtle_y) # 홀
    pendown()
    showturtle()

    # 진행
    for g in range(num2):
        forward(L[g])
        g = g + 1

        if g % 2 == 0: # 방향전환
            left(90)
            forward(2*turtle_x)
            right(90)
        else:
            right(90)
            forward(2*turtle_x)
            left(90)
    
    print(g)

    # first와는 반대 방향을 가도록 설정
    if ranch > dp: # 짝 가도록 설정
        if g % 2 == 0: # 줄 개수가 짝수
            print('짝짝 수개')
            forward(40)
            right(90)
            forward(2*turtle_x)
            left(90) # 홀 방향으로 가도록 줄 하나 추가하고 진행
        else: # 줄 개수가 홀수
            print('짝홀수개')
            goto(-1*turtle_x,  ycor()) # 짝 
    else: # 홀 가도록 설정
                if g  % 2 == 0: # 줄개수가 짝수
                    print('홀짝수개')
                    goto(turtle_x,  ycor()) # 짝
                else:
                    print('홀홀수개') # 줄 개수가 홀수
                    forward(40)
                    left(90)
                    forward(2*turtle_x)
                    right(90) # 짝 방향으로 가도록 줄 하나 추가하고 진행

    goto(xcor(), turtle_y - mv) # 끝에 깔작

    penup()
    hideturtle()

'''----------------------------------------------------------------'''
def start(): # 사다리 지도 그리기

    # 설정
    d = turtle_y
    e = 0

    pensize(5)
    pencolor("black")
    goto(-1*turtle_x, turtle_y)
    right(90)
    pendown()

    # 진행
    while True:
        tm = random.choice(S) # 리스트 S에 있는 원소들 중 하나 선택 {turtle move}
        L.append(tm)

        forward(tm)
        d -= tm
        e += 1

        if e % 2 != 0:
            left(90)
            forward(2*turtle_x)
            right(90)
        else:
            right(90)
            forward(2*turtle_x)
            left(90)

        if d - tm <= turtle_y - mv + 60: #끝까지 안 닿도록 설정 50정도 간격 띄우기
            print(e)
            if ranch <= dp: # 홀 가도록 설정
                if e % 2 == 0: # 줄 개수가 짝수
                    print('홀짝수개')
                    goto(-1*turtle_x,  ycor()) # 홀 
                else: # 줄 개수가 홀수
                    print('홀홀수개')
                    forward(40)
                    right(90)
                    forward(2*turtle_x)
                    left(90) # 홀 방향으로 가도록 줄 하나 추가하고 진행
            else: # 짝으로 가도록 설정
                if e  % 2 == 0: # 줄개수가 짝수
                    print('짝짝수개')
                    forward(40)
                    left(90)
                    forward(2*turtle_x)
                    right(90) # 짝 방향으로 가도록 줄 하나 추가하고 진행
                else:
                    print('짝홀수개') # 줄 개수가 홀수
                    goto(turtle_x,  ycor()) # 짝

            goto(xcor(), turtle_y - mv) # 끝에 깔작
            break
    penup()
    home()
    first()
    second()

'''----------------------------------------------------------------'''

# 키 클릭시 함수 실행
onkeypress(reset, "r")
onkeypress(start, "s")

reset() # 첫화면 실행
listen() # 키 입력 받음
mainloop() # 창 지우기 전까지 무한실행