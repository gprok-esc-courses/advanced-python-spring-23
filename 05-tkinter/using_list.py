import tkinter as tk


def add_name():
    name = input("Name: ")
    data.append(name)
    list_box.insert(0, name)


window = tk.Tk()
window.title("List Box")

frame = tk.Frame(window)

data = ['John', 'Peter', 'Mike', 'Ann', 'Jenn']

data_var = tk.Variable(value=data)

list_box = tk.Listbox(frame, listvariable=data_var, height=7)
list_box.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)

sbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=list_box.yview)
list_box['yscrollcommand'] = sbar.set
sbar.pack(side=tk.LEFT, expand=True, fill=tk.Y)

frame.pack()

btn = tk.Button(window, text="CLICK", command=add_name)
btn.pack()

window.mainloop()
