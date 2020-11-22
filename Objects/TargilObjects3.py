from Objects.Amud1 import Course

course1 = Course()
course1.number = input("enter a course number: \n")
course1.name = input("enter a course name: \n")
course1.enrolled = int(input("enter a number of enrolled students rn: \n"))
course1.max = int(input("enter the maximux number of students possible: \n"))
course1.write()

newstdns = int(input("enter the number of new students that want to enroll: \n"))
course1.newstudents(newstdns)
course1.write()

