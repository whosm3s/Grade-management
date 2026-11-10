# Student Grade Management System

def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


student_name = input("Enter student name: ")

while True:
    try:
        subjects = int(input("Enter number of subjects: "))
        if subjects > 0:
            break
        else:
            print("Number of subjects must be greater than zero.")
    except ValueError:
        print("Please enter a valid number.")

marks = []
subject_names = []

for i in range(subjects):
    subject = input(f"Enter name of subject {i+1}: ")
    subject_names.append(subject)

    while True:
        try:
            mark = float(input(f"Enter mark for {subject}: "))
            if 0 <= mark <= 100:
                marks.append(mark)
                break
            else:
                print("Mark must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")

average = sum(marks) / len(marks)
grade = calculate_grade(average)

print("\n===== STUDENT REPORT =====")
print("Student:", student_name)

for subject, mark in zip(subject_names, marks):
    print(f"{subject}: {mark}")

print(f"Average: {average:.2f}")
print(f"Grade: {grade}")