class Student:
  def __init__(self, name, roll_number, cgpa):
      self.name = name
      self.roll_number = roll_number
      self.cgpa = cgpa
def sort_students(student_list):
  sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
  return sorted_students
students = [
Student ("Durga","22UCS04",9.3),
Student ("praveena","22UCS21",9.4),
Student ("Eswari","22UCS05",9.2),
Student ("Dharaniya","22UCS02",9.1) 
]
sorted_students = sort_students(students)
for student in sorted_students:
  print("name:{},roll Number:{},CGPA:{}".format(student.name,
student.roll_number,student.cgpa))