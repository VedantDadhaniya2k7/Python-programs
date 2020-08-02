from tkinter import *

desk = Tk()
desk.title("This is a Desktop Window")




e = Entry(desk, width = 60)
e.grid(column = 0, row = 0, columnspan = 4)


def Insert(digit):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(digit))

def clear():
    e.delete(0, END)

def add():
    first_number = e.get()
    global f_num
    global math
    math = 'addition'
    f_num = int(first_number)
    e.delete(0, END)

def sub():
    first_number = e.get()
    global f_num
    global math
    math = 'subtraction'
    f_num = int(first_number)
    e.delete(0, END)

def div():
    first_number = e.get()
    global f_num
    global math
    math = 'division'
    f_num = int(first_number)
    e.delete(0, END)

def multi():
    first_number = e.get()
    global f_num
    global math
    math = 'multiplication'
    f_num = int(first_number)
    e.delete(0, END)

def ans():
    second_number = e.get()
    e.delete(0, END)

    if math == 'subtraction':
        e.insert(0,f_num - int(second_number))
    if math == 'addition':
        e.insert(0,f_num + int(second_number))
    if math == 'multiplication':
        e.insert(0,f_num * int(second_number))
    if math == 'division':
        e.insert(0,f_num / int(second_number))



btn_clr = Button(desk, text = 'X', padx = 40, pady = 20, command = clear)
btn_div = Button(desk, text = '/', padx = 40, pady = 20, command = div)
btn_multi = Button(desk, text = 'x', padx = 40, pady = 20, command = multi)
btn_sub = Button(desk, text = '-', padx = 20, pady = 20, command = sub)

btn_1 = Button(desk, text = '1', padx = 40, pady = 20, command = lambda: Insert(1))
btn_2 = Button(desk, text = '2', padx = 40, pady = 20, command = lambda: Insert(2))
btn_3 = Button(desk, text = '3', padx = 40, pady = 20, command = lambda: Insert(3))
btn_4 = Button(desk, text = '4', padx = 40, pady = 20, command = lambda: Insert(4))
btn_5 = Button(desk, text = '5', padx = 40, pady = 20, command = lambda: Insert(5))
btn_6 = Button(desk, text = '6', padx = 40, pady = 20, command = lambda: Insert(6))
btn_7 = Button(desk, text = '7', padx = 40, pady = 20, command = lambda: Insert(7))
btn_8 = Button(desk, text = '8', padx = 40, pady = 20, command = lambda: Insert(8))
btn_9 = Button(desk, text = '9', padx = 40, pady = 20, command = lambda: Insert(9))
btn_0 = Button(desk, text = '0', padx = 145, pady = 20, command = lambda: Insert(0))

btn_add = Button(desk, text = '+', padx = 20, pady = 60, command = add)
btn_ent = Button(desk, text = '=', padx = 20, pady = 60, command = ans)




btn_clr.grid(column=0, row=1, padx = 5, pady = 5)
btn_div.grid(column=1, row=1, padx = 5, pady = 5)
btn_multi.grid(column=2, row=1, padx = 5, pady = 5)
btn_sub.grid(column=3, row=1, padx = 5, pady = 5)

btn_1.grid(column=0, row=2, padx = 5, pady = 5)
btn_2.grid(column=1, row=2, padx = 5, pady = 5)
btn_3.grid(column=2, row=2, padx = 5, pady = 5)
btn_4.grid(column=0, row=3, padx = 5, pady = 5)
btn_5.grid(column=1, row=3, padx = 5, pady = 5)
btn_6.grid(column=2, row=3, padx = 5, pady = 5)
btn_7.grid(column=0, row=4, padx = 5, pady = 5)
btn_8.grid(column=1, row=4, padx = 5, pady = 5)
btn_9.grid(column=2, row=4, padx = 5, pady = 5)
btn_0.grid(column=0, row=5, padx = 5, pady = 5, columnspan = 3)

btn_add.grid(column=3, row=2, padx = 5, pady = 5, rowspan = 2)
btn_ent.grid(column=3, row=4, padx = 5, pady = 5, rowspan = 2)





desk.mainloop
