from tkinter import *
from tkinter import Menu
from tkinter import ttk

class PyTabOpener :
    def Open_Page( Name, height = 400, width = 600) :

        window = Tk()
        
        window.title(Name)
        window.geometry( height, width)
        
        tab_control = ttk.Notebook(window)
        tab1 = ttk.Frame(tab_control)
        
        lbl1 = Label(tab1, text= 'New Tab')
        lbl1.grid(column=0, row=0)
        
        
        window.mainloop()

    def RenamePage(NewName):
        window.title(NewName)

    def SetMenu(MenuName ,*Functions):
        menu = Menu(menu, tearoff=0)
        new_item = Menu(menu)
        
        for x in Functions:
            new_item.add_command(label=x)

        menu.add_cascade(label=MenuName, menu=new_item)
        window.config(menu = menu)

    def Default(Title):
	window = Tk()
	window.title(Title)
	window.geometry('600x600')

	#opens a window with the given title and dimensions
	
	txt = Entry(window, width=70)
	txt.grid(column=0, row=1)
	
	Button(window, text = 'Search', bg = 'yellow', fg = 'blue')
	btn.grid(column=1, row=1)
	
	#opens a search box
	
	menu = Menu(menu, tearoff=0)
        new_item = Menu(menu)

	def clicked :
                Tab = ttk.Frame(tab_control)
                
                lbl2 = Label(Tab, text= 'New Tab')
                lbl2.grid(column=0, row=0)
	new_item.add_command(label='New Tab',command = clicked)
        def OpEmptyWin():
            window2 = Tk()
            window2.title("Empty Window")
            window2.geometry('600x600')
	new_item.add_command(label='Open Empty Window', command = OpEmptyWin)
	
	new_item.add_separator()

	def Exit():
            window.destroy()
	new_item.add_command(label='Exit Window', command = Exit )
	
	new_item.add_separator()

	def Help():
            help1 = Tk()
            help1.title("Empty Window")
            help1.geometry('600x600')

            lbl = Label(window, text="To work on a Normal Window, use the following steps :")
            lbl.grid(column=0, row=1)
            
            lbl = Label(window, text="  - To see what you all can do, click the Options Menu")
            lbl.grid(column=0, row=2)
            
            lbl = Label(window, text="  - To conduct search, type what you want to search in the textbox and then press the search button")
            lbl.grid(column=0, row=3)
            
            lbl = Label(window, text="  - To minimize / maximize or close the tabsee the options on the top right corner of the Window")
            lbl.grid(column=0, row=1)
	new_item.add_command(label='Help', command = Help)
	
	new_item.add_cascade(label='Options' , menu = new_item)
	window.config(menu=menu)
	#opens a menu with options
	
	window.mainloop()
