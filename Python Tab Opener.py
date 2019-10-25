from time import sleep
from tkinter import *
#imports the required items

def TabOpener(Title,name,x_axis,y_axis):
	tab = Tk()
	tab.title(Title)
	tab.geometry('600x600')
	#opens a tab with the given title and dimensions
	
	lbl = Label(tab, text='Hello,what is your name?')
	lbl.grid(column=0, row=0)
	
	txt = Entry(tab, width=20)
	txt.grid(column=1, row=0)
	
	def clicked():
		
	#asks for your name along with button
