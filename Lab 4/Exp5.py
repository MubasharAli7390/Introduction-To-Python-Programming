#Determining the grade of a student based on their score:
score = float(input("Enter your score: "))
if  score >= 90:
    grade = "A+"
elif score >= 80 and score < 90:
    grade = "A"
elif score >= 70 and score < 80:
    grade = "B+"
elif score >= 60 and score < 70:
    grade = "B"
elif score >= 50 and score < 60:
    grade = "C"
else:
    grade = "F"
    
print(grade)




