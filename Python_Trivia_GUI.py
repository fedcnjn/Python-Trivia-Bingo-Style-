import tkinter as tk
import random

# All 50 beginner questions
questions = [
    ("What keyword defines a function?", ["def", "func", "define"], "def"),
    ("What symbol starts a comment?", ["#", "//", "--"], "#"),
    ("Which type stores text?", ["int", "str", "bool"], "str"),
    ("What is the output of print(2 + 3 * 2)?", ["10", "8", "12"], "8"),
    ("What does 'int' stand for?", ["integrate", "integer", "intact"], "integer"),
    ("Which function gets input?", ["input()", "scan()", "read()"], "input()"),
    ("Which data type stores True/False?", ["int", "bool", "float"], "bool"),
    ("What operator checks equality?", ["=", "==", "==="], "=="),
    ("What keyword starts a loop?", ["for", "loop", "start"], "for"),
    ("How do you print 'Hello'?", ["show('Hello')", "print('Hello')", "echo('Hello')"], "print('Hello')"),
    ("How do you create a list?", ["()", "{}", "[]"], "[]"),
    ("Which data type is 3.14?", ["int", "float", "double"], "float"),
    ("What function gives you length?", ["length()", "count()", "len()"], "len()"),
    ("How do you make a comment?", ["//", "#", "/* */"], "#"),
    ("Which loop checks condition before running?", ["for", "while", "repeat"], "while"),
    ("What is x after: x = 5; x += 2?", ["5", "7", "2"], "7"),
    ("What is a correct boolean?", ["'True'", "true", "True"], "True"),
    ("Which function shows text on screen?", ["output()", "display()", "print()"], "print()"),
    ("What does 'elif' mean?", ["else if", "else loop", "end if"], "else if"),
    ("What is 'None' in Python?", ["zero", "empty string", "null value"], "null value"),
    ("Which keyword skips a loop turn?", ["break", "skip", "continue"], "continue"),
    ("Which keyword exits a loop?", ["exit", "break", "stop"], "break"),
    ("What is the index of first list item?", ["1", "0", "-1"], "0"),
    ("What type is ['apple', 'banana']?", ["tuple", "list", "dictionary"], "list"),
    ("What does '==' check?", ["assignment", "equality", "reference"], "equality"),
    ("How do you create a function?", ["make()", "function()", "def"], "def"),
    ("How do you check a condition?", ["if", "loop", "define"], "if"),
    ("What is the result of 10 % 3?", ["1", "0", "3"], "1"),
    ("How do you round 4.7 down?", ["int(4.7)", "round(4.7)", "floor(4.7)"], "int(4.7)"),
    ("What’s a variable?", ["Stored data", "A loop", "An output"], "Stored data"),
    ("How do you make a dictionary?", ["{}", "[]", "()"], "{}"),
    ("What does input() return?", ["int", "str", "float"], "str"),
    ("What’s wrong with 5 = x?", ["Nothing", "It's backwards", "Missing colon"], "It's backwards"),
    ("Which of these is an error?", ["SyntaxError", "IndexFound", "LogicIssue"], "SyntaxError"),
    ("What’s the opposite of 'if'?", ["loop", "else", "print"], "else"),
    ("Which operator adds numbers?", ["-", "*", "+"], "+"),
    ("What does str(123) do?", ["Split 123", "Convert to string", "Make list"], "Convert to string"),
    ("How to get last list item?", ["mylist[0]", "mylist[-1]", "mylist[1]"], "mylist[-1]"),
    ("Which keyword handles errors?", ["try", "error", "except"], "try"),
    ("How do you stop your program?", ["stop()", "quit()", "exit()"], "exit()"),
    ("Which one is not a data type?", ["list", "value", "tuple"], "value"),
    ("Which is a tuple?", ["[1,2]", "{1,2}", "(1,2)"], "(1,2)"),
    ("Which starts a block of code?", [":", ";", "{}"], ":"),
    ("Which keyword defines a class?", ["define", "class", "object"], "class"),
    ("What keyword returns a result from a function?", ["back", "return", "send"], "return"),
    ("What’s the result of bool('')?", ["True", "False", "None"], "False"),
    ("What is the use of 'in'?", ["loops", "check membership", "assignment"], "check membership"),
    ("What do you call a reusable block of code?", ["comment", "function", "if"], "function"),
    ("What type is {'a':1, 'b':2}?", ["list", "dictionary", "tuple"], "dictionary"),
    ("Which keyword does nothing?", ["pass", "skip", "none"], "pass"),
]

random.shuffle(questions)

python_letters = ["P", "Y", "T", "H", "O", "N"]
score = 0

root = tk.Tk()
root.title("PYTHON Trivia Bingo")
root.geometry("600x450")

title_label = tk.Label(root, text="🐍 PYTHON Bingo Trivia Game", font=("Helvetica", 18, "bold"))
title_label.pack(pady=10)

progress_label = tk.Label(root, text="Progress: ", font=("Helvetica", 14))
progress_label.pack()

question_frame = tk.Frame(root)
question_frame.pack(pady=20)

question_label = tk.Label(question_frame, text="", wraplength=500, font=("Helvetica", 14))
question_label.pack(pady=10)

options_frame = tk.Frame(root)
options_frame.pack()

feedback_label = tk.Label(root, text="", font=("Helvetica", 12))
feedback_label.pack(pady=10)

def update_progress():
    display = ""
    for i in range(6):
        if i < score:
            display += f"[{python_letters[i]}] "
        else:
            display += "[ ] "
    progress_label.config(text="Progress: " + display)

def ask_next_question():
    global current_q
    if score == 6:
        show_win()
        return
    if not questions:
        question_label.config(text="No more questions.")
        return

    current_q = questions.pop()
    question, options, answer = current_q
    question_label.config(text=question)
    feedback_label.config(text="")

    for widget in options_frame.winfo_children():
        widget.destroy()

    for opt in options:
        btn = tk.Button(options_frame, text=opt, width=30, command=lambda o=opt: check_answer(o))
        btn.pack(pady=2)

def check_answer(selected):
    global score
    _, _, answer = current_q
    if selected == answer:
        feedback_label.config(text="✅ Correct!")
        score += 1
        update_progress()
        root.after(1000, ask_next_question)
    else:
        feedback_label.config(text=f"❌ Incorrect! Correct answer was: {answer}")
        root.after(1500, ask_next_question)

def show_win():
    for widget in root.winfo_children():
        widget.destroy()

    win_label = tk.Label(root, text="🎉 YOU COMPLETED PYTHON! 🎉", font=("Helvetica", 22, "bold"), fg="green")
    win_label.pack(pady=50)

    python_word = tk.Label(root, text="P Y T H O N", font=("Helvetica", 30, "bold"), fg="blue")
    python_word.pack(pady=10)

    retry_button = tk.Button(root, text="Play Again", command=reset_game, font=("Helvetica", 14))
    retry_button.pack(pady=30)

def reset_game():
    global questions, score
    score = 0
    random.shuffle(questions)
    for widget in root.winfo_children():
        widget.destroy()
    title_label.pack(pady=10)
    progress_label.pack()
    question_frame.pack(pady=20)
    question_label.pack(pady=10)
    options_frame.pack()
    feedback_label.pack(pady=10)
    update_progress()
    ask_next_question()

# Start game
update_progress()
ask_next_question()
root.mainloop()
