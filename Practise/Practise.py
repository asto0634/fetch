import tkinter as tk

root = tk.Tk()
root.title("Todo App")
root.geometry("800x600")
root.configure(bg="#2c3e50")

title = tk.Label(
    root,
    text="My tasks",
    bg= "#2c3e50",
    fg= "white",
    font=("Verdana",22, "bold")
)
title.pack(pady=10)

task_entry = tk.Entry(root,width=25, font=("Arial",12))
task_entry.pack(pady=5)

task_list = tk.Listbox(root, width=30, height=10, font=("Arial",11))
task_list.pack()

def add_task():
    task = task_entry.get()
    if task != "":
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)
def delete_task():
    selected = task_list.curselection()
    if selected:
        task_list.delete(selected)


tk.Button(
    root,
    text= "Add Task",
    bg="#04ccd6",
    fg="white",
    width=20,
    command= add_task
).pack(pady=5)


tk.Button(
    root,
    text= "Delete Task",
    bg="#c7505d",
    fg="white",
    width=20,
    command= delete_task
).pack(pady=5)

def clear_all():
    task_list.delete(0,tk.END)

tk.Button(
    root,
    text= "Clear all",
    bg="#e3c819",
    fg="white",
    width=20,
    command= clear_all
).pack(pady=5)

root.mainloop()