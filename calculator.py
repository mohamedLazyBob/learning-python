"""
a simple calculator that i did to learn tkinter and graphic interfaces

"""


from tkinter import * 

# we create the main window
win = Tk()

# win.configure(background="light blue")
win.configure(background="#191b28")
win.title("lazyBob calculator")
win.geometry('350x450')

text_var = ''
entry1 = Entry(win, textvariable=text_var, width=21)
entry1.grid(row=0, columnspan=4, ipadx = 100, ipady = 8)

entry2 = Entry(win, width=21)
entry2.grid(row=1, columnspan=4, ipadx = 100, ipady = 4)

# the 1st line
button0 = Button(win, text="CE",  height=5, width=7, bg='#52c9dd')
button1 = Button(win, text="+/-", height=5, width=7, bg='#52c9dd')
button2 = Button(win, text="%",   height=5, width=7, bg='#52c9dd')
button3 = Button(win, text="/",   height=5, width=7, bg='#52c9dd')

button0.grid(row=2, column=0, padx = 5, pady=5)
button1.grid(row=2, column=1, padx = 5, pady=5)
button2.grid(row=2, column=2, padx = 5, pady=5)
button3.grid(row=2, column=3, padx = 5, pady=5)


# the 2nd line
button4 = Button(win, text=" 7 ", bd=0, height=5, width=7, bg='#1e2336', fg='white')
button5 = Button(win, text=" 8 ", bd=0, height=5, width=7, bg='#1e2336', fg='white')
button6 = Button(win, text=" 9 ", bd=0, height=5, width=7, bg='#1e2336', fg='white')
button7 = Button(win, text=" * ", bd=0, height=5, width=7, bg='#52c9dd')

button4.grid(row=3, column=0, padx = 5, pady=5)
button5.grid(row=3, column=1, padx = 5, pady=5)
button6.grid(row=3, column=2, padx = 5, pady=5)
button7.grid(row=3, column=3, padx = 5, pady=5)

# the 3rd line
button8 = Button(win, text=" 4 ", bd=0,  height=5, width=7, bg='#1e2336', fg='white')
button9 = Button(win, text=" 5 ", bd=0,  height=5, width=7, bg='#1e2336', fg='white')
button10 = Button(win, text=" 6 ", bd=0, height=5, width=7, bg='#1e2336', fg='white')
button11 = Button(win, text=" - ", bd=0, height=5, width=7, bg='#52c9dd')

button8.grid(row=4, column=0, padx = 5, pady=5)
button9.grid(row=4, column=1, padx = 5, pady=5)
button10.grid(row=4, column=2, padx = 5, pady=5)
button11.grid(row=4, column=3, padx = 5, pady=5)

# the 4th line
button12 = Button(win, text=" 1 ", bd=0, height=5, width=7, bg='#1e2336', fg='white')
button13 = Button(win, text=" 2 ", bd=0, height=5, width=7, bg='#1e2336', fg='white')
button14 = Button(win, text=" 3 ", bd=0, height=5, width=7, bg='#1e2336', fg='white')
button15 = Button(win, text=" + ", bd=0, height=12, width=7, bg='#52c9dd')

button12.grid(row=5, column=0, padx = 5, pady=3)
button13.grid(row=5, column=1, padx = 5, pady=3)
button14.grid(row=5, column=2, padx = 5, pady=3)
button15.grid(row=5, column=3, padx = 5, pady=3, rowspan=2)

# the 5th line
button16 = Button(win, text=" 0 ", bd=0, height=5, width=7, bg='#1e2336', fg='white')
button17 = Button(win, text=" . ", bd=0, height=5, width=7, bg='#1e2336', fg='white')
button18 = Button(win, text=" = ", bd=0, height=5, width=7, bg='#52c9dd')

button16.grid(row=6, column=0, padx = 5, pady=3)
button17.grid(row=6, column=1, padx = 5, pady=3)
button18.grid(row=6, column=2, padx = 5, pady=3)

win.mainloop()
