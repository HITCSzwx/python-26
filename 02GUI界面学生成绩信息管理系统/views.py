import tkinter
from db import db


class InsertFrame(tkinter.Frame):
    def __init__(self, root):
        super().__init__(master=root)
        self.username = tkinter.StringVar()
        self.math = tkinter.StringVar()
        self.chinese = tkinter.StringVar()
        self.english = tkinter.StringVar()
        self.status = tkinter.StringVar()
        self.create_page()

    def create_page(self):
        tkinter.Label(self, width=15).grid(row=0, column=0, padx=5, pady=5)
        tkinter.Label(self, text="用户名").grid(row=1, column=0, padx=5, pady=5)
        tkinter.Entry(self, textvariable=self.username).grid(
            row=1,
            column=1,
            padx=5,
            pady=5,
        )
        tkinter.Label(self, text="数学成绩").grid(row=2, column=0, padx=5, pady=5)
        tkinter.Entry(self, textvariable=self.math).grid(
            row=2, column=1, padx=5, pady=5
        )
        tkinter.Label(self, text="语文成绩").grid(row=3, column=0, padx=5, pady=5)
        tkinter.Entry(self, textvariable=self.chinese).grid(
            row=3, column=1, padx=5, pady=5
        )
        tkinter.Label(self, text="英语成绩").grid(row=4, column=0, padx=5, pady=5)
        tkinter.Entry(self, textvariable=self.english).grid(
            row=4, column=1, padx=5, pady=5
        )

        tkinter.Button(self, text="插入", command=self.insert_data).grid(row=5, column=1)
        tkinter.Label(self, textvariable=self.status).grid(row=5, column=0)

    def insert_data(self):
        print("插入数据")

        # 插入数据的逻辑

        stu = {
            "姓名": self.username.get(),
            "数学": self.math.get(),
            "语文": self.chinese.get(),
            "英语": self.english.get(),
        }
        db.insert(stu)
        self.status.set("插入成功")
        print(db.all())


class SearchFrame(tkinter.Frame):
    def __init__(self, root):
        super().__init__(master=root)
        self.itemName = tkinter.StringVar()

        tkinter.Label(self, text="查询界面").pack()
        self.table_frame = tkinter.Frame(self)
        self.table_frame.pack()
        self.row = 1

        self.create_page()

    def create_page(self):
        tkinter.Button(self, text="刷新数据", command=self.show_data_frame).pack(
            anchor=tkinter.E, pady=5
        )
        self.show_data_frame()

    def show_data_frame(self):
        self.row = 1
        for widget in self.table_frame.winfo_children():
            widget.destroy()
        for item in db.all():
            self.create_table(item) 

    def create_table(self, item):
        tkinter.Label(self.table_frame, text=item["姓名"]).grid(row=self.row, column=0)
        tkinter.Label(self.table_frame, text=item["数学"]).grid(row=self.row, column=1)
        tkinter.Label(self.table_frame, text=item["语文"]).grid(row=self.row, column=2)
        tkinter.Label(self.table_frame, text=item["英语"]).grid(row=self.row, column=3)



class UpdateFrame(tkinter.Frame):
    def __init__(self, root):
        super().__init__(master=root)
        self.itemName = tkinter.StringVar()

        tkinter.Label(self, text="更新界面").pack()
        self.table_frame = tkinter.Frame(self)
        self.table_frame.pack()
        self.row = 1

        self.create_page()

    def create_page(self):
        tkinter.Button(self, text="刷新数据", command=self.show_data_frame).pack(
            anchor=tkinter.E, pady=5
        )
        self.show_data_frame()

    def show_data_frame(self):
        self.row = 1
        for widget in self.table_frame.winfo_children():
            widget.destroy()
        for item in db.all():
            self.create_table(item)
    def create_table(self, item):
        tkinter.Label(self.table_frame, text=item["姓名"]).grid(row=self.row, column=0)
        tkinter.Label(self.table_frame, text=item["数学"]).grid(row=self.row, column=1)
        tkinter.Label(self.table_frame, text=item["语文"]).grid(row=self.row, column=2)
        tkinter.Label(self.table_frame, text=item["英语"]).grid(row=self.row, column=3)    



class DeleteFrame(tkinter.Frame):
    def __init__(self, root):
        super().__init__(master=root)
        self.itemName = tkinter.StringVar()

        tkinter.Label(self, text="删除界面").pack()
        self.table_frame = tkinter.Frame(self)
        self.table_frame.pack()
        self.row = 1

        tkinter.Button


class AboutFrame(tkinter.Frame):
    def __init__(self, root):
        super().__init__(master=root)
        tkinter.Label(self, text="关于界面").pack()
        


if __name__ == "__main__":
    root = tkinter.Tk()
    root.geometry("%dx%d" % (600, 400))
    q = InsertFrame(root)
    q.pack()
    root.mainloop()
