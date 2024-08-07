THEME_COLOR = "#375362"
from tkinter import*
from quiz_brain import QuizBrain





class QuizIntreface:
    def __init__(self,quiz_brain:QuizBrain):

        self.quiz=quiz_brain
        self.window=Tk()
        self.window.title=("Quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        self.canvas=Canvas(width=300,height=250)
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)

        self.cross_image  = PhotoImage(file="images/false.png")
        self.unknown_button = Button(image=self.cross_image, highlightthickness=0)
        self.unknown_button.grid(row=2, column=1)

        self.check_image = PhotoImage(file="images/true.png")
        self.known_button = Button(image=self.check_image, highlightthickness=0)
        self.known_button.grid(row=2, column=0)

        self.score_label = Label(text="Score: 0",fg="white",bg=THEME_COLOR)
        self.score_label.grid(row=0,column=1)

        self.question_text = self.canvas.create_text(150, 125, text="", font=("Ariel", 20, "bold"),fill=THEME_COLOR,width=280)


        self.get_next_question()
        self.window,mainloop()


    def get_next_question(self):
        q_text=self.quiz.next_question()
        self.canvas.itemconfig(self.question_text,text=q_text)




