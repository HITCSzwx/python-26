from flask import Flask, render_template, request, redirect

app = Flask(__name__)  # 使用Flask应用的APP对象
students = [
    {
        "name": "张三",
        "math": 1,
        "english": 1,
        "chinese": 1,
        "total": 3
    },
    {
        "name": "李四",
        "math": 80,
        "english": 88,
        "chinese": 92,
        "total": 260
    },
    {
        "name": "王五",
        "math": 85,
        "english": 83,
        "chinese": 90,
        "total": 258
    }
]


@app.route('/')  # 定义一个路由，当用户访问根路径时，执行hello_world函数
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        print("从服务器接受到的数据：", username, password)
        return redirect('/admin')
    return render_template('login.html')


@app.route('/admin')
def admin():
    return render_template('admin.html', students=students)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form.get('name')
        math = request.form.get('math')
        english = request.form.get('english')
        chinese = request.form.get('chinese')
        print("从服务器接受到的数据：", name, math, english, chinese)
        students.append({
            "name": name,
            "math": math,
            "english": english,
            "chinese": chinese,
            "total": int(math) + int(english) + int(chinese)
        })
        return redirect('/admin')
    return render_template('add.html')


@app.route('/delete')
def delete():
    print(request.method)
    name = request.args.get('name')
    for stu in students:
        if stu['name'] == name:
            students.remove(stu)
    return redirect('/admin')


@app.route('/change', methods=['GET', 'POST'])
def change():
    name = request.args.get('name')
    if request.method == 'POST':
        name = request.form.get('name')
        math = request.form.get('math')
        english = request.form.get('english')
        chinese = request.form.get('chinese')
        for stu in students:
            if stu['name'] == name:
                stu['math'] = math
                stu['english'] = english
                stu['chinese'] = chinese
                stu['total'] = int(math) + int(english) + int(chinese)
        return redirect('/admin')
    for stu in students:
        if stu['name'] == name:
            return render_template('change.html', student=stu)



if __name__ == '__main__':
    app.run()
