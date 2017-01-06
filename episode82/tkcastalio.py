import tkinter as tk
from tkinter import ttk


class MainWindow(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.grid(column=0, row=0, sticky=(tk.W, tk.W, tk.E, tk.S))
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.master.title('Castalio Podcast')

        self.label = ttk.Label(self, text="")
        self.label.grid(column=0, row=0)

        self.tree = ttk.Treeview(self, columns=('date',))
        self.tree.heading('#1', text="Date")
        self.tree.insert('', 0, 'episodes', text='Episodes', open=True)
        self.tree.insert(
            'episodes',
            1,
            text='Episode 82',
            values=('Jan. 8, 2017',)
        )
        self.tree.grid(column=0, row=0, sticky=(tk.W, tk.W, tk.E, tk.S))

        self.pack(fill=tk.X)


win = tk.Tk()
app = MainWindow(master=win)
app.mainloop()

