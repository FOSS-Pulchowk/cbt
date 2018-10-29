"This code is run to add questions in a file or to add a  new file of question itself."\
"Two tkinter and Tkinter modules are written so it could run both in" \
"3.X and 2.X versions of python IDE.Remember, 1st option is always the correct one."



try:
    import Tkinter as tk
except:
    import tkinter as tk
try:
    import Tkinter.messagebox as msg                            # explicit function of tkinter
except:
    import tkinter.messagebox as msg

class edits_que:
    "A class to add questions and question files"
    def __init__(self, master):
        self.master = master
        self.frame1 = tk.Frame(master)
        self.frame1.pack()
        label1 = tk.Label(self.frame1,
                          text="You can add questions.",
                          font=("Ariel", 15, "bold"))
        label1.pack()
        add_btn = tk.Button(self.frame1, text="Add questions",
                            command=self.pass_file_name)
        add_btn.pack()

        self.simp_var = ["Correct Option:", "Incorrect Option #1:",
                    "Incorrect Option #2:", "Incorrect Option #3:"]
        self.que = ""

    def pass_file_name(self):
        "used to pass the name of question file to be added"

        self.frame1.destroy()

        self.frame1 = tk.Frame(self.master)
        self.frame1.pack()
        self.add_lab = tk.Label(self.frame1,
                                text="Pass the name of the question file:",
                                font=("bold"))
        self.add_lab.pack()
        self.name_entry = tk.Entry(self.frame1)                             # entry box for the name of file
        self.name_entry.pack()

        cont_btn = tk.Button(self.frame1, text="Continue-->", command=self.get_name)
        cont_btn.pack()
        back_btn1 = tk.Button(self.frame1, text="<--Back", command=self.back_to_main)
        back_btn1.pack()
        self.file = ""

    def get_name(self):
        "sets the entered name to file name variable"

        self.file_name = self.name_entry.get()
        self.add_que()

    def add_que(self):
        "Actual part to add question  and options"

        self.frame1.destroy()
        self.frame1 = tk.Frame(self.master)
        self.frame1.pack()

        self.file = open(self.file_name + ".dat", 'a')
        info_lab = tk.Label(self.frame1, text="Enter the question below to be added.",
                            font=("bold"))
        info_lab.pack(anchor="w")
        self.que_txt = tk.Entry(self.frame1, width=70)
        self.que_txt.pack()

        self.optn_entry = {}

        for j in self.simp_var:
            optn = tk.Label(self.frame1, text=j)
            optn.pack(anchor='w')
            self.optn_entry[j] = tk.Entry(self.frame1)
            self.optn_entry[j].pack(anchor='w')

        next_btn = tk.Button(self.frame1, text="Next-->", command=self.add_nxt_que)
        next_btn.pack()
        back_btn = tk.Button(self.frame1, text="<--Back", command=self.back)
        back_btn.pack()
        ext_btn = tk.Button(self.frame1, text="Exit", command=self.ext)
        ext_btn.pack()
        
    def back_to_main(self):
        self.frame1.destroy()
        self.__init__(self.master)
        
    def back(self):
        self.pass_file_name()
        
        
    def add_nxt_que(self):
        "A function to add question in loop."\
        "It also doesn't allow the empty question and options to be saved and show a warning box ."

        que = self.que_txt.get()
        if que == "" or que == " ":
            tk.messagebox.showinfo("QuestionError", " The question-box should not be empty!")
            self.add_que()
        optns = {}
        for j in self.simp_var:
            optns[j] = self.optn_entry[j].get()
            if optns[j] == "" or optns[j] == " ":
                msg.showinfo("OptionsError", " The options-box should not be empty!")
                self.add_que()
                break

        line = "_".join(optns.values())
        line = que+"_"+line+'\n'
        self.file.write(line)
        self.file.close()
        self.add_que()                                                      # calls the same function to add question

    def ext(self):
        "function to kill the program"

        self.master.destroy()

main_win = tk.Tk()
main_win.geometry("1000x700")
main_win.title("Adds question in CBT file")
main = edits_que(main_win)                                          # implementation of class
main_win.mainloop()