# age = float(input("enter your age: ")) 

# if age < 3:
#     ticket_price = 0
# elif age >= 3 and age <= 12:
#     ticket_price = 10
# elif age >= 13 and age <= 17:
#     ticket_price = 12
# else:
#     ticket_price = 15
# print("Ticket price: $" + str(ticket_price))

# score = int(input("enter your exam score: ")) 

# if score >= 90:
#     grade = "A"
# elif score >= 80:
#     grade = "B" 
# elif score >= 70:
#     grade = "C"
# elif score >= 60:
#     grade = "P"
# else:
#     grade = "F"
# print("Grade:" ,grade )


def calculate_average_grade(grades):
    sum_grades = 0
    count_value_grades = 0
    for grade in grades:
        try:
            if grade < 0 or grade > 100:
                raise ValueError("Invalid: " + str(grade)) 
            sum_grades += grade
            count_value_grades += 1
        except ValueError as e:
            print(e) 
    if count_value_grades == 0:
        return 0
    else:
        average_grade = sum_grades / count_value_grades
        return average_grade
# Main program
students_grades = [80, 95, 70, -10, 88, 102, 77, 92] 

average = calculate_average_grade(students_grades)

print("Average grade: ", average)

