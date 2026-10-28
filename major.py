import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title("Denominator Calculator")
root.geometry("400x550")
root.configure(bg="orange")
def calculate():
    try:
        amount = int(entry.get())
        if amount < 0:
            messagebox.showerror("Error", "Enter a positive amount.")
            return
        denominations = [100, 50, 20, 10, 5, 2,  1]
        result.delete(1.0, tk.END)
        total_notes = 0
        for note in denominations:
            count = amount // note
            if count > 0:
                result.insert(tk.END, f"{note} : {count}\n")
                total_notes += count
        result.insert(tk.END, f"\Total Notes and Coins: {total_notes}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")
def clear():
            entry.delete(0, tk.END)
            result.delete(1.0, tk.END)
tk.Label(root, text="Denomination calculator", font=("Arial", 14,  "bold"), bg="orange", fg="white").pack(pady=10)
tk.Label(root, text="Enter the amount:", font=("Arial", 12), bg="orange", fg="purple").pack(pady=5)
entry = tk.Entry(root, font=("Arial", 12), justify="center")
entry.pack(pady=10)
tk.Button(root, text="Calculate", font=("Arial", 12), bg="yellow", fg="red", command=calculate).pack(pady=10)
tk.Button(root, text="Clear", font=("Arial", 12), bg="green", fg="white", command=clear).pack(pady=10)
tk.Label(root, text="Result:", font=("Arial", 12), bg="orange", fg="purple").pack(pady=5)
result = tk.Text(root, height=10, width=40, font=("Arial", 12), bg="white", fg="black")
result.pack(pady=10)
root.mainloop()