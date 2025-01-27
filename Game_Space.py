from tkinter import *
import subprocess
class Work:
    def __init__(self, win):
        self.b1=Button(win, text='Snake Game',activebackground="gray",activeforeground="blue",font=('Helvetica 20'),command=lambda:self.game(1))
        self.b1.place(x=50, y=250,width=225,height=100)
        self.b2=Button(win, text='Flappy Bird',activebackground="gray",activeforeground="blue",font=('Helvetica 20'),command=lambda:self.game(2))
        self.b2.place(x=325, y=250,width=225,height=100)
        self.b3=Button(win, text='Word Puzzle',activebackground="gray",activeforeground="blue",font=('Helvetica 20'),command=lambda:self.game(3))
        self.b3.place(x=50, y=450,width=225,height=100)
        self.b4=Button(win, text='Tic-Tac-Toe',activebackground="gray",activeforeground="blue",font=('Helvetica 20'),command=lambda:self.game(4))
        self.b4.place(x=325, y=450,width=225,height=100)
        self.p1=Label(window, text='Welcome to Game Space !',activebackground="gray",activeforeground="blue",font=('Helvetica 20'),justify='center')
        self.p1.place(x=50, y=50,width=500,height=100)
    def game(self,a):
        i=a
        if i==1:
                subprocess.run(["python", "Z:\Game_space\snake.py"], shell=True)
        elif i==3:
                subprocess.run(["python", "Z:\Game_space\word_puzzle.py"], shell=True)
        elif i==2 :
                subprocess.call(["python", 'Z:\Game_space\Flappy.py'])
        elif i==4 :
                subprocess.run(["python", 'Z:\Game_space\Tic-Tac-Toe_TKINTER.py'],shell=True)

            




                
window=Tk()
frame = Frame(window, width=720, height=720, )
frame.pack()
frame.place(anchor='center',relx=0.5, rely=0.5)
mywin=Work(window)
window.title('Game Space!')
window.geometry("600x600+200+200")
window.mainloop()

