###
#   File name : LogInFrame.py
#   Author    : Hyunjin Kim
#   Date      : Jan 5, 2019
#   Email     : firadazer@gmail.com
#   Purpose   : Make a log in frame for the game
#
#   Instruction
#               1. import LogInFrame
#               2. Run the function LogInFrame.start() - specify the inputs
#               3. The results will be generated in the outputPath
###

### import modules
import tkinter as tk

### a class for Log In frame
class LogInApp():
    def __init__(self, master):
        frame = tk.Frame(master)
        frame.pack()

        ### set title of the frame
        master.title("Log In")

        ### ID
        self.idLbl = tk.Label(frame, text="ID:")
        self.idEty = tk.Entry(frame)

        ### Password
        self.pwdLbl = tk.Label(frame, text="Password:")
        self.pwdEty = tk.Entry(frame, show='*')

        ### Log in button
        self.okBtn = tk.Button(frame,
                               text="Log In", fg="black", width=20,
                               command=lambda: self.printInfo(self.idEty.get(), self.pwdEty.get()))

        ### Sign up button
        self.signupBtn = tk.Button(frame,
                                   text="Sign Up", fg="black", width=20,
                                   command=lambda: self.signUp())

        ### Quit button
        self.qBtn = tk.Button(frame,
                              text="Quit", fg="black", width=20,
                              command=frame.quit)

        ### set grid of all the components of the frame
        self.idLbl.grid(row=0, column=0)
        self.idEty.grid(row=0, column=1)
        self.pwdLbl.grid(row=1, column=0)
        self.pwdEty.grid(row=1, column=1)
        self.okBtn.grid(row=2, column=0)
        self.signupBtn.grid(row=2, column=1)
        self.qBtn.grid(row=2, column=2)

    def printInfo(self, id, pwd):
        print("id = ", id, ", pwd = ", pwd)

    def signUp(self):
        suFrm = tk.Toplevel()
        SignUpApp(suFrm)
        center(suFrm)

### a class for Sign Up frame
class SignUpApp():
    def __init__(self, master):
        frame = tk.Frame(master)
        frame.pack()

        ### set title of the frame
        master.title("Sign Up")

        ### Name
        self.nameLbl = tk.Label(frame, text="Full Name:")
        self.nameEty = tk.Entry(frame)

        ### Contact
        self.contactLbl = tk.Label(frame, text="E-mail:")
        self.contactEty = tk.Entry(frame)

        ### ID
        self.idLbl = tk.Label(frame, text="ID:")
        self.idEty = tk.Entry(frame)

        ### Password
        self.pwdLbl = tk.Label(frame, text="Password:")
        self.pwdEty = tk.Entry(frame, show='*')

        ### Password confirm
        self.pwdLbl2 = tk.Label(frame, text="Confirm Password:")
        self.pwdEty2 = tk.Entry(frame, show='*')

        ### Sign up button
        self.signupBtn = tk.Button(frame,
                                   text="Sign Up", fg="black", width=20,
                                   command=lambda: self.printAlert("Sign Up"))

        ### Quit button
        self.qBtn = tk.Button(frame,
                              text="Quit", fg="black", width=20,
                              command=frame.master.destroy)

        ### set grid of all the components of the frame
        self.nameLbl.grid(row=0, column=0)
        self.nameEty.grid(row=0, column=1)
        self.contactLbl.grid(row=1, column=0)
        self.contactEty.grid(row=1, column=1)
        self.idLbl.grid(row=2, column=0)
        self.idEty.grid(row=2, column=1)
        self.pwdLbl.grid(row=3, column=0)
        self.pwdEty.grid(row=3, column=1)
        self.pwdLbl2.grid(row=4, column=0)
        self.pwdEty2.grid(row=4, column=1)
        self.signupBtn.grid(row=5, column=0)
        self.qBtn.grid(row=5, column=1)

    def printAlert(self, str):
        print(str)

### a function to make a tkinter frame centered
"""
:param win: the root or top level window to be centered
"""
def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()

###  proceed the root frame
def printFrame():
    print("printFrame()")

    rootFrm = tk.Tk()
    LogInApp(rootFrm)
    center(rootFrm)
    rootFrm.mainloop()

###
def start():
    print("LogInFrame.py")
    printFrame()

###
start()
