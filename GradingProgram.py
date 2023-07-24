'''
Write a program that converts their scores to grades. By the end of your program, 
you should have a new dictionary called student_grades that should contain student names for keys and their grades for values. 
The final version of the student_grades dictionary will be checked.'''

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades={}


for j in student_scores:
  score = student_scores[j]
  if score > 90:
    student_grades[j] = "Outstanding"
  elif score > 80:
    student_grades[j] = "Exceeds Expectations"
  elif score > 70:
    student_grades[j] = "Acceptable"
  else:
    student_grades[j] = "Fail"

print(student_grades)
