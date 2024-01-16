import json

info = """
************************************************
欢迎使用【学生信息管理系统】V1.0
请选择你想要进行的操作
1.新建学生信息
2.显示全部信息
3.查询学生信息
4.删除学生信息
5.修改学生信息

0.退出系统

************************************************
"""
# students = [
#     {"name": "张三", "math": 90, "english": 85, "chinese": 95, "total": 270},
#     {"name": "李四", "math": 80, "english": 88, "chinese": 92, "total": 260},
#     {"name": "王五", "math": 85, "english": 83, "chinese": 90, "total": 258},
# ]
with open("students.json", "r", encoding="utf-8") as f:
    students = json.load(f)


while True:
    print(info)

    # 从外部输入用户操作
    action = input("小伙子请输入你的操作：")
    # 根据用户操作，执行相应的代码
    if action == "1":
        # print("新建学生信息")
        name = input("请输入学生姓名：")
        math = int(input("请输入数学成绩："))
        english = int(input("请输入英语成绩："))
        chinese = int(input("请输入语文成绩："))
        total = math + english + chinese
        students.append(
            {
                "name": name,
                "math": math,
                "english": english,
                "chinese": chinese,
                "total": total,
            }
        )
    elif action == "2":
        # print('2. 显示全部信息')
        print("姓名\t数学\t语文\t英语\t总分")
        for student in students:
            print("{}\t{}\t{}\t{}\t{}".format(*student.values()))
    elif action == "3":
        # print("查询学生信息")
        name = input("请输入学生姓名：")
        for student in students:
            if student["name"] == name:
                print("姓名\t数学\t语文\t英语\t总分")
                print("{}\t{}\t{}\t{}\t{}".format(*student.values()))
                break
        else:
            print("查无此人{}".format(name))

    elif action == "4":
        #print("删除学生信息")
        name = input("请输入学生姓名：")
        for student in students:
            if student["name"] == name:
                del students[students.index(student)]
                print("删除成功")
                break
        else:
            print("查无此人{}".format(name))
    elif action == "5":
        print("修改学生信息")
        name = input("请输入学生姓名：")
        for student in students:
            if student["name"] == name:
                
                math = input("请输入数学成绩：")
                if math:
                    student["math"] = int(math)

                chinese = input("请输入语文成绩：")
                if chinese:
                    student["chinese"] = int(chinese)
               
                english = input("请输入英语成绩：")
                if english:
                    student["english"] = int(english)
               
             
                student["total"] = student["math"] + student["english"] + student["chinese"]
                print("修改成功")
                break
        else:
            print("查无此人{}".format(name))

    elif action == "0":
        print("退出系统")
        with open("students.json", mode="w", encoding="utf-8") as f:
            f.write(json.dumps(students, indent=4, ensure_ascii=False))
        break
    else:
        print("无效操作，请重新输入")
