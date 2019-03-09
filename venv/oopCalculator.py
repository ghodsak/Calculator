from tkinter import*
import tkinter as tk
import math
import tkinter.messagebox



class Calculator():

    def __init__(self, window):

        self.window = window1
        self.text_input = StringVar(window)
        self.var = IntVar(window)
        self.value = ''

        window.title('Calculator')
        window.resizable(width=False, height=False)
        window.geometry("328x384+0+0")

        self.frame = Frame(window)
        self.frame.configure(bg="gray39")
        self.frame.grid(columnspan=10)

        #self.radio_btn = Radiobutton(self.frame, bg = "gray39", fg="gray39", borderwidth=-100)
        #self.radio_btn.grid(row=0, column=6)

    # ========= Entry ===========
        self.column_span = 4
        self.entry = tk.Entry(self.frame, font=("arial", 17, 'bold'),
                              bd=20, bg='black', fg='white',
                              textvariable=self.text_input, justify='right')
        self.entry.grid(row=0, column=0, columnspan=self.column_span, sticky="NEWS")
        self.entry.insert(0,'0')


    #=========== Buttons ===========
    #=========== Row1 ==============

        self.btn_allclear = Button(self.frame, text="C", bd=10, bg="gray67",
                                command=lambda:self.all_clear_btn(),fg='black',
                                font=('arial', 17, 'bold')).grid(row=1, column=0, sticky='NSEW')

        self.btn_square_root = Button(self.frame, text="√", bd=10, bg="gray67",
                                      command=lambda:self.square_root(),fg='black',
                                      font=('arial', 17, 'bold')).grid(row=1, column=1, sticky='NSEW')

        self.btn_neg = Button(self.frame, text="+", bd=10, bg="gray67",
                              command=lambda:self.negative_btn(),fg='black',
                              font=('arial', 17, 'bold',"underline")).grid(row=1, column=2, sticky='NSEW')

        self.btn_div = Button(self.frame, text="/", bd=10, bg="darkorange3",
                              command=lambda:self.click_btn('/'),fg='black',
                              font=('arial', 17, 'bold')).grid(row=1, column=3, sticky='NSEW')

    # =========== Row2 ============

        self.btn7 = Button(self.frame, text="7", bd=10, bg="gray32",
                           command=lambda:self.click_btn(7),fg='white',
                           font=('arial', 17, 'bold')).grid(row=2, column=0, sticky='NSEW')

        self.btn8 = Button(self.frame, text="8", bd=10, bg="gray32",
                           command=lambda:self.click_btn(8), fg='white',
                           font=('arial', 17, 'bold')).grid(row=2, column=1, sticky='NSEW')

        self.btn9 = Button(self.frame, text="9", bd=10, bg="gray32",
                           command=lambda:self.click_btn(9),fg='white',
                           font=('arial', 17, 'bold')).grid(row=2, column=2, sticky='NSEW')

        self.btn_plus = Button(self.frame, padx=17, text="+", bd=10, bg="darkorange3",
                               command=lambda:self.click_btn('+'), fg='black',
                               font=('arial', 17, 'bold')).grid(row=2, column=3, sticky='NSEW')

    # =========== Row3 =============

        self.btn4 = Button(self.frame, padx=17, text="4", bd=10, bg="gray32",
                           command=lambda:self.click_btn(4),fg='white',
                           font=('arial', 17, 'bold')).grid(row=3, column=0, sticky='NSEW')

        self.btn5 = Button(self.frame, padx=17, text="5", bd=10, bg="gray32",
                           command=lambda:self.click_btn(5),fg='white',
                           font=('arial', 17, 'bold')).grid(row=3, column=1, sticky='NSEW')

        self.btn6 = Button(self.frame, padx=17, text="6", bd=10, bg="gray32",
                           command=lambda:self.click_btn(6), fg='white',
                           font=('arial', 17, 'bold')).grid(row=3, column=2, sticky='NSEW')

        self.btn_sub = Button(self.frame, text="-", bd=10, bg="darkorange3",
                              command=lambda:self.click_btn('-'),fg='black',
                              font=('arial', 17, 'bold')).grid(row=3, column=3, sticky='NSEW')

    # =========== Row4 =============

        self.btn1 = Button(self.frame, text="1", bd=10, bg="gray32",
                           command=lambda:self.click_btn(1),fg='white',
                           font=('arial', 17, 'bold')).grid(row=4, column=0, sticky='NSEW')

        self.btn2 = Button(self.frame, text="2", bd=10, bg="gray32",
                           command=lambda:self.click_btn(2),fg='white',
                           font=('arial', 17, 'bold')).grid(row=4, column=1, sticky='NSEW')

        self.btn3 = Button(self.frame, text="3", bd=10, bg="gray32",
                           command=lambda:self.click_btn(3), fg='white',
                           font=('arial', 17, 'bold')).grid(row=4, column=2, sticky='NSEW')

        self.btn_mul = Button(self.frame, text="*", bd=10, bg="darkorange3",
                             command=lambda:self.click_btn("*"), fg='black',
                             font=('arial', 17, 'bold')).grid(row=4, column=3, sticky='NSEW')


    # =========== Row5 =============

        self.zero = "0"
        self.btn0 = Button(self.frame, text=self.zero.ljust(15), bd=10,
                           bg="gray32",command=lambda:self.click_btn(0), fg='white',
                           font=('arial', 17, 'bold')).grid(row=5, column=0, columnspan=2, sticky='NSEW')

        self.btn_dec = Button(self.frame, text=".", bd=10, bg="gray32",
                              command=lambda:self.click_btn('.'), fg='white',
                              font=('arial', 17, 'bold')).grid(row=5, column=2, sticky='NSEW')

        self.btn_equ = Button(self.frame, text="=", bd=10, bg="darkorange3",
                              command=lambda:self.equal_btn(),fg='black',
                              font=('arial', 17, 'bold')).grid(row=5, column=3, sticky='NSEW')


    # =========== Menu =============

        self.menubar = tk.Menu(window)

        self.file_menu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="View", menu=self.file_menu)
        self.file_menu.add_radiobutton(label="Standard", command= lambda:self.standard())
        self.file_menu.add_radiobutton(label="Scientific", command= lambda:self.scientific())
        self.file_menu.insert_separator(2)
        self.file_menu.add_command(label="Exit", command = lambda:self.exit_app())


        self.edit_menu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Copy")
        self.edit_menu.add_command(label="Cut")
        self.edit_menu.add_command(label="Paste")

        self.help_menu = tk.Menu (self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Help", menu=self.help_menu)
        self.help_menu.add_command(label="Help")

        window.config(menu=self.menubar)


    # ========== Menu Methods ============

    def exit_app(self):

        choice = tkinter.messagebox.askyesno("Calculator", "Confirm if you want o exit?")
        if choice > 0:
            window.destroy()

    def standard(self):

        window.resizable(width=False, height=False)
        window.geometry("328x384+0+0")
        self.column_span = 4
        self.entry = tk.Entry(self.frame, font=("arial", 17, 'bold'),
                              bd=20, bg='black', fg='white',
                              textvariable=self.text_input, justify='right')
        self.entry.grid(row=0, column=0, columnspan=self.column_span, sticky="NEWS")


    def scientific(self):

        window.resizable(width=False, height=False)
        window.geometry("820x384+0+0")
        self.column_span = 6
        self.entry = tk.Entry(self.frame, font=("arial", 17, 'bold'),
                              bd=20, bg='black', fg='white',
                              textvariable=self.text_input, justify='right')
        self.entry.grid(row=0, column=0, columnspan=self.column_span, sticky="NEWS")

    # =========== Buttons ===========
    # =========== Row1 ==============

        self.btn_pi = Button(self.frame, text="π", bd=10, bg="gray19",
                             command=lambda: self.clear_btn(), fg='white', width=4,
                             font=('arial', 17, 'bold')).grid(row=1, column=4, sticky='NSEW')

        self.btn_e = Button(self.frame, text="e", bd=10, bg="gray19",
                            command=lambda: self.clear_btn(), fg='white', width=4,
                            font=('arial', 17, 'bold')).grid(row=1, column=5, sticky='NSEW')

        self.btn_log = Button(self.frame, text="log", bd=10, bg="gray19",
                            command=lambda: self.clear_btn(), fg='white', width=4,
                            font=('arial', 17, 'bold')).grid(row=1, column=6, sticky='NSEW')

        self.btn_x = Button(self.frame, text="", bd=10, bg="gray19",
                            command=lambda: self.clear_btn(), fg='white', width=4,
                            font=('arial', 17, 'bold')).grid(row=1, column=7, sticky='NSEW')

        self.btn_pi = Button(self.frame, text="", bd=10, bg="gray19",
                             command=lambda: self.clear_btn(), fg='white', width=4,
                             font=('arial', 17, 'bold')).grid(row=1, column=8, sticky='NSEW')

        self.btn_pi = Button(self.frame, text="", bd=10, bg="gray19",
                             command=lambda: self.clear_btn(), fg='white', width=4,
                             font=('arial', 17, 'bold')).grid(row=1, column=9, sticky='NSEW')

        self.btn_pi = Button(self.frame, text="", bd=10, bg="gray19",
                             command=lambda: self.clear_btn(), fg='white', width=4,
                             font=('arial', 17, 'bold')).grid(row=2, column=4, sticky='NSEW')

        self.btn_e = Button(self.frame, text="", bd=10, bg="gray19",
                            command=lambda: self.clear_btn(), fg='white', width=4,
                            font=('arial', 17, 'bold')).grid(row=2, column=5, sticky='NSEW')

        self.btn_x = Button(self.frame, text="", bd=10, bg="gray19",
                            command=lambda: self.clear_btn(), fg='white', width=4,
                            font=('arial', 17, 'bold')).grid(row=2, column=6, sticky='NSEW')

        self.btn_x = Button(self.frame, text="", bd=10, bg="gray19",
                            command=lambda: self.clear_btn(), fg='white', width=4,
                            font=('arial', 17, 'bold')).grid(row=2, column=7, sticky='NSEW')

        self.btn_pi = Button(self.frame, text="", bd=10, bg="gray19",
                             command=lambda: self.clear_btn(), fg='white', width=4,
                             font=('arial', 17, 'bold')).grid(row=2, column=8, sticky='NSEW')

        self.btn_pi = Button(self.frame, text="", bd=10, bg="gray19",
                             command=lambda: self.clear_btn(), fg='white', width=4,
                             font=('arial', 17, 'bold')).grid(row=2, column=9, sticky='NSEW')

        self.btn_pi = Button(self.frame, text="", bd=10, bg="gray19",
                             command=lambda: self.clear_btn(), fg='white', width=4,
                             font=('arial', 17, 'bold')).grid(row=3, column=4, sticky='NSEW')

        self.btn_e = Button(self.frame, text="", bd=10, bg="gray19",
                            command=lambda: self.clear_btn(), fg='white', width=4,
                            font=('arial', 17, 'bold')).grid(row=3, column=5, sticky='NSEW')

        self.btn_x = Button(self.frame, text="", bd=10, bg="gray19",
                            command=lambda: self.clear_btn(), fg='white', width=4,
                            font=('arial', 17, 'bold')).grid(row=3, column=6, sticky='NSEW')

        self.btn_x = Button(self.frame, text="", bd=10, bg="gray19",
                            command=lambda: self.clear_btn(), fg='white', width=4,
                            font=('arial', 17, 'bold')).grid(row=3, column=7, sticky='NSEW')

        self.btn_pi = Button(self.frame, text="", bd=10, bg="gray19",
                             command=lambda: self.clear_btn(), fg='white', width=4,
                             font=('arial', 17, 'bold')).grid(row=3, column=8, sticky='NSEW')

        self.btn_pi = Button(self.frame, text="", bd=10, bg="gray19",
                             command=lambda: self.clear_btn(), fg='white', width=4,
                             font=('arial', 17, 'bold')).grid(row=3, column=9, sticky='NSEW')

        self.btn_pi = Button(self.frame, text="", bd=10, bg="gray19",
                             command=lambda: self.clear_btn(), fg='white', width=4,
                             font=('arial', 17, 'bold')).grid(row=4, column=4, sticky='NSEW')

        self.btn_e = Button(self.frame, text="", bd=10, bg="gray19",
                            command=lambda: self.clear_btn(), fg='white', width=4,
                            font=('arial', 17, 'bold')).grid(row=4, column=5, sticky='NSEW')

        self.btn_x = Button(self.frame, text="", bd=10, bg="gray19",
                            command=lambda: self.clear_btn(), fg='white', width=4,
                            font=('arial', 17, 'bold')).grid(row=4, column=6, sticky='NSEW')

        self.btn_x = Button(self.frame, text="", bd=10, bg="gray19",
                            command=lambda: self.clear_btn(), fg='white', width=4,
                            font=('arial', 17, 'bold')).grid(row=4, column=7, sticky='NSEW')

        self.btn_pi = Button(self.frame, text="", bd=10, bg="gray19",
                             command=lambda: self.clear_btn(), fg='white', width=4,
                             font=('arial', 17, 'bold')).grid(row=4, column=8, sticky='NSEW')

        self.btn_pi = Button(self.frame, text="", bd=10, bg="gray19",
                             command=lambda: self.clear_btn(), fg='white', width=4,
                             font=('arial', 17, 'bold')).grid(row=4, column=9, sticky='NSEW')

        self.btn_pi = Button(self.frame, text="", bd=10, bg="gray19",
                             command=lambda: self.clear_btn(), fg='white', width=4,
                             font=('arial', 17, 'bold')).grid(row=5, column=4, sticky='NSEW')

        self.btn_e = Button(self.frame, text="", bd=10, bg="gray19",
                            command=lambda: self.clear_btn(), fg='white', width=4,
                            font=('arial', 17, 'bold')).grid(row=5, column=5, sticky='NSEW')

        self.btn_x = Button(self.frame, text="", bd=10, bg="gray19",
                            command=lambda: self.clear_btn(), fg='white', width=4,
                            font=('arial', 17, 'bold')).grid(row=5, column=6, sticky='NSEW')

        self.btn_x = Button(self.frame, text="", bd=10, bg="gray19",
                            command=lambda: self.clear_btn(), fg='white', width=4,
                            font=('arial', 17, 'bold')).grid(row=5, column=7, sticky='NSEW')

        self.btn_pi = Button(self.frame, text="", bd=10, bg="gray19",
                             command=lambda: self.clear_btn(), fg='white', width=4,
                             font=('arial', 17, 'bold')).grid(row=5, column=8, sticky='NSEW')

        self.btn_pi = Button(self.frame, text="", bd=10, bg="gray19",
                             command=lambda: self.clear_btn(), fg='white', width=4,
                             font=('arial', 17, 'bold')).grid(row=5, column=9, sticky='NSEW')

# ============ Button Methods ==========

    def center(self):

        self.height = window.winfo_reqheight()
        self.width = window.winfo_reqwidth()

        self.screen_width = window.winfo_screenwidth()
        self.screen_height = window.winfo_screenheight()

        self.x = (self.screen_width/2) - (self.width/2)
        self.y = (self.screen_height/2) - (self.height/2)

        print(f"calculator height: {self.height}\n"
              f"calculator width: {self.width}\n ")
        print(f"({self.x}, {self.y})")

        window.geometry('%dx%d+%d+%d' % (self.width, self.height, self.x, self.y))


    def click_btn(self,user_click):

        self.value += str(user_click)
        self.text_input.set(self.value)
        self.current_value = self.text_input.get()

        self.entry.delete(0, 'end')
        self.entry.insert(0, self.current_value)
        print(self.current_value)


    def all_clear_btn(self):

        self.value = ''
        self.text_input.set('0')


    def equal_btn(self):

        self.equal = str(eval(self.value))
        self.text_input.set(self.equal)
        self.current_value = self.text_input.get()
        self.value = self.current_value
        self.text_input.set(self.current_value)

        print(self.current_value)
        print(type(self.current_value))


    def negative_btn(self):

        self.negative_num = eval((self.text_input.get() + '*(-1)'))
        self.value = str(self.negative_num)
        self.text_input.set(self.value)
        print(self.value)


    def square_root(self):

        self.current_value = self.text_input.get()
        self.current_value = math.sqrt(int(self.current_value))
        self.text_input.set(self.current_value)



window = Tk()
calc = Calculator(window)
window.update()
calc.center()
window.mainloop()