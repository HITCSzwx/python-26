import tkinter as tk
from tkinter import ttk
from db import db


class InputFrame(tk.Frame):  # 继承Frame类
    def __init__(self, master=None):
        super().__init__(master)
        self.root = master  # 定义内部变量root
        self.name = tk.StringVar()
        self.math = tk.StringVar()
        self.chinese = tk.StringVar()
        self.english = tk.StringVar()
        self.status = tk.StringVar()
        self.create_page()

    def create_page(self):
        # stick 控件对象方向 tk.W 西方位
        # pady padding y 上下的宽度
        # row 行 表格布局
        tk.Label(self).grid(row=0, stick=tk.W, pady=10)
        tk.Label(self, text="姓 名: ").grid(row=1, stick=tk.W, pady=10)
        # text variable 绑定控件里面的数据内容
        tk.Entry(self, textvariable=self.name).grid(row=1, column=1, stick=tk.E)
        tk.Label(self, text="数 学: ").grid(row=2, stick=tk.W, pady=10)
        tk.Entry(self, textvariable=self.math).grid(row=2, column=1, stick=tk.E)
        tk.Label(self, text="语 文: ").grid(row=3, stick=tk.W, pady=10)
        tk.Entry(self, textvariable=self.chinese).grid(row=3, column=1, stick=tk.E)
        tk.Label(self, text="英 语: ").grid(row=4, stick=tk.W, pady=10)
        tk.Entry(self, textvariable=self.english).grid(row=4, column=1, stick=tk.E)
        tk.Button(self, text="录入", command=self.recode_student).grid(
            row=5, column=1, stick=tk.E, pady=10
        )
        tk.Label(self, textvariable=self.status).grid(
            row=6, column=1, stick=tk.E, pady=10
        )

    def recode_student(self):
        pass


class QueryFrame(tk.Frame):  # 继承Frame类
    def __init__(self, master=None):
        super().__init__(master)
        self.root = master  # 定义内部变量root
        self.itemName = tk.StringVar()

        tk.Label(self, text="查询界面").pack()
        self.table_frame = tk.Frame(self)
        self.table_frame.pack()
        self.row = 1

        self.create_page()

    def create_page(self):
        self.create_tree_view()
        self.show_data_frame()
        tk.Button(self, text="刷新数据", command=self.show_data_frame).pack(
            anchor=tk.E, pady=5
        )

    def show_data_frame(self):
        for _ in map(self.tree_view.delete, self.tree_view.get_children("")):
            pass
        students = db.all()
        for index, stu in enumerate(students):
            print(stu)
            self.tree_view.insert(
                "",
                index + 1,
                values=(
                    stu["name"],
                    str(stu["chinese"]),
                    str(stu["math"]),
                    str(stu["english"]),
                ),
            )

    def create_tree_view(self):
        columns = ("name", "chinese", "math", "english")
        columns_value = ("姓名", "语文", "数学", "英语")

        self.tree_view = ttk.Treeview(self, show="headings", columns=columns)
        self.tree_view.column("name", width=100, anchor="center")
        self.tree_view.column("chinese", width=100, anchor="center")
        self.tree_view.column("math", width=100, anchor="center")
        self.tree_view.column("english", width=100, anchor="center")
        self.tree_view.heading("name", text="姓名")
        self.tree_view.heading("chinese", text="语文")
        self.tree_view.heading("math", text="数学")
        self.tree_view.heading("english", text="英语")
        self.tree_view.pack(fill=tk.BOTH, expand=True)


class DeleteFrame(tk.Frame):  # 继承Frame类
    def __init__(self, master=None):
        super().__init__(master)
        self.root = master  # 定义内部变量root
        tk.Label(self, text="删除数据").pack()
        self.delete_frame = tk.Frame(self)
        self.delete_frame.pack()
        self.status = tk.StringVar()
        self.v1 = tk.StringVar()
        self.create_page()

    def create_page(self):
        tk.Label(self.delete_frame, text="根据名字删除信息").pack(anchor=tk.W, padx=20)
        e1 = tk.Entry(self.delete_frame, textvariable=self.v1)
        e1.pack(side=tk.LEFT, padx=20, pady=5)

        tk.Button(self.delete_frame, text="删除", command=self._delete).pack()
        tk.Label(self, textvariable=self.status).pack()

    def _delete(self):
        pass


class ChangeFrame(tk.Frame):  # 继承Frame类
    def __init__(self, master=None):
        super().__init__(master)
        self.root = master  # 定义内部变量root

        tk.Label(self, text="修改界面").pack()
        self.change_frame = tk.Frame(self)
        self.change_frame.pack()
        self.status = tk.StringVar()
        self.name = tk.StringVar()
        self.math = tk.StringVar()
        self.chinese = tk.StringVar()
        self.english = tk.StringVar()

        self.create_page()

    def create_page(self):
        tk.Label(self.change_frame).grid(row=0, stick=tk.W, pady=1)
        tk.Label(self.change_frame, text="姓 名: ").grid(row=1, stick=tk.W, pady=10)
        tk.Entry(self.change_frame, textvariable=self.name).grid(
            row=1, column=1, stick=tk.E
        )
        tk.Label(self.change_frame, text="数 学: ").grid(row=2, stick=tk.W, pady=10)
        tk.Entry(self.change_frame, textvariable=self.math).grid(
            row=2, column=1, stick=tk.E
        )
        tk.Label(self.change_frame, text="语 文: ").grid(row=3, stick=tk.W, pady=10)
        tk.Entry(self.change_frame, textvariable=self.chinese).grid(
            row=3, column=1, stick=tk.E
        )
        tk.Label(self.change_frame, text="英 语: ").grid(row=4, stick=tk.W, pady=10)
        tk.Entry(self.change_frame, textvariable=self.english).grid(
            row=4, column=1, stick=tk.E
        )
        tk.Button(self.change_frame, text="查询", command=self._search).grid(
            row=6, column=0, stick=tk.W, pady=10
        )
        tk.Button(self.change_frame, text="修改", command=self._change).grid(
            row=6, column=1, stick=tk.E, pady=10
        )
        tk.Label(self.change_frame, textvariable=self.status).grid(
            row=7, column=1, stick=tk.E, pady=10
        )

    def _search(self):
        pass

    def _change(self):
        pass



class AboutFrame(tk.Frame):  # 继承Frame类
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.create_page()

    def create_page(self):
        tk.Label(self, text="关于作品：本作品由 tkinter 制作").pack(anchor=tk.W)
        tk.Label(self, text="关于作者：青灯教育-正心老师").pack(anchor=tk.W)
        tk.Label(self, text="版权所有：湖南青灯教育科技有限公司Python学院").pack(anchor=tk.W)


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("%dx%d" % (600, 400))
    q = QueryFrame(root)
    q.pack()
    root.mainloop()
