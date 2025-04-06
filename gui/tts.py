import tkinter as tk
from tkinter import messagebox
import pyttsx3

# Initialize TTS engine
engine = pyttsx3.init()

# Main window setup
root = tk.Tk()
root.title("Text to Speech Editor")
root.geometry("350x400")

# Create the main frame to hold text and buttons side by side
main_frame = tk.Frame(root)
main_frame.pack(fill="both", expand=True, padx=10, pady=10)

# Text widget inside a frame (for padding)
text_frame = tk.Frame(main_frame)
text_frame.pack(side="left", fill="both", expand=True)

text_box = tk.Text(text_frame, wrap="word", font=("Arial", 14))
text_box.pack(fill="both", expand=True)

# Button frame on the right side
button_frame = tk.Frame(main_frame)
button_frame.pack(side="right", fill="y", padx=10)

# Function to read all text
def read_all():
    content = text_box.get("1.0", tk.END).strip()
    if content:
        engine.say(content)
        engine.runAndWait()
    else:
        messagebox.showwarning("Warning", "Text box is empty!")

# Function to read selected text
def read_selected():
    try:
        selected_text = text_box.get(tk.SEL_FIRST, tk.SEL_LAST)
        engine.say(selected_text)
        engine.runAndWait()
    except tk.TclError:
        messagebox.showinfo("Info", "Please select some text to read.")

# Buttons on the right side
btn_read_all = tk.Button(button_frame, text="🔊 Read All", command=read_all, width=15, height=2, bg="#90ee90", font=("Arial", 10))
btn_read_all.pack(pady=10)

btn_read_selected = tk.Button(button_frame, text="🔊 Read Selected", command=read_selected, width=15, height=2, bg="#add8e6", font=("Arial", 10))
btn_read_selected.pack(pady=10)

# Run the app
root.mainloop()
