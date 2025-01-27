from tkinter import *
from random import *
x=[1,2,3,4,5,6,7,8,9]
_1='1'
_2='2'
_3='3'
_4='4'
_5='5'
_6='6'
_7='7'
_8='8'
_9='9'
c=0
class Choice:
    def __init__(self,win):
        self.b1=Button(win, text='X',activebackground="gray",activeforeground="blue",font=('Helvetica 20'),command=lambda:self.option(1))
        self.b1.place(x=50, y=100,width=100,height=100)
        self.b2=Button(win, text='O',activebackground="gray",activeforeground="blue",font=('Helvetica 20'),command=lambda:self.option(2))
        self.b2.place(x=170, y=100,width=100,height=100)
    def option(self,a):
        global c
        if(a==1):
            c='X'
            Work(window)
        else:
            c='O'
            Work(window)
class Work:
    def __init__(self, win):
        self.b1=Button(win, text='',activebackground="gray",activeforeground="blue",font=('Helvetica 20'),command=lambda:self.game(1))
        self.b1.place(x=0, y=0,width=100,height=100)
        self.b2=Button(win, text='',activebackground="gray",activeforeground="blue",font=('Helvetica 20'),command=lambda:self.game(2))
        self.b2.place(x=0, y=100,width=100,height=100)
        self.b3=Button(win, text='',activebackground="gray",activeforeground="blue",font=('Helvetica 20'),command=lambda:self.game(3))
        self.b3.place(x=0, y=200,width=100,height=100)
        self.b4=Button(win, text='',activebackground="gray",activeforeground="blue",font=('Helvetica 20'),command=lambda:self.game(4))
        self.b4.place(x=100, y=0,width=100,height=100)
        self.b5=Button(win, text='',activebackground="gray",activeforeground="blue",font=('Helvetica 20'),command=lambda:self.game(5))
        self.b5.place(x=100, y=100,width=100,height=100)
        self.b6=Button(win, text='',activebackground="gray",activeforeground="blue",font=('Helvetica 20'),command=lambda:self.game(6))
        self.b6.place(x=100, y=200,width=100,height=100)
        self.b7=Button(win, text='',activebackground="gray",activeforeground="blue",font=('Helvetica 20'),command=lambda:self.game(7))
        self.b7.place(x=200, y=0,width=100,height=100)
        self.b8=Button(win, text='',activebackground="gray",activeforeground="blue",font=('Helvetica 20'),command=lambda:self.game(8))
        self.b8.place(x=200, y=100,width=100,height=100)
        self.b9=Button(win, text='',activebackground="gray",activeforeground="blue",font=('Helvetica 20'),command=lambda:self.game(9))
        self.b9.place(x=200, y=200,width=100,height=100)
        
    def  game(self,a):
            global x,c
            x.remove(a)
            if(len(x) !=0):
                o=choice(x)
                if (c=='X'):
                    self.gamex(a)
                    self.gameo(o)
                    x.remove(o)
                else:
                    self.gamex(o)
                    self.gameo(a)
                    x.remove(o)
            else:
                if (c=='X'):
                    self.gamex(a)
                else:
                    self.gameo(a)
                    
    def gamex(self,a):
        global _1,_2,_3,_4,_5,_6,_7,_8,_9
        a=str(a)
        self.l1=Label(window, text='X',activebackground="gray",activeforeground="blue",font=('Helvetica 20'))
        if(a=='1'):
            self.l1.place(x=0, y=0,width=100,height=100)
            _1='X'
        elif(a=='2'):
            self.l1.place(x=0, y=100,width=100,height=100)
            _2='X'
        elif(a=='3'):
            self.l1.place(x=0, y=200,width=100,height=100)
            _3='X'
        elif(a=='4'):
            self.l1.place(x=100, y=0,width=100,height=100)
            _4='X'
        elif(a=='5'):
            self.l1.place(x=100, y=100,width=100,height=100)
            _5='X'
        elif(a=='6'):
            self.l1.place(x=100, y=200,width=100,height=100)
            _6='X'
        elif(a=='7'):
            self.l1.place(x=200, y=0,width=100,height=100)
            _7='X'
        elif(a=='8'):
            self.l1.place(x=200, y=100,width=100,height=100)
            _8='X'
        elif(a=='9'):
            self.l1.place(x=200, y=200,width=100,height=100)
            _9='X'
        self.con()
    def gameo(self,a):
        global _1,_2,_3,_4,_5,_6,_7,_8,_9,x
        a=str(a)
        self.l1=Label(window, text='O',activebackground="gray",activeforeground="blue",font=('Helvetica 20'))
        if(a=='1'):
            self.l1.place(x=0, y=0,width=100,height=100)
            _1='O'
        elif(a=='2'):
            self.l1.place(x=0, y=100,width=100,height=100)
            _2='O'
        elif(a=='3'):
            self.l1.place(x=0, y=200,width=100,height=100)
            _3='O'
        elif(a=='4'):
            self.l1.place(x=100, y=0,width=100,height=100)
            _4='O'
        elif(a=='5'):
            self.l1.place(x=100, y=100,width=100,height=100)
            _5='O'
        elif(a=='6'):
            self.l1.place(x=100, y=200,width=100,height=100)
            _6='O'
        elif(a=='7'):
            self.l1.place(x=200, y=0,width=100,height=100)
            _7='O'
        elif(a=='8'):
            self.l1.place(x=200, y=100,width=100,height=100)
            _8='O'
        elif(a=='9'):
            self.l1.place(x=200, y=200,width=100,height=100)
            _9='O'
        self.con()
    def con(self):
        global c
        if((_1==_2 and _2==_3)or(_4==_5 and _5==_6)or(_7==_8 and _8==_9)or(_1==_4 and _4==_7)or(_2==_5 and _5==_8)or(_3==_6 and _6==_9)or(_1==_5 and _5==_9)or(_3==_5 and _5==_7)):
            if((_1==_2 and _2==_3 and _3==c)or(_4==_5 and _5==_6 and _6==c)or(_7==_8 and _8==_9 and _9==c)or(_1==_4 and _4==_7 and _7==c)or(_2==_5 and _5==_8 and _8==c)or(_3==_6 and _6==_9 and _9==c)or(_1==_5 and _5==_9 and _9==c)or(_3==_5 and _5==_7 and _7==c)):
                self.win()
            else:
                self.loss()
        elif(len(x) ==0):
            self.draw()
                
    def win(self):
        self.p1=Label(window, text='Congratulations!!!\nYou Win :)',activebackground="gray",activeforeground="blue",font=('Helvetica 20'),justify='center')
        self.p1.place(x=0, y=0,width=300,height=300)
        
    def loss(self):
        self.p1=Label(window, text='Sorry!!!\nYou Lost :(',activebackground="gray",activeforeground="blue",font=('Helvetica 20'),justify='center')
        self.p1.place(x=0, y=0,width=300,height=300)
    def draw(self):

        self.p1=Label(window, text='Opps!!!\nIt\'s a Draw :(:',activebackground="gray",activeforeground="blue",font=('Helvetica 20'),justify='center')
        self.p1.place(x=0, y=0,width=300,height=300)


window=Tk()
frame = Frame(window, width=720, height=720, )
frame.pack()
frame.place(anchor='center',relx=0.5, rely=0.5)
mywin=Choice(window)
window.title('Tic-Tac-Toe!')
window.geometry("300x300+200+200")
window.mainloop()
