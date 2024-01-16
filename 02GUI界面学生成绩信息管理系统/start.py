import tkinter


from main import MainPage


class LoginPage:
    def __init__(self, root2):
        # 定义一个窗口对象
        self.root = root2
        # 设置标题
        self.root.title("学生信息管理系统0.0.1")
        self.root.geometry("500x300")

        self.login_frame = tkinter.Frame(self.root)
        self.login_frame.grid(row=0, column=0)

        self.username = tkinter.StringVar()
        self.password = tkinter.StringVar()
        self.create_page()
        # 显示窗口对象
        # self.root.mainloop()
        self.logged_in = False

    def create_page(self):
        tkinter.Label(self.login_frame, height=3, width=35).grid(row=0, column=0)
        tkinter.Label(self.login_frame, text="账户").grid(row=1, column=0)
        tkinter.Label(self.login_frame, text="密码").grid(row=2, column=0)

        tkinter.Entry(self.login_frame, textvariable=self.username).grid(
            row=1, column=1
        )
        tkinter.Entry(self.login_frame, textvariable=self.password).grid(
            row=2, column=1
        )
        tkinter.Label(self.login_frame, height=1, width=25).grid(row=3, column=0)

        tkinter.Button(self.login_frame, text="登录", command=self.check_login).grid(
            row=4, column=0
        )
        tkinter.Button(self.login_frame, text="退出", command=self.root.quit).grid(
            row=4, column=1
        )

    def check_login(self):
        print("检查登录")
        print("用户名：", self.username.get())
        print("密码：", self.password.get())
        if self.username.get() == "admin" and self.password.get() == "123456":
            print("登录成功")
            self.login_frame.destroy()
            # 登录成功
            self.logged_in = True
            MainPage(self.root)
        else:
            print("登录失败")


if __name__ == "__main__":
    root = tkinter.Tk()

    login_page = LoginPage(root)

    root.mainloop()
