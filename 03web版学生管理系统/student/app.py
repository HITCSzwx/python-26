# 导入 Flask 对象
# https://bootstrapdoc.com/docs/5.0/content/tables
from flask import Flask, render_template, request, redirect

# 使用 Flask 对象创建一个 app 对象
app = Flask(__name__)

students = [
    {'name': '张三', 'chinese': '65', 'math': '65', 'english': '65'},
    {'name': '李四', 'chinese': '65', 'math': '65', 'english': '65'},
    {'name': '王五', 'chinese': '65', 'math': '65', 'english': '65'},
    {'name': '赵六', 'chinese': '65', 'math': '65', 'english': '65'},
]


# 路由
@app.route('/')  # / 访问的路径
def hello_world():
    return 'Hello World!'


@app.route('/login', methods=['GET', 'POST'])
def login():
    # 登录的功能
    # 全栈项目，前后端不分离
    # return '需要实现登录的逻辑'
    # request 对象可以拿到浏览器传递给服务器的所有数据
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # 登录成功之后，链接数据库，校验账号密码
        print('从服务器接收到的数据：', username, password)
        # 登录成功之后，应该调转到管理页面
        return redirect('/admin')
    return render_template('login.html')


@app.route('/admin')
def admin():
    # 重点 复制框架源码
    return render_template('admin.html', students=students)


@app.route('/add', methods=["GET", "POST"])
def add():
    if request.method == 'POST':
        username = request.form.get('username')
        chinese = request.form.get('chinese')
        math = request.form.get('math')
        english = request.form.get('english')
        print('获取的学员信息', username, math, chinese, english)
        students.append({'name': username, 'chinese': chinese, 'math': math, 'english': english})
        return redirect('/admin')
    return render_template('add.html')


@app.route('/delete')
def delete_student():
    # 在后台需要拿到学员的名字
    print(request.method)
    username = request.args.get('name')
    # 找到学员并删除信息
    for stu in students:
        if stu['name'] == username:
            students.remove(stu)
    return redirect('/admin')


@app.route('/change', methods=["GET", "POST"])
def change_student():
    # 先显示学员的数据，然后再浏览修改，提交到服务器保存
    username = request.args.get('name')

    if request.method == "POST":
        username = request.form.get('username')
        chinese = request.form.get('chinese')
        math = request.form.get('math')
        english = request.form.get('english')

        for stu in students:
            if stu['name'] == username:
                stu['math'] = math
                stu['chinese'] = chinese
                stu['english'] = english

        return redirect('/admin')
    for stu in students:
        if stu['name'] == username:
            # 需要在页面中渲染学生的成绩数据
            return render_template('change.html', student=stu)


# 需要实现其他的功能（例如退出、查看学生信息）等等其他的功能，该怎么实现
if __name__ == '__main__':
    app.run()

"""
    你的目标决定了你的努力程度
    
    一期学不会学两期
    
    6880 多吗？ 学会了之后出去找工作
    一整套的学习方案 最小的学员 小学五年级 你遇到的问题其他学员早就遇到过了
    
    TCL 维护工程师 薪资6-8k 加班获取加班工资
    能力不够 时间来凑 （蹭加班）
    大学生实在是太多了（什么都不会的）
    八小时之内求生存，八小时之外求发展 
    转行编程 java  18880 五个月的时间 租房 伙食 3-4万
    
    刚培训出来薪资比较低 只有 8K 后面又跳了几次槽
    
    学费要钱  技术能力可以赚钱
    
    项目
"""
