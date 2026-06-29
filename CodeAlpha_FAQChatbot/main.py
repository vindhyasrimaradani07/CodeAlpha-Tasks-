import tkinter as tk
from tkinter import messagebox
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from faq_data import faq_questions, faq_answers

# Convert questions into vectors
vectorizer = TfidfVectorizer()
question_vectors = vectorizer.fit_transform(faq_questions)


def get_answer(user_question):
    user_vector = vectorizer.transform([user_question])

    similarity = cosine_similarity(user_vector, question_vectors)

    best_match = similarity.argmax()

    score = similarity[0][best_match]

    if score < 0.2:
        return "Sorry, I couldn't understand your question."

    return faq_answers[best_match]

def ask_question():
    question = entry.get()

    if question.strip() == "":
        messagebox.showwarning("Warning", "Please enter a question.")
        return

    answer = get_answer(question)

    output.config(state="normal")
    output.delete("1.0", tk.END)

    output.insert(
        tk.END,
        f"You: {question}\n\nBot: {answer}"
    )

    output.config(state="disabled")

def clear_chat():
    output.config(state="normal")
    output.delete("1.0", tk.END)
    output.config(state="disabled")
    entry.delete(0, tk.END)

    # ------------------- GUI -------------------

root = tk.Tk()
root.title("CodeAlpha FAQ Chatbot")
root.geometry("600x500")
root.configure(bg="#EAF6FF")

title = tk.Label(
    root,
    text="🤖 FAQ Chatbot",
    font=("Arial", 20, "bold"),
    bg="#EAF6FF",
    fg="#003366"
)
title.pack(pady=15)

label = tk.Label(
    root,
    text="Ask your question:",
    font=("Arial", 12),
    bg="#EAF6FF"
)
label.pack()

entry = tk.Entry(root, width=60, font=("Arial", 11))
entry.pack(pady=10)

ask_btn = tk.Button(
    root,
    text="Ask",
    command=ask_question,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 11, "bold")
)
ask_btn.pack(pady=5)

clear_btn = tk.Button(
    root,
    text="Clear Chat",
    command=clear_chat,
    bg="#F44336",
    fg="white",
    font=("Arial", 11, "bold")
)

clear_btn.pack(pady=5)

output = tk.Text(
    root,
    width=65,
    height=15,
    font=("Arial", 11),
    state="disabled"
)
output.pack(pady=15)

root.mainloop()

def clear_chat():
    output.config(state="normal")
    output.delete("1.0", tk.END)
    output.config(state="disabled")
    entry.delete(0, tk.END)
    