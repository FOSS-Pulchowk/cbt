" This code creates a class to view all the questions line by line"\
" The list of all lines is passed into this function."\
"It uses random and tkinter modules. Two tkinter and Tkinter modules are written so it could run both in" \
"3.X and 2.X versions of python IDE.Remember, 1st option is always the correct one."

import random as rd
import time
try:
    import tkinter as tk
except:
    import Tkinter as tk

class display_question:
    "Creates a class with main window , list of lines, name of student,roll no and n is default parameter"

    def __init__(self, master, lines, name, roll, n=0):
        self.name = name
        self.roll = roll
        self.master = master
        self.n = n
        self.lines = self.decrypt_lines(lines)
        name_label = tk.Label(self.master, text="Name: "+name,
                              font=("Ariel", 15, "bold"))
        name_label.pack(anchor='w')
        roll_label = tk.Label(self.master, text="Roll No. "+roll,
                              font=("Ariel", 15, "bold"))
        roll_label.pack(anchor='w')
        self.score = 0
        self.my_ans = ""

    def decrypt_lines(self, lines):
        "This function deciphers the data in file and gives off  clear line of question and answer."
        for i in range(len(lines)):
            lines[i] = lines[i].rstrip()
            set1 = []
            for char in lines[i]:
                set1.append(chr(ord(char)-15))
            lines[i] = "".join(set1)
        return lines

    def display(self):
        "displays the question and  Radiobutton for options "

        start = time.time()
        self.frame = tk.Frame(self.master)
        self.frame.pack()

        self.lines[self.n] = self.lines[self.n]
        ans = self.lines[self.n].split("_")
        que_label = tk.Label(self.frame, text=ans[0])
        que_label.pack()

        self.correct = ans[1]
        ans = ans[1:]
        rd.shuffle(ans)                                                   # uses random function to shuffle the options
        rad_butns = {}

        for optn in ans:
            action = lambda x = optn: self.set_ans(x)                        # { lambda function is used here  so that
            rad_butns[optn] = tk.Radiobutton(self.frame, text=optn,          # the value of optn updating in every loop
                                             value=optn, variable=self.my_ans, # wont affect the command function set_ans }
                                             command=action)
            rad_butns[optn].pack(anchor='w')

        self.nxt_buttn = tk.Button(self.frame,
                                   text="Next", command=self.next)
        self.nxt_buttn.pack()



    def set_ans(self, optn):
        "sets the picked option to a variable "

        self.my_ans = optn

    def next(self):
        self.frame.destroy()                                                   # clears the frame
        self.n += 1
        self.checkpoint()                                                      # calls class function to check ans


        "Displays the final score"
    def showFinalScore(self):
        final_score = (self.score / self.n) * 100
        score_label = tk.Label(self.master,  # prints the final score
                               text="Your final score is :{0:.2f}".format(final_score))

        score_label.pack()


    def checkpoint(self):

        "checks if the picked ans is correct, if value of obtained score is -ve, and also gives -ve marking "

        if self.my_ans == self.correct:
            self.score += 1
        else:
            self.score -= 0.1
        if self.score < 0:                                                     #doesn't  let the score be negative
            self.score = 0
        if self.n == len(self.lines):                                          # checks if questions are finished
            self.showFinalScore()

        else:
            self.display()                                                     # again displays a new line of question
