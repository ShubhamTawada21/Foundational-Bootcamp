import tkinter as tk

expression = ""

def press_number(num):
    """Adds a number to the current calculation expression."""
    global expression
    expression = expression + str(num)
    display_variable.set(expression)


def press_operator(op):
    """Adds an operator (+, -, *, /) to the expression."""
    global expression

    if expression == "":
        expression = "0"
    expression = expression + str(op)
    display_variable.set(expression)

6
def calculate():
    """Evaluates the mathematical string and updates history."""
    global expression 
    try:
        if expression == "":
            return

        result = eval(expression)

        friendly_expr = expression.replace("*", "×").replace("/", "÷")
        display_variable.set(str(result))

        history_listbox.insert(0, f" {friendly_expr} = {result}")


        expression = str(result)

    except ZeroDivisionError:
        display_variable.set("Error: Div by 0")
        expression = ""
    except Exception:
        display_variable.set("Error")
        expression = ""


def clear_all():
    """Resets everything back to blank."""
    global expression
    expression = ""
    display_variable.set("0")


def clear_history():
    """Clears out the history sidebar log."""
    history_listbox.delete(0, tk.END)

root = tk.Tk()
root.title("Simple Beginner Calculator")
root.geometry("500x400")
root.configure(bg="#222222")

display_variable = tk.StringVar()
display_variable.set("0")

screen = tk.Label(
    root,
    textvariable=display_variable,
    font=("Arial", 20),
    anchor="e",
    bg="#111111",
    fg="white",
    padx=10,
    pady=15,
)
screen.pack(fill="x", padx=10, pady=10)

main_frame = tk.Frame(root, bg="#222222")
main_frame.pack(fill="both", expand=True, padx=10, pady=5)

button_frame = tk.Frame(main_frame, bg="#222222")
button_frame.pack(side="left", fill="both", expand=True)

history_frame = tk.Frame(main_frame, bg="#333333", padx=5, pady=5)
history_frame.pack(side="right", fill="both", padx=(10, 0))

history_label = tk.Label(
    history_frame, text="History Log", bg="#333333", fg="white", font=("Arial", 10)
)
history_label.pack()

history_listbox = tk.Listbox(history_frame, width=22, bg="#111111", fg="lightgreen")
history_listbox.pack(fill="both", expand=True, pady=5)

clear_hist_btn = tk.Button(
    history_frame, text="Clear Log", command=clear_history, bg="#555555", fg="white"
)
clear_hist_btn.pack(fill="x")

for i in range(5):
    button_frame.rowconfigure(i, weight=1)
for i in range(4):
    button_frame.columnconfigure(i, weight=1)

buttons = [
    ("7", 0, 0, lambda: press_number(7)),
    ("8", 0, 1, lambda: press_number(8)),
    ("9", 0, 2, lambda: press_number(9)),
    ("÷", 0, 3, lambda: press_operator("/")),
    ("4", 1, 0, lambda: press_number(4)),
    ("5", 1, 1, lambda: press_number(5)),
    ("6", 1, 2, lambda: press_number(6)),
    ("×", 1, 3, lambda: press_operator("*")),
    ("1", 2, 0, lambda: press_number(1)),
    ("2", 2, 1, lambda: press_number(2)),
    ("3", 2, 2, lambda: press_number(3)),
    ("-", 2, 3, lambda: press_operator("-")),
    ("0", 3, 0, lambda: press_number(0)),
    (".", 3, 1, lambda: press_number(".")),
    ("+", 3, 2, lambda: press_operator("+")),
    ("C", 3, 3, clear_all),
    ("=", 4, 0, calculate),
]

for text, row, col, command in buttons:
    if text == "=":

        btn = tk.Button(
            button_frame,
            text=text,
            font=("Arial", 14),
            command=command,
            bg="orange",
            fg="white",
        )
        btn.grid(row=row, column=col, columnspan=4, sticky="nsew", padx=2, pady=2)
    else:
        btn = tk.Button(
            button_frame, text=text, font=("Arial", 14), command=command, bd=1
        )
        btn.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)

root.mainloop()

