""""""
"""
你是不是现在在用python做爬虫，那么其实我们爬取的网站，也可以用python去开发，
今天带你初步了解 python的一个小而美的框架 Flask，并且带领大家完成一个简单的视频搜索网站


课题：《零基础入门 Flask 框架，带你打造视频搜索网站》
课程时间：20:00-22:00
讲师：正心老师


开发环境：
    1. 解释器： Python 3.6.5 | Anaconda, Inc.
    2. 编辑器： pycharm 专业版  不是这个编辑器敲1

知识点：
    1. 安装配置 flask 运行的环境
    2. sqlite3 数据库
    3. 视图函数与路由
"""
from flask import Flask, render_template, request  # 框架

from models import DB

# 使用 flask 创建一个应用
app = Flask(__name__)


# 路由 实现请求的分发
@app.route('/')
def index():  # 实现分发的视图函数
    # 需要返回 html 文件
    """"""
    """
        mvt
        m models        模型 数据模型
        v view          视图 视图函数
        t templates     模板 模板文件
        定制化需求 
    """
    return render_template('index.html')  # 返回给浏览器的内容


# 输入搜索内容，点击提交
@app.route('/result', methods=['POST'])
def result():
    name = request.form.get('search_text')
    print(f"Searching for: {name}")
    data = DB().search_by_name(name)
    print(f"Query result: {data}")
    return render_template('result.html', results=data)


if __name__ == '__main__':
    app.run()
