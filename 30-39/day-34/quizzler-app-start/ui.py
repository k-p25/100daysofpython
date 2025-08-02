from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    
    
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        
        self.sn = 0
        self.score = Label(text=f"Score: {self.sn}", fg="white", bg=THEME_COLOR)

        self.score.grid(column=1, row=0)
       
       
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas_text = self.canvas.create_text(
            150, 
            125, 
            width=280,
            text="Some question text", 
            fill=THEME_COLOR, 
            font=("Arial", 20, "italic"))
        
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        
        
        
        r = PhotoImage(file="images/true.png")
        w = PhotoImage(file="images/false.png")
        
        self.right = Button(image=r, highlightthickness=0,command=self.right)
        self.right.grid(column=0, row=2)
        
        self.wrong = Button(image=w, highlightthickness=0,command=self.wrong)
        self.wrong.grid(column=1, row=2)
        
        self.get_next_question()
        
        self.window.mainloop()
        
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text, text=q_text)
        else:
            self.canvas.itemconfig(self.canvas_text, text="You've reached the end of the quiz!")
            self.right.config(state='disabled')
            self.wrong.config(state='disabled')
        
    def right(self):
        self.give_feedback(self.quiz.check_answer("True"))
        
    def wrong(self):
        self.give_feedback(self.quiz.check_answer("False"))       
         
    def give_feedback(self, is_right):
        self.canvas.config(bg="green") if is_right else self.canvas.config(bg="red")
        
        self.window.after(1000, self.get_next_question)

        
        