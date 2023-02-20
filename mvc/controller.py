from mvc.model import myModel
from mvc.view import myView

class myController:
    def __init__(self):
        self.view = myView()
        self.model = myModel()

    def start(self):
        self.view.setup(self)
        self.refresh_button_pressed()
        self.view.run()

    def btn_new_article_pressed(self):
        tmp = self.view.new_art_frm
        self.model.insert_new_article(
            "$" + tmp.var_article_number.get(), 
            tmp.var_article_plan_number.get(), 
            tmp.var_cbo_class.get())

    def refresh_button_pressed(self):
        print("Refresh!")
        self.view.article_treeview.clear_all()
        list_of_article = self.model.get_all_articles()
        for article in list_of_article:
            self.view.article_treeview.tree.insert("", "end", values = article)

    def delete_button_pressed(self):
    # verify that an item has been selected

    # return the selected article
        tree = self.view.article_treeview.tree
        article_number = tree.item(tree.selection())["values"][0]
    # delete the article in the db
        self.model.delete_article(article_number)

    # print to command line as user feedback
        print("Delete!")