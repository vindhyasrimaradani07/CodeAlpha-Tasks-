import tkinter as tk
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator
import pyperclip

# Function to translate text
def translate_text():
    try:
        text = input_text.get("1.0", tk.END).strip()

        if text == "":
            messagebox.showwarning("Warning", "Please enter some text!")
            return

        source = source_lang.get()
        target = target_lang.get()

        translated = GoogleTranslator(source=source, target=target).translate(text)

        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translated)

    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to copy translated text
def copy_text():    
    translated = output_text.get("1.0", tk.END).strip()

    if translated:
        pyperclip.copy(translated)
        messagebox.showinfo("Copied", "Translation copied to clipboard!")
# Function to swap languages
def swap_languages():
    source = source_lang.get()
    target = target_lang.get()

    source_lang.set(target)
    target_lang.set(source)

# Function to clear all text
def clear_text():
    input_text.delete("1.0", tk.END)
    output_text.delete("1.0", tk.END)

# Main Window
root = tk.Tk()
root.title("CodeAlpha AI Language Translation Tool")
root.geometry("700x600")
root.resizable(False, False)
root.configure(bg="#EAF6FF")

# Heading
title = tk.Label(
    root,
    text="🌍 AI Language Translation Tool",
    font=("Arial", 18, "bold"),
    bg="#EAF6FF",
    fg="#003366"
)
title.pack(pady=10)

# Input Label
tk.Label(root, text="Enter Text:", font=("Arial", 12)).pack()

input_text = tk.Text(root, height=6, width=60)
input_text.pack(pady=5)

# Language Selection
frame = tk.Frame(root)
frame.pack(pady=10)
swap_btn = tk.Button(
    frame,
    text="🔄 Swap",
    command=swap_languages,
    bg="#FFA500",
    fg="white",
    font=("Arial", 10, "bold")
)

languages = {
    "English": "en",
    "Telugu": "te",
    "Hindi": "hi",
    "Tamil": "ta",
    "Kannada": "kn",
    "Malayalam": "ml",
    "Marathi": "mr",
    "Gujarati": "gu",
    "Punjabi": "pa",
    "Bengali": "bn",
    "Urdu": "ur",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Italian": "it",
    "Portuguese": "pt",
    "Russian": "ru",
    "Japanese": "ja",
    "Korean": "ko",
    "Chinese": "zh-CN",
    "Arabic": "ar"
}


tk.Label(frame, text="From").grid(row=0, column=0, padx=10)

source_lang = ttk.Combobox(frame, values=list(languages.keys()), state="readonly")
source_lang.current(0)
source_lang.grid(row=0, column=1)

tk.Label(frame, text="To").grid(row=0, column=2, padx=10)

target_lang = ttk.Combobox(frame, values=list(languages.keys()), state="readonly")
target_lang.current(1)
target_lang.grid(row=0, column=3)
swap_btn.grid(row=0, column=4, padx=10)

# Translate Button
def perform_translation():
    source = languages[source_lang.get()]
    target = languages[target_lang.get()]

    text = input_text.get("1.0", tk.END).strip()

    if text == "":
        messagebox.showwarning("Warning", "Please enter text.")
        return

    try:
        translated = GoogleTranslator(source=source, target=target).translate(text)

        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translated)

    except Exception as e:
        messagebox.showerror("Error", str(e))

translate_btn = tk.Button(
    root,
    text="Translate",
    command=perform_translation,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 12, "bold")
)
translate_btn.pack(pady=10)

# Output Label
tk.Label(root, text="Translated Text:", font=("Arial", 12)).pack()

output_text = tk.Text(root, height=6, width=60)
output_text.pack(pady=5)

# Copy Button
copy_btn = tk.Button(
    root,
    text="Copy Translation",
    command=copy_text,
    bg="#2196F3",
    fg="white",
    font=("Arial", 11, "bold")
)
copy_btn.pack(pady=10)

clear_btn = tk.Button(
    root,
    text="🗑 Clear All",
    command=clear_text,
    bg="#F44336",
    fg="white",
    font=("Arial", 11, "bold")
)

clear_btn.pack(pady=5)

root.mainloop()