class student(object):
    def __init__(self, name, id, grade):
        self.name = name
        self.id = id
        self.grade = grade
    
    def output(self):
        print('Student: ' + self.name + ', ID: ' + self.id + ', grade: ' + self.grade)

x = student('Jeff', '113590053', '100')
y = student('Jason', '113590054', '60')
x.output()
y.output()