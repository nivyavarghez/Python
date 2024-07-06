def get_student_details():
    students = []
    n = int(input("Enter the number of students: "))
    
    for _ in range(n):
        name = input("Enter the student's name: ")
        roll_no = input("Enter the student's roll number: ")
        total_mark = int(input("Enter the student's total marks: "))
        students.append({'name': name, 'roll_no': roll_no, 'total_mark': total_mark})
    
    return students

def find_top_student(students):
    top_student = max(students, key=lambda x: x['total_mark'])
    return top_student

# Example usage
students = get_student_details()
top_student = find_top_student(students)

print("\nDetails of the student with the highest total marks:")
print(f"Name: {top_student['name']}")
print(f"Roll Number: {top_student['roll_no']}")
print(f"Total Marks: {top_student['total_mark']}")
