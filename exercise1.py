grade = int(input("Enter grade percentage (out of 100): "))
letter = " "

def percentage_to_letter_grade(grade):
    if grade >= 90:
        letter = "A+"
    elif 90 > grade >= 85:
        letter = "A"
    elif 85 > grade >= 80:
        letter = "A-"
    elif 80 > grade >= 77:
        letter = "B+"
    elif 77 > grade >= 73:
        letter = "B"
    elif 73 > grade >= 70:
        letter = "B-"
    elif 70 > grade >= 67:
        letter = "C+"
    elif 67 > grade >= 63:
        letter = "C"
    elif 63 > grade >= 60:
        letter = "C-"
    elif 60 > grade >= 57:
        letter = "D+"
    elif 57 > grade >= 53:
        letter = "D"
    elif 53 > grade >= 50:
        letter = "D-"
    else:
        letter = "F"
    return letter

letter_grade = percentage_to_letter_grade(grade)
print("A percentage grade of {} is equal to a letter grade of {}".format(grade, letter_grade))
