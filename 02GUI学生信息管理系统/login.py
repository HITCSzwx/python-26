""""""
"""
使用面向对象与GUI编程，打造一个桌面版的学生信息管理系统。

让我们一起看一下使用面向对象编程思维写出来的代码是怎么样的。

课题：使用 python 打造桌面版学生信息管理系统
课程时间：20:00-22:00
讲师：正心老师

课程收获：
    - Tkinter 的使用（GUI）
    - 面向对象编程思维

开发环境：
    1. 解释器： Python 3.6.5 | Anaconda, Inc.
    2. 编辑器： pycharm 社区版
"""
import tkinter as tk
import tkinter.messagebox
from main import MainPage

# 标准开发代码
class LoginPage:
    """登录界面"""

    def __init__(self, master):
        # 将画板绑定到实例对象
        self.root = master
        # self.page 画纸
        self.page = tk.Frame(self.root)
        self.page.pack()
        self.root.geometry("%dx%d" % (300, 180))

        # tkinter 提供的可变变量
        self.username = tk.StringVar()
        self.password = tk.StringVar()

        # 创建一个lab
        # 网格布局
        tk.Label(self.page).grid(row=0, column=0)
        # textvariable 这个参数是把 tkinter 里面的字符串变量与 空间绑定起来
        tk.Label(self.page, text="账户").grid(row=1, column=0, stick=tk.E, pady=10)
        tk.Entry(self.page, textvariable=self.username).grid(row=1, column=1, stick=tk.W, pady=10)
        tk.Label(self.page, text="密码").grid(row=2, column=0, stick=tk.E, pady=10)
        tk.Entry(self.page, textvariable=self.password).grid(row=2, column=1, stick=tk.W, pady=10)
        # command 接受一个函数 执行登录的逻辑
        tk.Button(self.page, text="登录", command=self.login_check).grid(row=3, column=0, stick=tk.W, pady=10)
        tk.Button(self.page, text="退出").grid(row=3, column=1, stick=tk.E, pady=10)

    def login_check(self):
        """检验登录"""
        # 拿到账号与密码
        name = self.username.get()
        pwd = self.password.get()
        # 不去查询数据库
        print(name, pwd)
        if name == 'admin' and pwd == '123456':
            print('恭喜登录成功')
            # 摧毁当前页面绘制的内容
            self.page.destroy()
            # 页面的切换
            MainPage(self.root)
        else:
            tkinter.messagebox.showinfo(title='错误', message='账户或者密码错误')


if __name__ == '__main__':
    # 创建一个对象 窗口对象
    root = tk.Tk()
    LoginPage(root)
    # 显示界面
    root.mainloop()

"""
    界面 UI
    代码的逻辑
    数据库 只要联网就能用
"""
"""
    基础知识、基本语法、python的语言特性
    思路，

"""
"""
基础课程： 基本数据类型、基本流程控制、基本数据容器、函数

进阶课程： tkinter、面向对象（封装、继承、魔法函数、元类编程）、
          网络编程、并发编程、内置函数（特性、反射、、、）、
          python语法（装饰器、迭代器、生成器、垃圾回收）、mysql（数据库）、Linux、git

爬虫课程：爬虫知识、数据解析、数据保存、反扒技术（验证码、模拟登陆、模拟点击）
         scrapy、redis、MongoDB数据库、分布式爬虫、js解密

数分课程：数据清洗、数据处理（numpy/pandas）、数据可视化（matplotliob/pyechart）、数据分析（数学模型、算法）

全栈课程：html/css/js, flask(权鉴、会话、反扒、数据、Linux、服务器、项目部署的)

最重要

从入门到放弃


看大量的书看大量的教程
    到大内容中总结 高频的知识点
    要学的是一种能力，培养自己的思路，构建自己的编程体系（技术栈）
    
    记笔记 + 学习 
    
    好多不懂 不要去纠结 继续学，说不定后面那天就懂了
    
    培养自己的学习能力，与编程思维，注意代码的编程规范
    
    花费很长的时间，
    
    
"""