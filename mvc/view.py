import tkinter as tk
import tkinter.ttk as ttk
from pygubu.widgets.combobox import Combobox

class new_article_frame(ttk.Frame):
    def __init__(self, controller, master):
        super().__init__(master)
    # static labels
        label4 = ttk.Label(self)
        label4.configure(text='article n° :')
        label4.grid(column=0, row=0)
        label5 = ttk.Label(self)
        label5.configure(text='article plan n° :')
        label5.grid(column=0, row=1)
        label6 = ttk.Label(self)
        label6.configure(text='article class :')
        label6.grid(column=0, row=2)
    # entry widgets
        # article number entry widget
        self.var_article_number = tk.StringVar()
        self.e_article_number = ttk.Entry(self, textvariable=self.var_article_number)
        self.e_article_number.grid(column=1, row=0)
        # article plan entry widget
        self.var_article_plan_number = tk.StringVar()
        self.e_article_plan = ttk.Entry(self, textvariable=self.var_article_plan_number)
        self.e_article_plan.grid(column=1, row=1)
    # combobox widget
        self.var_cbo_class = tk.StringVar()
        self.cbo_class = Combobox(self, textvariable=self.var_cbo_class)
        self.cbo_class.grid(column=1, padx=10, pady=10, row=2)
    # button widget
        self.btn_new_article = ttk.Button(self, text='Create new article', command=controller.btn_new_article_pressed)
        self.btn_new_article.grid(column=2, row=0)

class view_db_treeView(ttk.Frame):
    pass

class myView():
    def setup(self, controller):
        self.root = tk.Tk()
        self.new_art_frm = new_article_frame(controller, self.root)
        self.new_art_frm.pack()
        options = ["MBODY", "SEAT", "LOWER SPINDLE", "UPPER SPINDLE"]
        self.new_art_frm.cbo_class.configure(values = options)
    def run(self):
        self.root.mainloop()