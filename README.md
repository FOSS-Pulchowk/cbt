# cbt
Computer Based Test (ramailo)

Use tkinter module and enjoy!!!!

This program mainly uses tkinter( for python3.X) or Tkinter( for python2.X) and random modules. "....dat" files contains the data of questions and options. 'add_question.py' file allows  us to add contents to the existing file or create a  new file itself. 'cbt_main.py' displays the questions and options by importing the 'displays_question.py' and its functions and class.

The data conatined by "...dat" files is unreadable by the user and has to be deciphered by the cbt_main program. The cbt_main takes the name and roll no. and views a list of all available question collections. A single line contains a single question. The first option in the every line is the correct one so the options are shuffled using the random module. There is also the provision of negative marking in the program. At last the final score is displayed.

What add_question does is that it takes the name of question collection that you want to create or want to add questions into and asks to enter queries and options. The first option should always be the correct one and the option or question box can't be left empty. The question and options are appended into a single line and the lines is ciphered then added to the respective files.
