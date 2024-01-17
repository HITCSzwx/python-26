""""""
"""
课题：学生信息管理系统

新手小白的福利课，零基础也能上手的项目课——学生信息管理系统。

知识点：
    基本的数据类型与结构(int/str/float/bool, list,dict,tuple,set)
    基本的逻辑控制语句(if/for/while/break/continue)
    
打卡截图发老师微信号获取当录播与资料
婧琪老师微信号：Python_jingqi
    + Python的安装包、安装视频
    + Pycharm的安装包、安装视频
    + 虚拟机与ubuntu的安装包、安装视频
    + 常用的安装包与安装资料
"""
info = """
**************************************************
欢迎使用【学生信息管理系统】V1.0
请选择你想要进行的操作
1. 新建学生信息
2. 显示全部信息
3. 查询学生信息
4. 删除学生信息
5. 修改学生信息

0. 退出系统
**************************************************"""
import json

# students = [
#     {'name': '张三', 'math': 65, 'chinese': 65, 'english': 65, 'total': 195},
#     {'name': '李四', 'math': 65, 'chinese': 65, 'english': 65, 'total': 195},
# ]

with open('students.json', mode='r', encoding='utf-8') as f:
    text = f.read()
students = json.loads(text)
while True:
    print(info)
    # 从外部输入用户的操作
    action = input('请选择你想要的进行的操作:')
    # 增删改查, 应该在那里面操作
    if action == '1':
        print('1. 新建学生信息')
        name = input('请输入学生的名字:')
        math = int(input('请输入学生的数学成绩:'))
        chinese = int(input('请输入学生的语文成绩:'))
        english = int(input('请输入学生的英语成绩:'))

        total = math + chinese + english
        students.append({
            'name': name,
            'math': math,
            'chinese': chinese,
            'english': english,
            'total': total})

    elif action == '2':
        # print('2. 显示全部信息')
        print('姓名\t数学\t语文\t英语\t总分')
        for student in students:
            print('{}\t{}\t\t{}\t\t{}\t\t{}'.format(*student.values()))
    elif action == '3':
        # print('3. 查询学生信息')
        name = input('请输入你想查询的学员名字:')
        for student in students:
            # for 循环下面会查找三个
            if student['name'] == name:
                print('姓名\t数学\t语文\t英语\t总分')
                print('{}\t{}\t\t{}\t\t{}\t\t{}'.format(*student.values()))
                break
        else:
            # 学员不存在只有一个
            print(f'{name} 这个学员不存在')
    elif action == '4':
        print('4. 删除学生信息')
        name = input('请输入你想要的删除的学员姓名')
        for student in students:
            if student['name'] == name:
                # 把原本打印新的地方变成删除的
                # del pop remove
                # students.remove(student)
                # students.pop(students.index(student))
                del students[students.index(student)]
                break
        else:
            # 学员不存在只有一个
            print(f'{name} 这个学员不存在')
    elif action == '5':
        # 首先找到学员,然后在修改学员的信息
        name = input('请输入你想要的修改的学员姓名')
        print('(如果输入为空,就不修改学生信息)')
        for student in students:
            if student['name'] == name:
                # 如果不输入内容,就不修改成绩
                math = input('请重新输入学生的数学成绩:')
                if math:
                    math = int(math)
                    student['math'] = math

                chinese = input('请重新输入学生的语文成绩:')
                if chinese:
                    chinese = int(chinese)
                    student['chinese'] = chinese

                english = input('请重新输入学生的英语成绩:')
                if english:
                    english = int(english)
                    student['english'] = english
                student['total'] = student['math'] + student['chinese'] + student['english']
                break
        else:
            # 学员不存在只有一个
            print(f'{name} 这个学员不存在')

    elif action == '0':
        print('0. 退出系统')
        with open('students.json', mode='w', encoding='utf-8') as f:
            f.write(json.dumps(students, ensure_ascii=False))
        break
    else:
        print('你输入的选项错了,请重新在选择')
