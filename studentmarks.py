def calculate_grade(marks):
    average = sum(marks) / len(marks)

    if 90 <= average <= 100:
        return "S"
    elif 80 <= average < 90:
        return "A"
    elif 65 <= average < 80:
        return "B"
    elif 50 <= average < 65:
        return "C"
    elif 40 <= average < 50:
        return "D"
    else:
        return "F"


def get_student_details():
    name = "srigouri"
    department = "BCA"
    semester = 3

    marks = []
    for i in range(1, 4):
        mark = 70 
        marks.append(mark)

    grade = calculate_grade(marks)

    print("\n--- Student Result ---")
    print("Name:", name)
    print("Department:", department)
    print("Semester:", semester)
    print("Marks:", marks)
    print("Grade:", grade)


if __name__ == "__main__":
    get_student_details()
