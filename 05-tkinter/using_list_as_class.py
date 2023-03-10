import tkinter as tk


class AppWindow:
    def __init__(self):
        self.window = tk.Tk()
        self.data = ['John', 'Peter', 'Mike', 'Ann', 'Jenn']
        self.data_var = tk.Variable(value=self.data)
        self.list_box = None
        self.sbar = None
        self.create_list()
        btn = tk.Button(self.window, text="CLICK", command=self.add_name)
        btn.pack()

    def create_list(self):
        frame = tk.Frame(self.window)
        self.list_box = tk.Listbox(frame, listvariable=self.data_var, height=7)
        self.list_box.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)
        self.sbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=self.list_box.yview)
        self.list_box['yscrollcommand'] = self.sbar.set
        self.sbar.pack(side=tk.LEFT, expand=True, fill=tk.Y)
        frame.pack()

    def add_name(self):
        name = input("Name: ")
        self.data.append(name)
        self.list_box.insert(0, name)

    def start(self):
        self.window.mainloop()


app =AppWindow()
app.start()
