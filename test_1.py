grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_list = sorted(list(students))
middle_grades = []
for grade in grades:
    middle_grades.append(sum (grade) /len (grade))
students_grades = dict(zip(students_list,middle_grades))
print(students_grades)

