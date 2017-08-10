class Student:
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID
        self.testScore = []
    def __str__(self):
        nameInfo = "Name: " + self.name
        IDInfo = "ID: " + str(self.ID)
        return nameInfo + " " + IDInfo + "\n"
    def addScore(self, score):
        self.testScore.append(score)
    def averageScore(self):
        a = 0
        for x in self.testScore:
            a = x + a
        average = a / len(self.testScore)
        return average
    def returnInfo(self, average): #prints all this in that order
        nameInfo = "Name: " + self.name
        IDInfo = "ID: " + str(self.ID)
        testScoreInfo = "Test Scores: " + str(self.testScore)
        averageInfo = "Average: " + str(average)
        return nameInfo + "\n" + IDInfo +"\n" + testScoreInfo + "\n" + averageInfo

class Roster:
    def __init__(self): #student is list
        self.studentList = []
    def __str__(self):
        a = "Student: "
        for student in self.studentList:
            a = a + str(student)
        return a

    def addStudent(self, newStudent):
        self.studentList.append(newStudent)

    def deleteStudent(self, studentID):
        for student in self.studentList:
            if student.ID == studentID:
                self.studentList.remove(student)
                return True
        return False
    def viewRecord(self, studentID):
        for student in self.studentList:
            if student.ID == studentID:
                return student.name
        return False



student1 = Student("Philli", 142159)
student2 = Student("Yoii", 120934)
student3 = Student("Franky", 333993)
roster = Roster()
roster.addStudent(student1)
roster.addStudent(student2)
roster.addStudent(student3)

y = roster.viewRecord(333993)
print(y)

x = roster.deleteStudent(142159)
print(x)
print(roster)
