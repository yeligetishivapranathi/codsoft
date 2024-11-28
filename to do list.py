import tkinter
window=tkinter.Tk()
window.geometry("300x300")
window.title("TO-Do List App")
task_list=[]
task_box = tkinter.Entry(window)
task_box.pack()

def add_task():
    task = task_box.get()
    task_list.append(task)
    task_box.delete(0, tkinter.END)
    update_listbox()
def update_listbox():
    listbox.delete(0, tkinter.END)
    for task in task_list:
        listbox.insert(tkinter.END, task)

add_button = tkinter.Button(window, text="Add Task", command=add_task)
add_button.pack()

listbox = tkinter.Listbox(window)
listbox.pack()
update_listbox()
window.mainloop()
