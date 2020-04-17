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
	
	txt = Entry(window, width=70)
	txt.grid(column=0, row=1)
	
	Button(window, text = 'Search', bg = 'yellow', fg = 'blue')
	btn.grid(column=1, row=1)
	
	#opens a search box
	
	menu = Menu(window)
	
	options = Menu(menu)
	
	options.add_command(label='New Tab')
	options.add_command(label='Open...')
	options.add_command(label='Recent Files')
	
	options.add_separator()
	
	options.add_command(label='Save')
	options.add_command(label='Save as')
	
	options.add_separator()
	
	options.add_command(label='Undo')
	options.add_command(label='Redo')
	
	options.add_separator()
	
	options.add_command(label='Cut')
	options.add_command(label='Copy')
	options.add_command(label='Paste')
	options.add_command(label='Select all')
	
	options.add_separator()
	
	options.add_command(label='Close')
	options.add_command(label='Exit Window')
	
	options.add_separator()
	
	options.add_command(label='Help')
	
	options.add_cascade(label='Options' , menu = options)
	window.config(menu=menu)
	#opens a menu with options
	
	window.mainloop()
