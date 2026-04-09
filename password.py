import re
import tkinter as tk
from tkinter import messagebox

def check_password():
    password = entry.get()
    score = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("At least 8 characters required")

    # Uppercase check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letter")

    # Number check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add a number")

    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add special character")

    # Strength result
    if score == 4:
        result = "Strong 💪"
        color = "green"
    elif score == 3:
        result = "Medium ⚠️"
        color = "orange"
    else:
        result = "Weak ❗"
        color = "red"

    result_label.config(text="Strength: " + result, fg=color)

    # Show feedback
    if feedback:
        feedback_text.set("\n".join(feedback))
    else:
        feedback_text.set("Perfect password ✅")


# ----------- GUI WINDOW ----------- #

root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x300")
root.resizable(False, False)

# Title
tk.Label(root, text="🔐 Password Checker", font=("Arial", 16, "bold")).pack(pady=10)

# Input field
tk.Label(root, text="Enter Password:").pack()
entry = tk.Entry(root, show="*", width=30)
entry.pack(pady=5)

# Button
tk.Button(root, text="Check Strength", command=check_password).pack(pady=10)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack()

# Feedback text
feedback_text = tk.StringVar()
tk.Label(root, textvariable=feedback_text, fg="blue").pack(pady=10)

# Run GUI
root.mainloop()