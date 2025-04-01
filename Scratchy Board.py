from turtle import Turtle, Screen
import tkinter as tk  # Correct import for TK
import tkinter.ttk as ttk  # Correct import for ttk

tim = Turtle()
tim.speed("fastest")
screen = Screen()
screen.title("Scratchy Board!")

# Create a new tab for instructions
root = screen.getcanvas().winfo_toplevel()
tab_control = ttk.Notebook(root)
tab_control.pack(expand=1, fill='both')

drawing_tab = tk.Frame(tab_control) # Corrected TK to tk
instructions_tab = tk.Frame(tab_control) # Corrected TK to tk

tab_control.add(drawing_tab, text='Drawing')
tab_control.add(instructions_tab, text='Instructions')

# Attach the turtle canvas to the drawing tab
canvas = screen.getcanvas()
canvas.master = drawing_tab
canvas.pack(expand=1, fill='both', side=tk.LEFT) # Corrected TK to tk

def move_forward():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def move_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def move_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def clear_drawing():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

def penup_cursor():
    tim.penup()

def pendown_cursor():
    tim.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="c", fun=clear_drawing)
screen.onkey(key="q", fun=penup_cursor)
screen.onkey(key="e", fun=pendown_cursor)

# Add instructions to the instructions tab
instructions_text = tk.Text(instructions_tab, wrap=tk.WORD, width=25, height=10) # Corrected TK to tk
instructions_text.insert(tk.END, """
Controls:

- W: Forward
- S: Backward
- A: Left
- D: Right
- C: Clear
- Q: Pen Up
- E: Pen Down
""")
instructions_text.config(state=tk.DISABLED) # Corrected TK to tk
instructions_text.pack(fill='both')

screen.exitonclick()

