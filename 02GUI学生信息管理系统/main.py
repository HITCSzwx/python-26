import tkinter as tk
from view import AboutFrame, ChangeFrame, DeleteFrame, InputFrame, QueryFrame


# 标准开发代码
class MainPage:
    """登录界面"""

    def __init__(self, master):
        self.root = master
        self.page = tk.Frame(self.root)
        self.page.pack()
        self.root.geometry("%dx%d" % (600, 400))
        self.create_page()

    def create_page(self):
        #  创建一个顶级菜单
        menubar = tk.Menu(self.root)
        # 绑定封装好的页面
        self.input_page = InputFrame(self.root)
        self.change_page = ChangeFrame(self.root)
        self.query_page = QueryFrame(self.root)
        self.delete_page = DeleteFrame(self.root)
        self.about_page = AboutFrame(self.root)

        self.input_page.pack()

        menubar.add_command(label="录入", command=self.show_input)
        menubar.add_command(label="查询", command=self.show_all)
        menubar.add_command(label="删除", command=self.show_input)
        menubar.add_command(label="修改", command=self.show_change)
        menubar.add_command(label="关于", command=self.show_about)
        #  显示菜单
        self.root.config(menu=menubar)

    def show_about(self):
        self.input_page.pack_forget()
        self.change_page.pack_forget()
        self.query_page.pack_forget()
        self.delete_page.pack_forget()
        self.about_page.pack()

    def show_all(self):
        self.input_page.pack_forget()
        self.change_page.pack_forget()
        self.query_page.pack()
        self.delete_page.pack_forget()
        self.about_page.pack_forget()

    def show_input(self):
        self.input_page.pack()
        self.change_page.pack_forget()
        self.query_page.pack_forget()
        self.delete_page.pack_forget()
        self.about_page.pack_forget()

    def show_change(self):
        self.input_page.pack_forget()
        self.change_page.pack()
        self.query_page.pack_forget()
        self.delete_page.pack_forget()
        self.about_page.pack_forget()


if __name__ == '__main__':
    root = tk.Tk()
    MainPage(root)
    root.mainloop()
