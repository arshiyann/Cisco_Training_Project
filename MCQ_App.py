import random
import tkinter as tk
from tkinter import messagebox

def load_questions():
    questions = [
        {
            'question': 'What is the capital of France?',
            'options': ['Madrid', 'Berlin', 'Paris', 'Rome'],
            'answer': 'Paris'
        },
        {
            'question': 'Which programming language is used for AI/ML?',
            'options': ['Python', 'C++', 'Java', 'HTML'],
            'answer': 'Python'
        },
        {
            'question': 'Which planet is known as the Red Planet?',
            'options': ['Earth', 'Mars', 'Jupiter', 'Venus'],
            'answer': 'Mars'
        },
        {
            'question': 'What is the chemical symbol for water?',
            'options': ['O2', 'H2O', 'CO2', 'NaCl'],
            'answer': 'H2O'
        },
        {
            'question': 'Which data structure works on FIFO principle?',
            'options': ['Stack', 'Queue', 'Array', 'Linked List'],
            'answer': 'Queue'
        }
    ]
    return questions

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MCQ Quiz Application")
        self.questions = load_questions()
        random.shuffle(self.questions)  
        self.current_question_index = 0
        self.score = 0
        
        self.question_label = tk.Label(root, text="", font=("Arial", 16), wraplength=400, justify="center")
        self.question_label.pack(pady=20)
        
        self.options_buttons = []
        for i in range(4):  
            btn = tk.Button(root, text="", font=("Arial", 14), width=20, command=lambda i=i: self.check_answer(i))
            btn.pack(pady=5)
            self.options_buttons.append(btn)
        
        self.next_button = tk.Button(root, text="Next", font=("Arial", 14), command=self.next_question)
        self.next_button.pack(pady=20)
        
        self.display_question()
    
    def display_question(self):
        question_data = self.questions[self.current_question_index]
        self.question_label.config(text=f"Question {self.current_question_index + 1}: {question_data['question']}")
        options = question_data['options']
        random.shuffle(options)  
        
        for i, option in enumerate(options):
            self.options_buttons[i].config(text=option, state="normal")
    
    def check_answer(self, selected_index):
        selected_answer = self.options_buttons[selected_index].cget("text")
        correct_answer = self.questions[self.current_question_index]['answer']
        
        if selected_answer == correct_answer:
            self.score += 1
            messagebox.showinfo("showinfo"," Correct! That's the correct answer! 🎉")
        else:
            messagebox.showinfo("showinfo", f"Wrong! The correct answer was: {correct_answer}")
        
        for btn in self.options_buttons:  
            btn.config(state="disabled")
    
    def next_question(self):
        self.current_question_index += 1
        
        if self.current_question_index < len(self.questions):
            self.display_question()
        else:
            messagebox.showinfo("Quiz Finished", f"Your final score is {self.score}/{len(self.questions)}")
            self.root.quit()  

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()