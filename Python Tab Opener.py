from time import sleep
from tkinter import *
from tkinter import Menu
from tkinter import ttk

#imports the required items

def windowOpener(Title):
	window = Tk()
	window.title(Title)
	window.geometry('600x600')

	#opens a window with the given title and dimensions
	
	lbl = Label(window, text='Hello,what is your name?')
	lbl.grid(column=0, row=0)
	
	txt = Entry(window, width=20)
	txt.grid(column=1, row=0)
	
	def clicked():
		Name = "Hello," + txt.get() + ". Click options to explore more."
		lbl.configure(text = Name)
	
	btn = Button(window, text = 'Click Here', command = clicked(), bg = 'yellow', fg = 'blue')
	btn.grid(column=2, row=0)
	
	#asks for your name along with button
	
	menu = Menu(window)
	
	opt = Menu(menu)
	opt.add_command(label='New Tab')
	opt.add_command(label='Open...')
	opt.add_command(label='Recent Files')
	opt.add_separator()
	opt.add_command(label='Save')
	opt.add_command(label='Save as')
	opt.add_separator()
	opt.add_command(label='Undo')
	opt.add_command(label='Redo')
	opt.add_separator()
	opt.add_command(label='Cut')
	opt.add_command(label='Copy')
	opt.add_command(label='Paste')
	opt.add_command(label='Select all')
	opt.add_separator()
	opt.add_command(label='Close')
	opt.add_command(label='Exit Window')
	opt.add_separator()
	opt.add_command(label='Help')
	
	windo.config(menu=menu)
	#opens a menu with options
	
	window.mainloop()
