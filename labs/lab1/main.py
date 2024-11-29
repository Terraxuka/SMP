import multiprocessing
import tkinter as tk
from tkinter import messagebox
import math

history = []
memory = None
decimal_places = 2

def calculate(num1, num2, operator):
    try:
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2
        elif operator == '/':
            return num1 / num2
        elif operator == '^':
            return num1 ** num2
        elif operator == '%':
            return num1 % num2
        else:
            return None
    except ZeroDivisionError:
        return "Error"

def sqrt(num):
    try:
        return math.sqrt(num)
    except ValueError:
        return "Error"

def update_history(entry):
    history.append(entry)
    history_list.insert(tk.END, entry)

def clear_inputs():
    entry_num1.delete(0, tk.END)
    entry_num2.delete(0, tk.END)

def perform_calculation(operator):
    global memory
    try:
        if operator == 'sqrt':
            num = float(entry_num1.get())
            if sqrt(num) != "Error":
                result = sqrt(num)
                formatted_result = round(result, decimal_places)
                update_history(f"sqrt({num}) = {formatted_result}")
                result_label.config(text=f"Результат: {formatted_result}")
            else:
                messagebox.showerror("Помилка", "Не можна брати корінь від від'ємного числа!")
        else:
            num1 = float(entry_num1.get())
            num2 = float(entry_num2.get())
            if calculate(num1, num2, operator) != "Error":
                result = calculate(num1, num2, operator)
                formatted_result = round(result, decimal_places)
                update_history(f"{num1} {operator} {num2} = {formatted_result}")
                result_label.config(text=f"Результат: {formatted_result}")
            else:
                messagebox.showerror("Помилка", "Не можна ділити на нуль!")

        if memory_var.get():
            memory = formatted_result
            memory_label.config(text=f"Пам'ять: {memory}")

    except ValueError:
        messagebox.showerror("Помилка", "Введіть коректне число!")

def clear_history():
    history_list.delete(0, tk.END)
    history.clear()

def memory_clear():
    global memory
    memory = None
    memory_label.config(text="Пам'ять: Немає")

def memory_save():
    global memory
    memory = result_label.cget("text").split(": ")[1]  # Витягнути результат
    memory_label.config(text=f"Пам'ять: {memory}")

def memory_recall():
    if memory is not None:
        entry_num1.delete(0, tk.END)
        entry_num1.insert(0, memory)
    else:
        messagebox.showinfo("Пам'ять", "Пам'ять порожня!")

def memory_add():
    global memory

    try:
        if memory is None:
            memory = float(result_label.cget("text").split(": ")[1])
        else:
            memory += float(result_label.cget("text").split(": ")[1])
        memory_label.config(text=f"Пам'ять: {memory}")
    except ValueError:
        messagebox.showerror("Помилка", "Неможливо додати до пам'яті. Невірне значення!")

def set_decimal_places(value):
    global decimal_places
    decimal_places = int(value)
    decimal_label.config(text=f"Знаків після коми: {decimal_places}")

root = tk.Tk()
root.title("Lab 1")


label_num1 = tk.Label(root, text="Перше число:")
label_num1.grid(row=0, column=0, padx=10, pady=5)
entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1, padx=10, pady=5)
label_num2 = tk.Label(root, text="Друге число (не потрібно для √):")
label_num2.grid(row=1, column=0, padx=10, pady=5)
entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1, padx=10, pady=5)

def create_operator_button(text, operator):
    return tk.Button(root, text=text, command=lambda: perform_calculation(operator))

button_add = create_operator_button("+", "+")
button_add.grid(row=2, column=0, padx=10, pady=5)
button_subtract = create_operator_button("-", "-")
button_subtract.grid(row=2, column=1, padx=10, pady=5)
button_multiply = create_operator_button("*", "*")
button_multiply.grid(row=3, column=0, padx=10, pady=5)
button_divide = create_operator_button("/", "/")
button_divide.grid(row=3, column=1, padx=10, pady=5)
button_power = create_operator_button("^", "^")
button_power.grid(row=4, column=0, padx=10, pady=5)
button_modulus = create_operator_button("%", "%")
button_modulus.grid(row=4, column=1, padx=10, pady=5)
button_sqrt = create_operator_button("√", "sqrt")
button_sqrt.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

button_mc = tk.Button(root, text="MC", command=memory_clear)
button_mc.grid(row=6, column=0, padx=10, pady=5)

button_ms = tk.Button(root, text="MS", command=memory_save)
button_ms.grid(row=6, column=1, padx=10, pady=5)

button_mr = tk.Button(root, text="MR", command=memory_recall)
button_mr.grid(row=7, column=0, padx=10, pady=5)

button_mplus = tk.Button(root, text="M+", command=memory_add)
button_mplus.grid(row=7, column=1, padx=10, pady=5)


memory_var = tk.BooleanVar()
memory_checkbox = tk.Checkbutton(root, text="Зберегти результат у пам'ять", variable=memory_var)
memory_checkbox.grid(row=8, column=0, columnspan=2, padx=10, pady=5)

memory_label = tk.Label(root, text="Пам'ять: Немає")
memory_label.grid(row=9, column=0, columnspan=2, padx=10, pady=5)


result_label = tk.Label(root, text="Результат:")
result_label.grid(row=10, column=0, columnspan=2, padx=10, pady=5)

history_label = tk.Label(root, text="Історія:")
history_label.grid(row=11, column=0, padx=10, pady=5)
history_list = tk.Listbox(root, height=10, width=40)
history_list.grid(row=12, column=0, columnspan=2, padx=10, pady=5)

clear_history_button = tk.Button(root, text="Очистити історію", command=clear_history)
clear_history_button.grid(row=13, column=0, columnspan=2, padx=10, pady=5)


decimal_scale = tk.Scale(root, from_=0, to=10, orient=tk.HORIZONTAL, label="Знаки після коми", command=set_decimal_places)
decimal_scale.set(decimal_places)
decimal_scale.grid(row=14, column=0, columnspan=2, padx=5, pady=5)

decimal_label = tk.Label(root, text=f"Знаків після коми: {decimal_places}")
decimal_label.grid(row=15, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()