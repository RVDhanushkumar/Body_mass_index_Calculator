import tkinter as tk
from tkinter import messagebox


def check():
    if weight.get() == "" or height.get() == "":
        messagebox.showwarning("Missing","Enter all the entries")
        return ""
    click()


def click():
    y = float(int(height.get()) / 100)
    x = float(weight.get())
    bmi = float(x / (y * y))
    bmi = round(bmi, 1)
    l2.destroy()
    l3.destroy()
    weight.destroy()
    height.destroy()
    sb.destroy()
    color = "Red"
    if bmi < 18.5:
        c = "You are UNDERWEIGHT"
    elif 18.5 <= bmi < 25:
        c = "You are Normal Weighted"
        color = "Green"
    elif 25 <= bmi < 30:
        c = "Your are OVERWEIGHT"
    else:
        c = "You are OBESITY"

    l1.config(text=f"Your BMI is {bmi}\n" + c,fg=color)
    l1.pack(pady=50)


if __name__ == "__main__":
    window = tk.Tk()
    window.title("BMI APP")

    l1 = tk.Label(window, text="Let's find out your health status.\n\nBody Mass Index(BMI)",fg="Blue",font="18")
    l1.pack(pady=10)

    f1 = tk.Frame(window)
    f1.pack()

    l2 = tk.Label(f1, text="Enter Weight(KG): ")
    l2.pack(side=tk.LEFT)

    weight = tk.Entry(f1, width=20)
    weight.pack(side=tk.LEFT, padx=10)

    f2 = tk.Frame(window)
    f2.pack()

    l3 = tk.Label(f2, text="Enter Height(cm): ")
    l3.pack(side=tk.LEFT, pady=10)

    height = tk.Entry(f2, width=20)
    height.pack(side=tk.LEFT, padx=10)

    sb = tk.Button(text="Submit", command=check)
    sb.pack(pady=10)
    window.geometry('250x250')
    window.mainloop()
