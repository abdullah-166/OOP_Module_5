class Student:
    def __init__(self,name,cls,id):
        self.name = name
        self.id = id
        self.cls = cls
        

    def __repr__(self) -> str:
        return f'student name: {self.name}, class: {self.cls}, id: {self.id}'
    

class Teacher:
    def __init__(self, name, subject, id):
        self.name = name
        self.subject = subject
        self.id = id


    def __repr__(self) -> str:
        return f'Teacher name: {self.name}, subject: {self.subject}, id: {self.id}'
    
    
class School:
    def __init__(self,name):
        self.name = name
        self.teachers = []
        self.students = []


    def add_teacher(self, name, subject):
        id = len(self.teachers) + 101
        teacher = Teacher(name,subject,id)
        self.teachers.append(teacher)


    def enroll(self, name, fee):
        if fee < 6500:
            return 'not enough fee'
        else:
            id = len(self.students)+1
            student = Student(name,'C',id)
            self.students.append(student)
            print(f'{name} is enrolled with {id}, extra money {fee - 6500}')
        

    def __repr__(self) -> str:
        print('welcome to', self.name)
        print('------OUR TEACHERS------')
        for teacher in self.teachers:
            print(teacher)
        print('------OUR STUDENTS------')
        for student in self.students:
            print(student)


phitron = School('Phitron')
phitron.enroll('Abir',5500)
phitron.enroll('akash',6500)
phitron.enroll('arafat',7000)


phitron.add_teacher('suhala lamia', 'csc')
phitron.add_teacher('nusrat jahan sathi', 'sta')


