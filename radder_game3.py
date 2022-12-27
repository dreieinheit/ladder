from turtle import *
import random

'''--------------------------------------------------------'''

# 사전 설정
shape('turtle')
a = 720 # 가로
b = 720 # 세로
setup(a, b) # 화면크기

S = [30, 40, 50] # 속도 설정 리스트
L = [] # 선을 따라 거북이가 이동하도록 설정하기 위한 리스트
P = [] # 확률 리스트
pp = 50 #확률 지정 // 필요시 가변
r = 1 # 리스트 추가
while r <= 100:
    P.append(r) # P 리스트에 r 추가
    r += 1
rc = random.choice(P) # P 리스트에서 하나 지정
num = 0 # 줄 따라 거북이 이동
turtle_x = a/2 - 80 # 거북이 x위치 // 그림에 따라 변경
turtle_y = b/2 - 50 # 거북이 y위치 // 그림에 따라 변경
mv = b- b/4 #세로 길이 // 그림에 따라 변경

'''--------------------------------------------------------'''

def reset(): # 껏다 켰다 안하기 위해서 함수화
    
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
    goto(-1*turtle_x, turtle_y) # 1번라인 탑
    pendown()
    forward(mv) # 1번 라인 바텀
    penup()
    goto(turtle_x, turtle_y) # 2번 라인 탑
    pendown()
    forward(mv) # 2번 라인 바텀
    penup()
    home()

'''--------------------------------------------------------'''

def turtle_seconds(): # 2번라인 진행

    # 설정
    num = len(L)
    j = 1

    pensize(7)
    speed(5)
    pencolor('blue')
    goto (turtle_x, turtle_y)
    pendown()
    showturtle()

    # 진행
    for j in range(num):
        forward(L[j])
        j += 1

        if j % 2 == 0: # 방향전환
            left(90) 
            forward(2*turtle_x)
            right(90)
        else:
            right(90)
            forward(2*turtle_x)
            left(90)

    if j % 2 == 0:
        goto(turtle_x, ycor()) # 짝이면 1번라인
    else:
        goto(-1*turtle_x,  ycor()) # 홀이면 2번라인

    goto(xcor(), turtle_y - mv) # 끝에 깔작

    penup()
    hideturtle()

'''--------------------------------------------------------'''

def turtle_first(): #1번라인 진행

    # 설정
    num = len(L)
    j = 1

    pensize(7)
    speed(5)
    pencolor('red')
    goto (-1*turtle_x, turtle_y)
    pendown()
    showturtle()

    # 진행
    for j in range(num):
        forward(L[j])
        j += 1

        if j % 2 == 0: # 방향전환
            right(90)
            forward(2*turtle_x)
            left(90)
        else:
            left(90)
            forward(2*turtle_x)
            right(90)

    if rc <= pp:
            goto(-1*turtle_x,  ycor()) # 홀
    else:
        goto(turtle_x,  ycor()) # 짝
            
    goto(xcor(), turtle_y - mv) # 끝에 깔작

    penup()
    hideturtle()

'''--------------------------------------------------------'''

def start(): # 사다리 지도 그리기

    # 설정
    e = turtle_y
    i = 0

    pensize(5)
    pencolor("black")
    goto(-1*turtle_x, turtle_y)
    right(90)
    pendown()

    # 진행
    while True:
        tm = random.choice(S) # 리스트 S에 있는 원소들중 하나 선택
        L.append(tm) # 리스트 l에 g 추가

        forward(tm) # n만큼 이동

        e -= tm # 이동한 만큼 길이 재기
        i += 1 # 방향을 위한 횟수

        if i % 2 == 0: # 방향 전환
            right(90)
            forward(2*turtle_x)
            left(90)
        else:
            left(90)
            forward(2*turtle_x)
            right(90)

        if e - tm <= turtle_y - mv + 20: #끝까지 안 닿도록 설정(a = 720일 경우 c - d + 20 = -210) // 필요시 가변
            print(i)
            if i % 2 == 0:
                goto(-1*turtle_x,  ycor()) # 홀
            else:
                goto(turtle_x, ycor()) # 짝
            
            goto(xcor(), turtle_y - mv) # 끝에 깔작
            break

    penup()
    if random.choice(range(1, 3)) == 1: # 어디부터 시작할지 결정
        turtle_first()
        turtle_seconds()
    else:
        turtle_seconds()
        turtle_first()


'''--------------------------------------------------------'''

# 키 클릭시 함수 실행
onkeypress(reset, "r")
onkeypress(start, "s")

reset() # 첫화면 실행
listen() # 키 입력 받음
mainloop() # 창 지우기 전까지 무한실행
