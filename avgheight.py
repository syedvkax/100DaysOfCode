# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
count = 0
for student in student_heights:
  student += student
  count += 1

# Calculation of Average height of students

avg_height = student / count
print(f"Average height of student is: {avg_height}")