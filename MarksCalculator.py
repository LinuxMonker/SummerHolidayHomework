print("Marks Calculator")
max_marks=int(input("Enter the maximum marks which can be obtained: \n"))
num_subjects = int(input("Enter the number of subjects: \n"))
marks = {}

#subject data collection
for i in range(num_subjects):
    subject_name = input(f"Enter the name of subject {i + 1}: \n")
    marks[subject_name] = float(input(f"Enter marks obtained in {subject_name}: \n"))

#percentage calculation
marks_sum=sum(marks.values())
percentage=(marks_sum/(max_marks*num_subjects))*100

#grade calculation
if percentage >= 91:
    grade = "A1"
elif 81 <= percentage <= 90:
    grade = "A2"
elif 71 <= percentage <= 80:
    grade = "B1"
elif 61 <= percentage <= 70:
    grade = "B2"
elif 51 <= percentage <= 60:
    grade = "C1"
elif 41 <= percentage <= 50:
    grade = "C2"
elif 33 <= percentage <= 40:
    grade = "D"
else:
    grade = "E (Needs Improvement)"

#results print
print(" ")
print("Your grade is", grade,".")

print("Your percentage is", percentage,".")

for subject, score in marks.items():
    print(f"{subject}: {score}")
