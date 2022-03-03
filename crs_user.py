from tkinter import *
import pandas as pd
import os
import smtplib
from email.message import EmailMessage
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import messagebox as mb
import re
from PIL import ImageTk, Image
import os 
os.system('python3 crs_server.py')

def main():

    def brs():

        # import json to use json file for data
        import json

        def sem3():
            def java():
                def knowjava():
                    pass

                def examjava():
                    pass

                rootc = Tk()
                Label(rootc, text="Are you studying for exam or Knowledge?").pack()
                Button(rootc, text="Knowldege", command=lambda: [
                       rootc.destroy(), knowjava()]).pack()
                Button(rootc, text="Exam", command=lambda: [
                       rootc.destroy(), examjava()]).pack()
                rootc.mainloop()

            roota = Tk()
            roota.geometry("500x500+0+0")
            Label(roota, text="Choose your sem").pack()
            Button(roota, text="Java", command=java).pack()
            Button(roota, text="DBMS").pack()
            roota.mainloop()

        def sem4():
            def python():
                def knowpython():
                    def pythonbasics():
                        # Python program to create a simple GUI
                        # Simple Quiz using Tkinter
                        # import everything from tkinter

                        # class to define the components of the GUI
                        class Quiz:
                            # This is the first method which is called when a
                            # new object of the class is initialized. This method
                            # sets the question count to 0. and initialize all the
                            # other methoods to display the content and make all the
                            # functionalities available
                            def __init__(self):

                                # set question number to 0
                                self.q_no = 0

                                # assigns ques to the display_question function to update later.
                                self.display_title()
                                self.display_question()

                                # opt_selected holds an integer value which is used for
                                # selected option in a question.
                                self.opt_selected = IntVar()

                                # displaying radio button for the current question and used to
                                # display options for the current question
                                self.opts = self.radio_buttons()

                                # display options for the current question
                                self.display_options()

                                # displays the button for next and exit.
                                self.buttons()

                                # no of questions
                                self.data_size = len(question)

                                # keep a counter of correct answers
                                self.correct = 0

                            # This method is used to display the result
                            # It counts the number of correct and wrong answers
                            # and then display them at the end as a message Box
                            def display_result(self):

                                # calculates the wrong count
                                wrong_count = self.data_size - self.correct
                                correct = f"Correct: {self.correct}"
                                wrong = f"Wrong: {wrong_count}"

                                # calcultaes the percentage of correct answers
                                score = int(self.correct /
                                            self.data_size * 100)
                                result = f"Score: {score}%"
                                zxy = ''
                                if score == 100:
                                    zxy = "Learn Python the Hard Way"
                                elif score >= 75 and score < 100:
                                    zxy = "Python Crash Course"
                                elif score >= 50 and score < 75:
                                    zxy = "Head First Python"
                                elif score >= 25 and score < 50:
                                    zxy = "Real Python Course"
                                else:
                                    zxy = "Cover basics from w3schools.com"

                                # Shows a message box to display the result
                                mb.showinfo("Result",
                                            f"{result}\n{zxy}" + ",this book is recommended for you.")

                            # This method checks the Answer after we click on Next.
                            def check_ans(self, q_no):

                                # checks for if the selected option is correct
                                if self.opt_selected.get() == answer[q_no]:
                                    # if the option is correct it return true
                                    return True

                            # This method is used to check the answer of the
                            # current question by calling the check_ans and question no.
                            # if the question is correct it increases the count by 1
                            # and then increase the question number by 1. If it is last
                            # question then it calls display result to show the message box.
                            # otherwise shows next question.
                            def next_btn(self):

                                # Check if the answer is correct
                                if self.check_ans(self.q_no):
                                    # if the answer is correct it increments the correct by 1
                                    self.correct += 1

                                # Moves to next Question by incrementing the q_no counter
                                self.q_no += 1

                                # checks if the q_no size is equal to the data size
                                if self.q_no == self.data_size:

                                    # if it is correct then it displays the score
                                    self.display_result()

                                    # destroys the GUI
                                    gui.destroy()
                                else:
                                    # shows the next question
                                    self.display_question()
                                    self.display_options()

                            # This method shows the two buttons on the screen.
                            # The first one is the next_button which moves to next question
                            # It has properties like what text it shows the functionality,
                            # size, color, and property of text displayed on button. Then it
                            # mentions where to place the button on the screen. The second
                            # button is the exit button which is used to close the GUI without
                            # completing the quiz.
                            def buttons(self):

                                # The first button is the Next button to move to the
                                # next Question

                                next_button = Button(gui, text="Next", command=self.next_btn,
                                                     width=10, bg="blue", fg="white", font=("ariel", 16, "bold"))

                                # palcing the button on the screen
                                next_button.place(x=350, y=380)

                                # This is the second button which is used to Quit the GUI
                                quit_button = Button(gui, text="Quit", command=gui.destroy,
                                                     width=5, bg="black", fg="white", font=("ariel", 16, " bold"))

                                # placing the Quit button on the screen
                                quit_button.place(x=700, y=50)

                            # This method deselect the radio button on the screen
                            # Then it is used to display the options available for the current
                            # question which we obtain through the question number and Updates
                            # each of the options for the current question of the radio button.
                            def display_options(self):
                                val = 0

                                # deselecting the options
                                self.opt_selected.set(0)

                                # looping over the options to be displayed for the
                                # text of the radio buttons.
                                for option in options[self.q_no]:
                                    self.opts[val]['text'] = option
                                    val += 1

                            # This method shows the current Question on the screen
                            def display_question(self):

                                # setting the Quetion properties
                                q_no = Label(gui, text=question[self.q_no], width=60,
                                             font=('ariel', 16, 'bold'), anchor='w')

                                # placing the option on the screen
                                q_no.place(x=70, y=100)

                            # This method is used to Display Title
                            def display_title(self):

                                # The title to be shown
                                title = Label(gui, text="Python QUIZ",
                                              width=50, bg="green", fg="white", font=("ariel", 20, "bold"))

                                # place of the title
                                title.place(x=0, y=2)

                            # This method shows the radio buttons to select the Question
                            # on the screen at the specified position. It also returns a
                            # lsit of radio button which are later used to add the options to
                            # them.
                            def radio_buttons(self):

                                # initialize the list with an empty list of options
                                q_list = []

                                # position of the first option
                                y_pos = 150

                                # adding the options to the list
                                while len(q_list) < 4:
                                    # setting the radio button properties
                                    radio_btn = Radiobutton(gui, text=" ", variable=self.opt_selected,
                                                            value=len(q_list) + 1, font=("ariel", 14))

                                    # adding the button to the list
                                    q_list.append(radio_btn)

                                    # placing the button
                                    radio_btn.place(x=100, y=y_pos)

                                    # incrementing the y-axis position by 40
                                    y_pos += 40

                                # return the radio buttons
                                return q_list

                        # Create a GUI Window
                        gui = Tk()

                        # set the size of the GUI Window
                        gui.geometry("800x450")

                        # set the title of the Window
                        gui.title("Python Quiz")

                        # get the data from the json file
                        with open('json//basic.json') as f:
                            data = json.load(f)

                        # set the question, options, and answer
                        question = (data['question'])
                        options = (data['options'])
                        answer = (data['answer'])

                        # create an object of the Quiz Class.
                        quiz = Quiz()

                        # Start the GUI
                        gui.mainloop()

                        # END OF THE PROGRAM

                    def pythongui():
                        # Python program to create a simple GUI
                        # Simple Quiz using Tkinter

                        # import everything from tkinter

                        # class to define the components of the GUI
                        class Quiz:
                            # This is the first method which is called when a
                            # new object of the class is initialized. This method
                            # sets the question count to 0. and initialize all the
                            # other methoods to display the content and make all the
                            # functionalities available
                            def __init__(self):

                                # set question number to 0
                                self.q_no = 0

                                # assigns ques to the display_question function to update later.
                                self.display_title()
                                self.display_question()

                                # opt_selected holds an integer value which is used for
                                # selected option in a question.
                                self.opt_selected = IntVar()

                                # displaying radio button for the current question and used to
                                # display options for the current question
                                self.opts = self.radio_buttons()

                                # display options for the current question
                                self.display_options()

                                # displays the button for next and exit.
                                self.buttons()

                                # no of questions
                                self.data_size = len(question)

                                # keep a counter of correct answers
                                self.correct = 0

                            # This method is used to display the result
                            # It counts the number of correct and wrong answers
                            # and then display them at the end as a message Box
                            def display_result(self):

                                # calculates the wrong count
                                wrong_count = self.data_size - self.correct
                                correct = f"Correct: {self.correct}"
                                wrong = f"Wrong: {wrong_count}"

                                # calcultaes the percentage of correct answers
                                score = int(self.correct /
                                            self.data_size * 100)
                                result = f"Score: {score}%"
                                zxy = ''
                                if score == 100:
                                    zxy = "Python and TKinter Programming"
                                elif score >= 75 and score < 100:
                                    zxy = "Mastering GUI programming in Python"
                                elif score >= 50 and score < 75:
                                    zxy = "Modern Tkinter"
                                else:
                                    zxy = "Python GUI programming with Tkinter"

                                # Shows a message box to display the result
                                mb.showinfo("Result",
                                            f"{result}\n{zxy}" + ",this book is recommended for you.")

                            # This method checks the Answer after we click on Next.
                            def check_ans(self, q_no):

                                # checks for if the selected option is correct
                                if self.opt_selected.get() == answer[q_no]:
                                    # if the option is correct it return true
                                    return True

                            # This method is used to check the answer of the
                            # current question by calling the check_ans and question no.
                            # if the question is correct it increases the count by 1
                            # and then increase the question number by 1. If it is last
                            # question then it calls display result to show the message box.
                            # otherwise shows next question.
                            def next_btn(self):

                                # Check if the answer is correct
                                if self.check_ans(self.q_no):
                                    # if the answer is correct it increments the correct by 1
                                    self.correct += 1

                                # Moves to next Question by incrementing the q_no counter
                                self.q_no += 1

                                # checks if the q_no size is equal to the data size
                                if self.q_no == self.data_size:

                                    # if it is correct then it displays the score
                                    self.display_result()

                                    # destroys the GUI
                                    gui.destroy()
                                else:
                                    # shows the next question
                                    self.display_question()
                                    self.display_options()

                            # This method shows the two buttons on the screen.
                            # The first one is the next_button which moves to next question
                            # It has properties like what text it shows the functionality,
                            # size, color, and property of text displayed on button. Then it
                            # mentions where to place the button on the screen. The second
                            # button is the exit button which is used to close the GUI without
                            # completing the quiz.
                            def buttons(self):

                                # The first button is the Next button to move to the
                                # next Question
                                next_button = Button(gui, text="Next", command=self.next_btn,
                                                     width=10, bg="blue", fg="white", font=("ariel", 16, "bold"))

                                # palcing the button on the screen
                                next_button.place(x=350, y=380)

                                # This is the second button which is used to Quit the GUI
                                quit_button = Button(gui, text="Quit", command=gui.destroy,
                                                     width=5, bg="black", fg="white", font=("ariel", 16, " bold"))

                                # placing the Quit button on the screen
                                quit_button.place(x=700, y=50)

                            # This method deselect the radio button on the screen
                            # Then it is used to display the options available for the current
                            # question which we obtain through the question number and Updates
                            # each of the options for the current question of the radio button.
                            def display_options(self):
                                val = 0

                                # deselecting the options
                                self.opt_selected.set(0)

                                # looping over the options to be displayed for the
                                # text of the radio buttons.
                                for option in options[self.q_no]:
                                    self.opts[val]['text'] = option
                                    val += 1

                            # This method shows the current Question on the screen
                            def display_question(self):

                                # setting the Quetion properties
                                q_no = Label(gui, text=question[self.q_no], width=60,
                                             font=('ariel', 16, 'bold'), anchor='w')

                                # placing the option on the screen
                                q_no.place(x=70, y=100)

                            # This method is used to Display Title
                            def display_title(self):

                                # The title to be shown
                                title = Label(gui, text="Python QUIZ",
                                              width=50, bg="green", fg="white", font=("ariel", 20, "bold"))

                                # place of the title
                                title.place(x=0, y=2)

                            # This method shows the radio buttons to select the Question
                            # on the screen at the specified position. It also returns a
                            # lsit of radio button which are later used to add the options to
                            # them.
                            def radio_buttons(self):

                                # initialize the list with an empty list of options
                                q_list = []

                                # position of the first option
                                y_pos = 150

                                # adding the options to the list
                                while len(q_list) < 4:
                                    # setting the radio button properties
                                    radio_btn = Radiobutton(gui, text=" ", variable=self.opt_selected,
                                                            value=len(q_list) + 1, font=("ariel", 14))

                                    # adding the button to the list
                                    q_list.append(radio_btn)

                                    # placing the button
                                    radio_btn.place(x=100, y=y_pos)

                                    # incrementing the y-axis position by 40
                                    y_pos += 40

                                # return the radio buttons
                                return q_list

                        # Create a GUI Window
                        gui = Tk()

                        # set the size of the GUI Window
                        gui.geometry("800x450")

                        # set the title of the Window
                        gui.title("Python Quiz")

                        # get the data from the json file
                        with open('json//gui.json') as f:
                            data = json.load(f)

                        # set the question, options, and answer
                        question = (data['question'])
                        options = (data['options'])
                        answer = (data['answer'])

                        # create an object of the Quiz Class.
                        quiz = Quiz()

                        # Start the GUI
                        gui.mainloop()

                        # END OF THE PROGRAM

                    def pythonweb():
                        # Python program to create a simple GUI
                        # Simple Quiz using Tkinter

                        # import everything from tkinter

                        # class to define the components of the GUI
                        class Quiz:
                            # This is the first method which is called when a
                            # new object of the class is initialized. This method
                            # sets the question count to 0. and initialize all the
                            # other methoods to display the content and make all the
                            # functionalities available
                            def __init__(self):

                                # set question number to 0
                                self.q_no = 0

                                # assigns ques to the display_question function to update later.
                                self.display_title()
                                self.display_question()

                                # opt_selected holds an integer value which is used for
                                # selected option in a question.
                                self.opt_selected = IntVar()

                                # displaying radio button for the current question and used to
                                # display options for the current question
                                self.opts = self.radio_buttons()

                                # display options for the current question
                                self.display_options()

                                # displays the button for next and exit.
                                self.buttons()

                                # no of questions
                                self.data_size = len(question)

                                # keep a counter of correct answers
                                self.correct = 0

                            # This method is used to display the result
                            # It counts the number of correct and wrong answers
                            # and then display them at the end as a message Box
                            def display_result(self):

                                # calculates the wrong count
                                wrong_count = self.data_size - self.correct
                                correct = f"Correct: {self.correct}"
                                wrong = f"Wrong: {wrong_count}"

                                # calcultaes the percentage of correct answers
                                score = int(self.correct /
                                            self.data_size * 100)
                                result = f"Score: {score}%"
                                zxy = ''
                                if score == 100:
                                    zxy = "Django for Professionals"
                                elif score >= 75 and score < 100:
                                    zxy = "Mastering Django"
                                elif score >= 50 and score < 75:
                                    zxy = "Lightweight Django"
                                elif score >= 25 and score < 50:
                                    zxy = "Django3 by examples"
                                else:
                                    zxy = "Django for beginners"

                                # Shows a message box to display the result
                                mb.showinfo("Result",
                                            f"{result}\n{zxy}" + ",this book is recommended for you.")

                            # This method checks the Answer after we click on Next.
                            def check_ans(self, q_no):

                                # checks for if the selected option is correct
                                if self.opt_selected.get() == answer[q_no]:
                                    # if the option is correct it return true
                                    return True

                            # This method is used to check the answer of the
                            # current question by calling the check_ans and question no.
                            # if the question is correct it increases the count by 1
                            # and then increase the question number by 1. If it is last
                            # question then it calls display result to show the message box.
                            # otherwise shows next question.
                            def next_btn(self):

                                # Check if the answer is correct
                                if self.check_ans(self.q_no):
                                    # if the answer is correct it increments the correct by 1
                                    self.correct += 1

                                # Moves to next Question by incrementing the q_no counter
                                self.q_no += 1

                                # checks if the q_no size is equal to the data size
                                if self.q_no == self.data_size:

                                    # if it is correct then it displays the score
                                    self.display_result()

                                    # destroys the GUI
                                    gui.destroy()
                                else:
                                    # shows the next question
                                    self.display_question()
                                    self.display_options()

                            # This method shows the two buttons on the screen.
                            # The first one is the next_button which moves to next question
                            # It has properties like what text it shows the functionality,
                            # size, color, and property of text displayed on button. Then it
                            # mentions where to place the button on the screen. The second
                            # button is the exit button which is used to close the GUI without
                            # completing the quiz.
                            def buttons(self):

                                # The first button is the Next button to move to the
                                # next Question
                                next_button = Button(gui, text="Next", command=self.next_btn,
                                                     width=10, bg="blue", fg="white", font=("ariel", 16, "bold"))

                                # palcing the button on the screen
                                next_button.place(x=350, y=380)

                                # This is the second button which is used to Quit the GUI
                                quit_button = Button(gui, text="Quit", command=gui.destroy,
                                                     width=5, bg="black", fg="white", font=("ariel", 16, " bold"))

                                # placing the Quit button on the screen
                                quit_button.place(x=700, y=50)

                            # This method deselect the radio button on the screen
                            # Then it is used to display the options available for the current
                            # question which we obtain through the question number and Updates
                            # each of the options for the current question of the radio button.
                            def display_options(self):
                                val = 0

                                # deselecting the options
                                self.opt_selected.set(0)

                                # looping over the options to be displayed for the
                                # text of the radio buttons.
                                for option in options[self.q_no]:
                                    self.opts[val]['text'] = option
                                    val += 1

                            # This method shows the current Question on the screen
                            def display_question(self):

                                # setting the Quetion properties
                                q_no = Label(gui, text=question[self.q_no], width=60,
                                             font=('ariel', 16, 'bold'), anchor='w')

                                # placing the option on the screen
                                q_no.place(x=70, y=100)

                            # This method is used to Display Title
                            def display_title(self):

                                # The title to be shown
                                title = Label(gui, text="Python QUIZ",
                                              width=50, bg="green", fg="white", font=("ariel", 20, "bold"))

                                # place of the title
                                title.place(x=0, y=2)

                            # This method shows the radio buttons to select the Question
                            # on the screen at the specified position. It also returns a
                            # lsit of radio button which are later used to add the options to
                            # them.
                            def radio_buttons(self):

                                # initialize the list with an empty list of options
                                q_list = []

                                # position of the first option
                                y_pos = 150

                                # adding the options to the list
                                while len(q_list) < 4:
                                    # setting the radio button properties
                                    radio_btn = Radiobutton(gui, text=" ", variable=self.opt_selected,
                                                            value=len(q_list) + 1, font=("ariel", 14))

                                    # adding the button to the list
                                    q_list.append(radio_btn)

                                    # placing the button
                                    radio_btn.place(x=100, y=y_pos)

                                    # incrementing the y-axis position by 40
                                    y_pos += 40

                                # return the radio buttons
                                return q_list

                        # Create a GUI Window
                        gui = Tk()

                        # set the size of the GUI Window
                        gui.geometry("800x450")

                        # set the title of the Window
                        gui.title("Python Quiz")

                        # get the data from the json file
                        with open('json//web.json') as f:
                            data = json.load(f)

                        # set the question, options, and answer
                        question = (data['question'])
                        options = (data['options'])
                        answer = (data['answer'])

                        # create an object of the Quiz Class.
                        quiz = Quiz()

                        # Start the GUI
                        gui.mainloop()

                        # END OF THE PROGRAM

                    def pythoncs():
                        # Python program to create a simple GUI
                        # Simple Quiz using Tkinter

                        # import everything from tkinter

                        # class to define the components of the GUI
                        class Quiz:
                            # This is the first method which is called when a
                            # new object of the class is initialized. This method
                            # sets the question count to 0. and initialize all the
                            # other methoods to display the content and make all the
                            # functionalities available
                            def __init__(self):

                                # set question number to 0
                                self.q_no = 0

                                # assigns ques to the display_question function to update later.
                                self.display_title()
                                self.display_question()

                                # opt_selected holds an integer value which is used for
                                # selected option in a question.
                                self.opt_selected = IntVar()

                                # displaying radio button for the current question and used to
                                # display options for the current question
                                self.opts = self.radio_buttons()

                                # display options for the current question
                                self.display_options()

                                # displays the button for next and exit.
                                self.buttons()

                                # no of questions
                                self.data_size = len(question)

                                # keep a counter of correct answers
                                self.correct = 0

                            # This method is used to display the result
                            # It counts the number of correct and wrong answers
                            # and then display them at the end as a message Box
                            def display_result(self):

                                # calculates the wrong count
                                wrong_count = self.data_size - self.correct
                                correct = f"Correct: {self.correct}"
                                wrong = f"Wrong: {wrong_count}"

                                # calcultaes the percentage of correct answers
                                score = int(self.correct /
                                            self.data_size * 100)
                                result = f"Score: {score}%"
                                zxy = ''
                                if score == 100:
                                    zxy = "Mastering Python for Networking and Security"
                                elif score >= 75 and score < 100:
                                    zxy = "Blackhat Python"
                                elif score >= 50 and score < 75:
                                    zxy = "Cyber Security-The Beginners Guide"
                                else:
                                    zxy = "Violent Python"

                                # Shows a message box to display the result
                                mb.showinfo("Result",
                                            f"{result}\n{zxy}" + ",this book is recommended for you.")

                            # This method checks the Answer after we click on Next.
                            def check_ans(self, q_no):

                                # checks for if the selected option is correct
                                if self.opt_selected.get() == answer[q_no]:
                                    # if the option is correct it return true
                                    return True

                            # This method is used to check the answer of the
                            # current question by calling the check_ans and question no.
                            # if the question is correct it increases the count by 1
                            # and then increase the question number by 1. If it is last
                            # question then it calls display result to show the message box.
                            # otherwise shows next question.
                            def next_btn(self):

                                # Check if the answer is correct
                                if self.check_ans(self.q_no):
                                    # if the answer is correct it increments the correct by 1
                                    self.correct += 1

                                # Moves to next Question by incrementing the q_no counter
                                self.q_no += 1

                                # checks if the q_no size is equal to the data size
                                if self.q_no == self.data_size:

                                    # if it is correct then it displays the score
                                    self.display_result()

                                    # destroys the GUI
                                    gui.destroy()
                                else:
                                    # shows the next question
                                    self.display_question()
                                    self.display_options()

                            # This method shows the two buttons on the screen.
                            # The first one is the next_button which moves to next question
                            # It has properties like what text it shows the functionality,
                            # size, color, and property of text displayed on button. Then it
                            # mentions where to place the button on the screen. The second
                            # button is the exit button which is used to close the GUI without
                            # completing the quiz.
                            def buttons(self):

                                # The first button is the Next button to move to the
                                # next Question
                                next_button = Button(gui, text="Next", command=self.next_btn,
                                                     width=10, bg="blue", fg="white", font=("ariel", 16, "bold"))

                                # palcing the button on the screen
                                next_button.place(x=350, y=380)

                                # This is the second button which is used to Quit the GUI
                                quit_button = Button(gui, text="Quit", command=gui.destroy,
                                                     width=5, bg="black", fg="white", font=("ariel", 16, " bold"))

                                # placing the Quit button on the screen
                                quit_button.place(x=700, y=50)

                            # This method deselect the radio button on the screen
                            # Then it is used to display the options available for the current
                            # question which we obtain through the question number and Updates
                            # each of the options for the current question of the radio button.
                            def display_options(self):
                                val = 0

                                # deselecting the options
                                self.opt_selected.set(0)

                                # looping over the options to be displayed for the
                                # text of the radio buttons.
                                for option in options[self.q_no]:
                                    self.opts[val]['text'] = option
                                    val += 1

                            # This method shows the current Question on the screen
                            def display_question(self):

                                # setting the Quetion properties
                                q_no = Label(gui, text=question[self.q_no], width=60,
                                             font=('ariel', 16, 'bold'), anchor='w')

                                # placing the option on the screen
                                q_no.place(x=70, y=100)

                            # This method is used to Display Title
                            def display_title(self):

                                # The title to be shown
                                title = Label(gui, text="Python QUIZ",
                                              width=50, bg="green", fg="white", font=("ariel", 20, "bold"))

                                # place of the title
                                title.place(x=0, y=2)

                            # This method shows the radio buttons to select the Question
                            # on the screen at the specified position. It also returns a
                            # lsit of radio button which are later used to add the options to
                            # them.
                            def radio_buttons(self):

                                # initialize the list with an empty list of options
                                q_list = []

                                # position of the first option
                                y_pos = 150

                                # adding the options to the list
                                while len(q_list) < 4:
                                    # setting the radio button properties
                                    radio_btn = Radiobutton(gui, text=" ", variable=self.opt_selected,
                                                            value=len(q_list) + 1, font=("ariel", 14))

                                    # adding the button to the list
                                    q_list.append(radio_btn)

                                    # placing the button
                                    radio_btn.place(x=100, y=y_pos)

                                    # incrementing the y-axis position by 40
                                    y_pos += 40

                                # return the radio buttons
                                return q_list

                        # Create a GUI Window
                        gui = Tk()

                        # set the size of the GUI Window
                        gui.geometry("800x450")

                        # set the title of the Window
                        gui.title("Python Quiz")

                        # get the data from the json file
                        with open('json//cs.json') as f:
                            data = json.load(f)

                        # set the question, options, and answer
                        question = (data['question'])
                        options = (data['options'])
                        answer = (data['answer'])

                        # create an object of the Quiz Class.
                        quiz = Quiz()

                        # Start the GUI
                        gui.mainloop()

                        # END OF THE PROGRAM

                    def pythonauto():
                        # Python program to create a simple GUI
                        # Simple Quiz using Tkinter

                        # import everything from tkinter

                        # class to define the components of the GUI
                        class Quiz:
                            # This is the first method which is called when a
                            # new object of the class is initialized. This method
                            # sets the question count to 0. and initialize all the
                            # other methoods to display the content and make all the
                            # functionalities available
                            def __init__(self):

                                # set question number to 0
                                self.q_no = 0

                                # assigns ques to the display_question function to update later.
                                self.display_title()
                                self.display_question()

                                # opt_selected holds an integer value which is used for
                                # selected option in a question.
                                self.opt_selected = IntVar()

                                # displaying radio button for the current question and used to
                                # display options for the current question
                                self.opts = self.radio_buttons()

                                # display options for the current question
                                self.display_options()

                                # displays the button for next and exit.
                                self.buttons()

                                # no of questions
                                self.data_size = len(question)

                                # keep a counter of correct answers
                                self.correct = 0

                            # This method is used to display the result
                            # It counts the number of correct and wrong answers
                            # and then display them at the end as a message Box
                            def display_result(self):

                                # calculates the wrong count
                                wrong_count = self.data_size - self.correct
                                correct = f"Correct: {self.correct}"
                                wrong = f"Wrong: {wrong_count}"

                                # calcultaes the percentage of correct answers
                                score = int(self.correct /
                                            self.data_size * 100)
                                result = f"Score: {score}%"
                                zxy = ''
                                if score == 100:
                                    zxy = "Automate the Boring Stuff with Python"
                                elif score >= 75 and score < 100:
                                    zxy = "Test Driven Development with Python"
                                elif score >= 50 and score < 75:
                                    zxy = "Programming Python by Mark"
                                else:
                                    zxy = "Learning Python by Mark"

                                # Shows a message box to display the result
                                mb.showinfo("Result",
                                            f"{result}\n{zxy}" + ",this book is recommended for you.")

                            # This method checks the Answer after we click on Next.
                            def check_ans(self, q_no):

                                # checks for if the selected option is correct
                                if self.opt_selected.get() == answer[q_no]:
                                    # if the option is correct it return true
                                    return True

                            # This method is used to check the answer of the
                            # current question by calling the check_ans and question no.
                            # if the question is correct it increases the count by 1
                            # and then increase the question number by 1. If it is last
                            # question then it calls display result to show the message box.
                            # otherwise shows next question.
                            def next_btn(self):

                                # Check if the answer is correct
                                if self.check_ans(self.q_no):
                                    # if the answer is correct it increments the correct by 1
                                    self.correct += 1

                                # Moves to next Question by incrementing the q_no counter
                                self.q_no += 1

                                # checks if the q_no size is equal to the data size
                                if self.q_no == self.data_size:

                                    # if it is correct then it displays the score
                                    self.display_result()

                                    # destroys the GUI
                                    gui.destroy()
                                else:
                                    # shows the next question
                                    self.display_question()
                                    self.display_options()

                            # This method shows the two buttons on the screen.
                            # The first one is the next_button which moves to next question
                            # It has properties like what text it shows the functionality,
                            # size, color, and property of text displayed on button. Then it
                            # mentions where to place the button on the screen. The second
                            # button is the exit button which is used to close the GUI without
                            # completing the quiz.
                            def buttons(self):

                                # The first button is the Next button to move to the
                                # next Question
                                next_button = Button(gui, text="Next", command=self.next_btn,
                                                     width=10, bg="blue", fg="white", font=("ariel", 16, "bold"))

                                # palcing the button on the screen
                                next_button.place(x=350, y=380)

                                # This is the second button which is used to Quit the GUI
                                quit_button = Button(gui, text="Quit", command=gui.destroy,
                                                     width=5, bg="black", fg="white", font=("ariel", 16, " bold"))

                                # placing the Quit button on the screen
                                quit_button.place(x=700, y=50)

                            # This method deselect the radio button on the screen
                            # Then it is used to display the options available for the current
                            # question which we obtain through the question number and Updates
                            # each of the options for the current question of the radio button.
                            def display_options(self):
                                val = 0

                                # deselecting the options
                                self.opt_selected.set(0)

                                # looping over the options to be displayed for the
                                # text of the radio buttons.
                                for option in options[self.q_no]:
                                    self.opts[val]['text'] = option
                                    val += 1

                            # This method shows the current Question on the screen
                            def display_question(self):

                                # setting the Quetion properties
                                q_no = Label(gui, text=question[self.q_no], width=60,
                                             font=('ariel', 16, 'bold'), anchor='w')

                                # placing the option on the screen
                                q_no.place(x=70, y=100)

                            # This method is used to Display Title
                            def display_title(self):

                                # The title to be shown
                                title = Label(gui, text="Python QUIZ",
                                              width=50, bg="green", fg="white", font=("ariel", 20, "bold"))

                                # place of the title
                                title.place(x=0, y=2)

                            # This method shows the radio buttons to select the Question
                            # on the screen at the specified position. It also returns a
                            # lsit of radio button which are later used to add the options to
                            # them.
                            def radio_buttons(self):

                                # initialize the list with an empty list of options
                                q_list = []

                                # position of the first option
                                y_pos = 150

                                # adding the options to the list
                                while len(q_list) < 4:
                                    # setting the radio button properties
                                    radio_btn = Radiobutton(gui, text=" ", variable=self.opt_selected,
                                                            value=len(q_list) + 1, font=("ariel", 14))

                                    # adding the button to the list
                                    q_list.append(radio_btn)

                                    # placing the button
                                    radio_btn.place(x=100, y=y_pos)

                                    # incrementing the y-axis position by 40
                                    y_pos += 40

                                # return the radio buttons
                                return q_list

                        # Create a GUI Window
                        gui = Tk()

                        # set the size of the GUI Window
                        gui.geometry("800x450")

                        # set the title of the Window
                        gui.title("Python Quiz")

                        # get the data from the json file
                        with open('json//auto.json') as f:
                            data = json.load(f)

                        # set the question, options, and answer
                        question = (data['question'])
                        options = (data['options'])
                        answer = (data['answer'])

                        # create an object of the Quiz Class.
                        quiz = Quiz()

                        # Start the GUI
                        gui.mainloop()

                        # END OF THE PROGRAM

                    def pythongame():
                        # Python program to create a simple GUI
                        # Simple Quiz using Tkinter

                        # import everything from tkinter

                        # class to define the components of the GUI
                        class Quiz:
                            # This is the first method which is called when a
                            # new object of the class is initialized. This method
                            # sets the question count to 0. and initialize all the
                            # other methoods to display the content and make all the
                            # functionalities available
                            def __init__(self):

                                # set question number to 0
                                self.q_no = 0

                                # assigns ques to the display_question function to update later.
                                self.display_title()
                                self.display_question()

                                # opt_selected holds an integer value which is used for
                                # selected option in a question.
                                self.opt_selected = IntVar()

                                # displaying radio button for the current question and used to
                                # display options for the current question
                                self.opts = self.radio_buttons()

                                # display options for the current question
                                self.display_options()

                                # displays the button for next and exit.
                                self.buttons()

                                # no of questions
                                self.data_size = len(question)

                                # keep a counter of correct answers
                                self.correct = 0

                            # This method is used to display the result
                            # It counts the number of correct and wrong answers
                            # and then display them at the end as a message Box
                            def display_result(self):

                                # calculates the wrong count
                                wrong_count = self.data_size - self.correct
                                correct = f"Correct: {self.correct}"
                                wrong = f"Wrong: {wrong_count}"

                                # calcultaes the percentage of correct answers
                                score = int(self.correct /
                                            self.data_size * 100)
                                result = f"Score: {score}%"
                                zxy = ''
                                if score == 100:
                                    zxy = "Invent your own games with python"
                                elif score >= 75 and score < 100:
                                    zxy = "Python Arcade games"
                                elif score >= 50 and score < 75:
                                    zxy = "Pygame for python game development"
                                elif score >= 25 and score < 50:
                                    zxy = "Mission Python"
                                else:
                                    zxy = "Beginning Python Games Development"

                                # Shows a message box to display the result
                                abc = mb.showinfo("Result",
                                                  f"{result}\n{zxy}"+",this book is recommended for you.")

                            # This method checks the Answer after we click on Next.
                            def check_ans(self, q_no):

                                # checks for if the selected option is correct
                                if self.opt_selected.get() == answer[q_no]:
                                    # if the option is correct it return true
                                    return True

                            # This method is used to check the answer of the
                            # current question by calling the check_ans and question no.
                            # if the question is correct it increases the count by 1
                            # and then increase the question number by 1. If it is last
                            # question then it calls display result to show the message box.
                            # otherwise shows next question.
                            def next_btn(self):

                                # Check if the answer is correct
                                if self.check_ans(self.q_no):
                                    # if the answer is correct it increments the correct by 1
                                    self.correct += 1

                                # Moves to next Question by incrementing the q_no counter
                                self.q_no += 1

                                # checks if the q_no size is equal to the data size
                                if self.q_no == self.data_size:

                                    # if it is correct then it displays the score
                                    self.display_result()

                                    # destroys the GUI
                                    gui.destroy()
                                else:
                                    # shows the next question
                                    self.display_question()
                                    self.display_options()

                            # This method shows the two buttons on the screen.
                            # The first one is the next_button which moves to next question
                            # It has properties like what text it shows the functionality,
                            # size, color, and property of text displayed on button. Then it
                            # mentions where to place the button on the screen. The second
                            # button is the exit button which is used to close the GUI without
                            # completing the quiz.
                            def buttons(self):

                                # The first button is the Next button to move to the
                                # next Question
                                next_button = Button(gui, text="Next", command=self.next_btn,
                                                     width=10, bg="blue", fg="white", font=("ariel", 16, "bold"))

                                # palcing the button on the screen
                                next_button.place(x=350, y=380)

                                # This is the second button which is used to Quit the GUI
                                quit_button = Button(gui, text="Quit", command=gui.destroy,
                                                     width=5, bg="black", fg="white", font=("ariel", 16, " bold"))

                                # placing the Quit button on the screen
                                quit_button.place(x=700, y=50)

                            # This method deselect the radio button on the screen
                            # Then it is used to display the options available for the current
                            # question which we obtain through the question number and Updates
                            # each of the options for the current question of the radio button.
                            def display_options(self):
                                val = 0

                                # deselecting the options
                                self.opt_selected.set(0)

                                # looping over the options to be displayed for the
                                # text of the radio buttons.
                                for option in options[self.q_no]:
                                    self.opts[val]['text'] = option
                                    val += 1

                            # This method shows the current Question on the screen
                            def display_question(self):

                                # setting the Quetion properties
                                q_no = Label(gui, text=question[self.q_no], width=60,
                                             font=('ariel', 16, 'bold'), anchor='w')

                                # placing the option on the screen
                                q_no.place(x=70, y=100)

                            # This method is used to Display Title
                            def display_title(self):

                                # The title to be shown
                                title = Label(gui, text="Python QUIZ",
                                              width=50, bg="green", fg="white", font=("ariel", 20, "bold"))

                                # place of the title
                                title.place(x=0, y=2)

                            # This method shows the radio buttons to select the Question
                            # on the screen at the specified position. It also returns a
                            # lsit of radio button which are later used to add the options to
                            # them.
                            def radio_buttons(self):

                                # initialize the list with an empty list of options
                                q_list = []

                                # position of the first option
                                y_pos = 150

                                # adding the options to the list
                                while len(q_list) < 4:
                                    # setting the radio button properties
                                    radio_btn = Radiobutton(gui, text=" ", variable=self.opt_selected,
                                                            value=len(q_list) + 1, font=("ariel", 14))

                                    # adding the button to the list
                                    q_list.append(radio_btn)

                                    # placing the button
                                    radio_btn.place(x=100, y=y_pos)

                                    # incrementing the y-axis position by 40
                                    y_pos += 40

                                # return the radio buttons
                                return q_list

                        # Create a GUI Window
                        gui = Tk()

                        # set the size of the GUI Window
                        gui.geometry("800x450")

                        # set the title of the Window
                        gui.title("Python Quiz")

                        # get the data from the json file
                        with open('json//game.json') as f:
                            data = json.load(f)

                        # set the question, options, and answer
                        question = (data['question'])
                        options = (data['options'])
                        answer = (data['answer'])

                        # create an object of the Quiz Class.
                        quiz = Quiz()

                        # Start the GUI
                        gui.mainloop()

                        # END OF THE PROGRAM

                    def pythonml():
                        # Python program to create a simple GUI
                        # Simple Quiz using Tkinter

                        # import everything from tkinter

                        # class to define the components of the GUI
                        class Quiz:
                            # This is the first method which is called when a
                            # new object of the class is initialized. This method
                            # sets the question count to 0. and initialize all the
                            # other methoods to display the content and make all the
                            # functionalities available
                            def __init__(self):

                                # set question number to 0
                                self.q_no = 0

                                # assigns ques to the display_question function to update later.
                                self.display_title()
                                self.display_question()

                                # opt_selected holds an integer value which is used for
                                # selected option in a question.
                                self.opt_selected = IntVar()

                                # displaying radio button for the current question and used to
                                # display options for the current question
                                self.opts = self.radio_buttons()

                                # display options for the current question
                                self.display_options()

                                # displays the button for next and exit.
                                self.buttons()

                                # no of questions
                                self.data_size = len(question)

                                # keep a counter of correct answers
                                self.correct = 0

                            # This method is used to display the result
                            # It counts the number of correct and wrong answers
                            # and then display them at the end as a message Box
                            def display_result(self):

                                # calculates the wrong count
                                wrong_count = self.data_size - self.correct
                                correct = f"Correct: {self.correct}"
                                wrong = f"Wrong: {wrong_count}"

                                # calcultaes the percentage of correct answers
                                score = int(self.correct /
                                            self.data_size * 100)
                                result = f"Score: {score}%"
                                zxy = ''
                                if score == 100:
                                    zxy = "Oreilly'' Hands on ML"
                                elif score >= 75 and score < 100:
                                    zxy = "Oreilly Introduction to Machine Learning with Python"
                                elif score >= 50 and score < 75:
                                    zxy = "Understading Machine Learning"
                                else:
                                    zxy = "Machine Learning in action"

                                # Shows a message box to display the result
                                mb.showinfo("Result",
                                            f"{result}\n{zxy}" + ",this book is recommended for you.")

                            # This method checks the Answer after we click on Next.
                            def check_ans(self, q_no):

                                # checks for if the selected option is correct
                                if self.opt_selected.get() == answer[q_no]:
                                    # if the option is correct it return true
                                    return True

                            # This method is used to check the answer of the
                            # current question by calling the check_ans and question no.
                            # if the question is correct it increases the count by 1
                            # and then increase the question number by 1. If it is last
                            # question then it calls display result to show the message box.
                            # otherwise shows next question.
                            def next_btn(self):

                                # Check if the answer is correct
                                if self.check_ans(self.q_no):
                                    # if the answer is correct it increments the correct by 1
                                    self.correct += 1

                                # Moves to next Question by incrementing the q_no counter
                                self.q_no += 1

                                # checks if the q_no size is equal to the data size
                                if self.q_no == self.data_size:

                                    # if it is correct then it displays the score
                                    self.display_result()

                                    # destroys the GUI
                                    gui.destroy()
                                else:
                                    # shows the next question
                                    self.display_question()
                                    self.display_options()

                            # This method shows the two buttons on the screen.
                            # The first one is the next_button which moves to next question
                            # It has properties like what text it shows the functionality,
                            # size, color, and property of text displayed on button. Then it
                            # mentions where to place the button on the screen. The second
                            # button is the exit button which is used to close the GUI without
                            # completing the quiz.
                            def buttons(self):

                                # The first button is the Next button to move to the
                                # next Question
                                next_button = Button(gui, text="Next", command=self.next_btn,
                                                     width=10, bg="blue", fg="white", font=("ariel", 16, "bold"))

                                # palcing the button on the screen
                                next_button.place(x=350, y=380)

                                # This is the second button which is used to Quit the GUI
                                quit_button = Button(gui, text="Quit", command=gui.destroy,
                                                     width=5, bg="black", fg="white", font=("ariel", 16, " bold"))

                                # placing the Quit button on the screen
                                quit_button.place(x=700, y=50)

                            # This method deselect the radio button on the screen
                            # Then it is used to display the options available for the current
                            # question which we obtain through the question number and Updates
                            # each of the options for the current question of the radio button.
                            def display_options(self):
                                val = 0

                                # deselecting the options
                                self.opt_selected.set(0)

                                # looping over the options to be displayed for the
                                # text of the radio buttons.
                                for option in options[self.q_no]:
                                    self.opts[val]['text'] = option
                                    val += 1

                            # This method shows the current Question on the screen
                            def display_question(self):

                                # setting the Quetion properties
                                q_no = Label(gui, text=question[self.q_no], width=60,
                                             font=('ariel', 16, 'bold'), anchor='w')

                                # placing the option on the screen
                                q_no.place(x=70, y=100)

                            # This method is used to Display Title
                            def display_title(self):

                                # The title to be shown
                                title = Label(gui, text="Python QUIZ",
                                              width=50, bg="green", fg="white", font=("ariel", 20, "bold"))

                                # place of the title
                                title.place(x=0, y=2)

                            # This method shows the radio buttons to select the Question
                            # on the screen at the specified position. It also returns a
                            # lsit of radio button which are later used to add the options to
                            # them.
                            def radio_buttons(self):

                                # initialize the list with an empty list of options
                                q_list = []

                                # position of the first option
                                y_pos = 150

                                # adding the options to the list
                                while len(q_list) < 4:
                                    # setting the radio button properties
                                    radio_btn = Radiobutton(gui, text=" ", variable=self.opt_selected,
                                                            value=len(q_list) + 1, font=("ariel", 14))

                                    # adding the button to the list
                                    q_list.append(radio_btn)

                                    # placing the button
                                    radio_btn.place(x=100, y=y_pos)

                                    # incrementing the y-axis position by 40
                                    y_pos += 40

                                # return the radio buttons
                                return q_list

                        # Create a GUI Window
                        gui = Tk()

                        # set the size of the GUI Window
                        gui.geometry("800x450")

                        # set the title of the Window
                        gui.title("Python Quiz")

                        # get the data from the json file
                        with open('json//ml.json') as f:
                            data = json.load(f)

                        # set the question, options, and answer
                        question = (data['question'])
                        options = (data['options'])
                        answer = (data['answer'])

                        # create an object of the Quiz Class.
                        quiz = Quiz()

                        # Start the GUI
                        gui.mainloop()

                        # END OF THE PROGRAM

                    roote = Tk()
                    roote.configure(bg="light blue")
                    roote.title("College Connect")
                    roote.geometry("800x500+0+0")
                    Label(roote, text="Which topic you are looking for?", font="Algerian 15 underline",
                          bg="light blue").pack()
                    Button(roote, text="Python Basics", bg="turquoise4", fg="white", font="Verdana 14", height=1,
                           width=20, command=lambda: [roote.destroy(), pythonbasics()]).place(x=300, y=50)
                    Button(roote, text="Python tkinter gui", bg="turquoise4", fg="white", font="Verdana 14", height=1,
                           width=20, command=lambda: [roote.destroy(), pythongui()]).place(x=300, y=100)
                    Button(roote, text="Python Web", bg="turquoise4", fg="white", font="Verdana 14", height=1, width=20,
                           command=lambda: [roote.destroy(), pythonweb()]).place(x=300, y=150)
                    Button(roote, text="Python Cyber Security", bg="turquoise4", fg="white", font="Verdana 14",
                           height=1, width=20, command=lambda: [roote.destroy(), pythoncs()]).place(x=300, y=200)
                    Button(roote, text="Python Automation", bg="turquoise4", fg="white", font="Verdana 14", height=1,
                           width=20, command=lambda: [roote.destroy(), pythonauto()]).place(x=300, y=250)
                    Button(roote, text="Python Game Dev", bg="turquoise4", fg="white", font="Verdana 14", height=1,
                           width=20, command=lambda: [roote.destroy(), pythongame()]).place(x=300, y=300)
                    Button(roote, text="Python ML and Data Sciences", bg="turquoise4", fg="white", font="Verdana 14",
                           height=1, width=25, command=lambda: [roote.destroy(), pythonml()]).place(x=270, y=350)
                    Button(roote, text="Home", bg="steelblue", justify="l", fg="white", font="Verdana 12 ", height=2,
                           width=8,
                           command=roote.destroy).place(x=700, y=400)
                    roote.mainloop()

                def exaampython():

                    def more():
                        examrootb = Tk()
                        examrootb.geometry("800x450")
                        examrootb.title("Book recommendation")
                        examrootb.configure(bg="light blue")
                        Label(examrootb, text="We recommend you to go for Python Mcgreww for understanding\n"
                                              "the concepts clearly and deep diving as you have many days\n"
                                              "in hand for exam.", bg="steelblue", justify="l", fg="white",
                              font="Verdana 12 ").place(x=150, y=150)
                        Button(examrootb, text="Home", bg="steelblue", justify="l", fg="white", font="Verdana 12 ",
                               height=2, width=8, command=lambda: [examrootb.destroy(), python()]).place(x=700, y=400)
                        examrootb.mainloop()

                    def less():
                        examrootc = Tk()
                        examrootc.geometry("800x450")
                        examrootc.title("Book recommendation")
                        examrootc.configure(bg="light blue")
                        Label(examrootc, text="We think you need such a book which can cover all the topics in\n"
                                              "brief in less time and easy to understand.So we recommend you\n"
                                              " to go for Techmax of Python as it consists of all the important\n"
                                              "questions in the point of view of exam,and is the best for last\n"
                                              "moment preparation", justify="l", bg="steelblue", fg="white",
                              font="Verdana 12 ").place(x=150, y=150)
                        Button(examrootc, text="Home", bg="steelblue", justify="l", fg="white", font="Verdana 12 ",
                               height=2, width=8, command=lambda: [examrootc.destroy(), python()]).place(x=700, y=400)
                        examrootc.mainloop()

                    examroot = Tk()
                    examroot.geometry("800x450")
                    examroot.title("Book recommendation")
                    examroot.configure(bg="light blue")
                    Label(examroot, text="How many days are remaining for exam?", bg="light blue",
                          font="Algerian 15 ").place(x=205, y=50)
                    Button(examroot, text="More than 1 month", bg="steelblue", fg="white", font="Verdana 12 ", height=2,
                           width=18, command=lambda: [examroot.destroy(), more()]).place(x=300, y=150)
                    Button(examroot, text="Less than a month", bg="steelblue", fg="white", font="Verdana 12", height=2,
                           width=18, command=lambda: [less(), examroot.destroy()]).place(x=300, y=230)
                    examroot.mainloop()

                rootd = Tk()
                rootd.configure(bg="light blue")
                rootd.title("College Connect")
                rootd.geometry("800x500+0+0")
                Label(rootd, text="Book Recommendation", font="Algerian 20 underline", bg="light blue").place(x=210,
                                                                                                              y=75)
                Label(rootd, text="Are you studying for exam or Knowledge?", font="Algerian 15 underline",
                      bg="light blue").place(x=150, y=150)
                Button(rootd, text="Knowledge", bg="turquoise4", fg="white", font="Verdana 14", height=2, width=10,
                       command=lambda: [rootd.destroy(), knowpython()]).place(x=300, y=200)
                Button(rootd, text="Exam", bg="turquoise4", fg="white", font="Verdana 14", height=2, width=10,
                       command=lambda: [rootd.destroy(), exaampython()]).place(x=300, y=300)
                Button(rootd, text="Home", bg="steelblue", justify="l", fg="white", font="Verdana 12 ", height=2,
                       width=8,
                       command=rootd.destroy).place(x=700, y=400)
                rootd.mainloop()

            rootb = Tk()
            rootb.configure(bg="light blue")
            rootb.title("College Connect")
            """b = "image.jpeg"
            imgb = Image.open(b)
            imgb = imgb.resize((800, 800), Image.ANTIALIAS)
            imgb = ImageTk.PhotoImage(imgb)
            panelb = Label(rootb, image=imgb)
            panelb.image = imgb
            panelb.pack(anchor=W)"""
            rootb.geometry("800x500+0+0")
            Label(rootb, text="Book Recommendation",
                  font="Algerian 20 underline", bg="light blue").place(x=210, y=75)
            Label(rootb, text="Choose your subject",
                  font="Algerian 15 underline", bg="light blue").place(x=275, y=150)
            Button(rootb, text="Python", bg="turquoise4", fg="white", font="Verdana 14", height=2, width=10,
                   command=lambda: [rootb.destroy(), python()]).place(x=300, y=200)
            Button(rootb, text="OS", bg="turquoise4", fg="white", font="Verdana 14", height=2, width=10, ).place(x=300,
                                                                                                                 y=300)
            Button(rootb, text="Home", bg="steelblue", justify="l", fg="white", font="Verdana 12 ", height=2, width=8,
                   command=rootb.destroy).place(x=700, y=400)
            rootb.mainloop()

        brsroot = Tk()
        brsroot.configure(bg="light blue")
        brsroot.title("College Connect")
        brsroot.geometry("800x500+0+0")
        """b = "image.jpeg"
        imga = Image.open(b)
        imga = imga.resize((800, 800), Image.ANTIALIAS)
        imga = ImageTk.PhotoImage(imga)
        panela = Label(brsroot, image=imga)
        panela.image = imga
        panela.pack(anchor=W)"""
        Label(brsroot, text="College Connect", fg="teal",
              font="Algerian 30 underline", bg="light blue").place(x=200, y=25)
        Label(brsroot, text="Book Recommendation",
              font="Algerian 20 underline", bg="light blue").place(x=210, y=75)
        Label(brsroot, text="Choose your sem",
              font="Algerian 15 underline", bg="light blue").place(x=275, y=150)
        Button(text="Sem3", bg="turquoise4", fg="white", font="Verdana 14", height=2, width=10,
               command=lambda: [brsroot.destroy(), sem3()]).place(x=300, y=200)
        Button(text="Sem4", bg="turquoise4", fg="white", font="Verdana 14", height=2, width=10,
               command=lambda: [brsroot.destroy(), sem4()]).place(x=300, y=300)
        Button(brsroot, text="Home", bg="steelblue", justify="l", fg="white", font="Verdana 12 ", height=2, width=8,
               command=brsroot.destroy).place(x=700, y=400)
        brsroot.mainloop()

    def branch_select():
        def advance_search():

            mail_file = []

            def submitdisplayadv():
                maildone = mailid.get()

                if var1.get() == 1 and var7.get() == 1:
                    mail_file.append("comp_op_mu.html")
                    os.startfile("comp_op_mu.html")
                if var1.get() == 1 and var8.get() == 1:
                    mail_file.append("comp_op_pu.html")
                    os.startfile("comp_op_pu.html")
                if var1.get() == 1 and var9.get() == 1:
                    mail_file.append("comp_op_nag.html")
                    os.startfile("comp_op_nag.html")
                if var1.get() == 1 and var10.get() == 1:
                    mail_file.append("comp_op_nas.html")
                    os.startfile("comp_op_nas.html")
                if var1.get() == 1 and var11.get() == 1:
                    mail_file.append("comp_op_aug.html")
                    os.startfile("comp_op_aug.html")
                if var1.get() == 1 and var12.get() == 1:
                    mail_file.append("comp_op_amt.html")
                    os.startfile("comp_op_amt.html")
                if var2.get() == 1 and var7.get() == 1:
                    mail_file.append("IT_op_mu.html")
                    os.startfile("IT_op_mu.html")
                if var2.get() == 1 and var8.get() == 1:
                    mail_file.append("IT_op_pu.html")
                    os.startfile("IT_op_pu.html")
                if var2.get() == 1 and var9.get() == 1:
                    mail_file.append("IT_op_nag.html")
                    os.startfile("IT_op_nag.html")
                if var2.get() == 1 and var10.get() == 1:
                    mail_file.append("IT_op_nas.html")
                    os.startfile("IT_op_nas.html")
                if var2.get() == 1 and var11.get() == 1:
                    mail_file.append("IT_op_aug.html")
                    os.startfile("IT_op_aug.html")
                if var2.get() == 1 and var12.get() == 1:
                    mail_file.append("IT_op_amt.html")
                    os.startfile("IT_op_amt.html")
                if var3.get() == 1 and var7.get() == 1:
                    mail_file.append("Extc_op_mu.html")
                    os.startfile("Extc_op_mu.html")
                if var3.get() == 1 and var8.get() == 1:
                    mail_file.append("Extc_op_pu.html")
                    os.startfile("Extc_op_pu.html")
                if var3.get() == 1 and var9.get():
                    mail_file.append("Extc_op_nag.html")
                    os.startfile("Extc_op_nag.html")
                if var3.get() == 1 and var10.get():
                    mail_file.append("Extc_op_nas.html")
                    os.startfile("Extc_op_nas.html")
                if var3.get() == 1 and var11.get():
                    mail_file.append("Extc_op_mug.html")
                    os.startfile("EXTC_op_mug.html")
                if var3.get() == 1 and var12.get():
                    mail_file.append("Extc_op_amt.html")
                    os.startfile("Extc_op_amt.html")
                if var4.get() == 1 and var7.get() == 1:
                    mail_file.append("civil_op_mu.html")
                    os.startfile("civil_op_mu.html")
                if var4.get() == 1 and var8.get() == 1:
                    mail_file.append("civil_op_pu.html")
                    os.startfile("civil_op_pu.html")
                if var4.get() == 1 and var9.get():
                    mail_file.append("civil_op_nag.html")
                    os.startfile("civil_op_nag.html")
                if var4.get() == 1 and var10.get():
                    mail_file.append("civil_op_nas.html")
                    os.startfile("civil_op_nas.html")
                if var4.get() == 1 and var11.get():
                    mail_file.append("civil_op_aug.html")
                    os.startfile("civil_op_aug.html")
                if var4.get() == 1 and var12.get():
                    mail_file.append("civil_op_amt.html")
                    os.startfile("civil_op_amt.html")
                if var5.get() == 1 and var7.get() == 1:
                    mail_file.append("mech_op_mu.html")
                    os.startfile("mech_op_mu.html")
                if var5.get() == 1 and var8.get() == 1:
                    mail_file.append("mech_op_pu.html")
                    os.startfile("mech_op_pu.html")
                if var5.get() == 1 and var9.get():
                    mail_file.append("mech_op_nag.html")
                    os.startfile("mech_op_nag.html")
                if var5.get() == 1 and var10.get():
                    mail_file.append("mech_op_nas.html")
                    os.startfile("mech_op_nas.html")
                if var5.get() == 1 and var11.get():
                    mail_file.append("mech_op_aug.html")
                    os.startfile("mech_op_aug.html")
                if var5.get() == 1 and var12.get():
                    mail_file.append("mech_op_amt.html")
                    os.startfile("mech_op_amt.html")
                if var6.get() == 1:
                    if re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', maildone):
                        maildisplayadv()
                    else:
                        mb.showerror(
                            "Error", "Enter a valid Email Id to receive a mail.")

            def maildisplayadv():
                Sender = "collegeconnectcrsbrs@gmail.com"
                Reciever = mailid.get()
                Password = "crs2020#"
                Message = EmailMessage()
                Message['Subject'] = "Cutoff lists of your desired branches"
                Message['From'] = Sender
                Message['To'] = Reciever
                Message.set_content('Hello, Welcome to College Connect\n'
                                    'We have attached all colleges list according to branches of your choice.\n'
                                    'This is system generated mail,Do not reply.')

                files = mail_file

                for file in files:
                    with open(file, 'rb') as f:
                        filea = f.read()
                        fileb = f.name
                    Message.add_attachment(
                        filea, maintype='application', subtype='octet-stream', filename=fileb)

                try:
                    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                    smtp_server.ehlo()
                    smtp_server.login(Sender, Password)
                    smtp_server.sendmail(Sender, Reciever, Message.as_string())
                    smtp_server.close()
                    print ("Email sent successfully!")
                except Exception as ex:
                    print ("Something went wrong….",ex)   
                mail_file.clear()

            advroot = Tk()
            advroot.geometry('%dx%d+0+0' % (wi, he))
            advroot.config(bg="light blue")
            var1 = IntVar()
            var2 = IntVar()
            var3 = IntVar()
            var4 = IntVar()
            var5 = IntVar()
            var6 = IntVar()
            var7 = IntVar()
            var8 = IntVar()
            var9 = IntVar()
            var10 = IntVar()
            var11 = IntVar()
            var12 = IntVar()

            Checkbutton(advroot, text='Mumbai', font="Verdana 12 bold", height=3, width=10, bg="teal",
                        variable=var7, onvalue=1,
                        offvalue=0).place(x=500, y=25)
            Checkbutton(advroot, text='Pune', font="Verdana 12 bold", height=3, width=10, bg="teal",
                        variable=var8, onvalue=1,
                        offvalue=0).place(x=500, y=100)
            Checkbutton(advroot, text='Nagpur', font="Verdana 12 bold", height=3, width=10, bg="teal",
                        variable=var9, onvalue=1,
                        offvalue=0).place(x=500, y=175)
            Checkbutton(advroot, text='Nashik', font="Verdana 12 bold", height=3, width=10, bg="teal",
                        variable=var10, onvalue=1,
                        offvalue=0).place(x=500, y=250)
            Checkbutton(advroot, text='Aurangabad', font="Verdana 12 bold", height=3, width=10, bg="teal",
                        variable=var11, onvalue=1,
                        offvalue=0).place(x=500, y=325)
            Checkbutton(advroot, text='Amravati', font="Verdana 12 bold", height=3, width=10, bg="teal",
                        variable=var12, onvalue=1,
                        offvalue=0).place(x=500, y=400)

            compb = Checkbutton(advroot, text='Computer', font="Verdana 12 bold", height=3, width=10, bg="teal",
                                variable=var1, onvalue=1,
                                offvalue=0).place(x=700, y=25)
            itb = Checkbutton(advroot, text='IT', variable=var2, height=3, font="Verdana 12 bold", width=10, bg="teal",
                              onvalue=1,
                              offvalue=0).place(x=700, y=100)
            extcb = Checkbutton(advroot, text='EXTC', variable=var3, font="Verdana 12 bold", height=3, width=10,
                                bg="teal",
                                onvalue=1,
                                offvalue=0).place(x=700, y=175)
            civilb = Checkbutton(advroot, text='Civil', variable=var4, font="Verdana 12 bold", height=3, width=10,
                                 bg="teal",
                                 onvalue=1,
                                 offvalue=0).place(x=700, y=250)
            mechb = Checkbutton(advroot, text='Mechanical', variable=var5, font="Verdana 12 bold", height=3, width=10,
                                bg="teal",
                                onvalue=1,
                                offvalue=0).place(x=700, y=325)
            mailid = Entry(advroot)
            mailid.place(x=610, y=500, height=30, width=300)
            mailme = Checkbutton(advroot, text='Mail me all my advroot files', height=2, width=30,
                                 font="Verdana 12 bold",
                                 bg="teal",
                                 variable=var6, onvalue=1, offvalue=0).place(x=510, y=550)
            Label(advroot, font="Verdana 14 ", text="Email ID",
                  bg="teal", fg="white").place(x=500, y=500)

            submitd = Button(advroot, text="Submit", font="Verdana 12 bold", height=3, width=15, bg="teal",
                             fg="white", command=submitdisplayadv).place(
                x=600, y=620)

            c = "assets//college4.jpg"
            imga = Image.open(c)
            imga = imga.resize(
                (round(500 * he / 864), round(400 * wi / 1536)), Image.ANTIALIAS)
            imga = ImageTk.PhotoImage(imga)
            panela = Label(advroot, image=imga)
            panela.image = imga
            panela.place(x=0)

            d = "assets//colleges5.jpg"
            imgb = Image.open(d)
            imgb = imgb.resize(
                (round(500 * he / 864), round(400 * wi / 1536)), Image.ANTIALIAS)
            imgb = ImageTk.PhotoImage(imgb)
            panelb = Label(advroot, image=imgb, compound="center")
            panelb.image = imgb
            panelb.place(x=0 * wi / 1536, y=400 * he / 864)

            e = "assets//college7.jpeg"
            imgc = Image.open(e)
            imgc = imgc.resize((550, 400), Image.ANTIALIAS)
            imgc = ImageTk.PhotoImage(imgc)
            panelc = Label(advroot, image=imgc)
            panelc.image = imgc
            panelc.place(x=1000 * wi / 1536)

            f = "assets//college6.jpeg"
            imgd = Image.open(f)
            imgd = imgd.resize((550, 400), Image.ANTIALIAS)
            imgd = ImageTk.PhotoImage(imgd)
            paneld = Label(advroot, image=imgd)
            paneld.image = imgd
            paneld.place(x=1000 * wi / 1536, y=400 * he / 864)

            home = Button(advroot, text="Home", bg="lightsteelblue", font=f"Verdana {round(15 * wi / 1536)} ",
                        compound="center", command=lambda: [advroot.destroy(), main()]).place(x=10 * wi / 1536,
                                                                                            y=725 * he / 864)
            back = Button(advroot, text="Back", bg="lightsteelblue", font=f"Verdana {round(15 * wi / 1536)} ",
                        compound="center", command=lambda: [advroot.destroy(), fgh()]).place(x=1425 * wi / 1536,
                                                                                          y=725 * he / 864)

            advroot.mainloop()
        mail_file = []

        def submitdisplay():
            maildone = mailid.get()

            if var1.get() == 1:
                mail_file.append("comp_op.html")
                compdisplay()
            if var2.get() == 1:
                mail_file.append("it_op.html")
                itdisplay()
            if var3.get() == 1:
                mail_file.append("EXTC_op.html")
                extcdisplay()
            if var4.get() == 1:
                mail_file.append("civil_op.html")
                civildisplay()
            if var5.get() == 1:
                mail_file.append("mech_op.html")
                mechdisplay()
            if var6.get() == 1:
                if re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', maildone):
                    maildisplay()
                else:
                    mb.showerror(
                        "Error", "Enter a valid Email Id to receive a mail.")

        def compdisplay():
            os.startfile("comp_op.html")

        def itdisplay():
            os.startfile("IT_op.html")

        def extcdisplay():
            os.startfile("EXTC_op.html")

        def civildisplay():
            os.startfile("civil_op.html")

        def mechdisplay():
            os.startfile("mech_op.html")

        def maildisplay():
            Sender = "collegeconnectcrsbrs@gmail.com"
            Reciever = mailid.get()
            Password = "crs2020#"
            Message = EmailMessage()
            Message['Subject'] = "Cutoff lists of your desired branches"
            Message['From'] = Sender
            Message['To'] = Reciever
            Message.set_content('Hello,Welcome to College Connect\n'
                                'We have attached all colleges list according to branches of your choice.\n'
                                'This is system generated mail,Do not reply.')

            files = mail_file

            for file in files:
                with open(file, 'rb') as f:
                    filea = f.read()
                    fileb = f.name
                Message.add_attachment(
                    filea, maintype='application', subtype='octet-stream', filename=fileb)

            try:
                smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                smtp_server.ehlo()
                smtp_server.login(Sender, Password)
                smtp_server.sendmail(Sender, Reciever, Message.as_string())
                smtp_server.close()
                print ("Email sent successfully!")
            except Exception as ex:
                print ("Something went wrong….",ex)   
            mail_file.clear()

        branch = Tk()
        wi, he = branch.winfo_screenwidth(), branch.winfo_screenheight()
        branch.geometry('%dx%d+0+0' % (wi, he))
        branch.config(bg="light blue")
        var1 = IntVar()
        var2 = IntVar()
        var3 = IntVar()
        var4 = IntVar()
        var5 = IntVar()
        var6 = IntVar()

        compb = Checkbutton(branch, text='Computer', font=f"Verdana {round(12 * wi / 1536)} bold",
                            height=round(3 * wi / 1536), width=round(10 * wi / 1536), bg="teal",
                            variable=var1, onvalue=1,
                            offvalue=0).place(x=700 * wi / 1536, y=25 * he / 864)
        itb = Checkbutton(branch, text='IT', variable=var2, height=round(3 * wi / 1536),
                          font=f"Verdana {round(12 * wi / 1536)} bold", width=round(10 * wi / 1536), bg="teal",
                          onvalue=1,
                          offvalue=0).place(x=700 * wi / 1536, y=100 * he / 864)
        extcb = Checkbutton(branch, text='EXTC', variable=var3, font=f"Verdana {round(12 * wi / 1536)} bold",
                            height=round(3 * wi / 1536), width=round(10 * wi / 1536), bg="teal",
                            onvalue=1,
                            offvalue=0).place(x=700 * wi / 1536, y=175 * he / 864)
        civilb = Checkbutton(branch, text='Civil', variable=var4, font=f"Verdana {round(12 * wi / 1536)} bold",
                             height=round(3 * wi / 1536), width=round(10 * wi / 1536), bg="teal",
                             onvalue=1,
                             offvalue=0).place(x=700 * wi / 1536, y=250 * he / 864)
        mechb = Checkbutton(branch, text='Mechanical', variable=var5, font=f"Verdana {round(12 * wi / 1536)} bold",
                            height=round(3 * wi / 1536), width=round(10 * wi / 1536),
                            bg="teal",
                            onvalue=1,
                            offvalue=0).place(x=700 * wi / 1536, y=325 * he / 864)
        mailid = Entry(branch)
        mailid.place(x=650 * wi / 1536, y=425 * he / 864,
                     height=round(30 * wi / 1536), width=round(300 * wi / 1536))
        mailme = Checkbutton(branch, text='Mail me all my branch files', height=round(2 * wi / 1536),
                             width=round(30 * wi / 1536), font=f"Verdana {round(12 * wi / 1536)} bold",
                             bg="teal",
                             variable=var6, onvalue=1, offvalue=0).place(x=590 * wi / 1536, y=500 * he / 864)
        Label(branch, font=f"Verdana {round(14 * wi / 1536)} ", text="Email ID", bg="teal", fg="white").place(
            x=550 * wi / 1536, y=425 * he / 864)

        submitd = Button(branch, text="Submit", font=f"Verdana {round(12 * wi / 1536)} bold",
                         height=round(3 * wi / 1536), width=round(15 * wi / 1536), bg="teal",
                         fg="white", command=submitdisplay).place(
            x=680 * wi / 1536, y=600 * he / 864)
        advsearch = Button(branch, text="Advanced search", font=f"Verdana {round(12 * wi / 1536)} bold",
                           height=round(3 * wi / 1536), width=round(15 * wi / 1536), bg="teal",
                           fg="white", command=lambda: [branch.destroy(), advance_search()]).place(x=680 * wi / 1536, y=700 * he / 864)

        c = "assets//college4.jpg"
        imga = Image.open(c)
        imga = imga.resize(
            (round(500 * he / 864), round(400 * wi / 1536)), Image.ANTIALIAS)
        imga = ImageTk.PhotoImage(imga)
        panela = Label(branch, image=imga)
        panela.image = imga
        panela.place(x=0)

        d = "assets//colleges5.jpg"
        imgb = Image.open(d)
        imgb = imgb.resize(
            (round(500 * he / 864), round(400 * wi / 1536)), Image.ANTIALIAS)
        imgb = ImageTk.PhotoImage(imgb)
        panelb = Label(branch, image=imgb, compound="center")
        panelb.image = imgb
        panelb.place(x=0 * wi / 1536, y=400 * he / 864)

        e = "assets//college7.jpeg"
        imgc = Image.open(e)
        imgc = imgc.resize((550, 400), Image.ANTIALIAS)
        imgc = ImageTk.PhotoImage(imgc)
        panelc = Label(branch, image=imgc)
        panelc.image = imgc
        panelc.place(x=1000 * wi / 1536)

        f = "assets//college6.jpeg"
        imgd = Image.open(f)
        imgd = imgd.resize((550, 400), Image.ANTIALIAS)
        imgd = ImageTk.PhotoImage(imgd)
        paneld = Label(branch, image=imgd)
        paneld.image = imgd
        paneld.place(x=1000 * wi / 1536, y=400 * he / 864)

        home = Button(branch, text="Home", bg="lightsteelblue", font=f"Verdana {round(15 * wi / 1536)} ",
                      compound="center", command=lambda: [branch.destroy(), main()]).place(x=10 * wi / 1536,
                                                                                           y=725 * he / 864)
        back = Button(branch, text="Back", bg="lightsteelblue", font=f"Verdana {round(15 * wi / 1536)} ",
                      compound="center", command=lambda: [branch.destroy(), fgh()]).place(x=1425 * wi / 1536,
                                                                                          y=725 * he / 864)

        branch.mainloop()

    def fgh():

        choice = tk.Tk()
        choice.configure(bg="light blue")
        choice.title("College Connect")
        choice.geometry('%dx%d+0+0' % (wi, he))

        c = "assets//college1.jpeg"
        imga = Image.open(c)
        imga = imga.resize(
            (round(500 * he / 864), round(400 * wi / 1536)), Image.ANTIALIAS)
        imga = ImageTk.PhotoImage(imga)
        panela = Label(choice, image=imga)
        panela.image = imga
        panela.place(x=0)

        d = "assets//vesit3.jpeg"
        imgb = Image.open(d)
        imgb = imgb.resize(
            (round(500 * he / 864), round(400 * wi / 1536)), Image.ANTIALIAS)
        imgb = ImageTk.PhotoImage(imgb)
        panelb = Label(choice, image=imgb, compound="center")
        panelb.image = imgb
        panelb.place(x=500 * wi / 1536)

        e = "assets//college2.jpeg"
        imgc = Image.open(e)
        imgc = imgc.resize(
            (round(550 * he / 864), round(400 * wi / 1536)), Image.ANTIALIAS)
        imgc = ImageTk.PhotoImage(imgc)
        panelc = Label(choice, image=imgc)
        panelc.image = imgc
        panelc.place(x=1000 * wi / 1536)

        Label(choice, text="     Confused about which branch to choose for Enginnering,       \n"
                           "     Take Aptitude Test!!", font=f"Verdana {round(14 * wi / 1536)} bold", bg="teal",
              fg="white",
              justify=LEFT).place(x=0 * wi / 1536, y=425 * he / 864)
        lab = Label(choice, text="Choosing the right branch will take you towards your career goals.Have you thought\n"
                                 "about your branch? It is not a wise idea to proceed for the Best Engineering College\n"
                                 "choice without choosing your stream. Most of the people make it an easy task and\n"
                                 "later after a semester or a year,feel regret about it.The Engineering Branch Selector\n"
                                 "Test is a psychometric tool designed exclusively for helping students to ease down \n"
                                 "their engineering branch selection.With this report you will get an answer to which\n"
                                 "branch you can opt for.It assists your work interest with certain real life situation\n"
                                 "as per different Branches of engineering.", font=f"Verdana {round(12 * wi / 1536)} ",
                    bg="light blue",
                    justify=LEFT).place(x=25 * wi / 1536, y=500 * he / 864)
        aptitudeb = Button(choice, text="Take aptitude test", font=f"Verdana {round(12 * wi / 1536)} bold", fg="white",
                           bg="teal", height=round(3 * wi / 1536),
                           command=lambda: [choice.destroy(), choice_select()]).place(x=300 * wi / 1536,
                                                                                      y=700 * he / 864)
        Label(choice, text="     Sure about field but don't know which College to                            \n"
                           "     choose according to your scores", font=f"Verdana {round(14 * wi / 1536)} bold",
              bg="teal", fg="white",
              justify=LEFT).place(x=825 * wi / 1536, y=425 * he / 864)
        Label(choice, text="A choice, of course, is completely based on the abilities and the interest of\n"
                           "an individual towards that subject. If have decided your branch but confused\n"
                           "between two colleges. In such a case, a well-established college can be the best\n"
                           "choice. Here, Recognition plays an important role because it defines the quality\n"
                           "of faculty along with their experiences.We provide you the list of colleges you\n"
                           "can opt for based on your scores and your preferred branch.", bg="light blue",
              font=f"Verdana {round(12 * wi / 1536)} ", justify=LEFT).place(x=825 * wi / 1536, y=500 * he / 864)
        branchb = Button(choice, text="Recommended Colleges\n"
                                      "for you", font=f"Verdana {round(12 * wi / 1536)} bold", fg="white", bg="teal",
                         height=round(3 * wi / 1536),
                         command=lambda: [choice.destroy(), branch_select()]).place(x=1025 * wi / 1536,
                                                                                    y=700 * he / 864)
        home = Button(choice, text="Home", bg="turquoise4", fg="white", font=f"Verdana {round(15 * wi / 1536)} ",
                      compound="center", command=lambda: [choice.destroy(), main()]).place(x=10 * wi / 1536,
                                                                                           y=725 * he / 864)
        back = Button(choice, text="Back", bg="turquoise4", fg="white", font=f"Verdana {round(15 * wi / 1536)} ",
                      compound="center", command=lambda: [choice.destroy(), crs()]).place(x=1425 * wi / 1536,
                                                                                          y=725 * he / 864)
        choice.mainloop()

    def choice_select():

        def chosen():

            scores = {"Computer": 0, "IT": 0, "Extc": 0, "Mech": 0, "Civil": 0}

            if var.get() == 1:
                scores["Computer"] += 1
            if var.get() == 2:
                scores["Mech"] += 1
            if var.get() == 3:
                scores["IT"] += 1
            if var.get() == 4:
                scores["Extc"] += 1
            if var.get() == 5:
                scores["Civil"] += 1

            # Q.2
            if var2.get() == 5:
                scores["Computer"] += 1
            if var2.get() == 1:
                scores["Mech"] += 1
            if var2.get() == 4:
                scores["IT"] += 1
            if var2.get() == 3:
                scores["Extc"] += 1
            if var2.get() == 2:
                scores["Civil"] += 1

            # Q.3
            if var3.get() == 3:
                scores["Computer"] += 1
            if var3.get() == 2:
                scores["Mech"] += 1
            if var3.get() == 4:
                scores["IT"] += 1
            if var3.get() == 1:
                scores["Extc"] += 1
            if var3.get() == 5:
                scores["Civil"] += 1

            # Q.4
            if var4.get() == 2:
                scores["Extc"] += 1

            # Q.5
            if var5.get() == 3:
                scores["Mech"] += 1

            # Q.6
            if var6.get() == 1:
                scores["Civil"] += 1

            # Q.7
            if var7.get() == 1:
                scores["Computer"] += 1

            # Q.9
            if var9.get() == 2:
                scores["Extc"] += 1

            # Q.11
            if var11.get() == 1:
                scores["Mech"] += 1

            # Q.12
            if var12.get() == 3:
                scores["Civil"] += 1

            # Q.13
            if var13.get() == 1:
                scores["IT"] += 1

            # Q.14
            if var14.get() == 1:
                scores["Extc"] += 1
            # Q.17
            if var17.get() == 3:
                scores["Mech"] += 1

            # Q.20
            if var20.get() == 1:
                scores["Civil"] += 1

            # scores = {"Computer": 0, "IT": 0, "Mech": 0, "Extc": 0, "Civil": 0}
            scoredi = sorted(scores.items(), key=lambda x: x[1], reverse=True)
            scores = dict(scoredi)
            print(scores)
            maxs = list(scores)
            f = maxs[0]
            dd = scores[f]
            print(dd)
            val = list(scores.values())
            ke = list(scores.keys())
            val = [x for x in val if x == dd]

            print(val)
            l = len(val)
            prefer = ke[:l]
            gh = ",".join([str(i) for i in prefer])

            fooCRS = tk.Tk()
            fooCRS.config(bg="steelblue")
            fooCRS.title("College Connect")
            fooCRS.geometry("%dx%d+0+0" % (wi, he))
            Button(fooCRS, text="Close", command=fooCRS.destroy).place(x=600, y=300)
            figure2 = Figure(figsize=(4, 3), dpi=175)
            figure2.patch.set_facecolor('steelblue')

            subplot2 = figure2.add_subplot(111)
            labels2 = 'Computers', 'IT', 'Mechanical', "EXTC", 'Civil'
            pieSizes = [scores["Computer"], scores["IT"],
                        scores["Mech"], scores["Extc"], scores["Civil"]]
            my_colors2 = ['lightblue', 'lightsteelblue',
                          'silver', 'teal', 'pink']
            explode2 = (0, 0, 0, 0, 0)
            subplot2.pie(pieSizes, colors=my_colors2, explode=explode2, labels=labels2, autopct='%1.1f%%', shadow=True,
                         startangle=90)
            subplot2.axis('equal')
            pie2 = FigureCanvasTkAgg(figure2, fooCRS)
            pie2.get_tk_widget().pack(anchor=NW)

            Label(fooCRS, text="Branches are recommended in following order based on your aptitude test",
                  font="Verdana 12 bold").place(x=10, y=525)
            Label(fooCRS, text="1. " + ke[0], font="verdana 12",
                  bg="lightsteelblue", width=25).place(x=15, y=560)
            Label(fooCRS, text="2. " + ke[1], font="verdana 12",
                  bg="lightsteelblue", width=25).place(x=350, y=560)
            Label(fooCRS, text="3. " + ke[2], font="verdana 12",
                  bg="lightsteelblue", width=25).place(x=15, y=600)
            Label(fooCRS, text="4. " + ke[3], font="verdana 12",
                  bg="lightsteelblue", width=25).place(x=350, y=600)
            Label(fooCRS, text="5. " + ke[4], font="verdana 12",
                  bg="lightsteelblue", width=25).place(x=175, y=640)

            Label(fooCRS, text="Some pros for the branches are mentioned below\n",
                  bg="steel blue", fg="white", font="Verdana 12 bold", justify="l").place(x=700, y=25)
            Label(fooCRS, text="Computer branch is really a great choice.As we all know , world is getting\n"
                  "digital and shifted to technology creating ample amount of opportunities.\n"
                  "This branch is in most demand nowadays.This field has so much to explore.",
                  bg="steel blue",
                  fg="white", font="Verdana 12", justify="l").place(x=700, y=100)
            Label(fooCRS, text="IT branch is really a great choice.As we all know , world is getting\n"
                  "digital and shifted to technology creating ample amount of opportunities.\n"
                  "This branch is in most demand nowadays.This field has so much to explore.",
                  bg="steel blue",
                  fg="white", font="Verdana 12", justify="l").place(x=700, y=200)
            Label(fooCRS, text="Extc branch is really a great choice.As we all know , world is getting\n"
                  "digital and shifted to technology creating ample amount of opportunities.\n"
                  "This branch is in most demand nowadays.This field has so much to explore.",
                  bg="steel blue",
                  fg="white", font="Verdana 12", justify="l").place(x=700, y=300)
            Label(fooCRS, text="Mech branch is really a great choice.As we all know , world is getting\n"
                  "digital and shifted to technology creating ample amount of opportunities.\n"
                  "This branch is in most demand nowadays.This field has so much to explore.",
                  bg="steel blue",
                  fg="white", font="Verdana 12", justify="l").place(x=700, y=400)
            Label(fooCRS, text="Civil branch is really a great choice.As we all know , world is getting\n"
                  "digital and shifted to technology creating ample amount of opportunities.\n"
                  "This branch is in most demand nowadays.This field has so much to explore.",
                  bg="steel blue",
                  fg="white", font="Verdana 12", justify="l").place(x=700, y=500)
            Button(fooCRS, text="Proceed for \n"
                   "College list", bg="lightsteelblue", font="Verdana 12 bold", height=3, width=15,
                   command=lambda: [fooCRS.destroy(), branch_select()]).place(x=950,
                                                                             y=600)

            fooCRS.mainloop()

            """scores.append(scores[2)
            scores.append(scores[1)
            scores.append(comp)
            scores.append   scores[4)
            scores.append(scores[3)
            print(mech2,civil2,comp2)"""

        def scroll(event):

            canvas.configure(scrollregion=canvas.bbox('all'))

        special = tk.Tk()
        special.geometry('%dx%d+0+0' % (wi, he))
        special.config(bg="steelblue")

        # --- create canvas with scrollbar ---

        canvas = tk.Canvas(special, width=1300*wi/1536, height=800*he/864)
        canvas.pack()

        scrollbar = tk.Scrollbar(special, command=canvas.yview)
        scrollbar.place(x=1170*wi/1536, height=800*he/864)

        canvas.configure(yscrollcommand=scrollbar.set)

        # update scrollregion after starting 'mainloop'
        # when all widgets are in canvas
        canvas.bind('<Configure>', scroll)

        apti = tk.Frame(canvas)
        canvas.create_window((0, 0), window=apti, anchor=W)
        canvas.config(bg="yellow")
        canvas.place(height=800*he/864, width=800*wi/1536, x=370*wi/1536)
        apti.configure(bg="lightsteelblue")
        Label(apti, text="\nChoose one option from following questions.", bg="lightsteelblue", font=f"Algerian {round(16*wi/1536)}").pack(
            anchor=CENTER)
        Label(apti, text="\n", bg="lightsteelblue").pack()
        Label(apti, text="Q.1 Which of the following fascinates you the most?", bg="lightsteelblue",
              font=f"Verdana {round(15*wi/1536)} bold").pack(anchor=W)
        var = IntVar()
        R1 = Radiobutton(apti, text="How does an app work?", variable=var,
                         value=1, bg="lightsteelblue", font=f"Verdana {round(12*wi/1536)}")
        R1.pack(anchor=W)

        R2 = Radiobutton(apti, text="Can diesel car run on petrol?", variable=var, value=2, bg="lightsteelblue",
                         font=f"Verdana {round(12*wi/1536)}")
        R2.pack(anchor=W)

        R3 = Radiobutton(apti, text="How can someone get hacked?", variable=var, value=3, bg="lightsteelblue",
                         font=f"Verdana {round(12*wi/1536)}")
        R3.pack(anchor=W)

        R4 = Radiobutton(apti, text="How can I charge my mobile fast", variable=var, value=4, bg="lightsteelblue",
                         font=f"Verdana {round(12*wi/1536)}")
        R4.pack(anchor=W)

        R5 = Radiobutton(apti, text="3D Printed Houses", variable=var,
                         value=5, bg="lightsteelblue", font=f"Verdana {round(12*wi/1536)}")
        R5.pack(anchor=W)
        Label(apti, text="\n", bg="lightsteelblue").pack()
        # q.2

        Label(apti, text="Q.2 What would you like to develop", bg="lightsteelblue",
              font=f"Verdana {round(12*wi/1536)} bold").pack(anchor=W)
        var2 = IntVar()
        R6 = Radiobutton(apti, text="Cars running on hydrogen", variable=var2, value=1, bg="lightsteelblue",
                         font=f"Verdana {round(12*wi/1536)}")
        R6.pack(anchor=W)

        R7 = Radiobutton(apti, text="Underwater houses", variable=var2,
                         value=2, bg="lightsteelblue", font=f"Verdana {round(12*wi/1536)}")
        R7.pack(anchor=W)

        R8 = Radiobutton(apti, text="Mobiles charging wirelessly", variable=var2, value=3, bg="lightsteelblue",
                         font=f"Verdana {round(12*wi/1536)}")
        R8.pack(anchor=W)

        R9 = Radiobutton(apti, text="Internet free for all", variable=var2,
                         value=4, bg="lightsteelblue", font=f"Verdana {round(12*wi/1536)}")
        R9.pack(anchor=W)

        R10 = Radiobutton(apti, text="Games running at 120fps", variable=var2, value=5, bg="lightsteelblue",
                          font=f"Verdana {round(12*wi/1536)}")
        R10.pack(anchor=W)

        Label(apti, text="\n", bg="lightsteelblue").pack()

        # q.3
        Label(apti, text="Q.3 Which of the following activity would you like to do the most?", bg="lightsteelblue",
              font=f"Verdana {round(12*wi/1536)} bold").pack(anchor=W)
        var3 = IntVar()
        R11 = Radiobutton(apti, text="Calculating Electric bill of your house", variable=var3, value=1, bg="lightsteelblue",
                          font=f"Verdana {round(12*wi/1536)}")
        R11.pack(anchor=W)

        R12 = Radiobutton(apti, text="Finding the average of a bike", variable=var3, value=2, bg="lightsteelblue",
                          font=f"Verdana {round(12*wi/1536)}")
        R12.pack(anchor=W)

        R13 = Radiobutton(apti, text="Solving a logical question", variable=var3, value=3, bg="lightsteelblue",
                          font=f"Verdana {round(12*wi/1536)}")
        R13.pack(anchor=W)

        R14 = Radiobutton(apti, text="To calculate range can my wifi cover", variable=var3, value=4, bg="lightsteelblue",
                          font=f"Verdana {round(12*wi/1536)}")
        R14.pack(anchor=W)

        R15 = Radiobutton(apti, text="Thinking how many bricks it take to build your room?", variable=var3, value=5,
                          bg="lightsteelblue", font=f"Verdana {round(12*wi/1536)}")
        R15.pack(anchor=W)

        Label(apti, text="\n", bg="lightsteelblue").pack()

        # Q.4
        Label(apti, text="Q.4 What will you do if your house mcb drops?", bg="lightsteelblue", font=f"Verdana {round(12*wi/1536)} bold").pack(
            anchor=W)
        var4 = IntVar()
        R16 = Radiobutton(apti, text="Call an electrician", variable=var4,
                          value=1, bg="lightsteelblue", font=f"Verdana {round(12*wi/1536)}")
        R16.pack(anchor=W)

        R17 = Radiobutton(apti, text="Try to find where short circuit took place", variable=var4, value=2,
                          bg="lightsteelblue",
                          font=f"Verdana {round(12*wi/1536)}")
        R17.pack(anchor=W)

        R18 = Radiobutton(apti, text="Turn the mcb on even if it drops all the time", variable=var4, value=3,
                          bg="lightsteelblue", font=f"Verdana {round(12*wi/1536)}")
        R18.pack(anchor=W)

        Label(apti, text="\n", bg="lightsteelblue").pack()

        # Q.5

        Label(apti, text="Q.5 What if your car breakdowns?", bg="lightsteelblue",
              font=f"Verdana {round(12*wi/1536)} bold").pack(anchor=W)
        var5 = IntVar()
        R19 = Radiobutton(apti, text="I would prefer to call mechanic", variable=var5, value=1, bg="lightsteelblue",
                          font=f"Verdana {round(12*wi/1536)}")
        R19.pack(anchor=W)

        R20 = Radiobutton(apti, text="I woulld do nothing ", variable=var5,
                          value=2, bg="lightsteelblue", font=f"Verdana {round(12*wi/1536)}")
        R20.pack(anchor=W)

        R21 = Radiobutton(apti, text="I will try to fix the car", variable=var5, value=3, bg="lightsteelblue",
                          font=f"Verdana {round(12*wi/1536)}")
        R21.pack(anchor=W)

        Label(apti, text="\n", bg="lightsteelblue").pack()

        # Q.6
        Label(apti, text="Q.6 Do you like to draw geometric designs?", bg="lightsteelblue", font=f"Verdana {round(12*wi/1536)} bold").pack(
            anchor=W)
        var6 = IntVar()
        R22 = Radiobutton(apti, text="Yes,I love to", variable=var6, value=1,
                          bg="lightsteelblue", font=f"Verdana {round(12*wi/1536)}")
        R22.pack(anchor=W)

        R23 = Radiobutton(apti, text="I may do it", variable=var6, value=2,
                          bg="lightsteelblue", font=f"Verdana {round(12*wi/1536)}")
        R23.pack(anchor=W)

        R24 = Radiobutton(apti, text="I dont like it", variable=var6, value=3,
                          bg="lightsteelblue", font=f"Verdana {round(12*wi/1536)}")
        R24.pack(anchor=W)

        Label(apti, text="\n", bg="lightsteelblue").pack()

        # Q.7

        Label(apti, text="Q.7 Do you know processor used in your mobile and laptop?", bg="lightsteelblue",
              font=f"Verdana {round(12*wi/1536)} bold").pack(anchor=W)
        var7 = IntVar()
        R25 = Radiobutton(apti, text="Yes", variable=var7, value=1,
                          bg="lightsteelblue", font=f"Verdana {round(12*wi/1536)}")
        R25.pack(anchor=W)

        R26 = Radiobutton(apti, text="No", variable=var7, value=2,
                          bg="lightsteelblue", font=f"Verdana {round(12*wi/1536)}")
        R26.pack(anchor=W)

        Label(apti, text="\n", bg="lightsteelblue").pack()

        # Q.9
        Label(apti, text="Q.9 Is earthing necessary for a mobile charger?", bg="lightsteelblue",
              font=f"Verdana {round(12*wi/1536)} bold").pack(
            anchor=W)
        var9 = IntVar()
        R27 = Radiobutton(apti, text="Yes", variable=var9, value=1,
                          bg="lightsteelblue", font=f"Verdana {round(12*wi/1536)}")
        R27.pack(anchor=W)

        R28 = Radiobutton(apti, text="No", variable=var9, value=2,
                          bg="lightsteelblue", font=f"Verdana {round(12*wi/1536)}")
        R28.pack(anchor=W)

        Label(apti, text="\n", bg="lightsteelblue").pack()
        # Q.11

        Label(apti, text="Q.11 What is most important when choosing a car?", bg="lightsteelblue",
              font=f"Verdana {round(12*wi/1536)} bold").pack(
            anchor=W)
        var11 = IntVar()
        R29 = Radiobutton(apti, text="Engine type(cc/torque)", variable=var11, value=1, bg="lightsteelblue",
                          font=f"Verdana {round(12*wi/1536)}")
        R29.pack(anchor=W)

        R30 = Radiobutton(apti, text="Body type of car", variable=var11,
                          value=2, bg="lightsteelblue", font=f"Verdana {round(12*wi/1536)}")
        R30.pack(anchor=W)

        R31 = Radiobutton(apti, text="Colour of the car", variable=var11,
                          value=3, bg="lightsteelblue", font=f"Verdana {round(12*wi/1536)}")
        R31.pack(anchor=W)

        R32 = Radiobutton(apti, text="mileage", variable=var11, value=4,
                          bg="lightsteelblue", font=f"Verdana {round(12*wi/1536)}")
        R32.pack(anchor=W)

        Label(apti, text="\n", bg="lightsteelblue").pack()

        # Q.12

        Label(apti, text="Q.12 Can a house have n number of floors?", bg="lightsteelblue", font=f"Verdana {round(12*wi/1536)} bold").pack(
            anchor=W)
        var12 = IntVar()
        R33 = Radiobutton(apti, text="Yes", variable=var12, value=1,
                          bg="lightsteelblue", font=f"Verdana {round(12*wi/1536)}")
        R33.pack(anchor=W)

        R34 = Radiobutton(apti, text="Maybe", variable=var12, value=2,
                          bg="lightsteelblue", font=f"Verdana {round(12*wi/1536)}")
        R34.pack(anchor=W)

        R35 = Radiobutton(apti, text="depends on the ground sand", variable=var12, value=3, bg="lightsteelblue",
                          font=f"Verdana {round(12*wi/1536)}")
        R35.pack(anchor=W)

        Label(apti, text="\n", bg="lightsteelblue").pack()

        # Q.13

        Label(apti, text="Q.13 Are you good in mathematics,logical ability and algorithms?", bg="lightsteelblue",
              font=f"Verdana {round(12*wi/1536)} bold").pack(anchor=W)
        var13 = IntVar()
        R36 = Radiobutton(apti, text="Yes", variable=var13, value=1,
                          bg="lightsteelblue", font=f"Verdana {round(12*wi/1536)}")
        R36.pack(anchor=W)

        R37 = Radiobutton(apti, text="No", variable=var13, value=2,
                          bg="lightsteelblue", font=f"Verdana {round(12*wi/1536)}")
        R37.pack(anchor=W)

        R38 = Radiobutton(apti, text="Somewhat", variable=var13, value=3,
                          bg="lightsteelblue", font=f"Verdana {round(12*wi/1536)}")
        R38.pack(anchor=W)

        Label(apti, text="\n", bg="lightsteelblue").pack()

        # Q.14
        Label(apti,
              text="Q.14 If my neutral wire breaks down can i use earthing wire for some emergency reasons \n"
                   "          till neutral wire gets fixed ?", bg="lightsteelblue", font=f"Verdana {round(12*wi/1536)} bold",
              justify=LEFT).pack(
            anchor=W)
        var14 = IntVar()
        R39 = Radiobutton(apti, text="Yes", variable=var14, value=1,
                          bg="lightsteelblue", font=f"Verdana {round(12*wi/1536)}")
        R39.pack(anchor=W)

        R40 = Radiobutton(apti, text="No", variable=var14, value=2,
                          bg="lightsteelblue", font=f"Verdana {round(12*wi/1536)}")
        R40.pack(anchor=W)
        R41 = Radiobutton(apti, text="I dont know neutral wire", variable=var14, value=3, bg="lightsteelblue",
                          font=f"Verdana {round(12*wi/1536)}")
        R41.pack(anchor=W)

        Label(apti, text="\n", bg="lightsteelblue").pack()

        # Q.17

        Label(apti, text="Q.17 What is most important in moving part of machines?", bg="lightsteelblue",
              font=f"Verdana {round(12*wi/1536)} bold").pack(anchor=W)
        var17 = IntVar()
        R42 = Radiobutton(apti, text="Cleaning the dust between them", variable=var17, value=1, bg="lightsteelblue",
                          font=f"Verdana {round(12*wi/1536)}")
        R42.pack(anchor=W)

        R43 = Radiobutton(apti, text="Washing them every week", variable=var17, value=2, bg="lightsteelblue",
                          font=f"Verdana {round(12*wi/1536)}")
        R43.pack(anchor=W)

        R44 = Radiobutton(apti, text="Lubricating them with oil", variable=var17, value=3, bg="lightsteelblue",
                          font=f"Verdana {round(12*wi/1536)}")
        R44.pack(anchor=W)

        R45 = Radiobutton(apti, text="None of the above", variable=var11,
                          value=4, bg="lightsteelblue", font=f"Verdana {round(12*wi/1536)}")
        R45.pack(anchor=W)

        Label(apti, text="\n", bg="lightsteelblue").pack()

        # Q.20

        Label(apti, text="Q.20 Do you like to study geography?", bg="lightsteelblue",
              font=f"Verdana {round(12*wi/1536)} bold").pack(anchor=W)
        var20 = IntVar()
        R46 = Radiobutton(apti, text="Yes", variable=var20, value=1,
                          bg="lightsteelblue", font=f"Verdana {round(12*wi/1536)}")
        R46.pack(anchor=W)

        R47 = Radiobutton(apti, text="Maybe", variable=var20, value=2,
                          bg="lightsteelblue", font=f"Verdana {round(12*wi/1536)}")
        R47.pack(anchor=W)

        R48 = Radiobutton(apti, text="Not at all", variable=var20, value=3,
                          bg="lightsteelblue", font=f"Verdana {round(12*wi/1536)}")
        R48.pack(anchor=W)

        submit = Button(apti, text="Submit", command=lambda: [special.destroy(), chosen()], bg="steelblue", fg="white",
                        font=f"Verdana {round(12*wi/1536)} bold", height=round(2*he/864), width=round(15*wi/1536))
        submit.pack(anchor=CENTER)

        Label(apti, text="\n", bg="lightsteelblue").pack()

        home = Button(special, text="Home", bg="lightsteelblue", font=f"Verdana {round(15*wi/1536)} ",
                      compound="center", command=lambda: [special.destroy(), main()]).place(x=10*wi/1536, y=725*he/864)
        back = Button(special, text="Back", bg="lightsteelblue", font=f"Verdana {round(15*wi/1536)} ",
                      compound="center", command=lambda: [special.destroy(), fgh()]).place(x=1425*wi/1536, y=725*he/864)

        special.mainloop()

    def crs():
        def vali():
            marks = percentile.get()
            nom = phone.get()
            naaa = name.get()
            try:
                a = float(marks)

                if a > 0 and a <= 100 and re.match(r'[789]\d{9}$', nom) and re.match(r'(?P<first>\w+)\W+(?P<last>\w+)',naaa):
                    rootzz = Tk()
                    rootzz.title("College Connect")
                    rootzz.geometry("300x70+650+250")
                    Label(rootzz, text="Lets Go").pack()
                    Button(rootzz, text="Procced",
                           command=lambda: [rootzz.destroy(),
                                            comp_code(), it_code(), extc_code(), civil_code(), mech_code(),
                                            comp_mu_code(), comp_pu_code(), comp_nag_code(),
                                            comp_nas_code(), comp_aug_code(), comp_amt_code(),
                                            it_mu_code(), it_pu_code(), it_nag_code(),
                                            it_nas_code(), it_aug_code(), it_amt_code(),
                                            extc_mu_code(), extc_pu_code(), extc_nag_code(),
                                            extc_nas_code(), extc_mug_code(), extc_amt_code(),
                                            mech_mu_code(), mech_pu_code(), mech_nag_code(),
                                            mech_nas_code(), mech_aug_code(), mech_amt_code(),
                                            civil_mu_code(), civil_pu_code(), civil_nag_code(),
                                            civil_nas_code(), civil_aug_code(), civil_amt_code(),
                                            info.destroy(), fgh()]).pack()
                    rootzz.mainloop()

                else:
                    mb.showerror(
                        "Wrong Input", "Please Enter valid information to proceed further.")
            except:
                mb.showerror(
                    "Wrong Input", "Please Enter a valid information to proceed further.")

        def comp_code():
            df = pd.read_excel('Computers2.xlsx')
            marks = percentile.get()
            z = df[df['Merit (Score)'] <= float(marks)]
            z.to_excel("comp_temp.xlsx", index=False)
            df1 = pd.read_excel("comp_temp.xlsx")
            df2 = df1.reset_index()
            df1['Sr.No.'] = df2.index + 1
            df1.to_excel("comp_temp.xlsx", index=False)
            writer = pd.ExcelWriter('comp_temp2.xlsx')
            df = pd.read_excel('comp_temp.xlsx')
            df.to_excel(writer, sheet_name='Sheet1', index=False, na_rep='NaN')

            for column in df:
                column_width = max(df[column].astype(
                    str).map(len).max(), len(column))
                col_idx = df.columns.get_loc(column)
                writer.sheets['Sheet1'].set_column(
                    col_idx, col_idx, column_width)

            writer.save()
            wb = pd.read_excel('comp_temp2.xlsx')
            wb.to_html('comp_op.html', index=False)

        def comp_mu_code():
            df = pd.read_excel('ComputersMumbai2.xlsx')
            marks = percentile.get()
            z = df[df['Merit (Score)'] <= float(marks)]
            z.to_excel("comp_temp_mu.xlsx", index=False)
            df1 = pd.read_excel("comp_temp_mu.xlsx")
            df2 = df1.reset_index()
            df1['Sr.No.'] = df2.index + 1
            df1.to_excel("comp_temp_mu.xlsx", index=False)
            writer = pd.ExcelWriter('comp_temp_mu2.xlsx')
            df = pd.read_excel('comp_temp_mu.xlsx')
            df.to_excel(writer, sheet_name='Sheet1', index=False, na_rep='NaN')

            for column in df:
                column_width = max(df[column].astype(
                    str).map(len).max(), len(column))
                col_idx = df.columns.get_loc(column)
                writer.sheets['Sheet1'].set_column(
                    col_idx, col_idx, column_width)

            writer.save()
            wb = pd.read_excel('comp_temp_mu2.xlsx')
            wb.to_html('comp_op_mu.html', index=False)

        def comp_pu_code():
            df = pd.read_excel('ComputersPune2.xlsx')
            marks = percentile.get()
            z = df[df['Merit (Score)'] <= float(marks)]
            z.to_excel("comp_temp_pu.xlsx", index=False)
            df1 = pd.read_excel("comp_temp_pu.xlsx")
            df2 = df1.reset_index()
            df1['Sr.No.'] = df2.index + 1
            df1.to_excel("comp_temp_pu.xlsx", index=False)
            writer = pd.ExcelWriter('comp_temp_pu2.xlsx')
            df = pd.read_excel('comp_temp_pu.xlsx')
            df.to_excel(writer, sheet_name='Sheet1', index=False, na_rep='NaN')

            for column in df:
                column_width = max(df[column].astype(
                    str).map(len).max(), len(column))
                col_idx = df.columns.get_loc(column)
                writer.sheets['Sheet1'].set_column(
                    col_idx, col_idx, column_width)

            writer.save()
            wb = pd.read_excel('comp_temp_pu2.xlsx')
            wb.to_html('comp_op_pu.html', index=False)

        def comp_nag_code():
            df = pd.read_excel('ComputersNagpur2.xlsx')
            marks = percentile.get()
            z = df[df['Merit (Score)'] <= float(marks)]
            z.to_excel("comp_temp_nag.xlsx", index=False)
            df1 = pd.read_excel("comp_temp_nag.xlsx")
            df2 = df1.reset_index()
            df1['Sr.No.'] = df2.index + 1
            df1.to_excel("comp_temp_nag.xlsx", index=False)
            writer = pd.ExcelWriter('comp_temp_nag2.xlsx')
            df = pd.read_excel('comp_temp_nag.xlsx')
            df.to_excel(writer, sheet_name='Sheet1', index=False, na_rep='NaN')

            for column in df:
                column_width = max(df[column].astype(
                    str).map(len).max(), len(column))
                col_idx = df.columns.get_loc(column)
                writer.sheets['Sheet1'].set_column(
                    col_idx, col_idx, column_width)

            writer.save()
            wb = pd.read_excel('comp_temp_nag2.xlsx')
            wb.to_html('comp_op_nag.html', index=False)

        def comp_nas_code():
            df = pd.read_excel('ComputersNashik2.xlsx')
            marks = percentile.get()
            z = df[df['Merit (Score)'] <= float(marks)]
            z.to_excel("comp_temp_nas.xlsx", index=False)
            df1 = pd.read_excel("comp_temp_nas.xlsx")
            df2 = df1.reset_index()
            df1['Sr.No.'] = df2.index + 1
            df1.to_excel("comp_temp_nas.xlsx", index=False)
            writer = pd.ExcelWriter('comp_temp_nas2.xlsx')
            df = pd.read_excel('comp_temp_nas.xlsx')
            df.to_excel(writer, sheet_name='Sheet1', index=False, na_rep='NaN')

            for column in df:
                column_width = max(df[column].astype(
                    str).map(len).max(), len(column))
                col_idx = df.columns.get_loc(column)
                writer.sheets['Sheet1'].set_column(
                    col_idx, col_idx, column_width)

            writer.save()
            wb = pd.read_excel('comp_temp_nas2.xlsx')
            wb.to_html('comp_op_nas.html', index=False)

        def comp_aug_code():
            df = pd.read_excel('ComputersAurangabad2.xlsx')
            marks = percentile.get()
            z = df[df['Merit (Score)'] <= float(marks)]
            z.to_excel("comp_temp_aug.xlsx", index=False)
            df1 = pd.read_excel("comp_temp_aug.xlsx")
            df2 = df1.reset_index()
            df1['Sr.No.'] = df2.index + 1
            df1.to_excel("comp_temp_aug.xlsx", index=False)
            writer = pd.ExcelWriter('comp_temp_aug2.xlsx')
            df = pd.read_excel('comp_temp_aug.xlsx')
            df.to_excel(writer, sheet_name='Sheet1', index=False, na_rep='NaN')

            for column in df:
                column_width = max(df[column].astype(
                    str).map(len).max(), len(column))
                col_idx = df.columns.get_loc(column)
                writer.sheets['Sheet1'].set_column(
                    col_idx, col_idx, column_width)

            writer.save()
            wb = pd.read_excel('comp_temp_aug2.xlsx')
            wb.to_html('comp_op_aug.html', index=False)

        def comp_amt_code():
            df = pd.read_excel('ComputersAmravati2.xlsx')
            marks = percentile.get()
            z = df[df['Merit (Score)'] <= float(marks)]
            z.to_excel("comp_temp_amt.xlsx", index=False)
            df1 = pd.read_excel("comp_temp_amt.xlsx")
            df2 = df1.reset_index()
            df1['Sr.No.'] = df2.index + 1
            df1.to_excel("comp_temp_amt.xlsx", index=False)
            writer = pd.ExcelWriter('comp_temp_amt2.xlsx')
            df = pd.read_excel('comp_temp_amt.xlsx')
            df.to_excel(writer, sheet_name='Sheet1', index=False, na_rep='NaN')

            for column in df:
                column_width = max(df[column].astype(
                    str).map(len).max(), len(column))
                col_idx = df.columns.get_loc(column)
                writer.sheets['Sheet1'].set_column(
                    col_idx, col_idx, column_width)

            writer.save()
            wb = pd.read_excel('comp_temp_amt2.xlsx')
            wb.to_html('comp_op_amt.html', index=False)

        def it_code():
            df = pd.read_excel('IT2.xlsx')
            marks = percentile.get()
            z = df[df['Merit (Score)'] <= float(marks)]
            z.to_excel("IT_temp.xlsx", index=False)
            df1 = pd.read_excel("IT_temp.xlsx")
            df2 = df1.reset_index()
            df1['Sr.No.'] = df2.index + 1
            df1.to_excel("IT_temp.xlsx", index=False)
            writer = pd.ExcelWriter('IT_temp2.xlsx')
            df = pd.read_excel('IT_temp.xlsx')
            df.to_excel(writer, sheet_name='Sheet1', index=False, na_rep='NaN')

            for column in df:
                column_width = max(df[column].astype(
                    str).map(len).max(), len(column))
                col_idx = df.columns.get_loc(column)
                writer.sheets['Sheet1'].set_column(
                    col_idx, col_idx, column_width)

            writer.save()
            wb = pd.read_excel('IT_temp2.xlsx')
            wb.to_html('IT_op.html', index=False)

        def it_mu_code():
            df = pd.read_excel('ITMumbai2.xlsx')
            marks = percentile.get()
            z = df[df['Merit (Score)'] <= float(marks)]
            z.to_excel("IT_temp_mu.xlsx", index=False)
            df1 = pd.read_excel("IT_temp_mu.xlsx")
            df2 = df1.reset_index()
            df1['Sr.No.'] = df2.index + 1
            df1.to_excel("IT_temp_mu.xlsx", index=False)
            writer = pd.ExcelWriter('IT_temp2_mu.xlsx')
            df = pd.read_excel('IT_temp_mu.xlsx')
            df.to_excel(writer, sheet_name='Sheet1', index=False, na_rep='NaN')

            for column in df:
                column_width = max(df[column].astype(
                    str).map(len).max(), len(column))
                col_idx = df.columns.get_loc(column)
                writer.sheets['Sheet1'].set_column(
                    col_idx, col_idx, column_width)

            writer.save()
            wb = pd.read_excel('IT_temp2_mu.xlsx')
            wb.to_html('IT_op_mu.html', index=False)

        def it_pu_code():
            df = pd.read_excel('ITPune2.xlsx')
            marks = percentile.get()
            z = df[df['Merit (Score)'] <= float(marks)]
            z.to_excel("IT_temp_pu.xlsx", index=False)
            df1 = pd.read_excel("IT_temp_pu.xlsx")
            df2 = df1.reset_index()
            df1['Sr.No.'] = df2.index + 1
            df1.to_excel("IT_temp_pu.xlsx", index=False)
            writer = pd.ExcelWriter('IT_temp2_pu.xlsx')
            df = pd.read_excel('IT_temp_pu.xlsx')
            df.to_excel(writer, sheet_name='Sheet1', index=False, na_rep='NaN')

            for column in df:
                column_width = max(df[column].astype(
                    str).map(len).max(), len(column))
                col_idx = df.columns.get_loc(column)
                writer.sheets['Sheet1'].set_column(
                    col_idx, col_idx, column_width)

            writer.save()
            wb = pd.read_excel('IT_temp2_pu.xlsx')
            wb.to_html('IT_op_pu.html', index=False)

        def it_nag_code():
            df = pd.read_excel('ITNagpur2.xlsx')
            marks = percentile.get()
            z = df[df['Merit (Score)'] <= float(marks)]
            z.to_excel("IT_temp_nag.xlsx", index=False)
            df1 = pd.read_excel("IT_temp_nag.xlsx")
            df2 = df1.reset_index()
            df1['Sr.No.'] = df2.index + 1
            df1.to_excel("IT_temp_nag.xlsx", index=False)
            writer = pd.ExcelWriter('IT_temp2_nag.xlsx')
            df = pd.read_excel('IT_temp_nag.xlsx')
            df.to_excel(writer, sheet_name='Sheet1', index=False, na_rep='NaN')

            for column in df:
                column_width = max(df[column].astype(
                    str).map(len).max(), len(column))
                col_idx = df.columns.get_loc(column)
                writer.sheets['Sheet1'].set_column(
                    col_idx, col_idx, column_width)

            writer.save()
            wb = pd.read_excel('IT_temp2_nag.xlsx')
            wb.to_html('IT_op_nag.html', index=False)

        def it_nas_code():
            df = pd.read_excel('ITNashik2.xlsx')
            marks = percentile.get()
            z = df[df['Merit (Score)'] <= float(marks)]
            z.to_excel("IT_temp_nas.xlsx", index=False)
            df1 = pd.read_excel("IT_temp_nas.xlsx")
            df2 = df1.reset_index()
            df1['Sr.No.'] = df2.index + 1
            df1.to_excel("IT_temp_nas.xlsx", index=False)
            writer = pd.ExcelWriter('IT_temp2_nas.xlsx')
            df = pd.read_excel('IT_temp_nas.xlsx')
            df.to_excel(writer, sheet_name='Sheet1', index=False, na_rep='NaN')

            for column in df:
                column_width = max(df[column].astype(
                    str).map(len).max(), len(column))
                col_idx = df.columns.get_loc(column)
                writer.sheets['Sheet1'].set_column(
                    col_idx, col_idx, column_width)

            writer.save()
            wb = pd.read_excel('IT_temp2_nas.xlsx')
            wb.to_html('IT_op_nas.html', index=False)

        def it_aug_code():
            df = pd.read_excel('ITAurangabad2.xlsx')
            marks = percentile.get()
            z = df[df['Merit (Score)'] <= float(marks)]
            z.to_excel("IT_temp_aug.xlsx", index=False)
            df1 = pd.read_excel("IT_temp_aug.xlsx")
            df2 = df1.reset_index()
            df1['Sr.No.'] = df2.index + 1
            df1.to_excel("IT_temp_aug.xlsx", index=False)
            writer = pd.ExcelWriter('IT_temp2_aug.xlsx')
            df = pd.read_excel('IT_temp_aug.xlsx')
            df.to_excel(writer, sheet_name='Sheet1', index=False, na_rep='NaN')

            for column in df:
                column_width = max(df[column].astype(
                    str).map(len).max(), len(column))
                col_idx = df.columns.get_loc(column)
                writer.sheets['Sheet1'].set_column(
                    col_idx, col_idx, column_width)

            writer.save()
            wb = pd.read_excel('IT_temp2_aug.xlsx')
            wb.to_html('IT_op_aug.html', index=False)

        def it_amt_code():
            df = pd.read_excel('ITAmravati2.xlsx')
            marks = percentile.get()
            z = df[df['Merit (Score)'] <= float(marks)]
            z.to_excel("IT_temp_amt.xlsx", index=False)
            df1 = pd.read_excel("IT_temp_amt.xlsx")
            df2 = df1.reset_index()
            df1['Sr.No.'] = df2.index + 1
            df1.to_excel("IT_temp_amt.xlsx", index=False)
            writer = pd.ExcelWriter('IT_temp2_amt.xlsx')
            df = pd.read_excel('IT_temp_amt.xlsx')
            df.to_excel(writer, sheet_name='Sheet1', index=False, na_rep='NaN')

            for column in df:
                column_width = max(df[column].astype(
                    str).map(len).max(), len(column))
                col_idx = df.columns.get_loc(column)
                writer.sheets['Sheet1'].set_column(
                    col_idx, col_idx, column_width)

            writer.save()
            wb = pd.read_excel('IT_temp2_amt.xlsx')
            wb.to_html('IT_op_amt.html', index=False)

        def extc_code():
            df = pd.read_excel('EXTC2.xlsx')
            marks = percentile.get()
            z = df[df['Merit (Score)'] <= float(marks)]
            z.to_excel("EXTC_temp.xlsx", index=False)
            df1 = pd.read_excel("EXTC_temp.xlsx")
            df2 = df1.reset_index()
            df1['Sr.No.'] = df2.index + 1
            df1.to_excel("EXTC_temp.xlsx", index=False)
            writer = pd.ExcelWriter('EXTC_temp2.xlsx')
            df = pd.read_excel('EXTC_temp.xlsx')
            df.to_excel(writer, sheet_name='Sheet1', index=False, na_rep='NaN')

            for column in df:
                column_width = max(df[column].astype(
                    str).map(len).max(), len(column))
                col_idx = df.columns.get_loc(column)
                writer.sheets['Sheet1'].set_column(
                    col_idx, col_idx, column_width)

            writer.save()
            wb = pd.read_excel('EXTC_temp2.xlsx')
            wb.to_html('EXTC_op.html', index=False)

        def extc_mu_code():
            df = pd.read_excel('EXTC2Mumbai.xlsx')
            marks = percentile.get()
            z = df[df['Merit (Score)'] <= float(marks)]
            z.to_excel("EXTC_temp_mu.xlsx", index=False)
            df1 = pd.read_excel("EXTC_temp_mu.xlsx")
            df2 = df1.reset_index()
            df1['Sr.No.'] = df2.index + 1
            df1.to_excel("EXTC_temp_mu.xlsx", index=False)
            writer = pd.ExcelWriter('EXTC_temp2_mu.xlsx')
            df = pd.read_excel('EXTC_temp_mu.xlsx')
            df.to_excel(writer, sheet_name='Sheet1', index=False, na_rep='NaN')

            for column in df:
                column_width = max(df[column].astype(
                    str).map(len).max(), len(column))
                col_idx = df.columns.get_loc(column)
                writer.sheets['Sheet1'].set_column(
                    col_idx, col_idx, column_width)

            writer.save()
            wb = pd.read_excel('EXTC_temp2_mu.xlsx')
            wb.to_html('EXTC_op_mu.html', index=False)

        def extc_pu_code():
            df = pd.read_excel('EXTC2Pune.xlsx')
            marks = percentile.get()
            z = df[df['Merit (Score)'] <= float(marks)]
            z.to_excel("EXTC_temp_pu.xlsx", index=False)
            df1 = pd.read_excel("EXTC_temp_pu.xlsx")
            df2 = df1.reset_index()
            df1['Sr.No.'] = df2.index + 1
            df1.to_excel("EXTC_temp_pu.xlsx", index=False)
            writer = pd.ExcelWriter('EXTC_temp2_pu.xlsx')
            df = pd.read_excel('EXTC_temp_pu.xlsx')
            df.to_excel(writer, sheet_name='Sheet1', index=False, na_rep='NaN')

            for column in df:
                column_width = max(df[column].astype(
                    str).map(len).max(), len(column))
                col_idx = df.columns.get_loc(column)
                writer.sheets['Sheet1'].set_column(
                    col_idx, col_idx, column_width)

            writer.save()
            wb = pd.read_excel('EXTC_temp2_pu.xlsx')
            wb.to_html('EXTC_op_pu.html', index=False)

        def extc_nag_code():
            df = pd.read_excel('EXTC2Nagpur.xlsx')
            marks = percentile.get()
            z = df[df['Merit (Score)'] <= float(marks)]
            z.to_excel("EXTC_temp_nag.xlsx", index=False)
            df1 = pd.read_excel("EXTC_temp_nag.xlsx")
            df2 = df1.reset_index()
            df1['Sr.No.'] = df2.index + 1
            df1.to_excel("EXTC_temp_nag.xlsx", index=False)
            writer = pd.ExcelWriter('EXTC_temp2_nag.xlsx')
            df = pd.read_excel('EXTC_temp_nag.xlsx')
            df.to_excel(writer, sheet_name='Sheet1', index=False, na_rep='NaN')

            for column in df:
                column_width = max(df[column].astype(
                    str).map(len).max(), len(column))
                col_idx = df.columns.get_loc(column)
                writer.sheets['Sheet1'].set_column(
                    col_idx, col_idx, column_width)

            writer.save()
            wb = pd.read_excel('EXTC_temp2_nag.xlsx')
            wb.to_html('EXTC_op_nag.html', index=False)

        def extc_nas_code():
            df = pd.read_excel('EXTC2Nashik.xlsx')
            marks = percentile.get()
            z = df[df['Merit (Score)'] <= float(marks)]
            z.to_excel("EXTC_temp_nas.xlsx", index=False)
            df1 = pd.read_excel("EXTC_temp_nas.xlsx")
            df2 = df1.reset_index()
            df1['Sr.No.'] = df2.index + 1
            df1.to_excel("EXTC_temp_nas.xlsx", index=False)
            writer = pd.ExcelWriter('EXTC_temp2_nas.xlsx')
            df = pd.read_excel('EXTC_temp_nas.xlsx')
            df.to_excel(writer, sheet_name='Sheet1', index=False, na_rep='NaN')

            for column in df:
                column_width = max(df[column].astype(
                    str).map(len).max(), len(column))
                col_idx = df.columns.get_loc(column)
                writer.sheets['Sheet1'].set_column(
                    col_idx, col_idx, column_width)

            writer.save()
            wb = pd.read_excel('EXTC_temp2_nas.xlsx')
            wb.to_html('EXTC_op_nas.html', index=False)

        def extc_mug_code():
            df = pd.read_excel('EXTC2Aurangabad.xlsx')
            marks = percentile.get()
            z = df[df['Merit (Score)'] <= float(marks)]
            z.to_excel("EXTC_temp_mug.xlsx", index=False)
            df1 = pd.read_excel("EXTC_temp_mug.xlsx")
            df2 = df1.reset_index()
            df1['Sr.No.'] = df2.index + 1
            df1.to_excel("EXTC_temp_mug.xlsx", index=False)
            writer = pd.ExcelWriter('EXTC_temp2_mug.xlsx')
            df = pd.read_excel('EXTC_temp_mug.xlsx')
            df.to_excel(writer, sheet_name='Sheet1', index=False, na_rep='NaN')

            for column in df:
                column_width = max(df[column].astype(
                    str).map(len).max(), len(column))
                col_idx = df.columns.get_loc(column)
                writer.sheets['Sheet1'].set_column(
                    col_idx, col_idx, column_width)

            writer.save()
            wb = pd.read_excel('EXTC_temp2_mug.xlsx')
            wb.to_html('EXTC_op_mug.html', index=False)

        def extc_amt_code():
            df = pd.read_excel('EXTC2Amravati.xlsx')
            marks = percentile.get()
            z = df[df['Merit (Score)'] <= float(marks)]
            z.to_excel("EXTC_temp_amt.xlsx", index=False)
            df1 = pd.read_excel("EXTC_temp_amt.xlsx")
            df2 = df1.reset_index()
            df1['Sr.No.'] = df2.index + 1
            df1.to_excel("EXTC_temp_amt.xlsx", index=False)
            writer = pd.ExcelWriter('EXTC_temp2_amt.xlsx')
            df = pd.read_excel('EXTC_temp_amt.xlsx')
            df.to_excel(writer, sheet_name='Sheet1', index=False, na_rep='NaN')

            for column in df:
                column_width = max(df[column].astype(
                    str).map(len).max(), len(column))
                col_idx = df.columns.get_loc(column)
                writer.sheets['Sheet1'].set_column(
                    col_idx, col_idx, column_width)

            writer.save()
            wb = pd.read_excel('EXTC_temp2_amt.xlsx')
            wb.to_html('EXTC_op_amt.html', index=False)

        def civil_code():
            df = pd.read_excel('civil2.xlsx')
            marks = percentile.get()
            z = df[df['Merit (Score)'] <= float(marks)]
            z.to_excel("civil_temp.xlsx", index=False)
            df1 = pd.read_excel("civil_temp.xlsx")
            df2 = df1.reset_index()
            df1['Sr.No.'] = df2.index + 1
            df1.to_excel("civil_temp.xlsx", index=False)
            writer = pd.ExcelWriter('civil_temp2.xlsx')
            df = pd.read_excel('civil_temp.xlsx')
            df.to_excel(writer, sheet_name='Sheet1', index=False, na_rep='NaN')

            for column in df:
                column_width = max(df[column].astype(
                    str).map(len).max(), len(column))
                col_idx = df.columns.get_loc(column)
                writer.sheets['Sheet1'].set_column(
                    col_idx, col_idx, column_width)

            writer.save()
            wb = pd.read_excel('civil_temp2.xlsx')
            wb.to_html('civil_op.html', index=False)

        def civil_mu_code():
            df = pd.read_excel('civil2mumbai.xlsx')
            marks = percentile.get()
            z = df[df['Merit (Score)'] <= float(marks)]
            z.to_excel("civil_temp_mu.xlsx", index=False)
            df1 = pd.read_excel("civil_temp_mu.xlsx")
            df2 = df1.reset_index()
            df1['Sr.No.'] = df2.index + 1
            df1.to_excel("civil_temp_mu.xlsx", index=False)
            writer = pd.ExcelWriter('civil_temp2_mu.xlsx')
            df = pd.read_excel('civil_temp_mu.xlsx')
            df.to_excel(writer, sheet_name='Sheet1', index=False, na_rep='NaN')

            for column in df:
                column_width = max(df[column].astype(
                    str).map(len).max(), len(column))
                col_idx = df.columns.get_loc(column)
                writer.sheets['Sheet1'].set_column(
                    col_idx, col_idx, column_width)

            writer.save()
            wb = pd.read_excel('civil_temp2_mu.xlsx')
            wb.to_html('civil_op_mu.html', index=False)

        def civil_pu_code():
            df = pd.read_excel('civil2Pune.xlsx')
            marks = percentile.get()
            z = df[df['Merit (Score)'] <= float(marks)]
            z.to_excel("civil_temp_pu.xlsx", index=False)
            df1 = pd.read_excel("civil_temp_pu.xlsx")
            df2 = df1.reset_index()
            df1['Sr.No.'] = df2.index + 1
            df1.to_excel("civil_temp_pu.xlsx", index=False)
            writer = pd.ExcelWriter('civil_temp2_pu.xlsx')
            df = pd.read_excel('civil_temp_pu.xlsx')
            df.to_excel(writer, sheet_name='Sheet1', index=False, na_rep='NaN')

            for column in df:
                column_width = max(df[column].astype(
                    str).map(len).max(), len(column))
                col_idx = df.columns.get_loc(column)
                writer.sheets['Sheet1'].set_column(
                    col_idx, col_idx, column_width)

            writer.save()
            wb = pd.read_excel('civil_temp2_pu.xlsx')
            wb.to_html('civil_op_pu.html', index=False)

        def civil_nag_code():
            df = pd.read_excel('civil2Nagpur.xlsx')
            marks = percentile.get()
            z = df[df['Merit (Score)'] <= float(marks)]
            z.to_excel("civil_temp_nag.xlsx", index=False)
            df1 = pd.read_excel("civil_temp_nag.xlsx")
            df2 = df1.reset_index()
            df1['Sr.No.'] = df2.index + 1
            df1.to_excel("civil_temp_nag.xlsx", index=False)
            writer = pd.ExcelWriter('civil_temp2_nag.xlsx')
            df = pd.read_excel('civil_temp_nag.xlsx')
            df.to_excel(writer, sheet_name='Sheet1', index=False, na_rep='NaN')

            for column in df:
                column_width = max(df[column].astype(
                    str).map(len).max(), len(column))
                col_idx = df.columns.get_loc(column)
                writer.sheets['Sheet1'].set_column(
                    col_idx, col_idx, column_width)

            writer.save()
            wb = pd.read_excel('civil_temp2_nag.xlsx')
            wb.to_html('civil_op_nag.html', index=False)

        def civil_nas_code():
            df = pd.read_excel('civil2Nashik.xlsx')
            marks = percentile.get()
            z = df[df['Merit (Score)'] <= float(marks)]
            z.to_excel("civil_temp_nas.xlsx", index=False)
            df1 = pd.read_excel("civil_temp_nas.xlsx")
            df2 = df1.reset_index()
            df1['Sr.No.'] = df2.index + 1
            df1.to_excel("civil_temp_nas.xlsx", index=False)
            writer = pd.ExcelWriter('civil_temp2_nas.xlsx')
            df = pd.read_excel('civil_temp_nas.xlsx')
            df.to_excel(writer, sheet_name='Sheet1', index=False, na_rep='NaN')

            for column in df:
                column_width = max(df[column].astype(
                    str).map(len).max(), len(column))
                col_idx = df.columns.get_loc(column)
                writer.sheets['Sheet1'].set_column(
                    col_idx, col_idx, column_width)

            writer.save()
            wb = pd.read_excel('civil_temp2_nas.xlsx')
            wb.to_html('civil_op_nas.html', index=False)

        def civil_aug_code():
            df = pd.read_excel('civil2Aurangabad.xlsx')
            marks = percentile.get()
            z = df[df['Merit (Score)'] <= float(marks)]
            z.to_excel("civil_temp_aug.xlsx", index=False)
            df1 = pd.read_excel("civil_temp_aug.xlsx")
            df2 = df1.reset_index()
            df1['Sr.No.'] = df2.index + 1
            df1.to_excel("civil_temp_aug.xlsx", index=False)
            writer = pd.ExcelWriter('civil_temp2_aug.xlsx')
            df = pd.read_excel('civil_temp_aug.xlsx')
            df.to_excel(writer, sheet_name='Sheet1', index=False, na_rep='NaN')

            for column in df:
                column_width = max(df[column].astype(
                    str).map(len).max(), len(column))
                col_idx = df.columns.get_loc(column)
                writer.sheets['Sheet1'].set_column(
                    col_idx, col_idx, column_width)

            writer.save()
            wb = pd.read_excel('civil_temp2_aug.xlsx')
            wb.to_html('civil_op_aug.html', index=False)

        def civil_amt_code():
            df = pd.read_excel('civil2Amravati.xlsx')
            marks = percentile.get()
            z = df[df['Merit (Score)'] <= float(marks)]
            z.to_excel("civil_temp_amt.xlsx", index=False)
            df1 = pd.read_excel("civil_temp_amt.xlsx")
            df2 = df1.reset_index()
            df1['Sr.No.'] = df2.index + 1
            df1.to_excel("civil_temp_amt.xlsx", index=False)
            writer = pd.ExcelWriter('civil_temp2_amt.xlsx')
            df = pd.read_excel('civil_temp_amt.xlsx')
            df.to_excel(writer, sheet_name='Sheet1', index=False, na_rep='NaN')

            for column in df:
                column_width = max(df[column].astype(
                    str).map(len).max(), len(column))
                col_idx = df.columns.get_loc(column)
                writer.sheets['Sheet1'].set_column(
                    col_idx, col_idx, column_width)

            writer.save()
            wb = pd.read_excel('civil_temp2_amt.xlsx')
            wb.to_html('civil_op_amt.html', index=False)

        def mech_code():
            df = pd.read_excel('Mech2.xlsx')
            marks = percentile.get()
            z = df[df['Merit (Score)'] <= float(marks)]
            z.to_excel("mech_temp.xlsx", index=False)
            df1 = pd.read_excel("mech_temp.xlsx")
            df2 = df1.reset_index()
            df1['Sr.No.'] = df2.index + 1
            df1.to_excel("mech_temp.xlsx", index=False)
            writer = pd.ExcelWriter('mech_temp2.xlsx')
            df = pd.read_excel('mech_temp.xlsx')
            df.to_excel(writer, sheet_name='Sheet1', index=False, na_rep='NaN')

            for column in df:
                column_width = max(df[column].astype(
                    str).map(len).max(), len(column))
                col_idx = df.columns.get_loc(column)
                writer.sheets['Sheet1'].set_column(
                    col_idx, col_idx, column_width)

            writer.save()
            wb = pd.read_excel('mech_temp2.xlsx')
            wb.to_html('mech_op.html', index=False)

        def mech_mu_code():
            df = pd.read_excel('Mech2mumbai.xlsx')
            marks = percentile.get()
            z = df[df['Merit (Score)'] <= float(marks)]
            z.to_excel("mech_temp_mu.xlsx", index=False)
            df1 = pd.read_excel("mech_temp_mu.xlsx")
            df2 = df1.reset_index()
            df1['Sr.No.'] = df2.index + 1
            df1.to_excel("mech_temp_mu.xlsx", index=False)
            writer = pd.ExcelWriter('mech_temp2_mu.xlsx')
            df = pd.read_excel('mech_temp_mu.xlsx')
            df.to_excel(writer, sheet_name='Sheet1', index=False, na_rep='NaN')

            for column in df:
                column_width = max(df[column].astype(
                    str).map(len).max(), len(column))
                col_idx = df.columns.get_loc(column)
                writer.sheets['Sheet1'].set_column(
                    col_idx, col_idx, column_width)

            writer.save()
            wb = pd.read_excel('mech_temp2_mu.xlsx')
            wb.to_html('mech_op_mu.html', index=False)

        def mech_pu_code():
            df = pd.read_excel('Mech2Pune.xlsx')
            marks = percentile.get()
            z = df[df['Merit (Score)'] <= float(marks)]
            z.to_excel("mech_temp_pu.xlsx", index=False)
            df1 = pd.read_excel("mech_temp_pu.xlsx")
            df2 = df1.reset_index()
            df1['Sr.No.'] = df2.index + 1
            df1.to_excel("mech_temp_pu.xlsx", index=False)
            writer = pd.ExcelWriter('mech_temp2_pu.xlsx')
            df = pd.read_excel('mech_temp_pu.xlsx')
            df.to_excel(writer, sheet_name='Sheet1', index=False, na_rep='NaN')

            for column in df:
                column_width = max(df[column].astype(
                    str).map(len).max(), len(column))
                col_idx = df.columns.get_loc(column)
                writer.sheets['Sheet1'].set_column(
                    col_idx, col_idx, column_width)

            writer.save()
            wb = pd.read_excel('mech_temp2_pu.xlsx')
            wb.to_html('mech_op_pu.html', index=False)

        def mech_nag_code():
            df = pd.read_excel('Mech2Nagpur.xlsx')
            marks = percentile.get()
            z = df[df['Merit (Score)'] <= float(marks)]
            z.to_excel("mech_temp_nag.xlsx", index=False)
            df1 = pd.read_excel("mech_temp_nag.xlsx")
            df2 = df1.reset_index()
            df1['Sr.No.'] = df2.index + 1
            df1.to_excel("mech_temp_nag.xlsx", index=False)
            writer = pd.ExcelWriter('mech_temp2_nag.xlsx')
            df = pd.read_excel('mech_temp_nag.xlsx')
            df.to_excel(writer, sheet_name='Sheet1', index=False, na_rep='NaN')

            for column in df:
                column_width = max(df[column].astype(
                    str).map(len).max(), len(column))
                col_idx = df.columns.get_loc(column)
                writer.sheets['Sheet1'].set_column(
                    col_idx, col_idx, column_width)

            writer.save()
            wb = pd.read_excel('mech_temp2_nag.xlsx')
            wb.to_html('mech_op_nag.html', index=False)

        def mech_nas_code():
            df = pd.read_excel('Mech2Nashik.xlsx')
            marks = percentile.get()
            z = df[df['Merit (Score)'] <= float(marks)]
            z.to_excel("mech_temp_nas.xlsx", index=False)
            df1 = pd.read_excel("mech_temp_nas.xlsx")
            df2 = df1.reset_index()
            df1['Sr.No.'] = df2.index + 1
            df1.to_excel("mech_temp_nas.xlsx", index=False)
            writer = pd.ExcelWriter('mech_temp2_nas.xlsx')
            df = pd.read_excel('mech_temp_nas.xlsx')
            df.to_excel(writer, sheet_name='Sheet1', index=False, na_rep='NaN')

            for column in df:
                column_width = max(df[column].astype(
                    str).map(len).max(), len(column))
                col_idx = df.columns.get_loc(column)
                writer.sheets['Sheet1'].set_column(
                    col_idx, col_idx, column_width)

            writer.save()
            wb = pd.read_excel('mech_temp2_nas.xlsx')
            wb.to_html('mech_op_nas.html', index=False)

        def mech_aug_code():
            df = pd.read_excel('Mech2Aurangabad.xlsx')
            marks = percentile.get()
            z = df[df['Merit (Score)'] <= float(marks)]
            z.to_excel("mech_temp_aug.xlsx", index=False)
            df1 = pd.read_excel("mech_temp_aug.xlsx")
            df2 = df1.reset_index()
            df1['Sr.No.'] = df2.index + 1
            df1.to_excel("mech_temp_aug.xlsx", index=False)
            writer = pd.ExcelWriter('mech_temp2_aug.xlsx')
            df = pd.read_excel('mech_temp_aug.xlsx')
            df.to_excel(writer, sheet_name='Sheet1', index=False, na_rep='NaN')

            for column in df:
                column_width = max(df[column].astype(
                    str).map(len).max(), len(column))
                col_idx = df.columns.get_loc(column)
                writer.sheets['Sheet1'].set_column(
                    col_idx, col_idx, column_width)

            writer.save()
            wb = pd.read_excel('mech_temp2_aug.xlsx')
            wb.to_html('mech_op_aug.html', index=False)

        def mech_amt_code():
            df = pd.read_excel('Mech2Amravati.xlsx')
            marks = percentile.get()
            z = df[df['Merit (Score)'] <= float(marks)]
            z.to_excel("mech_temp_amt.xlsx", index=False)
            df1 = pd.read_excel("mech_temp_amt.xlsx")
            df2 = df1.reset_index()
            df1['Sr.No.'] = df2.index + 1
            df1.to_excel("mech_temp_amt.xlsx", index=False)
            writer = pd.ExcelWriter('mech_temp2_amt.xlsx')
            df = pd.read_excel('mech_temp_amt.xlsx')
            df.to_excel(writer, sheet_name='Sheet1', index=False, na_rep='NaN')

            for column in df:
                column_width = max(df[column].astype(
                    str).map(len).max(), len(column))
                col_idx = df.columns.get_loc(column)
                writer.sheets['Sheet1'].set_column(
                    col_idx, col_idx, column_width)

            writer.save()
            wb = pd.read_excel('mech_temp2_amt.xlsx')
            wb.to_html('mech_op_amt.html', index=False)
        info = tk.Tk()
        info.configure(bg="light blue")
        info.title("College Connect")
        info.geometry('%dx%d+0+0' % (wi, he))
        b = "assets//image.jpeg"
        imga = Image.open(b)
        imga = imga.resize(
            (round(800 * he / 864), round(800 * wi / 1536)), Image.ANTIALIAS)
        imga = ImageTk.PhotoImage(imga)
        panela = Label(info, image=imga)
        panela.image = imga
        panela.pack(anchor=W)
        Label(info, text="College Connect", fg="teal", font=f"Algerian {round(50*wi/1536)} underline", bg="light blue").place(x=850*wi / 1536,
                                                                                                                              y=25 * he / 864)

        c = "assets//teal1.jpg"
        imga = Image.open(c)
        imga = imga.resize(
            (round(500 * he / 864), round(400 * wi / 1536)), Image.ANTIALIAS)
        imga = ImageTk.PhotoImage(imga)
        panela = Label(info, image=imga)
        panela.image = imga
        panela.place(x=900 * wi / 1536,
                     y=200 * he / 864)

        gh = "#045960"
        Label(info, text="Enter your info", font=f"Verdana {round(15*wi/1536)} ", fg="white", bg=gh, justify=LEFT,
              compound="center").place(
            x=1050 * wi / 1536,
            y=240 * he / 864)
        Label(info, text="Name:", font=f"Verdana {round(15*wi/1536)} ", fg="white", bg=gh, justify=LEFT, compound="center").place(x=920* wi / 1536,y=320 * he / 864)

        name = Entry(info, font="Verdana 12")
        name.place(x=1080 * wi / 1536, y=320 * he / 864,
                   height=round(25*wi/1536), width=round(280*wi/1536))
        Label(info, text="Your percentile:", font=f"Verdana {round(15*wi/1536)} ", fg="white", bg=gh, justify=LEFT, compound="center").place(x=920* wi / 1536,y=380 * he / 864)

        percentile = Entry(info, font="Verdana 12")
        percentile.place(x=1080 * wi / 1536, y=380 *
                         he / 864, height=round(25*wi/1536), width=round(280*wi/1536))
        Label(info, text="Phone number:", font=f"Verdana {round(15*wi/1536)} ", fg="white", bg=gh, justify=LEFT, compound="center").place(x=920* wi / 1536,y=440 * he / 864)

        phone = Entry(info, font="Verdana 12")
        phone.place(x=1080 * wi / 1536, y=440 * he / 864, height=round(25*wi/1536), width=round(280*wi/1536))
        mailb = Button(info, text="Submit", bg="turquoise4", fg="white", font=f"Verdana {round(15*wi/1536)} ", height=2, width=10,
                       compound="center",
                       command=lambda: [vali(),
                                        """comp_code(), it_code(), extc_code(), civil_code(), mech_code(), info.destroy(),fgh()"""]).place(x=1080 * wi / 1536, y=500 * he / 864)
        info.bind('<Return>', lambda event: vali())
        home = Button(info, text="Home", bg="turquoise4", fg="white", font=f"Verdana {round(15*wi/1536)} ",
                      compound="center", command=lambda: [info.destroy(), main()]).place(x=1350 * wi / 1536,
                                                                                         y=715 * he / 864)

        info.mainloop()

    root = tk.Tk()
    root.configure(bg="light blue")
    wi, he = root.winfo_screenwidth(), root.winfo_screenheight()
    root.title("College Connect")
    root.geometry('%dx%d+0+0' % (wi, he))
    b = "assets//image.jpeg"
    imga = Image.open(b)
    imga = imga.resize(
        (round(800 * he / 864), round(800 * wi / 1536)), Image.ANTIALIAS)
    imga = ImageTk.PhotoImage(imga)
    panela = Label(root, image=imga)
    panela.image = imga
    panela.pack(anchor=W)
    Label(root, text="College Connect", fg="teal", font=f"Algerian {round(50*wi/1536)} underline", bg="light blue").place(
        x=850 * wi / 1536, y=25 * he / 864)
    lab = Label(root, text="College connect is an extensive search engine for the students,\n"
                           "parents, and education industry players who are seeking info\n"
                           "on higher education sector in Maharashtra.One can rely on College\n"
                           "Connect for getting unbiased and relevant data on colleges based\n"
                           "on your perfomance.\n"
                           "\n"
                           "College Choosing decision, the second biggest decision of anyone's\n"
                           "life should not go wrong CollegeConnect has been developed to fulfill\n"
                           "a vision of empowering studentswith knowledge so that they make a\n"
                           "wiser decision while choosing their career andalma mater.It is a\n"
                           "one-stop-solution making course and college selection easy for\n"
                           "students looking to pursue undergraduate (UG) courses\n"
                           "in Maharashtra.", font=f"Verdana {round(15*wi/1536)} ", bg="light blue", justify=LEFT).place(
        x=825 * wi / 1536, y=140 * he / 864)
    crsb = Button(text="College Recommendation", bg="turquoise4", fg="white", font=f"Verdana {round(14*wi/1536)}", height=round(3*wi/1536), width=round(30*wi/1536),
                  command=lambda: [root.destroy(), crs()]).place(x=1000 * wi / 1536, y=500 * he / 864)

    brsb = Button(text="Other Features ", font=f"Verdana {round(10*wi/1536)}", height=2, bg="turquoise4", fg="white", width=round(20*wi/1536),
                  command=lambda: [root.destroy(), brs(), main()]).place(
        x=1350 * wi / 1536, y=725 * he / 864)
    Label(root, text="CollegeConnect has been developed to fulfill a vision of\n"
                     "empowering students with knowledge so that they make a wiser\n"
                     "decision while choosing their career and alma mater", font=f"Verdana {round(12*wi/1536)} ", bg="light blue",
          justify=CENTER).place(x=905 * wi / 1536, y=625 * he / 864)

    root.mainloop()


main()
