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
class App():
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
        self.pwdEty = tk.Entry(frame)

        ### Log in button
        self.okBtn = tk.Button(frame,
                               text="Log In", fg="black", width=20,
                               command=lambda: self.printInfo(self.idEty.get(), self.pwdEty.get()))

        ### Sign up button
        self.signupBtn = tk.Button(frame,
                                   text="Sign Up", fg="black", width=20,
                                   command=lambda: self.printAlert("Sign Up"))

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

    def printAlert(self, str):
        print(str)

    def printInfo(self, id, pwd):
        print("id = ", id, ", pwd = ", pwd)

###
def printFrame():
    print("printFrame()")

    root = tk.Tk()
    app = App(root)
    root.mainloop()

###
def start():
    print("LogInFrame.py")
    printFrame()

###
start()
