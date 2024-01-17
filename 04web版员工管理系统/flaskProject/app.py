from flask import Flask, render_template, request
from data import salary_list

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    # 返回网页文件
    return render_template('index.html')


@app.route('/login', methods=["POST"])
def hello_login():
    # 登录到服务器 获取用户名与密码,然后进行校验,再记录信息
    # print(request.form)
    username = request.form.get('username')
    password = request.form.get('password')
    print(username, password)
    # 获取用户名与密码,然后进行校验,再记录信息
    # for sal in salary_list:
    #     if sal['name'] == username:

    # 登录成功之后返回后台页面
    return render_template('admin.html',
                           salary_list=salary_list)


@app.route('/delete/<name>')
def hello_delete(name):  # put application's code here
    # 删除逻辑 先找到信息,然后再删除
    for salary in salary_list:
        if salary['name'] == name:
            # 列表删除元素的几种方式
            salary_list.remove(salary)
    return render_template('admin.html',
                           salary_list=salary_list)


@app.route('/change/<name>')
def hello_change(name):  # put application's code here
    # 删除逻辑 先找到信息,然后再删除
    for salary in salary_list:
        if salary['name'] == name:
            # 应该是在前端进行修改
            return render_template('change.html',
                                   user=salary)

    return render_template('admin.html',
                           salary_list=salary_list)


@app.route('/changed/<name>', methods=["POST"])
def hello_changed(name):
    """修改 拿到提交的信息"""
    # 删除逻辑 先找到信息,然后再删除
    for salary in salary_list:
        if salary['name'] == name:
            salary['name'] = request.form.get('name')
            salary['department'] = request.form.get('department')
            salary['position'] = request.form.get('position')
            salary['salary'] = request.form.get('salary')

    return render_template('admin.html',
                           salary_list=salary_list)


@app.route('/add')
def hello_add():
    return render_template('add.html')


@app.route('/add2', methods=['POST'])
def hello_add2():
    salary = {}
    # 获取浏览器发送过来的数据
    salary['name'] = request.form.get('name')
    salary['department'] = request.form.get('department')
    salary['position'] = request.form.get('position')
    salary['salary'] = request.form.get('salary')
    # 将数据保存
    salary_list.insert(0, salary)
    # 返回保存之后的页面
    return render_template('admin.html',
                           salary_list=salary_list)


"""
    学 跟着 文章/视频/教程  教学(少部分人才能做到) 学习一遍
    习 写案例/写作业 检查是否学会了  如果想要学会,一定要敲
    做项目 用学习到的知识做有价值的东西

    先看一遍直播(学习知识点), 然后再写案例(了解知识点的应用场景) 敲代码是增加熟悉程度
    写作业 (整套的课件/源码/作业/老师的上课笔记/答疑)  VIP 直接加到微信
    上课时间 1 3 5 / 2 4 6  晚上8点到10点 提前半个小时开课 7:30 讲作业,可能还会拖堂答疑
    赶不上直播的,可以提前跟老师请假,课后单独辅导
    
    (整套的课件/源码/作业/老师的上课笔记/答疑) 
    讲师一对一的解答,有不懂的直接找到老师就行了 解答方式: QQ/微信/电话/远程协助  VIP 直接加到微信
    
    全套高薪就业班: 9380 优惠价 7880  
        双十一期间 满 300-30 7100 = 592
        赠送两年的学习权限 十二期分期免息 
        赠送两个课程 4860
        
    一次性收费,不存在二次收费,课程更新免费学       课程更新之后会继续涨价
    
    是学费不是消费
        报名之后,跟着老师完成每天的上课,作业,案例,答疑,项目,
        有不懂的课随时找老师沟通,经过七个月的学习之后,才能找到这样的工作
    
    兴趣 + 毕设
    想找工作
    编程 python
    门槛
"""

if __name__ == '__main__':
    app.run()
