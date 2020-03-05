"""
파이썬 기초과학 프로그래밍 tkinter 프로젝트
컴퓨터공학과 20165153 이재성
"""


from tkinter import *     # tkinter 라이브러리 
import numpy as np        # numpy 라이브러리
import matplotlib.pyplot as plt   # 그래프를 그리기 위한 라이브러

class Infomation:           # 클래스 inmation 선언
    TriFunc = ""        
    
    # 입력된 변수를 클래스 변수로 저장
    def __init__(self,timeRange,gap,amplitude,hz,phase,name,age,num,gender):
        self.timeRange = timeRange
        self.gap = gap
        self.amplitude = amplitude
        self.hz = hz
        self.phase = phase
        self.name = name
        self.age = age
        self.num = num
        self.gender = gender

    @classmethod
    def setFunc(cls, fun): 
        cls.TriFunc = fun 

    @classmethod
    def getFunc(cls): 
        return cls.TriFunc 
    
    def __str__(self): 
        value = Infomation.getFunc() 
        msg = ("\n삼각함수: {}\n시간범위: {}\n시간간격: {}\n진폭: {}\n주파수: {}\n위상: {}\n이름: {}\n나이: {}\n학번: {}\n성별: {}".format(value,self.timeRange,self.gap,self.amplitude,self.hz,self.phase,self.name,self.age,self.num,self.gender))
        return msg

def select():               # 삼각함수 체크버튼에 따라 값을 다르게 저장
    if v1.get() == 1:
        Infomation.setFunc("sin") 
    elif v2.get() == 1:
        Infomation.setFunc("cos")
    elif v3.get() == 1: 
        Infomation.setFunc("tan")
        

def textPrint() :           # 입력된 정보를 텍스트에 출력
    global info
    info = Infomation(timeRange.get(),gap.get(),amplitude.get(),hz.get(),phase.get(),name.get(),age.get(),num.get(),gender.get())
    t.insert(CURRENT,info)

def fileSave():     # 파일을 저장하기 위한 fileSave 함수
    file = open("input.txt","w")
    file.write("함수체크 : ")
    if v1.get() == 1:
        file.write("sin")
    elif v2.get() == 1:
        file.write("cos")
    elif v3.get() == 1: 
        file.write("tan")
    file.write("\n시간 범위 : " + timeRange.get())
    file.write("\n시간 간격 : " + gap.get())
    file.write("\n진폭 : " + amplitude.get())
    file.write("\n주파수 : " + hz.get())
    file.write("\n위상 : " + phase.get())
    file.write("\n이름 : " + name.get())
    file.write("\n나이 : " + age.get())
    file.write("\n학번 : " + num.get())
    file.write("\n성별 : " + gender.get())
    file.close()


def fileOpen():     # 파일을 열기위한 fileOpen 함수
    newRoot = Tk()
    newRoot.title("new text")
    
    newInputLabel = Label(newRoot, text = "파일명 입력 : ")
    newInputLabel.grid(row=0, column=0)
    global newInput
    newInput = Entry(newRoot)
    newInput.grid(row=0, column=1)
    newButton = Button(newRoot,text="확인",command = resultOpen)
    newButton.grid(row = 1, column =1)
    newRoot.mainloop() 

def resultOpen() :
    newFile = open(newInput.get(),"r") 
    line = newFile.read()
    t.insert(CURRENT,line)
    newFile.close()
    

def graph() :           #  그래프를 그리는 graph, result.txt를 만들어 값을 저장하는 것은 구현하지 못함
    tf = int(timeRange.get())    # 시간 범위
    dt = float(gap.get())          # 시간 간격
    w = int(hz.get())            # 주파수
    
    x = np.arange(0,tf,dt)
    y = np.sin(w*x)
    z = np.cos(w*x)
    zz = np.tan(w*x)
    plt.figure(1)
    
    
    if v1.get() == 1:
        plt.plot(x,y,c="b", marker="o",ms=5, lw=0.3, mew=1,ls="--",label="sin")
        plt.legend(loc=2)
    elif v2.get() == 1:
        plt.plot(x,z,c="g", marker="s",ms=5, lw=0.2, mew=2,ls="-",label="cos")
        plt.legend(loc=1)
    elif v3.get() == 1: 
        plt.plot(x,zz,c="r", marker="s",ms=5, lw=0.1, mew=3,ls="-",label="tan")
        plt.legend(loc=1)
     
    plt.xlabel('time[sec]')
    plt.ylabel(r'sin($\theta$)', fontsize=20)
    plt.axis([0, 20, -2,2])
    plt.grid(True)

root = Tk() 
root.title("text") 
    
v1 = IntVar()
v2 = IntVar()
v3 = IntVar()

sinFunc = Checkbutton(root,text = "sin", variable=v1, command=select)
cosFunc = Checkbutton(root,text = "cos", variable=v2, command=select)
tanFunc = Checkbutton(root,text = "tan", variable=v3, command=select)

sinFunc.grid(row=0, column=0)
cosFunc.grid(row=0, column=1)
tanFunc.grid(row=0, column=2)

timeRangeLabel = Label(root, text="시간 범위: ") 
timeRangeLabel.grid(row=1, column=0)
timeRange = Entry(root) 
timeRange.grid(row=1, column=1) 

gapLabel = Label(root, text="시간간격")
gapLabel.grid(row=2, column = 0)
gap = Entry(root)
gap.grid(row=2, column=1)

amplitudeLabel = Label(root, text="진폭")
amplitudeLabel.grid(row=3, column = 0)
amplitude = Entry(root)
amplitude.grid(row=3, column=1)

hzLabel = Label(root, text="주파수")
hzLabel.grid(row=4, column = 0)
hz = Entry(root)
hz.grid(row=4, column=1)

phaseLabel = Label(root, text="위상")
phaseLabel.grid(row=5, column = 0)
phase = Entry(root)
phase.grid(row=5, column=1)

nameLabel = Label(root, text="이름")
nameLabel.grid(row=1, column = 2)
name = Entry(root)
name.grid(row=1, column=3)

ageLabel = Label(root, text="나이")
ageLabel.grid(row=2, column = 2)
age = Entry(root)
age.grid(row=2, column=3)

numLabel = Label(root, text="학번")
numLabel.grid(row=3, column = 2)
num = Entry(root)
num.grid(row=3, column=3)

genderLabel = Label(root, text="성별")
genderLabel.grid(row=4, column = 2)
gender = Entry(root)
gender.grid(row=4, column=3)

t = Text(root) 
t.grid(row=1, column=4, rowspan=5) 

b1 = Button(root,text="입력완료",command = textPrint)
b1.grid(row = 6, column =1)
b2 = Button(root,text="저장하기",command = fileSave)
b2.grid(row = 6, column =3)
b3 = Button(root,text="함수실행",command =graph)
b3.grid(row = 7, column =1)
b4 = Button(root,text="파일읽기",command = fileOpen)
b4.grid(row = 7, column =3)

root.mainloop() 
