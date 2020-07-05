"""
a simple calculator that i did to learn tkinter and graphic interfaces

"""


from tkinter import * 
from tkinter.ttk import Separator, Style

# we create the main window
win = Tk()

# win.configure(background="light blue")
win.configure(background="#191b28")
win.title("lazyBob calculator")
win.geometry('350x475')
win.resizable(0, 0)

expression= ''

def button_clicked(var):
    print("{} got clicked!".format(var))
    global expression 
    expression += str(var)
    entr1.set(expression)
    
def clear_entry():
    global expression
    expression = ''
    entr1.set('')
    entr2.set('')

def print_result():
    print("test test")

entr1 = StringVar()
entry1 = Entry(win, textvariable=entr1, width=21, bg='#191b28', borderwidth=0, highlightthickness=0)
entry1.grid(row=0, columnspan=4, ipadx = 100, ipady = 15)

sep = Separator(win, orient="horizontal")
sep.grid(row=1, sticky="we", columnspan=150)

entr2 = StringVar()
entry2 = Entry(win, textvariable=entr2, width=21, bg='#191b28', bd=0, highlightthickness=0)
entry2.grid(row=2, columnspan=4, ipadx = 100, ipady = 10)

# the 1st line
button0 = Button(win, text="CE",  height=2, width=3, bg='#52c9dd', font='Leaner 20 bold', command = clear_entry)
button1 = Button(win, text="+/-", height=2, width=3, bg='#52c9dd', font='Leaner 20 bold')
button2 = Button(win, text="%",   height=2, width=3, bg='#52c9dd', font='Leaner 20 bold', command = lambda: button_clicked("%"))
button3 = Button(win, text="/",   height=2, width=3, bg='#52c9dd', font='Leaner 20 bold', command = lambda: button_clicked("/"))

button0.grid(row=3, column=0, padx = 5, pady=5)
button1.grid(row=3, column=1, padx = 5, pady=5)
button2.grid(row=3, column=2, padx = 5, pady=5)
button3.grid(row=3, column=3, padx = 5, pady=5)


# the 2nd line
# button4 = Button(win, text=" 7 ", bd=0, height=5, width=7, bg='#1e2336', fg='white', font='Arial 20 bold')
button4 = Button(win, text=" 7 ", bd=0, height=2, width=3, bg='#1e2336', fg='white', font='Leaner 20 bold', command=lambda: button_clicked("7"))
button5 = Button(win, text=" 8 ", bd=0, height=2, width=3, bg='#1e2336', fg='white', font='Leaner 20 bold', command=lambda: button_clicked("8"))
button6 = Button(win, text=" 9 ", bd=0, height=2, width=3, bg='#1e2336', fg='white', font='Leaner 20 bold', command=lambda: button_clicked("9"))
button7 = Button(win, text=" * ", bd=0, height=2, width=3, bg='#52c9dd', font='Leaner 20 ', command=lambda: button_clicked("*"))

button4.grid(row=4, column=0, padx = 5, pady=5)
button5.grid(row=4, column=1, padx = 5, pady=5)
button6.grid(row=4, column=2, padx = 5, pady=5)
button7.grid(row=4, column=3, padx = 5, pady=5)

# the 3rd line
button8 = Button(win, text="4", bd=0,  height=2, width=3, bg='#1e2336', fg='white', font='Leaner 20 bold', command = lambda: button_clicked("4"))
button9 = Button(win, text="5", bd=0,  height=2, width=3, bg='#1e2336', fg='white', font='Leaner 20 bold', command = lambda: button_clicked("5"))
button10 = Button(win, text="6", bd=0, height=2, width=3, bg='#1e2336', fg='white', font='Leaner 20 bold', command = lambda: button_clicked("6"))
button11 = Button(win, text="-", bd=0, height=2, width=3, bg='#52c9dd', font='Leaner 20 bold', command = lambda: button_clicked("-"))

button8.grid(row=5, column=0, padx = 5, pady=5)
button9.grid(row=5, column=1, padx = 5, pady=5)
button10.grid(row=5, column=2, padx = 5, pady=5)
button11.grid(row=5, column=3, padx = 5, pady=5)

# the 4th line
button12 = Button(win, text="1", bd=0, height=2, width=3, bg='#1e2336', fg='white', font='Leaner 20 bold', command = lambda: button_clicked("1"))
button13 = Button(win, text="2", bd=0, height=2, width=3, bg='#1e2336', fg='white', font='Leaner 20 bold', command = lambda: button_clicked("2"))
button14 = Button(win, text="3", bd=0, height=2, width=3, bg='#1e2336', fg='white', font='Leaner 20 bold', command = lambda: button_clicked("3"))
button15 = Button(win, text="+", bd=0, height=5, width=3, bg='#52c9dd', font='Leaner 20 bold', command = lambda: button_clicked("+"))

button12.grid(row=6, column=0, padx = 5, pady=3)
button13.grid(row=6, column=1, padx = 5, pady=3)
button14.grid(row=6, column=2, padx = 5, pady=3)
button15.grid(row=6, column=3, padx = 5, pady=3, rowspan=2)

# the 5th line
button16 = Button(win, text="0", bd=0, height=2, width=3, bg='#1e2336', fg='white', font='Leaner 20 bold', command = lambda: button_clicked("0"))
button17 = Button(win, text=".", bd=0, height=2, width=3, bg='#1e2336', fg='white', font='Leaner 20 bold', command = lambda: button_clicked("."))
button18 = Button(win, text="=", bd=0, height=2, width=3, bg='#52c9dd', font='Leaner 20 bold', command = print_result)

button16.grid(row=7, column=0, padx = 5, pady=3)
button17.grid(row=7, column=1, padx = 5, pady=3)
button18.grid(row=7, column=2, padx = 5, pady=3)


win.mainloop()
