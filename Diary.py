import tkinter as tk
from tkinter import filedialog, messagebox
from datetime import datetime

def save_entry():
    entry_text = text_box.get("1.0", tk.END).strip()
    if not entry_text:
        messagebox.showerror("Error", "The diary entry is empty!")
        return
    
    file_name = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file_name:
        try:
            with open(file_name, "w", encoding="utf-8") as file:
                file.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                file.write("Entry:\n")
                file.write(entry_text)
            messagebox.showinfo("Success", "Diary entry saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

def clear_entry():
    text_box.delete("1.0", tk.END)

def open_entry():
    file_name = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_name:
        try:
            with open(file_name, "r", encoding="utf-8") as file:
                content = file.read()
            text_box.delete("1.0", tk.END)
            text_box.insert(tk.END, content)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

root = tk.Tk()
root.title("Personal Diary")
root.geometry("600x400")

tk.Label(root, text="Personal Diary Application", font=("Arial", 16, "bold")).pack(pady=10)

text_box = tk.Text(root, wrap="word", font=("Arial", 12), height=15)
text_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Button(frame, text="Save Entry", command=save_entry, width=15).grid(row=0, column=0, padx=10)
tk.Button(frame, text="Open Entry", command=open_entry, width=15).grid(row=0, column=1, padx=10)
tk.Button(frame, text="Clear", command=clear_entry, width=15).grid(row=0, column=2, padx=10)

root.mainloop()
