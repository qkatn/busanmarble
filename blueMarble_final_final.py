import random, pygame, sys,time

# from pygame.constants import QUIT, K_ESCAPE, KEYUP
from pygame.locals import *

## File Directory Error 발생할경우 주석해제##
import os
sourceFileDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(sourceFileDir)

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

BROWN=(65,0,0)
SKYBLUE=(160,220,220)
YELLOW1=(255,255,50)
KOREAGREEN=(160,200,50)
UNIVBLUE=(0,120,170)
DARKGREEN = (0,155,0)
GRAY=(120,120,120)
RED = (255,0,0)
YELLOW=(255,255,10)
BLUE = (0,0,255)
WHITE = (255,255,255)
GREEN = (0,255,0)
BLUE = (0,0,128)
BLACK = (0,0,0)
widthSize = 200               #맵 지역 하나의 가로길이
heightSize = 100              #맵 지역 하나의 세로길이
padWidth = widthSize*8+1        #게임판의 전체 가로의 길이를 나타냄 - (맵이 9X9 크기이므로 지역하나의 가로길이*9만큼으로 구성함)
padHeight = heightSize*8+1       #게임판의 전체 세로의 길이를 나타냄 - (맵이 9X9 크기이므로 지역하나의 세로길이*9만큼으로 구성함)
nameBlank=20                  #20픽셀아래만큼 y좌표 아래에 글자를 찍어주기위함
padx = (padWidth - 1)  #보드판의 가로길이로 초기화
pady = (padHeight - 1) #보드판의 세로길이로 초기화
tax=0
bgcolor_name = WHITE

dic1={'출발':0,'온천천':1,'감천문화마을':2,'송정':3,'황금열쇠1':4,'국제시장':5,'자갈치시장':6,'무인도':7,'용궁사':8,\
    '광안리':9,'흰여울문화마을':10,'어린이대공원':11,'송도케이블카':12,'달맞이길':13,'세금받기':14,'용두산공원':15,'태종대':16,\
    '해운대':17,'범어사':18,'황금열쇠2':19,'서면':20,'우주여행':21,'영화의전당':22,'오시리아관광단지':23,'황금열쇠3':24,'시민공원':25,\
    '센텀시티':26,'국세청':27}

dic2={0:'출발' , 1: '온천천', 2 : '감천문화마을' , 3:'송정',4:'황금열쇠1', 5:'국제시장',6: '자갈치시장' , 7: '무인도',  8: '용궁사' , \
    9: '광안리' ,10: '흰여울문화마을' ,11:'어린이대공원', 12: '송도케이블카' , 13: '달맞이길' , 14: '세금받기' ,15 : '용두산공원' ,16:'태종대' , \
    17: '해운대' , 18: '범어사' , 19: '황금열쇠2' , 20: '서면' , 21: '우주여행' ,22: '영화의전당' , 23: '오시리아관광단지' ,24: '황금열쇠3' , 25:'시민공원',\
    26: '센텀시티' , 27:'국세청'}

distance=0



# list=[0,0,0,[0,0,0],[[0,0],[0,0],[0,0]]]

#lists=[ [0,0,0,[0,0,0],[[0,0],[0,0],[0,0]],'''플레이어 이미지1~3 x좌표,y좌표'''[[0,0],[0,0],[0,0]]  ]  ,
#        [0,0,0,[0,0,0],[[0,0],[0,0],[0,0]],'''플레이어 이미지1~3 x좌표,y좌표'''[[0,0],[0,0],[0,0]]  ]  ,
#        [0,0,0,[0,0,0],[[0,0],[0,0],[0,0]],'''플레이어 이미지1~3 x좌표,y좌표'''[[0,0],[0,0],[0,0]]  ]  , ... 등 32개의 정보저장

list=[]
players=[]         #플레이어들의 객체를 담고있음
playerOn=[]         #0 0 0 0/1

# 0:소유권 1:곱해줄 수 2:건물좌표 3:깃발좌표    - 리스트안의 정수
# 일반땅:[0:소유권,  1:곱해줄 수,  2:건물좌표[x,y],  3:깃발좌표[x,y],  4;p1좌표[x,y],  5;p2좌표[x,y],  6;p3좌표[x,y],  7;p4좌표[x,y] , 8: 2번째건물좌표 , 9: 3번째건물좌표]
# 특수땅:[0소유권 , 1[좌표,y좌표],2[좌표,y좌표],3[좌표,y좌표],4[좌표,y좌표]]
for i in range(0,28):           #토지의 정보들 삽입
    if i==0 :                       # 출발지
        list.append([3,[int((7+1/20-i)*widthSize),int((7+2/5)*heightSize)],[int((7+1/5-i)*widthSize),int((7+2/5)*heightSize)]\
            ,[int((7+1/20-i)*widthSize),int((7+7/10)*heightSize)],[int((7+1/5-i)*widthSize),int((7+7/10)*heightSize)]])
    elif i==4 :                    # 황금열쇠1
        list.append([2,[int((7+1/20-i)*widthSize),int((7+2/5)*heightSize)],[int((7+1/5-i)*widthSize),int((7+2/5)*heightSize)]\
            ,[int((7+1/20-i)*widthSize),int((7+7/10)*heightSize)],[int((7+1/5-i)*widthSize),int((7+7/10)*heightSize)]])
    elif i == 19:                   # 황금열쇠2
        list.append([2,[int((5+1/20)*widthSize),int((2/5)*heightSize)],[int((5+1/5)*widthSize),int((2/5)*heightSize)]\
            ,[int((5+1/20)*widthSize),int((7/10)*heightSize)],[int((5+1/5)*widthSize),int((7/10)*heightSize)]])
    elif i == 24:                   # 황금열쇠3
        list.append([2,[int((7+1/20)*widthSize),int((3+2/5)*heightSize)],[int((7+1/5)*widthSize),int((3+2/5)*heightSize)]\
            ,[int((7+1/20)*widthSize),int((3+7/10)*heightSize)],[int((7+1/5)*widthSize),int((3+7/10)*heightSize)]])
    elif i==7:                      # 무인도
        list.append([4,[int((7+1/20-i)*widthSize),int((7+2/5)*heightSize)],[int((7+1/5-i)*widthSize),int((7+2/5)*heightSize)]\
            ,[int((7+1/20-i)*widthSize),int((7+7/10)*heightSize)],[int((7+1/5-i)*widthSize),int((7+7/10)*heightSize)]])
    elif i==14:                     # 세금 받기
        list.append([5,[int((1/20)*widthSize),int((2/5)*heightSize)],[int((1/5)*widthSize),int((2/5)*heightSize)]\
            ,[int((1/20)*widthSize),int((7/10)*heightSize)],[int((1/5)*widthSize),int((7/10)*heightSize)]])
    elif i==21:                     # 우주여행
        list.append([-1,[int((7+1/20)*widthSize),int((2/5)*heightSize)],[int((7+1/5)*widthSize),int((2/5)*heightSize)]\
            ,[int((7+1/20)*widthSize),int((7/10)*heightSize)],[int((7+1/5)*widthSize),int((7/10)*heightSize)]])
    elif i==27:                     # 국세청
        list.append([-2,[int((7+1/20)*widthSize),int((6+2/5)*heightSize)],[int((7+1/5)*widthSize),int((6+2/5)*heightSize)]\
            ,[int((7+1/20)*widthSize),int((6+7/10)*heightSize)],[int((7+1/5)*widthSize),int((6+7/10)*heightSize)]])
    else:  # 건물을 지을수 있는 곳의 정보
        if 0 < i < 7:
            list.append([0, 0, [int((7 + 13 / 20 - i) * widthSize), int((7 + 83 / 100) * heightSize)],
                         [int((7 + 1 / 10 - i) * widthSize), int((7 + 1 / 10) * heightSize)] \
                            , [int((7 + 1 / 20 - i) * widthSize), int((7 + 2 / 5) * heightSize)],
                         [int((7 + 1 / 5 - i) * widthSize), int((7 + 2 / 5) * heightSize)] \
                            , [int((7 + 1 / 20 - i) * widthSize), int((7 + 7 / 10) * heightSize)],
                         [int((7 + 1 / 5 - i) * widthSize), int((7 + 7 / 10) * heightSize)],
                         [int((7 + 4 / 5 - i) * widthSize), int((7 + 75 / 100) * heightSize)],
                         [int((7 + 9 / 10 - i) * widthSize), int((7 + 72 / 100) * heightSize)]])
        elif 7 < i < 14:
            c = i - 7
            list.append([0, 0, [int((13 / 20) * widthSize), int((7 + 83 / 100 - c) * heightSize)],
                         [int((1 / 10) * widthSize), int((7 + 1 / 10 - c) * heightSize)] \
                            , [int((1 / 20) * widthSize), int((7 + 2 / 5 - c) * heightSize)],
                         [int((1 / 5) * widthSize), int((7 + 2 / 5 - c) * heightSize)] \
                            , [int((1 / 20) * widthSize), int((7 + 7 / 10 - c) * heightSize)],
                         [int((1 / 5) * widthSize), int((7 + 7 / 10 - c) * heightSize)],
                         [int((4 / 5) * widthSize), int((7 + 75 / 100 - c) * heightSize)],
                         [int((9 / 10) * widthSize), int((7 + 72 / 100 - c) * heightSize)]])
        elif 14 < i < 21:
            c1 = i - 14
            list.append([0, 0, [int((13 / 20 + c1) * widthSize), int((83 / 100) * heightSize)],
                         [int((1 / 10 + c1) * widthSize), int((1 / 10) * heightSize)], [int((1 / 20 + c1) * widthSize), int((2 / 5) * heightSize)]\
                         ,[int((1 / 5 + c1) * widthSize), int((2 / 5) * heightSize)], [int((1 / 20 + c1) * widthSize), int((7 / 10) * heightSize)]\
                         ,[int((1 / 5 + c1) * widthSize), int((7 / 10) * heightSize)],[int((4 / 5 + c1) * widthSize), int((75 / 100) * heightSize)]\
                         ,[int((9 / 10 + c1) * widthSize), int((72 / 100) * heightSize)]])
        else:
            c2 = i - 21
            list.append([0, 0, [int((7 + 13 / 20) * widthSize), int((83 / 100 + c2) * heightSize)],
                         [int((7 + 1 / 10) * widthSize), int((1 / 10 + c2) * heightSize)] \
                            , [int((7 + 1 / 20) * widthSize), int((2 / 5 + c2) * heightSize)],
                         [int((7 + 1 / 5) * widthSize), int((2 / 5 + c2) * heightSize)] \
                            , [int((7 + 1 / 20) * widthSize), int((7 / 10 + c2) * heightSize)],
                         [int((7 + 1 / 5) * widthSize), int((7 / 10 + c2) * heightSize)],
                         [int((7 + 4 / 5) * widthSize), int((75 / 100 + c2) * heightSize)],
                         [int((7 + 9 / 10) * widthSize), int((72 / 100 + c2) * heightSize)]])
print(list)

#황금열쇠
keylist={1:'건물유지비',2:'로또당첨',3:'불우이웃돕기',4:'노벨상 수상',5:'경주 대회 우승',6:'장학금 수여',7:'생일 축하금'\
         ,8:'교통 신호 범칙금',9:'화재사고',10:'세계여행'}

class button():
    def __init__(self,color,x,y,width,height,text=''):
        self.color=color
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.text=text


    def draw(self,win,outline=None):
        #call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win,outline,(self.x-2,self.y-2,self.width+4,self.height+4),0)

        pygame.draw.rect(win,self.color,(self.x,self.y,self.width,self.height),0)

        if self.text !='':
            font=pygame.font.SysFont('image/NanumGothic.ttf',30)
            text=font.render(self.text,1,(0,0,0))
            win.blit(text,(self.x+(self.width/2-text.get_width()/2),self.y+(self.height/2-text.get_height())))

    def isOver(self,pos):
        #pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0]>self.x and pos[0]<self.x+self.width:
            if pos[1]>self.y and pos[1]<self.y + self.height:
                return True

        return False

greenButton=button((0,255,0),5*widthSize,5*heightSize,400,200,'dice')
yesButton=button((0,255,0),5*widthSize,heightSize,200,100,'YES')
noButton=button((255,0,0),6*widthSize,heightSize,200,100,'NO')

building1Button=button((255,255,0),5*widthSize,2*heightSize,132,100,'RESORT')
building2Button=button((100,200,100),5*widthSize+132,2*heightSize,134,100,'BUILDING')
building3Button=button((0,255,255),5*widthSize+132+134,2*heightSize,134,100,'HOTEL')

Button0 = button((0,255,0), padWidth*0.93, padHeight*0.89, 80, 30, '나라이름!! ')
Button1 = button((0,255,0), (padWidth*0.915)-widthSize, (padHeight*0.89), 80, 30, '나라이름!! ')
Button2 = button((0,255,0), (padWidth*0.915)-(2*widthSize), (padHeight*0.89), 80, 30, '나라이름!! ')
Button3 = button((0,255,0), (padWidth*0.915)-(3*widthSize), (padHeight*0.89), 80, 30, '나라이름!! ')
Button4 = button((0,255,0), (padWidth*0.915)-(4*widthSize), (padHeight*0.89), 80, 30, '나라이름!! ')
Button5 = button((0,255,0), (padWidth*0.915)-(5*widthSize), (padHeight*0.89), 80, 30, '나라이름!! ')
Button6 = button((0,255,0), (padWidth*0.915)-(6*widthSize), (padHeight*0.89), 80, 30, '나라이름!! ')
Button7 = button((0,255,0), (padWidth*0.915)-(7*widthSize), (padHeight*0.89), 80, 30, '나라이름!! ')
Button8 = button((0,255,0), (padWidth*0.915)-(7*widthSize), (padHeight*0.89)-heightSize, 80, 30, '나라이름!! ')
Button9 = button((0,255,0), (padWidth*0.915)-(7*widthSize), (padHeight*0.89)-(2*heightSize), 80, 30, '나라이름!! ')
Button10 = button((0,255,0), (padWidth*0.915)-(7*widthSize), (padHeight*0.89)-(3*heightSize), 80, 30, '나라이름!! ')
Button11 = button((0,255,0), (padWidth*0.915)-(7*widthSize), (padHeight*0.89)-(4*heightSize), 80, 30, '나라이름!! ')
Button12 = button((0,255,0), (padWidth*0.915)-(7*widthSize), (padHeight*0.89)-(5*heightSize), 80, 30, '나라이름!! ')
Button13 = button((0,255,0), (padWidth*0.915)-(7*widthSize), (padHeight*0.89)-(6*heightSize), 80, 30, '나라이름!! ')
Button14 = button((0,255,0), (padWidth*0.915)-(7*widthSize), (padHeight*0.89)-(7*heightSize), 80, 30, '나라이름!! ')
Button15 = button((0,255,0), (padWidth / 20)+widthSize-20, 10, 80, 30, '나라이름!! ')
Button16 = button((0,255,0), (padWidth / 20)+(widthSize*2)-20, 10, 80, 30, '나라이름!! ')
Button17 = button((0,255,0), (padWidth / 20)+(widthSize*3)-20, 10, 80, 30, '나라이름!! ')
Button18 = button((0,255,0), (padWidth / 20)+(widthSize*4)-20, 10, 80, 30, '나라이름!! ')
Button19 = button((0,255,0), (padWidth / 20)+(widthSize*5)-20, 10, 80, 30, '나라이름!! ')
Button20 = button((0,255,0), (padWidth / 20)+(widthSize*6)-20, 10, 80, 30, '나라이름!! ')
Button21 = button((0,255,0), (padWidth / 20)+(widthSize*6.9), 10, 80, 30, '나라이름!! ')
Button22 = button((0,255,0), (padWidth / 20)+(widthSize*6.9), (padHeight*0.90)-(6*heightSize), 80, 30, '나라이름!! ')
Button23 = button((0,255,0), (padWidth / 20)+(widthSize*6.9), (padHeight*0.90)-(5*heightSize), 80, 30, '나라이름!! ')
Button24 = button((0,255,0), (padWidth / 20)+(widthSize*6.9), (padHeight*0.90)-(4*heightSize), 80, 30, '나라이름!! ')
Button25 = button((0,255,0), (padWidth / 20)+(widthSize*6.9), (padHeight*0.89)-(3*heightSize), 80, 30, '나라이름!! ')
Button26 = button((0,255,0), (padWidth / 20)+(widthSize*6.9), (padHeight*0.89)-(2*heightSize), 80, 30, '나라이름!! ')
Button27 = button((0,255,0), (padWidth / 20)+(widthSize*6.9), (padHeight*0.89)-heightSize, 80, 30, '나라이름!! ')



class RichPlayer():         #필드 중 14개의 땅을 획득하거나 한 라인의 땅을 독점하면 승리
    def __init__(self,name):
        # self.playeron=playerOn[0]
        self.name = name
        self.playeron=1     #객체 생성시 게임진행을 판단 하는 player 1로 설정.
        self.character="땅부자"
        self.land=0         #보유한 전체 땅의 갯수
        self.event=0        #한라인의 땅을 독점했는지 여부 검사
        self.sum=200        #현재보유금액
        self.distance=0     #현재 밟고있는 땅 위치
        self.x=0            #맵에서 이미지를 찍어줄 플레이어의 x좌표
        self.y=0            #맵에서 이미지를 찍어줄 플레이어의 x좌표
        self.landlist=[]        #자기가 보유한 땅의 정보를 담고있음
        self.escape=0

    def winJudge(self):
        setland = set(self.landlist)
        counting = 0
        set1 = {1, 2, 3, 5, 6}
        set2 = {8, 9, 10, 11, 12, 13}
        set3 = {15, 16, 17, 18, 20}
        set4 = {22, 23, 25, 26}
        if len(set1.difference(setland))==0 or len(set2.difference(setland))==0 or len(set3.difference(setland))==0 or len(set4.difference(setland))==0:
            self.event = 1      #라인독점여부조사
        counts=0
        for obj in objListCopy:
            if obj.playeron==1:
                counts+=1
        if self.sum>0 and counts==1:
            print("나머지 탈락으로   "+self.character+"승리 !! ")
            return True
        elif self.land>=10:             #보유한 전 땅의 갯수조사
            print("투기자의 땅 조건 만족으로 승리!! ")
            return True
        elif self.event==1:             #한라인 독점여부조사
            print("투기자의 라인독점으로 승리!!")
            return True
        else:
            return False
    def lose(self):
        for land in self.landlist:
            idx=int(str(land))
            list[idx][0]=0
            list[idx][1]=0

    # def isMonopoly(self):
    #     tupleland=tuple(self.landlist)
    #     counting=0
    #     tuple1=(1,2,3,5,6)
    #     tuple2=(8,9,10,11,12,13)
    #     tuple3=(15,16,17,18,20)
    #     tuple4=(22,23,25,26)
    #     if tupleland==tuple1 or tupleland==tuple2 or tupleland==tuple3 or tupleland==tuple4:
    #         self.event=1

class AngelPlayer():
    def __init__(self,name):
        self.name = name
        self.playeron =1
        self.land=0
        self.event=0                #신을 만났을때 1로 변경
        self.rate =20               #신을 만날확률
        self.character ="사이비 신자"
        self.sum = 200
        self.distance = 0
        self.x = 0
        self.y = 0
        self.landlist = []
        self.escape=0

    def winJudge(self):
        counts = 0
        for obj in objListCopy:
            if obj.playeron == 1:
                counts += 1
        if self.sum > 0 and counts == 1:
            print("나머지 탈락으로 "+self.character+"승리 !! ")
            return True
        elif self.event==1:  # 신을 만남
            print("신을 만나 게임 승리 !!")
            return True
        else:
            return False

    def lose(self):
        for land in self.landlist:
            idx = int(str(land))
            list[idx][0] = 0
            list[idx][1] = 0
class TravlerPlayer():          #한국 관광지 4곳 중 3곳 점령시 승리
    def __init__(self,name):    #70%의 확률로 세계여행 직행
        self.playeron = 1
        self.name=name
        self.land=0             #보유한 전체 땅의 갯수
        self.event=0            #한국 땅을 count
        self.rate=70            #70%의 확률로 세계여행 직행
        self.character="인스타 셀럽"
        self.sum=200
        self.distance=0
        self.x=0
        self.y=0
        self.landlist = []
        self.escape=0

    def winJudge(self):
        setland = set(self.landlist)
        setwin = {3, 9, 17, 26}
        setboth= setwin.intersection(setland)
        print(setboth)

        if len(setboth) == 4:  # 4군데 이상 점거하고있다면 여행자의 한국 관광지 독점으로 승리
            self.event = 1
        counts = 0
        for obj in objListCopy:
            if obj.playeron == 1:
                counts += 1
        if counts==1 and self.sum > 0: #상대 플레이어들 다 죽어있다면
            print("나머지 탈락으로 " + self.character + "승리 !! ")
            return True
        elif self.event == 1:  # 보유한 전체 땅의 갯수조사
            print("관광지 독점!! 게임승리!")
            return True
        else:
            return False

    def lose(self):
        for land in self.landlist:
            idx = int(str(land))
            list[idx][0] = 0
            list[idx][1] = 0

class F_StudentPlayer():
    def __init__(self, name):
        self.name = name
        self.playeron =1
        self.land = 0   # 보유한 전체 땅의 갯수
        self.event = 0  # 미래관 창조관 대학본부를 방문할때마다 1씩 증가. 8번 방문하면 게임승리조건
        self.lotto = 0  # 로또맞으면 승리!!
        self.character = '견주'
        self.sum = 200
        self.distance = 0
        self.x = 0
        self.y = 0
        self.landlist = []
        self.escape=0

    def winJudge(self):
        counts = 0
        for obj in objListCopy:
            if obj.playeron == 1:
                counts += 1
        # if self.distance == 11 or self.distance == 15 or self.distance == 25:   #현재 땅위치가 학교 건물중 한 곳이라면 event의 숫자를 하나 올려서 승리 여부 판단
        #         self.event += 1                                                 #현재 방문지역이 미래관,창조관,대학본부중 한곳이라면 # 졸업요건+1
        if counts==1 and self.sum > 0:
            print("나머지 탈락으로 "+self.character+"승리 !! ")
            return True
        elif self.event >= 8:  # 졸업요건을 다채웠는지 여부검사
            print("졸업요건 만족!")
            print("학고생의 게임승리!!")
            return True
        else:
            return False

    def lose(self):
        for land in self.landlist:
            idx = int(str(land))
            list[idx][0] = 0
            list[idx][1] = 0
def showingPlayerInfo():                                        #플레이어들의 캐릭터이름과 보유금액을 입력하는란
    # leng=len(objListCopy)
    NUM=1
    """whiteImage를 넣어주어 간헐적으로 숫자 잘못표기되는 경우 없도록하였음"""
    whiteImage = pygame.image.load('image/WHITE.png')
    Gamepad.blit(whiteImage, (202,102))
    """whiteImage를 넣어주어 간헐적으로 숫자 잘못표기되는 경우 없도록하였음"""

    for idx in range(0,4):
        Playerinfo=objListCopy[idx].character
        Playersum=objListCopy[idx].sum
        str1="Player"+str(NUM)+" : "+str(objListCopy[idx].character)
        str2="보유금액 :" +str(Playersum)
        NUM+=1
        playerinfo1_x=widthSize+nameBlank
        playerinfo1_y=heightSize+int(idx*heightSize*1.5)+nameBlank
        playerinfo2_x=playerinfo1_x
        playerinfo2_y=heightSize+int(heightSize//2)+int(idx*heightSize*1.5)+nameBlank
        playerInfoInput(playerinfo1_x,playerinfo1_y,str1)
        playerInfoInput(playerinfo2_x, playerinfo2_y,str2)

def buildButton():
    global Gamepad, clock, car1, car2, car3, car4, plag1, plag2, plag3, plag4, buildingi1, buildingi2, buildingi3, buildingi4, buildingii1, buildingii2, buildingii3, buildingii4, buildingiii1, buildingiii2, buildingiii3, buildingiii4
    global building1Button, building2Button, building3Button, backmusic, diceSound, music, startmusic


    t = True
    while t:
        allDrawings()
        for events2 in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if events2.type == pygame.MOUSEBUTTONDOWN:
                if building1Button.isOver(pos):
                    return "별장"
                    t=False
                elif building2Button.isOver(pos):
                    return "빌딩"
                    t = False
                elif building3Button.isOver(pos):
                    return "호텔"
                    t = False
            if events2.type == pygame.QUIT:
                pygame.quit()
                quit()

def allDrawings():
    global Gamepad, clock, car1, car2, car3, car4, plag1, plag2, plag3, plag4, buildingi1, buildingi2, buildingi3, buildingi4, buildingii1, buildingii2, buildingii3, buildingii4, buildingiii1, buildingiii2, buildingiii3, buildingiii4
    global building1Button, building2Button, building3Button, backmusic, diceSound, music, startmusic
    building1Button.draw(Gamepad)
    building2Button.draw(Gamepad)
    building3Button.draw(Gamepad)
    greenButton.draw(Gamepad)
    yesButton.draw(Gamepad)
    noButton.draw(Gamepad)
    drawingLand()
    putTheLandName()
    showingPlayerInfo()
    drawObject(car1, R1.x, R1.y)
    drawObject(car2, A1.x, A1.y)
    drawObject(car3, T1.x, T1.y)
    drawObject(car4, F1.x, F1.y)
    for i in range(28):  # 깃발, 건물 그리기
        if list[i][0] == 1:     #소유권이 있는땅이면
            if i in R1.landlist:
                if list[i][1] == 0:
                    drawObject(plag1, list[i][3][0], list[i][3][1])
                elif list[i][1] == 1:
                    drawObject(plag1, list[i][3][0], list[i][3][1])
                    drawObject(buildingi1, list[i][2][0], list[i][2][1])
                elif list[i][1] == 2:
                    drawObject(plag1, list[i][3][0], list[i][3][1])
                    drawObject(buildingi1, list[i][2][0], list[i][2][1])
                    drawObject(buildingii1, list[i][8][0], list[i][8][1])
                elif list[i][1] == 3:
                    drawObject(plag1, list[i][3][0], list[i][3][1])
                    drawObject(buildingi1, list[i][2][0], list[i][2][1])
                    drawObject(buildingii1, list[i][8][0], list[i][8][1])
                    drawObject(buildingiii1, list[i][9][0], list[i][9][1])
                else:
                    print("컴퓨터가 미쳤음")
            elif i in A1.landlist:
                if list[i][1] == 0:
                    drawObject(plag2, list[i][3][0], list[i][3][1])
                elif list[i][1] == 1:
                    drawObject(plag2, list[i][3][0], list[i][3][1])
                    drawObject(buildingi2, list[i][2][0], list[i][2][1])
                elif list[i][1] == 2:
                    drawObject(plag2, list[i][3][0], list[i][3][1])
                    drawObject(buildingi2, list[i][2][0], list[i][2][1])
                    drawObject(buildingii2, list[i][8][0], list[i][8][1])
                elif list[i][1] == 3:
                    drawObject(plag2, list[i][3][0], list[i][3][1])
                    drawObject(buildingi2, list[i][2][0], list[i][2][1])
                    drawObject(buildingii2, list[i][8][0], list[i][8][1])
                    drawObject(buildingiii2, list[i][9][0], list[i][9][1])
                else:
                    print("컴퓨터가 미쳤음!")
            elif i in T1.landlist:
                if list[i][1] == 0:
                    drawObject(plag3, list[i][3][0], list[i][3][1])
                elif list[i][1] == 1:
                    drawObject(plag3, list[i][3][0], list[i][3][1])
                    drawObject(buildingi3, list[i][2][0], list[i][2][1])
                elif list[i][1] == 2:
                    drawObject(plag3, list[i][3][0], list[i][3][1])
                    drawObject(buildingi3, list[i][2][0], list[i][2][1])
                    drawObject(buildingii3, list[i][8][0], list[i][8][1])
                elif list[i][1] == 3:
                    drawObject(plag3, list[i][3][0], list[i][3][1])
                    drawObject(buildingi3, list[i][2][0], list[i][2][1])
                    drawObject(buildingii3, list[i][8][0], list[i][8][1])
                    drawObject(buildingiii3, list[i][9][0], list[i][9][1])
                else:
                    print("컴퓨터가 미쳤음!")
            elif i in F1.landlist:
                if list[i][1] == 0:
                    drawObject(plag4, list[i][3][0], list[i][3][1])
                elif list[i][1] == 1:
                    drawObject(plag4, list[i][3][0], list[i][3][1])
                    drawObject(buildingi4, list[i][2][0], list[i][2][1])
                elif list[i][1] == 2:
                    drawObject(plag4, list[i][3][0], list[i][3][1])
                    drawObject(buildingi4, list[i][2][0], list[i][2][1])
                    drawObject(buildingii4, list[i][8][0], list[i][8][1])
                elif list[i][1] == 3:
                    drawObject(plag4, list[i][3][0], list[i][3][1])
                    drawObject(buildingi4, list[i][2][0], list[i][2][1])
                    drawObject(buildingii4, list[i][8][0], list[i][8][1])
                    drawObject(buildingiii4, list[i][9][0], list[i][9][1])
                else:
                    print("컴퓨터가 미쳤음!")
    pygame.display.update()

def playerInfoInput(playerinfo1_x,playerinfo_y,str):            #해당위치에 문자를 찍어주는 함수(캐릭터 이름과 보유금액..)
    fontObj = pygame.font.Font('image/SCDream5.otf',heightSize // 5)  # 파이썬에서 한글폰트 미사용시 한글이 출력되자않음!
    textSurfaceObj = fontObj.render(str, True, BLACK,WHITE)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj = (playerinfo1_x,playerinfo_y)
    Gamepad.blit(textSurfaceObj, textRectObj)

def CharactorSelect(x,y,str,color, bgcolor, size = 5):
    fontObj = pygame.font.Font('image/CookieRun Bold.ttf', heightSize // size)  # 파이썬에서 한글폰트 미사용시 한글이 출력되자않음!
    textSurfaceObj = fontObj.render(str, True, color, bgcolor)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj = (x, y)
    Gamepad.blit(textSurfaceObj, textRectObj)

def Charactor_Screen():
    Gamepad.fill(BLACK)
    clock = pygame.time.Clock()
    while True:
        # clock.tick(10)
        """캐릭터 이름설명"""
        CharactorSelect((padWidth//8)*0.65,200,'땅부자', WHITE, BLACK, 2)
        CharactorSelect(3*(padWidth//8)*0.82,200, '인스타셀럽',WHITE, BLACK,2)
        CharactorSelect(5*(padWidth//8)*0.88,200, '사이비 신자',WHITE, BLACK,2)
        CharactorSelect(7*(padWidth//8)*0.97,200, '견주',WHITE, BLACK,2)
        """캐릭터 능력, 승리조건, 배경이야기"""
        CharactorSelect((padWidth // 8) * 0.02, 400, '20년 전 무조건 재개발 된다는 친구의 말만 믿고', WHITE, BLACK) #투기자(땅부자)
        CharactorSelect((padWidth // 8) * 0.02, 430, '투자한 돈이 20년째 묶여있는 상태인 투기꾼', WHITE,BLACK)
        CharactorSelect((padWidth // 8) * 0.02, 460, "그 스트레스 때문에 '땅'에 집착하게 되었다" , WHITE, BLACK)
        CharactorSelect((padWidth // 8) * 0.02, 490, "마블을 시작한 계기도 그저 '땅'때문이다", WHITE, BLACK)
        CharactorSelect((padWidth // 8) * 0.02, 550, "<승리조건>", WHITE, BLACK)
        CharactorSelect((padWidth // 8) * 0.02, 580, "소유한 땅이 10개 이상이면 승리!", WHITE, BLACK)
        CharactorSelect((padWidth // 8) * 0.02, 620, "라인 독점시 승리!", WHITE, BLACK)

        CharactorSelect((3 * (padWidth // 8)) * 0.68, 400, '인스타 셀럽에게는 사진밖에 없다. ', WHITE, BLACK) #여행자(인스타셀럽)
        CharactorSelect((3 * (padWidth // 8)) * 0.68, 430, '자신의 사진을 마블게임에서도 찍고 싶어한다.', WHITE, BLACK)
        CharactorSelect((3 * (padWidth // 8)) * 0.68, 460, '찬스카드에서 시간여행을 뽑을 확률이 매우높다.', WHITE, BLACK)
        CharactorSelect((3 * (padWidth // 8)) * 0.68, 550, "<승리조건>", WHITE, BLACK)
        CharactorSelect((3 * (padWidth // 8)) * 0.68, 580, "해수욕장 3곳과 센텀시티를 얻으면 승리!", WHITE, BLACK)
        CharactorSelect((3 * (padWidth // 8)) * 0.68, 670, "<특수 능력>", WHITE, BLACK)
        CharactorSelect((3 * (padWidth // 8)) * 0.68, 700, "황금열쇠에서 세계여행을 뽑을 확률 70%로 증가", WHITE, BLACK)

        CharactorSelect((5 * (padWidth // 8)) * 0.81, 400, '1년 365일 교주님만을 믿어온 ', WHITE, BLACK)
        CharactorSelect((5 * (padWidth // 8)) * 0.81, 430, '이 바보 남자의 유일한 소원은', WHITE, BLACK)
        CharactorSelect((5 * (padWidth // 8)) * 0.81, 460, '굳게 존재할 것이라 믿는 신과의 만남이다.', WHITE, BLACK)
        CharactorSelect((5 * (padWidth // 8)) * 0.81, 550, "<승리조건>", WHITE, BLACK)
        CharactorSelect((5 * (padWidth // 8)) * 0.81, 580, "황금열쇠 도착시 신을만날 확률이 증가한다.", WHITE, BLACK)
        CharactorSelect((5 * (padWidth // 8)) * 0.81, 620, "우주여행에서 신을 마주할 기회가 주어진다.", WHITE, BLACK)
        CharactorSelect((5 * (padWidth // 8)) * 0.81, 650, "신을 만나면 게임 승리!", WHITE, BLACK)

        CharactorSelect((7 * (padWidth // 8)) * 0.867, 400, '까다로운 강아지 망고를 입양해', WHITE, BLACK) # 학고생(견주)
        CharactorSelect((7 * (padWidth // 8)) * 0.867, 430, '매일 공원에 산책을 시켜야 한다', WHITE, BLACK)
        CharactorSelect((7 * (padWidth // 8)) * 0.867, 460, '그는 과연 망고를 만족 시킬 수 있을까?', WHITE, BLACK)
        CharactorSelect((7 * (padWidth // 8)) * 0.867, 550, "<승리조건>", WHITE, BLACK)
        CharactorSelect((7 * (padWidth // 8)) * 0.867, 580, "로또당첨 / 승리요건(공원8번방문)만족시 승리!", WHITE, BLACK)

        """구분선"""
        pygame.draw.line(Gamepad, WHITE, [400-5,0], [400-5,800], 5) #선 굵기 색, 조정
        pygame.draw.aaline(Gamepad, WHITE, [800, 0], [800, 800], True)
        pygame.draw.aaline(Gamepad, WHITE, [1200, 0], [1200, 800], True)
        pygame.draw.aaline(Gamepad, WHITE, [1600, 0], [1600, 800], True)
        # pygame.display.flip()
        """캐릭터 이미지"""
        
        img1 = pygame.image.load('image/car1.png')
        img1 = pygame.transform.scale(img1, (100, 100))
        img2 = pygame.image.load('image/car2.png')
        img2 = pygame.transform.scale(img2, (100, 100))
        img3 = pygame.image.load('image/car3.png')
        img3 = pygame.transform.scale(img3, (100, 100))
        img4 = pygame.image.load('image/car4.png')
        img4 = pygame.transform.scale(img4, (100, 100))
        """배경이미지"""


        Gamepad.blit(img1, ((padWidth//8)*0.78,0))
        Gamepad.blit(img2, ((3*(padWidth // 8)), 0))
        Gamepad.blit(img3, ((5*(padWidth // 8)), 0))
        Gamepad.blit(img4, ((7*(padWidth // 8)), 0))
        if checkForKeyPress():
            pygame.event.get()
            cln()
            break

        pygame.display.update()

def Main():
    initGame()
    Rungame()
    print("종료!!")
    pygame.quit()
R1=RichPlayer('P_Rich')
A1=AngelPlayer('P_Angel')
T1=TravlerPlayer('P_Traveler')
F1=F_StudentPlayer('P_F_Std')
objList=[]
objList.append(R1)
objList.append(A1)
objList.append(T1)
objList.append(F1)
# type(objList[0])
random.shuffle(objList)
objListCopy=objList

def CountingPlayerOn():     #생존 플레이어의 수를 담는 변수가 필요함.
    count=0
    for player in range(len(objList)):
        if player.playeron==1:
            count+=1
    return count


def showStartScreen():
    Gamepad.fill(BLACK)
    fontObj = pygame.font.Font('image/CookieRun Bold.ttf', 100)
    textSurfaceObj = fontObj.render('Busan Marvle', True, WHITE, BLACK)
    textRectObj = textSurfaceObj.get_rect()
   
    countmsg = 0
    FPS = 10
    clock = pygame.time.Clock()
    while True:
       
        textRectObj.center = (padWidth / 2 , padHeight / 2)
        Gamepad.blit(textSurfaceObj, textRectObj)

        if (countmsg %2) == 0:
            drawPressKeyMsg(WHITE) ## 아래쪽에 presskeytoplay 나오게끔 한다.
            countmsg+=1
        elif (countmsg %2) == 1:
            drawPressKeyMsg(BLACK)
            countmsg += 1

        if checkForKeyPress(): ## 키입력시 다음 화면으로 넘어가게끔 해주는 함수
            pygame.event.get()
            cln()
            break

        pygame.display.update()
        clock.tick(FPS)

def purchaseButton():

    t=True
    pygame.display.update()
    while t:
        allDrawings()
        for events1 in pygame.event.get():
            pos=pygame.mouse.get_pos()
            if events1.type==pygame.MOUSEBUTTONDOWN:
                if yesButton.isOver(pos):
                    return "YES"
                    t=False

                elif noButton.isOver(pos):
                    return "NO"
                    t=False
            if events1.type == pygame.QUIT:
                pygame.quit()
                quit()

            if not hasattr(events1, 'key'):  # 키 관련 이벤트가 아닐 경우, 건너뛰도록 처리하는 부분
                continue


def checkForKeyPress():
    pygame.init()
    if len(pygame.event.get(QUIT)) > 0:
        terminate()

    keyUpEvents = pygame.event.get(KEYUP)
    if len(keyUpEvents) == 0:
        return None
    if keyUpEvents[0].key == K_ESCAPE:
        terminate()
    return keyUpEvents[0].key

def terminate():
    pygame.quit()
    sys.exit()



def drawPressKeyMsg(color): # 왼쪽 하단에 press a key to play 나오게 하는 함수
    pressKeySurf = pygame.font.Font('image/CookieRun Regular.ttf', 22)
    pressKeySurfObj = pressKeySurf.render('Press key to start', True, color)
    pressKeyRect = pressKeySurfObj.get_rect()
    pressKeyRect.center = (padWidth / 2, padHeight/1.5)
    Gamepad.blit(pressKeySurfObj, pressKeyRect)


def gameOverFontsys(text, x,y,font): # 게임오버 부분 나오는 함수
    gameOverFont = pygame.font.Font('image/NanumGothic.ttf', font)
    gameSurf = gameOverFont.render(text, True, WHITE)
    gameRect = gameSurf.get_rect()
    gameRect.midtop = (x, y)
    Gamepad.blit(gameSurf, gameRect)

def showGameOverScreen(name): # 게임종료 화면 구성하고 키가 입력되면 다시 캐릭터 선택창으로 돌아가게끔 하는 부분인데 현재는 게임 루프가 안끝나서 실행 안됨
    Gamepad.fill(BLACK)
    if name == '투기자':
        gameOverFontsys('승리자',(padWidth / 2), 10,100)
        gameOverFontsys(name,(padWidth/2),padHeight / 4, 100)
        gameOverFontsys('투기자는 드디어 20년간의 존버를 끝내고 건물주가 되어 행복하게 살게 되었습니다', (padWidth / 2), padHeight / 2, 40)
    if name == '여행자':
        gameOverFontsys('승리자',(padWidth / 2), 10, 100)
        gameOverFontsys(name, (padWidth / 2), padHeight / 4, 100)
        gameOverFontsys('부루마블에서 승리한 여행자는 자신의 운을 다시금 믿게되었습니다.', (padWidth / 2), padHeight / 2, 40)
    if name == '선행자':
        gameOverFontsys('승리자',(padWidth / 2), 10, 100)
        gameOverFontsys(name, (padWidth / 2), padHeight / 4, 100)
        gameOverFontsys('운이 지지리도 없던 선행자는 결국 신을 만나 그동안 모아왔던 복을 한번에 받게 되었습니다', (padWidth / 2), padHeight / 2, 40)
    if name == '학고생':
        gameOverFontsys('승리자',(padWidth / 2), 10, 100)
        gameOverFontsys(name, (padWidth / 2), padHeight / 4, 100)
        gameOverFontsys('학고생은 부루마블 덕분에 결국 학교를 졸업할 수 있게 되었습니다', (padWidth / 2), padHeight / 2, 40)


    pygame.display.update()
    pygame.time.wait(800) # 게임이 종료된 걸 판단하고 8초뒤에 다음화면으로 넘어가게끔 하는 부분
    checkForKeyPress() # clear out any key presses in the event queue
    pygame.time.wait(800)    #게임 종료화면 나오고 8초뒤에 다른 키먹게끔 하는 부분

   

    while True:
        if checkForKeyPress():
            pygame.event.get() #
            break

def cln(): # 게임판을 정해진 색으로 덮어버리는 거, 화면을 재구성하고 싶을때 사용가능
    Gamepad.fill(WHITE)

def drawObject(obj, x, y):  #obj를 받아와서 화면상에 x,y에 뿌려주겠다.
    global Gamepad          #보드판 전역변수로 사용함
    Gamepad.blit(obj,(x,y)) #보드판에 그림같은 객체의 정보를받아 x,y좌표에 뿌려서 출력해줌

def TextsInput(num_x,num_y,i):      #putTheLandName함수에서 각 지역의 이름을 적어주기위해 0~27까지 딕셔너리에 저장된 땅의 이름들을 해당좌표에 넣어주는 함수
    fontObj = pygame.font.Font('image/SCDream5.otf',heightSize // 5)  # 파이썬에서 한글폰트 미사용시 한글이 출력되자않음!
    textSurfaceObj = fontObj.render(dic2[i], True, BLACK)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (num_x, num_y)
    Gamepad.blit(textSurfaceObj, textRectObj)

def putTheLandName():           #각 지역의 이름을 써준 후 황금열쇠,우주,화살표,무인도 이미지삽입
    global Gamepad, bgcolor_name         #실습실경로  C:/Users/nicen/python/파이썬폰트/sw폰트/PySpaceship/NanumGothic.ttf                  /  노트북 경로...C:/Windows/파이썬폰트/sw폰트/PySpaceship/NanumGothic.ttf

    fontObj = pygame.font.Font('image/SCDream5.otf',heightSize//5)    #파이썬에서 한글폰트 미사용시 한글이 출력되자않음!
    thick = 2  # 박스의 테두리 크기를 결정하는 변수
    nx = 0
    ny = 0
    for i in range(0,28):       #오른쪽아래 맨아래의 START 지점부터 맵의 지역이름을 반시계방향으로 넣어주기위함
        num_x=padx
        num_y=pady
        if (i>=0 and i<=7) or (i>=14 and i<=21):        #맨 아래와 맨 위의 좌우로 지역들에 대해 글자를 채워줌.
            for k in range(0,4):                        #이지역들은 공통적으로 x좌표를 획득(아래 START는 오른쪽 아래이므로 좌표를 전체 보드판의 크기에서 한번 빼주는 작업이 필요)
                num_x=num_x//2                         #전체 보드판의 가로의 길이를 2로 4번 나누어줌
            if i >= 0 and i <= 7:                     #맨 오른쪽 아래 지역  <-------------방향으로
                num_x = padx - num_x-(nx*widthSize)                #전체 보드판의 가로의 길이에서 이 길이만큼 빼주면 START 지점의 x좌표 기준점이됨
                nx+=1
                num_y=pady-(heightSize-nameBlank)  #보드판의 세로의길이-(맵 세로의 길이-공백의길이) 를 하면 START지점의 y좌표가됨
                if i==3:
                    bgcolor_name = KOREAGREEN
                else:
                    bgcolor_name = GRAY
            if i>=14 and i<=21 :       #맨 왼쪽 위 ---------> 방향으로
                num_x=num_x+nx*widthSize
                nx+=1
                num_y=nameBlank
                if i==15:
                    bgcolor_name = UNIVBLUE
                elif i==17:
                    bgcolor_name = KOREAGREEN
                else:
                    bgcolor_name = GRAY
        elif (i>=8 and i<=13) or (i>=22 and i<=27):   #(i>=8 and i<=13) or 21>=i and i<=27
            for k in range(0,3):   #공통적으로 y좌표를 획득
                num_y=num_y//2
            if(i>=8 and i<=13):     # 맨 왼쪽 6개의 땅에대해 이름을 채워줌
                for k in range(0,4):
                    num_x=num_x//2
                num_y=pady-(num_y-nameBlank)-heightSize-heightSize*ny
                ny+=1
                if i==9:
                    bgcolor_name = KOREAGREEN
                elif i==11:
                    bgcolor_name = UNIVBLUE
                else:
                    bgcolor_name = GRAY
            if(i>=22 and i<=27):                   #맨 오른쪽 6개의 땅에대해 이름을 채워줌
                for k in range(0,4):
                    num_x=num_x//2
                num_x=padx-num_x
                num_y=num_y+nameBlank+heightSize*ny
                ny+=1
                if i==25:
                    bgcolor_name = UNIVBLUE
                elif i==26:
                    bgcolor_name = KOREAGREEN
                else:
                    bgcolor_name = GRAY
        else:                                     #print 되면 이상한 로직임
            print("Program is not working well!!!")
        if(nx==8):      # 순차적으로 (한칸의 길이) *0 *1 *2에 사용되는연산
            nx=0
        if(ny==6):
            ny=0
        textSurfaceObj = fontObj.render(dic2[i], True, BLACK,bgcolor_name)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (num_x, num_y)
        Gamepad.blit(textSurfaceObj, textRectObj)
    money = pygame.image.load('image/money.jpg')
    space = pygame.image.load('image/space.jpg')
    island = pygame.image.load('image/island.jpg')
    arrowleft = pygame.image.load('image/left.jpg')
    key=pygame.image.load('image/key.jpg')
    nomoney=pygame.image.load('image/nomoney.jpg')

    #
    #세금받기 - 돈그림 / 우주여행 - 우주그림 / 출발 - 화살표그림 / 무인도 - 섬그림

    drawObject(money, 0, 0)
    drawObject(nomoney,padWidth-widthSize,padHeight-2*heightSize)
    drawObject(space,padWidth-widthSize,0)
    drawObject(island, 0, padHeight - heightSize)
    drawObject(arrowleft, padx - widthSize, padHeight-heightSize)

    #황금열쇠 그림
    drawObject(key,3 * widthSize, padHeight - heightSize)
    drawObject(key,5 * widthSize, 0)
    drawObject(key, padWidth - widthSize, 3 * heightSize)

    #검은색 테두리 그려주기
    for i in range(0, 9):
        pygame.draw.rect(Gamepad, BLACK, [i * widthSize, 0, widthSize, heightSize], thick)  # 검은색 테두리 씌워주기 - 맨위의 좌우로 9칸 직사각형 그림
        pygame.draw.rect(Gamepad, BLACK, [0, i * heightSize, widthSize, heightSize], thick)  # 검은색 테두리 씌워주기 - 맨왼쪽 상하로 9칸 직사각형 그림
        pygame.draw.rect(Gamepad, BLACK, [widthSize * 7, i * heightSize, widthSize, heightSize],thick)  # 검은색 테두리 씌워주기 - 맨오른쪽 상하로 9칸 직사각형 그림
        pygame.draw.rect(Gamepad, BLACK, [i * widthSize, heightSize * 7, widthSize, heightSize],thick)  # 검은색 테두리 씌워주기 - 맨아래 좌우로 9칸 직사각형 그림

    #버튼들 검은색 테두리 그려주기
    pygame.draw.rect(Gamepad, BLACK, [5 * widthSize, 5 * heightSize, 400, 200],thick)   # greenbutton
    pygame.draw.rect(Gamepad, BLACK, [5 * widthSize, heightSize, 200, 100], thick)      # yesbutton
    pygame.draw.rect(Gamepad, BLACK, [6 * widthSize, heightSize, 200, 100], thick)  # greenbutton

    pygame.draw.rect(Gamepad, BLACK, [5 * widthSize, 2 * heightSize, 132, 100], thick)  # Resort
    pygame.draw.rect(Gamepad, BLACK, [5 * widthSize + 132, 2 * heightSize, 134, 100], thick)  # Building
    pygame.draw.rect(Gamepad, BLACK, [5 * widthSize + 132 + 134, 2 * heightSize, 134, 100], thick)  # Hotel

    


def drawingLand():
    global money,space,island,leftarrow

    for i in range(0, 9):
        pygame.draw.rect(Gamepad,GRAY, [i * widthSize + 2, 0, widthSize + 2, heightSize])  # 맨위의 좌우로 9칸 직사각형 그림
        pygame.draw.rect(Gamepad,GRAY, [0, i * heightSize + 2, widthSize + 2, heightSize])  # 맨왼쪽 상하로 9칸 직사각형 그림
        pygame.draw.rect(Gamepad,GRAY,[widthSize * 7 + 2, i * heightSize + 2, widthSize, heightSize])  # 맨오른쪽 상하로 9칸 직사각형 그림
        pygame.draw.rect(Gamepad,GRAY,[i * widthSize + 2, heightSize * 7 + 2, widthSize, heightSize])  # 맨아래 좌우로 9칸 직사각형 그림

    #한국땅
    pygame.draw.rect(Gamepad,KOREAGREEN,[3*widthSize,0,widthSize,heightSize])            #17부산
    pygame.draw.rect(Gamepad,KOREAGREEN, [0,5*heightSize,widthSize,heightSize])         #9원주
    pygame.draw.rect(Gamepad,KOREAGREEN, [4*widthSize,padHeight-heightSize,widthSize, heightSize]) #3 제주
    pygame.draw.rect(Gamepad,KOREAGREEN, [padWidth - widthSize, 5* heightSize,widthSize, heightSize])  # 26 서울
    #학교건물
    pygame.draw.rect(Gamepad, UNIVBLUE, [0, 3* heightSize, widthSize, heightSize])  # 11미래관
    pygame.draw.rect(Gamepad, UNIVBLUE, [widthSize,0,widthSize, heightSize])  #15 창조관
    pygame.draw.rect(Gamepad, UNIVBLUE, [padWidth-widthSize,4*heightSize,widthSize, heightSize])  # 25 대학본부

   
def SpaceWorld():
    global Gamepad, clock, car1, car2, car3, car4, plag1, plag2, plag3, plag4, buildingi1, buildingi2, buildingi3, buildingi4, buildingii1, buildingii2, buildingii3, buildingii4, buildingiii1, buildingiii2, buildingiii3, buildingiii4
    global building1Button, building2Button, building3Button, backmusic, diceSound, music, startmusic

    global pos
    t = True
    while t:
        Button0.draw(Gamepad)
        Button1.draw(Gamepad)
        Button2.draw(Gamepad)
        Button3.draw(Gamepad)
        Button4.draw(Gamepad)
        Button5.draw(Gamepad)
        Button6.draw(Gamepad)
        Button7.draw(Gamepad)
        Button8.draw(Gamepad)
        Button9.draw(Gamepad)
        Button10.draw(Gamepad)
        Button11.draw(Gamepad)
        Button12.draw(Gamepad)
        Button13.draw(Gamepad)
        Button14.draw(Gamepad)
        Button15.draw(Gamepad)
        Button16.draw(Gamepad)
        Button17.draw(Gamepad)
        Button18.draw(Gamepad)
        Button19.draw(Gamepad)
        Button20.draw(Gamepad)
        Button21.draw(Gamepad)
        Button22.draw(Gamepad)
        Button23.draw(Gamepad)
        Button24.draw(Gamepad)
        Button25.draw(Gamepad)
        Button26.draw(Gamepad)

        allDrawings()
        for events1 in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if events1.type == pygame.MOUSEBUTTONDOWN:
                if Button0.isOver(pos):
                    return 0
                    t = False

                elif Button1.isOver(pos):
                    return 1
                    t = False
                elif Button2.isOver(pos):
                    return 2
                    t = False
                elif Button3.isOver(pos):
                    return 3
                    t = False
                elif Button4.isOver(pos):
                    return 4
                    t = False
                elif Button5.isOver(pos):
                    return 5
                    t = False
                elif Button6.isOver(pos):
                    return 6
                    t = False
                elif Button7.isOver(pos):
                    return 7
                    t = False
                elif Button8.isOver(pos):
                    return 8
                    t = False
                elif Button9.isOver(pos):
                    return 9
                    t = False
                elif Button10.isOver(pos):
                    return 10
                    t = False
                elif Button11.isOver(pos):
                    return 11
                    t = False
                elif Button12.isOver(pos):
                    return 12
                    t = False
                elif Button13.isOver(pos):
                    return 13
                    t = False
                elif Button14.isOver(pos):
                    return 14
                    t = False
                elif Button15.isOver(pos):
                    return 15
                    t = False
                elif Button16.isOver(pos):
                    return 16
                    t = False
                elif Button17.isOver(pos):
                    return 17
                    t = False
                elif Button18.isOver(pos):
                    return 18
                    t = False
                elif Button19.isOver(pos):
                    return 19
                    t = False
                elif Button20.isOver(pos):
                    return 20
                    t = False
                elif Button21.isOver(pos):
                    return 21
                    t = False
                elif Button22.isOver(pos):
                    return 22
                    t = False
                elif Button23.isOver(pos):
                    return 23
                    t = False
                elif Button24.isOver(pos):
                    return 24
                    t = False
                elif Button25.isOver(pos):
                    return 25
                    t = False
                elif Button26.isOver(pos):
                    return 26
                    t = False
                elif Button27.isOver(pos):
                    return 27
                    t = False
            if events1.type == pygame.QUIT:
                pygame.quit()
                quit()


            if not hasattr(events1, 'key'):  # 키 관련 이벤트가 아닐 경우, 건너뛰도록 처리하는 부분
                continue

def buildingUpgrade():
    global showingtext_y,nextLine,showingtext_x,obj,price

    if list[obj.distance][1]==3:
        print("주사위를 굴려주십시오.")
        upstr = "주사위를 굴려주십시오."
        showingtext_y += nextLine
        playerInfoInput(showingtext_x, showingtext_y, upstr)
    else:
        print('while들어가기전 price: ' + str(price))
        print('while들어가기전 '+str(obj.character)+'의 보유금액: '+str(obj.sum))
        while True:
            print("어떤 건물을 구입하시겠습니까?")
            upstr = "어떤 건물을 구입하시겠습니까?"
            showingtext_y += nextLine
            playerInfoInput(showingtext_x, showingtext_y, upstr)
            answer = buildButton()
            if answer=='별장':
                if list[obj.distance][1]==0:
                    if obj.sum>=price:
                        obj.sum -=price
                        list[obj.distance][1] +=1
                        print("업그레이드 성공!")
                        upstr = "업그레이드 성공!"
                        showingtext_y += nextLine
                        playerInfoInput(showingtext_x, showingtext_y, upstr)
                    else:
                        print("비용이 부족합니다!!")
                        str10 = "비용이 부족합니다!!"
                        showingtext_y += nextLine
                        playerInfoInput(showingtext_x, showingtext_y, str10)

                else:
                    print("이미 있는 건물입니다.")
                    upstr = "이미 있는 건물입니다."
                    showingtext_y += nextLine
                    playerInfoInput(showingtext_x, showingtext_y, upstr)
            elif answer=='빌딩':
                if list[obj.distance][1]==1:     #빌딩을 사려는데 건물이 이미 별장이 있는경우
                    if obj.sum>=price:
                        obj.sum -=price
                        list[obj.distance][1] +=1
                        print("업그레이드 성공!")
                        upstr = "업그레이드 성공!"
                        showingtext_y += nextLine
                        playerInfoInput(showingtext_x, showingtext_y, upstr)
                    else:
                        print("비용이 부족합니다!!")
                        str10 = "비용이 부족합니다!!"
                        showingtext_y += nextLine
                        playerInfoInput(showingtext_x, showingtext_y, str10)
                elif list[obj.distance][1]==0:      #빌딩을 사려는데 건물이 없는경우
                    if obj.sum>=2*price:
                        obj.sum -=2*price
                        list[obj.distance][1] +=2
                        print("업그레이드 성공!")
                        upstr = "업그레이드 성공!"
                        showingtext_y += nextLine
                        playerInfoInput(showingtext_x, showingtext_y, upstr)
                    else:
                        print("비용이 부족합니다!!")
                        str10 = "비용이 부족합니다!!"
                        showingtext_y += nextLine
                        playerInfoInput(showingtext_x, showingtext_y, str10)
                else:
                    print("이미 있는 건물입니다.")
                    upstr = "이미 있는 건물입니다."
                    showingtext_y += nextLine
                    playerInfoInput(showingtext_x, showingtext_y, upstr)
            elif answer=='호텔':
                if list[obj.distance][1]==0:     #호텔을 사려는데 건물이 없는경우
                    if obj.sum>=3*price:
                        obj.sum -=3*price
                        list[obj.distance][1] +=3
                        print("업그레이드 성공!")
                        upstr = "업그레이드 성공!"
                        showingtext_y += nextLine
                        playerInfoInput(showingtext_x, showingtext_y, upstr)
                        print("건물을 모두 구입하였습니다.")
                        upstr = "건물을 모두 구입하였습니다."
                        showingtext_y += nextLine
                        playerInfoInput(showingtext_x, showingtext_y, upstr)
                        print("주사위를 굴려주십시오.")
                        upstr = "주사위를 굴려주십시오.."
                        showingtext_y += nextLine
                        playerInfoInput(showingtext_x, showingtext_y, upstr)
                        break
                    else:
                        print("비용이 부족합니다!!")
                        str10 = "비용이 부족합니다!!"
                        showingtext_y += nextLine
                        playerInfoInput(showingtext_x, showingtext_y, str10)
                elif list[obj.distance][1]==1:     #호텔을 사려는데 별장이 있는경우
                    if obj.sum>=2*price:
                        obj.sum -=2*price
                        list[obj.distance][1] +=2
                        print("업그레이드 성공!")
                        upstr = "업그레이드 성공!"
                        showingtext_y += nextLine
                        playerInfoInput(showingtext_x, showingtext_y, upstr)
                        print("건물을 모두 구입하였습니다.")
                        upstr = "건물을 모두 구입하였습니다."
                        showingtext_y += nextLine
                        playerInfoInput(showingtext_x, showingtext_y, upstr)
                        print("주사위를 굴려주십시오.")
                        upstr = "주사위를 굴려주십시오.."
                        showingtext_y += nextLine
                        playerInfoInput(showingtext_x, showingtext_y, upstr)
                        break
                    else:
                        print("비용이 부족합니다!!")
                        str10 = "비용이 부족합니다!!"
                        showingtext_y += nextLine
                        playerInfoInput(showingtext_x, showingtext_y, str10)
                elif list[obj.distance][1]==2:     #호텔을 사려는데 빌딩이 있는경우
                    if obj.sum>=price:
                        obj.sum -=price
                        list[obj.distance][1] +=1
                        print("업그레이드 성공!")
                        upstr = "업그레이드 성공!"
                        showingtext_y += nextLine
                        playerInfoInput(showingtext_x, showingtext_y, upstr)
                        print("건물을 모두 구입하였습니다.")
                        upstr = "건물을 모두 구입하였습니다."
                        showingtext_y += nextLine
                        playerInfoInput(showingtext_x, showingtext_y, upstr)
                        print("주사위를 굴려주십시오.")
                        upstr = "주사위를 굴려주십시오.."
                        showingtext_y += nextLine
                        playerInfoInput(showingtext_x, showingtext_y, upstr)
                        break
                    else:
                        print("비용이 부족합니다!!")
                        str10 = "비용이 부족합니다!!"
                        showingtext_y += nextLine
                        playerInfoInput(showingtext_x, showingtext_y, str10)
                else:
                    print("이미 있는 건물입니다.")
                    upstr = "이미 있는 건물입니다."
                    showingtext_y += nextLine
                    playerInfoInput(showingtext_x, showingtext_y, upstr)
                    print("주사위를 굴려주십시오.")
                    upstr = "주사위를 굴려주십시오.."
                    showingtext_y += nextLine
                    playerInfoInput(showingtext_x, showingtext_y, upstr)
                    break
            else:
                print('출력되면 이상한로직')
            print("건물을 더 사시겠습니까?")
            upstr = "건물을 더 사시겠습니까?"
            showingtext_y += nextLine
            playerInfoInput(showingtext_x, showingtext_y, upstr)
            answer=purchaseButton()
            if answer=="YES":
                continue
            if answer=="NO":
                print("이제 건물을 구매하지 않습니다.")
                upstr = "이제 건물을 구매하지 않습니다."
                showingtext_y += nextLine
                playerInfoInput(showingtext_x, showingtext_y, upstr)
                print("주사위를 굴려주십시오.")
                upstr = "주사위를 굴려주십시오.."
                showingtext_y += nextLine
                playerInfoInput(showingtext_x, showingtext_y, upstr)
                break

        print('while 나온 후 price: ' + str(price))
        print(str(obj.character)+'의 보유금액: ' + str(obj.sum))


def initGame():     #메인함수라고 생각하면됨.
    global Gamepad,clock,car1,car2,car3,car4,plag1,plag2,plag3,plag4,buildingi1,buildingi2,buildingi3,buildingi4,buildingii1,buildingii2,buildingii3,buildingii4,buildingiii1,buildingiii2,buildingiii3,buildingiii4,whiteImage
    global building1Button,building2Button,building3Button,backmusic,diceSound,music,startmusic
    pygame.init()
    Gamepad = pygame.display.set_mode((padWidth, padHeight))  # 보드판 생성 1600*800
    Gamepad.fill(WHITE)

    diceSound = pygame.mixer.Sound('image/diceSound.wav')
    startmusic = pygame.mixer.Sound('image/gamestart.wav')
    music = pygame.mixer.music.load('image/gamestart.wav')
    pygame.mixer.music.play(-1)
    pygame.display.set_caption('Busan Marble')  # 게임의 제목 MarbleGame
    car1 = pygame.image.load('image/car1.png')
    car2 = pygame.image.load('image/car2.png')
    car3 = pygame.image.load('image/car3.png')
    car4 = pygame.image.load('image/car4.png')
    plag1 = pygame.image.load('image/plag1.png')
    plag2 = pygame.image.load('image/plag2.png')
    plag3 = pygame.image.load('image/plag3.png')
    plag4 = pygame.image.load('image/plag4.png')
    buildingi1 = pygame.image.load('image/buildingi1.png')
    buildingi2 = pygame.image.load('image/buildingi2.png')
    buildingi3 = pygame.image.load('image/buildingi3.png')
    buildingi4 = pygame.image.load('image/buildingi4.png')
    buildingii1 = pygame.image.load('image/buildingii1.png')
    buildingii2 = pygame.image.load('image/buildingii2.png')
    buildingii3 = pygame.image.load('image/buildingii3.png')
    buildingii4 = pygame.image.load('image/buildingii4.png')
    buildingiii1 = pygame.image.load('image/buildingiii1.png')
    buildingiii2 = pygame.image.load('image/buildingiii2.png')
    buildingiii3 = pygame.image.load('image/buildingiii3.png')
    buildingiii4 = pygame.image.load('image/buildingiii4.png')
    whiteImage = pygame.image.load('image/WHITE.png')

    showStartScreen()
    Charactor_Screen()
    startmusic.play()
    drawingLand()
    putTheLandName()
    showingPlayerInfo()

    Rungame()
    #showGameOverScreen() # 게임 종료시 다시 캐릭터선택창

def Rungame():
    global Gamepad,clock,car1,car2,car3,car4,tax,R1,A1,T1,F1,plag1,plag2,plag3,plag4,buildingi1,buildingi2,buildingi3,buildingi4,buildingii1,buildingii2,buildingii3,buildingii4,buildingiii1,buildingiii2,buildingiii3,buildingiii4
    global greenButton,yesButton,noButton,pos,building1Button,building2Button,building3Button
    global showingtext_y, nextLine, showingtext_x, obj, price,diceSound,backMusic,startmusic
    startmusic.play()
    clock = pygame.time.Clock()
    p1 = 0;     #DISTANCE 밟고있는 위치
    p2 = 0;
    p3 = 0;
    p4 = 0
    # 이미지크기는 토지의 세로의 비율 *0.몇 해서 만들고...
    # 화면상에 배치는 보드판 가로세로비율 생각해서 한점 찍기 성공하면
    R1.x = (7 + 1 / 20) * widthSize  # 플레이어 말의 X좌표
    A1.x = (7 + 1 / 5) * widthSize
    T1.x = (7 + 1 / 20) * widthSize
    F1.x = (7 + 1 / 5) * widthSize
    R1.y = (7 + 2 / 5) * heightSize  # 플레이어 말의 y좌표
    A1.y = (7 + 2 / 5) * heightSize
    T1.y = (7 + 7 / 10) * heightSize
    F1.y = (7 + 7 / 10) * heightSize


    turnpage=1
    iswin=False

    alive = []
    search=0

    while not iswin:
        pygame.init()
       
        alive=[]
        greenButton.draw(Gamepad)
        yesButton.draw(Gamepad)
        noButton.draw(Gamepad)
        building1Button.draw(Gamepad)
        building2Button.draw(Gamepad)
        building3Button.draw(Gamepad)


        for obj in objList:
            if obj.playeron == 1:
                alive.append(obj)


        for events in pygame.event.get():


            if events.type==pygame.QUIT:                        #창을 닫으면 iswin==True로 만들어서 반복문탈출
                iswin = True

            pygame.event.get()


            if events.type==pygame.MOUSEBUTTONDOWN: #AND NOT 땅을사는조건 AND NOT 세계여행:
                pos=pygame.mouse.get_pos()
                if events.type==pygame.MOUSEBUTTONDOWN:                  #구동원리는 특정 캐릭터의 턴에서 주사위를 굴리거나 행위동작을 클릭 이벤트로 받아서처리 , 다른 플레이어가 주사위를 굴리면서 턴이 넘어감
                    if greenButton.isOver(pos):

                        Gamepad.fill(WHITE)
                        obj=alive[search]  #@@@@@@@@@@@@@@@@  2021 02 14 터지는 경우 간헐적으로 있음. 아마 턴 돌때 적용해주려고 만든것 같은데 alive에서 빼주거나 해서 index가 벗어나는경우 생길듯.  @@@@@@@@@@@@@@@@@@@@@@@

                        showingtext_x = widthSize * 2 + int(widthSize / 2)  # 해당 x,y좌표위치에 한줄씩 텍스트를 콘솔창처럼 출력해주기위함
                        showingtext_y = heightSize+nameBlank  # 텍스트가 늘어날때마다 y축의 변경이생김
                        nextLine = nameBlank+int(nameBlank//2)  # 해당 수만큼 y좌표를 변경해 한줄씩의 여백이되어 출력해줄것임


                        judge = obj.winJudge()

                        if judge:
                            iswin = True
                            time.sleep(2)
                            showGameOverScreen(obj.character)
                            strwin=obj.character + ("님이 게임에서 승리했습니다.")
                            playerInfoInput(showingtext_x, showingtext_y, strwin)
                            break
                        print(str(obj.character)+'의 현재 보유금액 : ' + str(obj.sum))
                        print(turnpage, "턴!")
                        showingtext_y += nextLine
                        # List.append(str(str(List[1]))
                        str1=str(turnpage) +"턴!"
                        playerInfoInput(showingtext_x,showingtext_y,str1)
                        # !!!!!!!!여기에 세계여행과 무인도 조건 걸어주어야함.!!!!!!!!!!!!!!!
                        if obj.distance==7 and obj.escape>=1 and obj.escape<=3:                                  #무인도지역이면 탈출실패시 continue로 빠져나감
                            print(obj.character," : 더블이면 탈출(3회누적시 무조건탈출)!")
                            str34 = obj.character+" 더블이면 탈출(3회누적시 무조건탈출)!"
                            showingtext_y += nextLine
                            playerInfoInput(showingtext_x, showingtext_y, str34)
                            dice1 = random.randint(1, 6)
                            dice2 = random.randint(1, 6)
                            print(dice1, dice2)
                            if dice1 != dice2:              #탈출 실패하면 이동없이 해당 플레이어 턴종료
                                print("탈출 실패!")
                                str36 = "탈출 실패!"
                                showingtext_y += nextLine
                                playerInfoInput(showingtext_x, showingtext_y, str36)
                                obj.escape += 1
                                # search += 1                 #플레이어의 턴을 바꾸어줌.
                                if obj.escape == 4:
                                    obj.escape = 0
                                    print("다음턴부터 무조건 탈출합니다!")
                                    strescape = "다음턴부터 무조건 탈출합니다!"
                                    showingtext_y += nextLine
                                    playerInfoInput(showingtext_x, showingtext_y, strescape)
                                continue
                            else:                          #탈출 성공하면 주사위를 굴리게하여 턴진행
                                obj.escape=0
                                print(obj.character,"탈출 성공! 새로 주사위를 굴리세요!")
                                strescape=obj.character+"탈출 성공! 새로 주사위를 굴립니다!!"
                                showingtext_y += nextLine
                                playerInfoInput(showingtext_x, showingtext_y, strescape)

                        if (obj.distance != 21 and obj.distance != 7) or (obj.distance == 7 and obj.escape == 0):  # 무인도와 세계여행지역의 조건이 아니면 주사위 굴려야함
                            diceSound.play()
                            print(obj.character + "님이 주사위를 굴립니다.")
                            showingtext_y += nextLine
                            # List.append(obj.character + "님이 주사위를 굴립니다.")
                            str2 = obj.character + "님이 주사위를 굴립니다."
                            playerInfoInput(showingtext_x, showingtext_y, str2)
                            showingtext_y += nextLine  # 다음줄에 출력되도록함
                            r = random.randint(1, 6)
                            obj.distance += r
                            ### strList.append(str(r)+"만큼 이동합니다.")
                            print(str(r) + "만큼 이동합니다.")
                            showingtext_y += nextLine
                            str3 = str(r) + "만큼 이동합니다."
                            playerInfoInput(showingtext_x, showingtext_y, str3)
                            if (obj.distance>=28):
                                strsalary = "월급을 획득합니다."
                                showingtext_y += nextLine
                                playerInfoInput(showingtext_x, showingtext_y, strsalary)
                                obj.distance=obj.distance%28
                                obj.sum+=30



                        ######위의 2개의 if문을 안거치면 세계여행이 수행된 거리에서 아래의 로직들을 동작#############
                        if obj.distance==21:
                            print(obj.character,"세계 여행에 오신것을 환영합니다.")
                            strspace= obj.character+"님. 세계 여행에 오신것을 환영합니다."
                            if obj.character=="선행자":
                                if obj.rate>=100:
                                    print("신에게 도달할 확률이 100%가 되었습니다.")
                                    strgod = obj.character+ "는 신께 도달할 확률이 100%가 되었습니다."
                                    showingtext_y += nextLine
                                    playerInfoInput(showingtext_x, showingtext_y, strgod)

                                    print("신께서", obj.character, "님에게 은총을 주었습니다.")
                                    strbless = "신께서 "+ obj.character+"님에게 은총을 주었습니다.";
                                    showingtext_y += nextLine
                                    playerInfoInput(showingtext_x, showingtext_y, strbless)


                                    print(obj.character + "의 게임 조건 만족!")
                                    obj.event==1
                                    strwin = obj.character + ("님이 게임에서 승리하셨습니다.")
                                    playerInfoInput(showingtext_x, showingtext_y, strwin)
                                    iswin = True
                                    time.sleep(2)
                                    break
                                else:
                                    rate = obj.rate // 10
                                    winnum = random.randint(1, 10)
                                    if winnum>=1 and rate>=winnum:
                                        print("신께서", obj.character, "님에게 은총을 주었습니다.")
                                        strbless = "신께서 " + obj.character + "님에게 은총을 주었습니다.";
                                        showingtext_y += nextLine
                                        playerInfoInput(showingtext_x, showingtext_y, strbless)
                                        print(obj.character + "의 게임 조건 만족!")
                                        obj.event=1
                                        strwin = obj.character + ("님이 게임에서 승리하셨습니다.")
                                        playerInfoInput(showingtext_x, showingtext_y, strwin)
                                        iswin = True
                                        time.sleep(2)
                                        break
                                    else:
                                        print("신을 만나는데 실패하였습니다.")
                                        strfail = "신을 만나는데 실패하였습니다."
                                        showingtext_y += nextLine
                                        playerInfoInput(showingtext_x, showingtext_y, strfail)
                            showingtext_y += nextLine
                            playerInfoInput(showingtext_x, showingtext_y, strspace)
                            print("가고싶은 지역의 이름을 클릭하세요.")
                            strspace = "가고싶은 지역의 이름을 클릭하세요."
                            showingtext_y += nextLine
                            playerInfoInput(showingtext_x, showingtext_y, strspace)
                            wannago=SpaceWorld()
                            if (wannago<=22 and wannago>=0):
                                strsalary = "월급을 획득합니다."
                                showingtext_y += nextLine
                                playerInfoInput(showingtext_x, showingtext_y, strsalary)
                                obj.distance = obj.distance % 28
                                obj.sum += 30
                            obj.distance=wannago



                        ###세계여행 - 맵 이름 클릭으로 distance를 변경해줌
                        ########################################################################################
                        choice = list[obj.distance][0]

                        if obj==R1:
                            if choice==1 or choice==0:
                                R1.x=list[obj.distance][4][0]
                                R1.y=list[obj.distance][4][1]
                            else:
                                R1.x = list[obj.distance][1][0]
                                R1.y = list[obj.distance][1][1]
                        elif obj==A1:
                            if choice==1 or choice==0:
                                A1.x=list[obj.distance][5][0]
                                A1.y=list[obj.distance][5][1]
                            else:
                                A1.x = list[obj.distance][2][0]
                                A1.y = list[obj.distance][2][1]
                        elif obj==T1:
                            if choice==1 or choice==0:
                                T1.x=list[obj.distance][6][0]
                                T1.y=list[obj.distance][6][1]
                            else:
                                T1.x = list[obj.distance][3][0]
                                T1.y = list[obj.distance][3][1]
                        elif obj==F1:
                            if choice==1 or choice==0:
                                F1.x=list[obj.distance][7][0]
                                F1.y=list[obj.distance][7][1]
                            else:
                                F1.x = list[obj.distance][4][0]
                                F1.y = list[obj.distance][4][1]


                        print("해당지역은 ", dic2[int(obj.distance)], "입니다.")
                        str4="해당지역은 "+str(dic2[int(obj.distance)])+"입니다."
                        # if obj.character==""
                        showingtext_y+=nextLine
                        playerInfoInput(showingtext_x, showingtext_y, str4)

                        if (choice == 0) or (choice == 1):  # 도착한곳이 건물을 지을 수 있는 곳인지 여부
                            price=0
                            if (obj.distance >= 1 and obj.distance <= 6):  # 첫라인에서는 5*0+ 5 = 5만원
                                price = list[obj.distance][1] * 5 + 5
                            if (obj.distance >= 8 and obj.distance <= 13):  # 두번째라인에서는 10*0+10=10만원
                                price = list[obj.distance][1] * 10 + 10
                            if (obj.distance >= 15 and obj.distance <= 20):  # 두번째라인에서는 15*0+15=15만원
                                price = list[obj.distance][1] * 15 + 15
                            if (obj.distance >= 22 and obj.distance <= 26):  # 세번째라인에서는 20*0+20=20만원
                                price = list[obj.distance][1] * 20 + 20


                            if obj.character=="학고생":    #학고생은 학교 건물 EVENT 횟수 방문만 하면 증가!!!(8회)
                                if obj.distance==11 or obj.distance == 15 or obj.distance == 25:# 현재 땅위치가 학교 건물중 한 곳이라면 event의 숫자를 하나 올려서 승리 여부 판단
                                    obj.event += 1                                                 #현재 방문지역이 미래관,창조관,대학본부중 한곳이라면 # 졸업요건+1
                                judge = obj.winJudge()
                                if judge:
                                    showingtext_y += nextLine
                                    strwin = obj.character + ("님이 게임에서 승리하셨습니다.")
                                    playerInfoInput(showingtext_x, showingtext_y, strwin)
                                    iswin = True
                                    time.sleep(2)
                                    break
                            if (list[obj.distance][0] == 0):  # 그 땅의 소유권이 아무에게도 없는경우
                                # 땅을 사는조건=TRUE
                                # price = 0
                                print(dic2[obj.distance]," 지역을 구매하시겠습니까?")
                                str5=str(dic2[obj.distance]+"지역을 구매하시겠습니까?")
                                showingtext_y += nextLine
                                playerInfoInput(showingtext_x, showingtext_y, str5)
                                answer=purchaseButton()
                                # YES       /      NO
                                ######YES버튼######
                                ######YES버튼######
                                if answer=="YES":

                                    if (obj.sum >= price):  # 돈이 지불할 가격보다 많이 있을때만 살 수 있음
                                        obj.sum -= price
                                        # 20210214 넣은코드  #
                                        #obj.landlist.append(obj.distance) => obj.landlist.append(int(obj.distance))
                                        # 20210214 넣은코드  #
                                        obj.landlist.append(int(obj.distance))    # 해당 땅의 0~27 넘버가  객체의 땅 정보에 들어있음
                                        print(obj,obj.landlist)
                                        list[obj.distance][0] = 1     #에러 발견
                                        print(dic2[obj.distance]," 지역을 구매합니다.")
                                        str6=dic2[obj.distance]+" 지역을 구매합니다."
                                        showingtext_y += nextLine
                                        playerInfoInput(showingtext_x, showingtext_y, str6)

                                        judge = obj.winJudge()
                                        if judge:
                                            showingtext_y += nextLine
                                            strwin = obj.character + ("님이 게임에서 승리하셨습니다.")
                                            playerInfoInput(showingtext_x, showingtext_y, strwin)
                                            iswin = True
                                            time.sleep(2)
                                            break
                                        buildingUpgrade()
                                    else:
                                        print("돈이 없습니다!!")
                                        str7="돈이 부족합니다! 구매실패."
                                        showingtext_y += nextLine
                                        playerInfoInput(showingtext_x, showingtext_y, str7)

                                ######NO버튼######
                                ######NO버튼######
                                # if No버튼:
                                # 내돈 전혀 안까임(아무행위 없게 하면됨
                                if answer=="NO":
                                    print("구매하지 않습니다.")
                                    nostr=dic2[obj.distance]+"를 구매하지 않습니다."
                                    showingtext_y += nextLine
                                    playerInfoInput(showingtext_x, showingtext_y, nostr)
                            else:  # (list[obj.distance][0] == 1):    # 다른사람이 그 땅을 소유하고 있는경우

                                if obj.distance in obj.landlist:  # 소유주가 있는 땅이 내 소유의 땅이라면
                                    if (list[obj.distance][1] >= 3):
                                        print("이미 풀 업그레이드입니다.")
                                        str8="이미 풀 업그레이드입니다."
                                        showingtext_y += nextLine
                                        playerInfoInput(showingtext_x, showingtext_y, str8)
                                    else:
                                        print("업그레이드 하시겠습니까?")
                                        str9 = "업그레이드 하시겠습니까?"
                                        showingtext_y += nextLine
                                        playerInfoInput(showingtext_x, showingtext_y, str9)
                                        answer = purchaseButton()
                                        if answer == "YES":
                                            buildingUpgrade()
                                        judge = obj.winJudge()

                                        if judge:
                                            showingtext_y += nextLine
                                            strwin = obj.character + ("님이 게임에서 승리하셨습니다.")
                                            playerInfoInput(showingtext_x, showingtext_y, strwin)
                                            iswin = True
                                            time.sleep(2)
                                            break
                                        if answer=="NO":
                                            print("업그레이드 하지 않습니다.")
                                            upstr="업그레이드 하지 않습니다."
                                            showingtext_y += nextLine
                                            playerInfoInput(showingtext_x, showingtext_y, upstr)
                                        ###NO 버튼###
                                        ###NO 버튼###
                                        #아무일도 안일어남

                                else:                       #내 소유주가 아닌땅이면 금액지불 후 인수여부결정
                                    # 20210214 넣은코드 #
                                    print('price:'+str(price))
                                    #price=price*list[obj.distance][1]
                                    print('인수 price:'+str(price))
                                    # 20210214 넣은코드 #
                                    if (obj.sum >= price):  #금액을 지불할 수 있으면
                                        obj.sum -= price
                                        print(price, "만원을 지불합니다.")
                                        str10 = str(price)+"만원을 지불합니다."
                                        showingtext_y += nextLine
                                        playerInfoInput(showingtext_x, showingtext_y, str10)

                                        print(dic2[obj.distance]," 지역을 구매하시겠습니까?")
                                        str11 =str(dic2[obj.distance])+"지역을 구매하시겠습니까?"
                                        showingtext_y += nextLine
                                        playerInfoInput(showingtext_x, showingtext_y, str11)

                                        answer = purchaseButton()
                                        if answer == "YES":
                                            # YES       /      NO
                                            ###YES버튼###
                                            ###YES버튼###
                                            if (obj.sum >= price):      #사용자가 YES를 눌러 인수하려할때 돈이충분하면
                                                print(dic2[obj.distance], " 지역을 구매합니다.")
                                                str12 = str(dic2[obj.distance]+" 지역을 구매합니다.")
                                                showingtext_y += nextLine
                                                playerInfoInput(showingtext_x, showingtext_y, str12)
                                                obj.sum -= price
                                                print(str(obj.character) + '의 인수하기 전 기존땅 :' + str(obj.landlist))
                                                obj.landlist.append(int(obj.distance))   #클래스들이 소유한 landList에 땅index추가
                                                for objects in alive: #객체들을 하나씩조사
                                                    numberis = int(obj.distance)
                                                    if objects==obj:    #내땅을 조사하려고하면 continue
                                                        continue
                                                    elif numberis in objects.landlist: #내가 산땅이 다른 사람의 땅에 있으면        #landlist 임
                                                        print(str(objects.name)+'의 기존땅 :'+str(objects.landlist))
                                                        print('인수하려는자 '+str(obj.character) + '의 인수한 후 땅 :'+str(obj.landlist))
                                                        # for lengs in range(0,len(objects.landlist)):  #그 객체들의 땅보유수만큼 돌려서 index확인
                                                        #     target=objects.landlist[lengs]
                                                        #     if (numberis==target):   #해당번째에 땅정보가 있으면
                                                        #         del objects.landlist[lengs]             #그 객체의 땅정보 제거
                                                        objects.landlist.remove(numberis)
                                                        #20210214 추가#
                                                        print(str(objects.name)+'의 땅 삭제 후 보유땅 : ' + str(objects.landlist))
                                                        print(str(obj.character)+'의 땅 추가')
                                                        # 20210214 추가#
                                                    else:   #조사한 객체가 내가 산땅에 대한 정보가 없으면 다른객체 조사
                                                        continue
                                                # 21 02 14 allDrawings 아래로내려봄#
                                                #allDrawings()
                                                # 21 02 14 allDrawings 아래로내려봄#
                                                buildingUpgrade()
                                                #21 02 14 allDrawings 아래로내려봄#
                                                allDrawings()
                                                if judge:
                                                    showingtext_y += nextLine
                                                    strwin = obj.character + ("님이 게임에서 승리하셨습니다.")
                                                    playerInfoInput(showingtext_x, showingtext_y, strwin)
                                                    iswin = True
                                                    time.sleep(2)
                                                    break

                                            else:                       #사용자가 YES를 눌렀지만 돈이 부족함.
                                                print("돈이 부족합니다. 턴종료!")
                                                str13 = "돈이 부족합니다. 턴종료!"
                                                showingtext_y += nextLine
                                                playerInfoInput(showingtext_x, showingtext_y, str13)
                                        if answer == "NO":
                                            print(dic2[obj.distance]," 지역을 인수하지 않습니다.")
                                            strno=str(dic2[obj.distance])+" 지역을 인수하지 않습니다."
                                            showingtext_y += nextLine
                                            playerInfoInput(showingtext_x, showingtext_y, strno)

                                        ### NO버튼###
                                        ### NO버튼###
                                        #인수하지 않고 턴종료

                                    else:       #통행료를 지불할 수 없다면 게임에서 제외됨
                                        print("GAME OVER!!!!!")
                                        str14 = "돈이 부족합니다. 턴종료!"
                                        showingtext_y += nextLine
                                        playerInfoInput(showingtext_x, showingtext_y, str14)
                                        print(str(obj.character)+"은(는) 게임에서 제외되었습니다.")
                                        str15 = str(obj.character)+"은(는) 게임에서 제외되었습니다."
                                        showingtext_y += nextLine
                                        playerInfoInput(showingtext_x, showingtext_y, str15)
                                        obj.playeron = 0        #게임에서 제외됨.
                                        obj.sum=0
                                        obj.lose()
                                        alive.remove(obj)

                        elif (choice == 2):  # 황금열쇠 땅에 도착한 경우
                            rand = random.randint(1, 10)
                            # keylist={1:'건물유지비',2:'로또당첨',3:'뒤로 세칸',4:'노벨상 수상',5:'경주 대회 우승',6:'장학금 수여',7:'생일 축하금'\
                            # ,8:'교통 신호 범칙금',9:'병원비',10:'세계여행'}
                            if obj.character=="선행자":
                                obj.rate+=8
                                print("신을 만날 확률이 증가합니다.")
                                strgod="신을 만날 확률이 증가합니다."
                                showingtext_y += nextLine
                                playerInfoInput(showingtext_x, showingtext_y, strgod)
                            elif obj.character == "여행자":
                                if rand >= 4:
                                    # 세계여행=TRUE
                                    print("능력발동! 우주여행 직행!")
                                    str16 = "능력발동! 우주여행 직행!"
                                    showingtext_y += nextLine
                                    playerInfoInput(showingtext_x, showingtext_y, str16)
                                    obj.distance=21     #우주여행으로 이동
                                    # continue    #다른 플레이어의 턴으로 넘김
                                else:
                                    print("능력 미발동! 다음기회에!")
                                    strnoability = "능력 미발동! 다음기회에!"
                                    showingtext_y += nextLine
                                    playerInfoInput(showingtext_x, showingtext_y, strnoability)

                            elif rand == 1:  # 1.건물유지비
                                print(keylist[1] + "를 지불합니다.")
                                str17 = str(keylist[1]) + "를 지불합니다"
                                showingtext_y += nextLine
                                playerInfoInput(showingtext_x, showingtext_y, str17)

                                price = len(obj.landlist) * 10
                                print("가격: %d" % price)
                                str18 = "가격: "+str(price) + "를 지불합니다"
                                showingtext_y += nextLine
                                playerInfoInput(showingtext_x, showingtext_y, str18)

                                if obj.sum >= price:
                                    obj.sum -= price
                                else:
                                    print("금액이 부족하여 사망하셨습니다.")
                                    strlose=obj.character+ "이(가) 금액이 부족하여 사망하셨습니다."
                                    showingtext_y += nextLine
                                    playerInfoInput(showingtext_x, showingtext_y, strlose)
                                    obj.playeron=0
                                    obj.sum = 0
                                    obj.lose()
                                    alive.remove(obj)


                            elif rand == 2:  # 2:로또당첨       #학고생이 로또당첨되면 게임승리
                                print(keylist[2])
                                print("당신은 로또에 당첨되었습니다.")
                                str19 = "당신은 로또에 당첨되었습니다."
                                showingtext_y += nextLine
                                playerInfoInput(showingtext_x, showingtext_y, str19)

                                if obj.character == "학고생":
                                    print(obj.character + "의 게임승리조건 충족!!")

                                    str20 = obj.character + "의 게임승리조건 충족!!"
                                    showingtext_y += nextLine
                                    playerInfoInput(showingtext_x, showingtext_y, str20)

                                    print("게임에서 승리하셨습니다.")
                                    str21 = str(obj.character)+" 게임에서 승리하셨습니다." #strwin!
                                    showingtext_y += nextLine
                                    playerInfoInput(showingtext_x, showingtext_y, str21)
                                    time.sleep(2)
                                    iswin=True
                                    showGameOverScreen(obj.character)
                                    #
                                    # break
                                else:       #학고생이 아니라면 20만원 로또상금수여
                                    obj.sum += 20
                            elif rand == 3:  # 3:불우이웃돕기
                                print(keylist[3])
                                price=30
                                str22=("불우 이웃을 돕습니다.")
                                showingtext_y += nextLine
                                playerInfoInput(showingtext_x, showingtext_y, str22)
                                if obj.sum >= price:    #금액 30만원만큼차감
                                    obj.sum -= price
                                else:
                                    print("금액이 부족하여 사망하셨습니다.")
                                    str23="금액이 부족하여 사망하셨습니다."
                                    showingtext_y += nextLine
                                    playerInfoInput(showingtext_x, showingtext_y, str23)
                                    obj.sum=0
                                    obj.playeron=0
                                    obj.lose()
                                    alive.remove(obj)

                            elif rand == 4:  # 노벨상수상
                                print(keylist[4])
                                obj.sum += 30
                                str24 = str(keylist[4])
                                showingtext_y += nextLine
                                playerInfoInput(showingtext_x, showingtext_y, str24)
                            elif rand == 5:  # 경주대회우승
                                str25 = str(keylist[5])
                                obj.sum+=30
                                showingtext_y += nextLine
                                playerInfoInput(showingtext_x, showingtext_y, str25)
                            elif rand == 6:  # 장학금 수여
                                str26 = str(keylist[6])
                                obj.sum += 30
                                showingtext_y += nextLine
                                playerInfoInput(showingtext_x, showingtext_y, str26)
                            elif rand == 7:  # 생일 축하금
                                str27 = str(keylist[7])
                                obj.sum += 30
                                showingtext_y += nextLine
                                playerInfoInput(showingtext_x, showingtext_y, str27)
                            elif rand == 8:  # 교통 신호 범칙금
                                print(keylist[8])
                                price=30
                                obj.sum-=price
                                str28=str(keylist[8])
                                showingtext_y += nextLine
                                playerInfoInput(showingtext_x, showingtext_y, str28)

                                str29=str(price) + "만원의 금액을 부과합니다! "
                                showingtext_y += nextLine
                                playerInfoInput(showingtext_x, showingtext_y, str29)

                                if obj.sum >= price:
                                    obj.sum -= price
                                    #금액만큼 차감
                                else:
                                    print("금액이 부족하여 사망하셨습니다.")
                                    str30 = obj.character + "이(가) 금액이 부족하여 사망하셨습니다."
                                    showingtext_y += nextLine
                                    playerInfoInput(showingtext_x, showingtext_y, str30)
                                    obj.playeron=0
                                    obj.sum=0
                                    obj.lose()
                                    alive.remove(obj)


                            elif rand == 9:  # 9:화재사고
                                price=30
                                if obj.sum >= price:
                                    obj.sum -= price
                                else:
                                    print("화재예방 구축금액이 없어 사망하셨습니다.")
                                    str31 = str(price) + "화재예방 구축금액이 없어 사망하셨습니다."
                                    strlose=obj.character+"의 GAME OVER!"
                                    showingtext_y += nextLine
                                    playerInfoInput(showingtext_x, showingtext_y, str31)

                                    strlose = obj.character + "의 GAME OVER!"
                                    showingtext_y += nextLine
                                    playerInfoInput(showingtext_x, showingtext_y, strlose)
                                    obj.playeron=0
                                    obj.sum=0
                                    obj.lose()
                                    alive.remove(obj)
                            elif rand == 10:  # 10:'
                                # 세계여행=TRUE
                                print(keylist[10])
                                print("우주여행 직행!")
                                str32 = "우주여행 직행!"
                                showingtext_y += nextLine
                                playerInfoInput(showingtext_x, showingtext_y, str32)
                                obj.distance = 21  # 우주여행으로 이동
                            else:
                                print("프로그램이 미쳤음")

                        elif (choice == 3):  # 출발지점인경우 월급만 줌
                            print("월급 획득!")
                            str33 = "월급 획득!"
                            showingtext_y += nextLine
                            playerInfoInput(showingtext_x, showingtext_y, str33)
                            obj.sum+=30
                        elif (choice == 4):  # 무인도지점
                            obj.escape+=1
                            print("다음턴부터 주사위 3회 더블이면 탈출!")
                            str34 = "다음턴부터 주사위 3회 더블이면 탈출!"
                            showingtext_y += nextLine
                            playerInfoInput(showingtext_x, showingtext_y, str34)
                        elif (choice == 5):  # 세금을 득템
                            print("누적된 세금 획득!!")
                            str37 = "누적된 세금 획득!!"
                            showingtext_y += nextLine
                            playerInfoInput(showingtext_x, showingtext_y, str37)
                            obj.sum += tax  # 현재까지 적립된 세금 획득
                            tax = 0  # 세금 0으로 초기화
                        elif (choice == -1):  # 우주여행
                            print("우주여행!")
                            print("다음 턴에 원하는 지역으로 이동합니다.")
                            str38 = "다음 턴에 원하는 지역으로 이동합니다."
                            showingtext_y += nextLine
                            playerInfoInput(showingtext_x, showingtext_y, str38)
                            obj.distance=21

                        elif (choice == -2):  # 국세청 : 돈지불(30)
                            print("세금 지불!")
                            strtax = "세금 지불!"
                            showingtext_y += nextLine
                            playerInfoInput(showingtext_x, showingtext_y, strtax)
                            price=30
                            if obj.sum >= price:
                                obj.sum -= price
                                tax+=30
                            else:
                                print("세금 미납 !  Game Over!  ")
                                showingtext_y+=nextLine
                                strgameover=obj.character+("세금 미납 !  Game Over!  ")
                                playerInfoInput(showingtext_x, showingtext_y, strgameover)
                                obj.playeron=0
                                obj.sum=0
                                obj.lose()
                                alive.remove(obj)
                        else:
                            print("컴퓨터가 미쳤음!")
                        pygame.event.get()
                        search += 1
                        if search == len(alive) or search == len(alive)+1:  # 모든 플레이어의 턴이 돌면 턴 1씩 증가
                            turnpage += 1
                            search = 0

                        judge = obj.winJudge()
                        if judge:
                            showingtext_y += nextLine
                            strwin = obj.character + ("님이 게임에서 승리하셨습니다.")
                            playerInfoInput(showingtext_x, showingtext_y, strwin)
                            iswin = True
                            strwait = "잠시 기다려주세요!"
                            showingtext_y += nextLine
                            playerInfoInput(showingtext_x, showingtext_y, strwait)
                            time.sleep(2)
                            break


            if not hasattr(events, 'key'):  # 키 관련 이벤트가 아닐 경우, 건너뛰도록 처리하는 부분
                continue

        allDrawings()

    pygame.quit()


Main()
