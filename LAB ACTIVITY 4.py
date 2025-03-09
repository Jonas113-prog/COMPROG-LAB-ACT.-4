def assign_grade(score):
    if score < 0 or score > 100:
        print("Invalid score! Please enter a value between 0 and 100.")
    elif score >= 80:
        print("Grade: A")
    elif score >= 75:
        print("Grade: B")
    elif score >= 70:
        print("Grade: C")
    elif score >= 65:
        print("Grade: D")
    else:
        print("Grade: F")

assign_grade(81)
assign_grade(76)
assign_grade(71)
assign_grade(66)
assign_grade(64)