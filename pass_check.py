import tkinter as tk
from tkinter import ttk,messagebox
import re

def check_password_strength():
    password = password_entry.get()
    
    # Define regex patterns for different criteria
    length_regex = re.compile(r'.{8,}')  # at least 8 characters
    uppercase_regex = re.compile(r'[A-Z]')  # at least one uppercase letter
    lowercase_regex = re.compile(r'[a-z]')  # at least one lowercase letter
    digit_regex = re.compile(r'\d')  # at least one digit
    special_char_regex = re.compile(r'[!@#$%^&*(),.?":{}|<>]')  # at least one special character

    # Check each criteria
    length_check = length_regex.search(password)
    uppercase_check = uppercase_regex.search(password)
    lowercase_check = lowercase_regex.search(password)
    digit_check = digit_regex.search(password)
    special_char_check = special_char_regex.search(password)

    # Determine overall strength
    if (length_check and uppercase_check and lowercase_check
            and digit_check and special_char_check):
        strength_label.config(text="Strong", foreground="green")
        messagebox.showinfo("Password Strength", "Password is strong!")
    else:
        strength_label.config(text="Weak", foreground="red")
        messagebox.showwarning("Password Strength", "Password is weak. Please choose a stronger password.")

# Create main window
root = tk.Tk()
root.title("Password Strength Checker")

# Create and place themed widgets
style = ttk.Style()
style.theme_use("clam")

password_label = ttk.Label(root, text="Enter Password:")
password_label.pack(pady=5)

password_entry = ttk.Entry(root, show="^")
password_entry.pack(pady=5)

check_button = ttk.Button(root, text="Check Strength", command=check_password_strength)
check_button.pack(pady=5)

strength_label = ttk.Label(root, text="", font=("Helvetica", 16))
strength_label.pack(pady=5)

# Run the application
root.mainloop()