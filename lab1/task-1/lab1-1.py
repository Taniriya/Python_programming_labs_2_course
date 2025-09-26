class Student:
  def __init__(self, name: str, group: int, grades: list):
      self.__name = name
      self.__group = group
      self.__grades = grades
  def average_grade(self):
      return f'Ваш средний балл: {sum(self.__grades)/len(self.__grades)}'
  def is_excelent(self):
      if (sum(self.__grades)/len(self.__grades)) >= 4.5:
        return True
      else:
        return False
  def get_info(self):
      return f'{self.__name} - {self.__group}'


name_list = []
count = 0
with open('students.txt', 'r', encoding="utf-8") as f:
  for line in f:
    name, group, grades = map(str, line.strip().split(';'))
    grades_list = [int(i) for i in map(str, grades.split(','))]
    name_list.append(name)
    name_list[count] = Student(name, group, grades_list)
    count += 1

grages_avg = [0, 0, 0, 0]
with open('excellent_students.txt', 'w', encoding="utf-8") as f:
  for i in range(len(name_list)):
    if name_list[i].is_excelent():
      f.writelines(name_list[i].get_info() + '\n')
