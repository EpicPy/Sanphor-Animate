from curses import wrapper
from tkinter import *
from bin import patternDatabase
static=patternDatabase.static
animation=patternDatabase.animation
from time import  sleep

class Pattern:
    def __init__(self,patternData:dict,patternType:str='Static') -> None:
        self.paternType=patternType.lower()
        self.patternData=patternData
        self.animationdelay=0
    
class PatternGenration:
    def __init__(self) -> None:
        self.repeat=False
        self.pattern=None
    def representStaticCommand(self,patternData):
        data=patternData
        print()
        for columns in range(100):
            if columns in data['columns']:
                if len(data['rows'][columns])!=0:
                    for i in range(len(data['rows'][columns])):
                        if data['rows'][columns][i]==1:
                            print('*',end='')
                        elif data['rows'][columns][i]==2:
                            print('|',end='')
                        elif data['rows'][columns][i]==3:
                            print('_',end='')
                        elif data['rows'][columns][i]==4:
                            print('-',end='')
                        elif data['rows'][columns][i]==0:
                            print(' ',end='')
                    print()
    
    def representAnimatedCommand(self,stdscr):
        while True:
            stdscr.clear()
            if self.repeat==True:
                    for x in range(3):
                        stdscr.clear()
                        for i in range(self.pattern['animationCount']):
                            animation=f'animation{i+1}'
                            stdscr.clear()
                            data=self.pattern
                            for columns in range(100):
                                if columns in data[animation]['columns']:
                                    for i in range(len(data[animation]['rows'][columns])):
                                        if data[animation]['rows'][columns][i]==1:
                                            stdscr.addstr(columns,i,'*')
                                        elif data[animation]['rows'][columns][i]==2:
                                            stdscr.addstr(columns,i,'|')
                                        elif data[animation]['rows'][columns][i]==3:
                                            stdscr.addstr(columns,i,'_')
                                        elif data[animation]['rows'][columns][i]==4:
                                            stdscr.addstr(columns,i,'-')
                                        elif data[animation]['rows'][columns][i]==0:
                                            stdscr.addstr(columns,i,' ')
                            stdscr.refresh() 
                            sleep(self.animationDelay)
            else:
                for i in range(self.pattern['animationCount']):
                    animation=f'animation{i+1}'
                    stdscr.clear()
                    data=self.pattern
                    for columns in range(100):
                        if columns in data[animation]['columns']:
                            for i in range(len(data[animation]['rows'][columns])):
                                if data[animation]['rows'][columns][i]==1:
                                    stdscr.addstr(columns,i,'*')
                                elif data[animation]['rows'][columns][i]==2:
                                    stdscr.addstr(columns,i,'|')
                                elif data[animation]['rows'][columns][i]==3:
                                    stdscr.addstr(columns,i,'_')
                                elif data[animation]['rows'][columns][i]==4:
                                    stdscr.addstr(columns,i,'-')
                                elif data[animation]['rows'][columns][i]==0:
                                    stdscr.addstr(columns,i,' ')
                    stdscr.refresh() 
                    sleep(self.animationDelay)
            break
        pass
    def getPattern(self,packedDict:dict):
        if packedDict['animation']==False:
            self.representStaticCommand(static[packedDict["iterationType"]])
        elif packedDict['animation']==True:
            self.repeat=packedDict['repeat']
            self.pattern=animation[packedDict['iterationType']]
            self.animationDelay=animation[packedDict['iterationType']]['animationDelay']
            wrapper(self.representAnimatedCommand)
        
class patternGUI:
    def __init__(self,_window) -> None:
        self.windowComponents=[]
        self.window=_window
        self.pageNumber=1
        self.chooseText=''
        self.page1()

    def page1(self):
        self.dropDownVar=StringVar(self.window)
        self.dropDownVar.set('Select the pattern')
        self.dropDown=OptionMenu(self.window,self.dropDownVar,'Minion','Rocket','Scripture','Car','Test')
        self.dropDown.place(x=200,y=105)

        self.divideLableVar=StringVar(self.window,value="--------------------------------------------------------------------------------------------------------")
        self.divideLable=Label(self.window,textvariable=self.divideLableVar)
        self.divideLable.place(x=0,y=200)
        #---------------------------------------------------------------------------------------------------------------------------------------------
        self.animationVar=IntVar(self.window)
        self.animationRadio=Checkbutton(self.window,text='Animation',onvalue=1,offvalue=0,variable=self.animationVar)
        self.animationRadio.place(x=10,y=220)

        self.repeatVar=IntVar(self.window)
        self.repeatRadio=Checkbutton(self.window,text='Repeat',onvalue=1,offvalue=0,variable=self.repeatVar)
        self.repeatRadio.place(x=10,y=240)

        self.make=Button(self.window,text='Start making')
        self.make.bind('<Button-1>',self.patternMake)
        self.make.place(x=225,y=300)

    def patternMake(self,event):
       self.packComponents()

    def packComponents(self):
        #{'iterationType':'triangle','animation':True|False,'repeat':True|False}
        animation=True if self.animationVar.get()==1 else False
        repeat=True if self.repeatVar.get()==1 else False
        packedDict={'iterationType':self.dropDownVar.get(),'animation':animation,'repeat':repeat}
        patternGenrator.getPattern(packedDict)
    
    # def chooseUpdate(self,e):
    #     self.chooseText=self.chooseVariable.get()

window=Tk()
window.geometry('500x350')
window.title("Pattern Maker")
patternGenrator=PatternGenration()
patternGUI(window)

window.mainloop()
