from mvc.model import myModel
from mvc.view import myView

class myController:
    def __init__(self):
        self.view = myView()
        self.model = myModel()

    def start(self):
        self.view.setup(self)
        self.view.run()

    def btn_new_article_pressed(self):
        tmp = self.view.new_art_frm
        new_article = tmp.var_article_number.get(), tmp.var_article_plan_number.get(), tmp.var_cbo_class.get()
        self.model.insert_new_article(
            tmp.var_article_number.get(), 
            tmp.var_article_plan_number.get(), 
            tmp.var_cbo_class.get())
        #self.model.insert_new_class(tmp.var_article_number.get(), tmp.var_article_plan_number.get())