import tkinter as tk
from tkinter import messagebox

def add_task():
    task_name = entry.get()
    if task_name:
        listbox.insert(tk.END, task_name)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task name")

def delete_task():
    try:
        task_index = listbox.curselection()[0]
        listbox.delete(task_index)
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete")

def mark_completed():
    try:
        task_index = listbox.curselection()[0]
        task = listbox.get(task_index)
        # Change the color of the completed task
        listbox.itemconfig(task_index, {'bg': 'lightgreen', 'fg': 'black'})
        # Optionally, you can remove it from the list and add it to a completed list
        # listbox.delete(task_index) 
        # completed_listbox.insert(tk.END, task)
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to mark as completed")

# Initialize the main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")
root.configure(bg='orange')  # Set background color

# Create a frame for the entry and add button
frame = tk.Frame(root, bg='orange')
frame.pack(pady=10)

# Entry widget for task input
entry = tk.Entry(frame, width=30, font=('Arial', 14))
entry.pack(side=tk.LEFT, padx=10)

# Add Task button
add_button = tk.Button(frame, text="Add Task", command=add_task, bg='#4CAF50', fg='white')
add_button.pack(side=tk.LEFT)

# Listbox to display tasks
listbox = tk.Listbox(root, width=45, height=10, font=('Arial', 12), selectmode=tk.SINGLE)
listbox.pack(pady=20)

# Buttons for deleting and marking tasks
delete_button = tk.Button(root, text="Delete Task", command=delete_task, bg='#f44336', fg='white')
delete_button.pack(pady=5)

completed_button = tk.Button(root, text="Mark as Completed", command=mark_completed, bg='#008CBA', fg='white')
completed_button.pack(pady=5)

# Run the main loop
root.mainloop()
