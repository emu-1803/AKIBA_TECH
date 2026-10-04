student_name = input("Student name: ")
python_score = float(input("Python score: "))
english_score = float(input("English score: "))
mathematics_score = float(input("Mathematics score: "))

average = (python_score + english_score + mathematics_score) / 3

print()
print(f"Student: {student_name}")
print(f"Python: {python_score}")
print(f"English: {english_score}")
print(f"Mathematics: {mathematics_score}")
print(f"Average: {average:.2f}")