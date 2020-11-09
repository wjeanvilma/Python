from tkinter import *
import random

root = Tk()
root.geometry('400x400')
root.resizable(0,0)
root.title('My Python project')
root.config(bg ='seashell3')


Label(root, text = 'Rock, Paper ,Scissors' , font='arial 20 bold', bg = 'seashell2').pack()
root.mainloop()