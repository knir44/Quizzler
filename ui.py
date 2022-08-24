from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"




class QuizInterface:

    def __init__(self,quiz_brain:QuizBrain):

        self.quiz = quiz_brain

        # window button
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx = 20,pady = 20,bg = THEME_COLOR,highlightthickness=0)

        # Label button
        self.score_level = Label(text= "Score: 0",fg = 'white',bg = THEME_COLOR,font = ("Arial", 15, "italic"))
        self.score_level.grid(row=0,column= 1)

        # canvas button
        self.canvas = Canvas(width=300, height=250)
        self.canvas.grid(row=1,column=0,columnspan=2,pady= 20)


        self.question_text = self.canvas.create_text(
            150,
            125,
            width= 280,
            text="Some question Text",
            fill = THEME_COLOR,
            font =("Arial", 20, "italic")
        )
        self.get_next_question()

        # correct button
        correct_img = PhotoImage(file = "true.png")
        self.correct_btn = Button(image=correct_img,highlightthickness=0,command=self.is_true)
        self.correct_btn.grid(row=2, column=0)

        #wrong button
        false_img = PhotoImage(file="false.png")
        self.false_btn = Button(image=false_img, highlightthickness=0,command=self.is_false)
        self.false_btn.grid(row=2, column=1)

        self.window.mainloop()

    def get_next_question(self):
       self.canvas.config(bg="white")
       if self.quiz.still_has_questions():
           self.score_level.config(text=f"Score: {self.quiz.score}")
           q_text =  self.quiz.next_question()
           self.canvas.itemconfig(self.question_text,text = q_text)


       else:
           self.canvas.itemconfig(self.question_text,
                                  text=f"You've completed the quiz\n\n Your score is {self.quiz.score}")
           self.correct_btn.config(state="disabled")
           self.false_btn.config(state="disabled")



    def is_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)



    def is_false(self):
       is_right = self.quiz.check_answer("False")
       self.give_feedback(is_right)



    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000,self.get_next_question)

