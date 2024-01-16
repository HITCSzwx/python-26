import tkinter

from views import InsertFrame,SearchFrame, AboutFrame



class MainPage:
    def __init__(self, root1):
        # 定义一个窗口对象
        self.root = root1
        # 设置标题
        self.root.title("学生信息管理系统0.0.1")
        self.root.geometry("700x600")
        self.create_page()


        self.insert_frame = InsertFrame(self.root)
        self.search_frame = SearchFrame(self.root)
        self.about_frame = AboutFrame(self.root)
        self.insert_frame.pack()
        self.search_frame.pack()
        self.about_frame.pack()


    def create_page(self):
        menu_bar = tkinter.Menu(self.root)
        menu_bar.add_command(label="录入",command=self.show_insert_frame)
        menu_bar.add_command(label="查询",command=self.show_search_frame)
        menu_bar.add_command(label="删除")
        menu_bar.add_command(label="修改")
        menu_bar.add_command(label="关于",command=self.show_about_frame)
        self.root["menu"] = menu_bar

    def show_insert_frame(self):
        self.insert_frame.pack()
        self.search_frame.forget()
        self.about_frame.forget()

    def show_search_frame(self):
        self.search_frame.pack()
        self.insert_frame.forget()
        self.about_frame.forget()


    def show_about_frame(self):
        self.about_frame.pack()
        self.insert_frame.forget()
        self.search_frame.forget()






root = tkinter.Tk()


MainPage(root)

root.mainloop()
