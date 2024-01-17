import json


class StudentsDB:
    def __init__(self):
        self.students = []
        self._load_students_data()

    def insert(self, student):
        self.students.append(student)

    def all(self):
        return self.students

    def delete_by_name(self, name):
        for student in self.students:
            if name == student['name']:
                self.students.remove(student)
                break
        else:
            return False
        return True

    def search_by_name(self, name):
        for student in self.students:
            if name == student['name']:
                return student
        else:
            return False

    def update(self, stu):
        name = stu['name']
        for student in self.students:
            if name == student['name']:
                student.update(stu)
                return True
        else:
            return False

    def _load_students_data(self):
        with open('students.json', mode='r', encoding='utf-8') as f:
            text = f.read()
        if text:
            self.students = json.loads(text)

    def save_data(self):
        with open('students.json', mode='w', encoding='utf-8') as f:
            text = json.dumps(self.students, ensure_ascii=False)
            f.write(text)


db = StudentsDB()

if __name__ == '__main__':
    del db #删除所有学生
