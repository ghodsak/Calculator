from tkinter import*
import tkinter as tk


window = tk.Tk()1
window.title("Calculator")
window.configure(bg="darkgray")

user_click = ''
text_input = StringVar()
text_input.set('0')

E = Entry(window,font=('arial',18,'bold'),
                textvariable=text_input,bd=20,
                bg='darkorange2',justify='right')

E.grid(row=0,columnspan=4,sticky='NSEW')


def center():

    height  = window.winfo_reqheight()
    width = window.winfo_reqwidth()

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width/2)-(width/2)
    y = (screen_height/2)-(height/2)

    window.geometry('%dx%d+%d+%d'%(width,height,x,y))


def click_btn(Input):

    global user_click
    user_click = user_click + str(Input)
    text_input.set(user_click)


def clear_btn():

    global user_click
    user_click = ''
    text_input.set('0')


def equal_btn():

    global user_click
    equal = str(eval(user_click))
    text_input.set(equal)
    window.update()


#===========Row2=============

btn_clear = Button(window,text="C",bd=10,bg="darkorange2",command=lambda: clear_btn(),
              fg='black',font=('arial',17,'bold')).grid(row=1,columnspan=2,sticky='NSEW')

btn_mul= Button(window,text="*",bd=10,bg="gray",command=lambda: click_btn('*'),
              fg='black',font=('arial',17,'bold')).grid(row=1,column=2,sticky='NSEW')

btn_div = Button(window,text="/",bd=10,bg="gray",command=lambda: click_btn('/'),
              fg='black',font=('arial',17,'bold')).grid(row=1,column=3,sticky='NSEW')

#===========Row2=============

btn7 = Button(window,text="7",bd=10,bg="darkorange2",command=lambda: click_btn(7),
              fg='black',font=('arial',17,'bold')).grid(row=2,column=0,sticky='NSEW')

btn8 = Button(window,text="8",bd=10,bg="darkorange2",command=lambda: click_btn(8),
              fg='black',font=('arial',17,'bold')).grid(row=2,column=1,sticky='NSEW')

btn9 = Button(window,text="9",bd=10,bg= "darkorange2",command=lambda: click_btn(9),
              fg='black',font=('arial',17,'bold')).grid(row=2,column=2,sticky='NSEW')

btn_plus = Button(window,padx=17,text="+",bd=10,bg="gray",command=lambda: click_btn('+'),
              fg='black',font=('arial',17,'bold')).grid(row=2,column=3,sticky='NSEW')

#===========Row3=============

btn4 = Button(window,padx=17,text="4",bd=10,bg="darkorange2",command=lambda: click_btn(4),
              fg='black',font=('arial',17,'bold')).grid(row=3,column=0,sticky='W')

btn5 = Button(window,padx=17,text="5",bd=10,bg="darkorange2",command=lambda: click_btn(5),
              fg='black',font=('arial',17,'bold')).grid(row=3,column=1,sticky='W')

btn6 = Button(window,padx=17,text="6",bd=10,bg="darkorange2",command=lambda: click_btn(6),
              fg='black',font=('arial',17,'bold')).grid(row=3,column=2,sticky='W')

btn_sub = Button(window,text="-",bd=10,bg="gray",command=lambda: click_btn('-'),
              fg='black',font=('arial',17,'bold')).grid(row=3,column=3,sticky='NSEW')

#===========Row4=============

btn1 = Button(window,text="1",bd=10,bg="darkorange2",command=lambda: click_btn(1),
              fg='black',font=('arial',17,'bold')).grid(row=4,column=0,sticky='NSEW')

btn2 = Button(window,text="2",bd=10,bg="darkorange2",command=lambda: click_btn(2),
              fg='black',font=('arial',17,'bold')).grid(row=4,column=1,sticky='NSEW')

btn3 = Button(window,text="3",bd=10,bg="darkorange2",command=lambda: click_btn(3),
              fg='black',font=('arial',17,'bold')).grid(row=4,column=2,sticky='NSEW')

#===========Row5=============

btn_neg = Button(window,text="-/+",bd=10,bg="darkorange2",
              fg='black',font=('arial',17,'bold')).grid(row=5,column=0,sticky='NSEW')

btn0 = Button(window,text="0",bd=10,bg="darkorange2",command=lambda: click_btn(0),
              fg='black',font=('arial',17,'bold')).grid(row=5,column=1,sticky='NSEW')

btn_dec = Button(window,text=".",bd=10,bg="darkorange2",command=lambda: click_btn('.'),
              fg='black',font=('arial',17,'bold')).grid(row=5,column=2,sticky='NSEW')

btn_equ = Button(window,text="=",bd=10,bg="darkorange2",command=lambda: equal_btn(),
              fg='black',font=('arial',17,'bold')).grid(rowspan=2,row=4,column=3,sticky='NSEW')


menubar = Menu(window)
file = Menu(menubar, tearoff= 0)
file.add_command(label="New")
menubar.add_cascade(label="File")
window.config(menu=menubar)


window.resizable(False,False)
window.update()

center()
window.mainloop()



#window.resizable(False,False)