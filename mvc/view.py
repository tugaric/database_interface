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

    # widget based on frame witch contains: 
        #   treeview which contains the articles in db article ( number, plan, class) 
        #   refresh button: retrieves data from db
        #   delete  button: deletes selected datapoint
class view_db_treeView(ttk.Frame):
    # function on object creation
    def __init__(self, controller, master):
        # initialisation of frame / attach frame to a master=root tk.Tk() object
        super().__init__(master)
    # create the treeview
        self.tree = ttk.Treeview(self, columns = ("number", "plan", "class"))
        # enable name of the columns to be seen
        self.tree["show"] = "headings"
        #first parameter = "name of the column"
        #second parameter = "text that is visible"
        self.tree.heading("number", text="article number") 
        self.tree.heading("plan", text="plan number")
        self.tree.heading("class", text="article class")
    # visual changes
        self.tree.column("plan", width=80)
        self.tree.column("number", width=120)
        self.tree.column("class", width=80)
    # --> Change to grid ! position tree
        self.tree.pack()

    # --> Do on item selection
    
    # Add refresh button:   retrieve information from database
        self.refresh_button = ttk.Button(master, text="Refresh button", command=controller.refresh_button_pressed)
        self.refresh_button.pack()
    # Add delete button:    delete selected item in treeview
        self.delete_button = ttk.Button(master, text="Delete article", command=controller.delete_button_pressed)
        self.delete_button.pack()
    # Clear the treeview
    def clear_all(self):
        tree = self.tree
        for item in tree.get_children():
            tree.delete(item)

class myView():
    def setup(self, controller):
        self.root = tk.Tk()
    # create the frame to create new articles
        self.new_art_frm = new_article_frame(controller, self.root)
        self.new_art_frm.pack()
        options = ["MBODY", "SEAT", "LOWER SPINDLE", "UPPER SPINDLE"]
        self.new_art_frm.cbo_class.configure(values = options)
    # frame containing treeview to show data in db
        self.article_treeview = view_db_treeView(controller, self.root)
        self.article_treeview.pack()
    # start the view object
    def run(self):
        self.root.mainloop()