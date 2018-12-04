import os
from displays_question import display_question as dq

try :
    import tkinter as tk
except:
    import Tkinter as tk


def read_questions(que_file,que_selection, student, roll_no):
    que_selection.destroy()
    file = open(que_file+".dat", 'r')
    questions = file.readlines()                                # reads the files line by line & puts it in a list
    file.close()

    final_cbt = dq(win, questions, student, roll_no)             # uses the class display_question
    final_cbt.display()                                         # function to display questions from the class


def win2(newframe):
    student = username.get()
    roll_no = roll_entry.get()
    newframe.destroy()

    que_selection= tk.Frame(win)
    que_selection.pack()
    file_sel_lab = tk.Label(que_selection,
                            text="The list of all the questions"
                                 " available here are given below:\n",
                            font=("Ariel", 15, "bold italic"))
    file_sel_lab.pack()

    dat_file = []

    for que_file in os.listdir():                               # to find all the files in  the directory
        if que_file.endswith(".dat"):                           # to find the files ending with .dat format
            que_file = que_file.replace(".dat", "")
            dat_file.append(que_file)                           # creates a list of the questions files for cbt


    que_buttons = {}

    for i in range(len(dat_file)):
        action = lambda x= dat_file[i]: read_questions(x, que_selection, student, roll_no)
        que_buttons[i] = tk.Button(que_selection, text=dat_file[i], command=action)
        que_buttons[i].pack()


win = tk.Tk()
win.title("CBT in your own way")
win.geometry("1000x700")

newframe = tk.Frame(win)                                         # creates frame
newframe.pack()

welcome = tk.Label(newframe,
                   text= "WELCOME TO COMPUTER BASED TEST",
                   font=("Times", 20, "bold italic"))
welcome.pack()

label2 = tk.Label(newframe, text= "Enter your full name:",
                  font=("Times", 15, "bold"))
label2.pack()

username= tk.Entry(newframe)                                      # creates entry box for name of student
username.pack()

roll_label = tk.Label(newframe, text="Enter your Roll no.:",
                      font=("Times", 15, "bold"))
roll_label.pack()

roll_entry = tk.Entry(newframe)                                    # creates entry box for roll
roll_entry.pack()

Continue = tk.Button(newframe, text ="continue-->",                # creates buttons to proceed to next step
                     command=lambda: win2(newframe))
Continue.pack()

win.mainloop()
