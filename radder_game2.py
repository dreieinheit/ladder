from turtle import * # 터틀 그래픽스, 앞에 turttle. 붙이는거 삭제
import random # 무작위 추가 함수


shape('turtle') # 화살 모양 거북이
a = 720 # 까다롭긴 하지만 이 변수만 바꿔서 다른 코드 수정없이 바로 진행 가능하게 설정   // 그림에 따라 설정
setup(a,a) # 직사각형 까다로워서 정사각형으로 함

# 함수 설정
l = [] # 선발 주자 진행 칸 = 후발 주자 진행 칸 용
S = [30, 40, 50] # 속도 30~50 사이 // 계산하기 편하게 10단위로만
b = a/2 - 80 # x위치 설정    // 그림에 따라 가변
c = a/2 - 50 # y위치 설정    // 그림에 따라 가변
d = a-a/4 # 위 아래 길이 설정
f = 0 #선발 모양 카피해 후발

def reset(): # 껐다 켰다 안 하기 위해서 모든 작동을 함수로 진행
    
    #기초 설정
    l.clear() # 리스트 사용시 필수로 초기화 해야지 연속진행 차질 없음
    penup()
    clear() # 초기화
    home() # 거북이 위치 0,0
    pensize(5)
    color('black')
    hideturtle()
    speed(0) # 거북이 속도 가장빠름
    
    # 맵 만들기
    right(90) #기본적으로 방향은 오른쪽이기에 아래쪽 향하기 위해서 회전
    goto(b,c) # 1번라인 탑
    pendown()
    forward(d) # 1번 라인 바텀
    penup()
    goto(-1*b,c) # 2번 라인 탑
    pendown()
    forward(d) # 2번 라인 바텀
    penup()
    home()
    speed(4) # 거북이 속도 조절


def second(): # 후발 진행을 위해 먼저 선언

    #함수설정
    pensize(7)
    pencolor('blue') # 색깔 가변 가능
    f = len(l) # len 함수를 통해 리스트 l 속 원소들의 개수 파악
    j = 1

    # 시작위치 설정
    goto(b,c)
    showturtle()
    pendown()

    # 진행
    for j in range(f): # j를 f번 반복
        forward(l[j]) # 선발에서 리스트에 저장된 만큼 가기
        j += 1

        if j % 2 == 0: # 방향전환
            left(90) 
            forward(2*b)
            right(90)
        else:
            right(90)
            forward(2*b)
            left(90)

    if j % 2 == 0:
        goto(b, ycor()) # 짝이면 1번라인
    else:
        goto(-1*b,  ycor()) # 홀이면 2번라인
            
    goto(xcor(), c -d) # 끝에 깔작

    # 정리
    penup()
    hideturtle()
    home()

def first(): # 선발 진행후 후발 진행
    
    # 함수 설정
    pensize(7)
    pencolor("red") # 색깔 가변 가능
    e = c # 끝점 계산기 매번 초기화
    
    # 초반 거북이 설정
    goto(-1*b,c)
    right(90)
    showturtle()
    pendown()

    i = 0

    # 진행
    while True:
        n = random.choice(S) # 리스트 S에 있는 원소들중 하나 선택
        l.append(n) # 리스트 l에 n 추가

        forward(n) # n만큼 이동

        e -= n # 이동한 만큼 길이 재기
        i += 1 # 방향을 위한 횟수

        if i % 2 == 0: # 방향 전환
            right(90)
            forward(2*b)
            left(90)
        else:
            left(90)
            forward(2*b)
            right(90)

        if e - n <= c - d + 20: #끝까지 안 닿도록 설정(a = 720일 경우 c - d + 20 = -210) // 필요시 가변
            if i % 2 == 0:
                goto(-1*b,  e) # 짝이면 2번라인으로
            else:
                goto(b, e) # 홀이면 1번 라인으로
            
            goto(xcor(), c -d) # 끝에 깔작
            break 
    
    # 정리
    penup()
    hideturtle()
    second() # 자동 실행

# 키 클릭시 함수 실행
onkeypress(reset, "r")
onkeypress(first, "1")

reset() # 첫화면 실행
listen() # 키입력 받음
mainloop() # 창 지우기 전까지는 무한 실행