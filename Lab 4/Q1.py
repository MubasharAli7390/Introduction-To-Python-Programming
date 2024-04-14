#Write a program that input marks of 5 subject from user, then show grade wise subject.
MH = float(input("Enter marks of Math: "))
CS = float(input("Enter marks of Computer Science: "))
Eng = float(input("Enter marks of English: "))
Ur = float(input("Enter marks of Urdu: "))
Chem = float(input("Enter marks of Chemistry: "))
if  MH >= 90:
    MH_grade = "A+"
elif MH >= 80 and MH < 90:
    MH_grade = "A"
elif MH >= 70 and MH < 80:
    MH_grade = "B+"
elif MH >= 60 and MH < 70:
    MH_grade = "B"
elif MH >= 50 and MH < 60:
    MH_grade = "C"
else:
    MH_grade = "F"
if  CS >= 90:
    CS_grade = "A+"
elif CS >= 80 and CS < 90:
    CS_grade = "A"
elif CS >= 70 and CS < 80:
    CS_grade = "B+"
elif CS >= 60 and CS < 70:
    CS_grade = "B"
elif CS >= 50 and CS < 60:
    CS_grade = "C"
else:
    CS_grade = "F"
if  Eng >= 90:
    Eng_grade = "A+"
elif Eng >= 80 and Eng < 90:
    Eng_grade = "A"
elif Eng >= 70 and Eng < 80:
    Eng_grade = "B+"
elif Eng >= 60 and Eng < 70:
    Eng_grade = "B"
elif Eng >= 50 and Eng < 60:
    Eng_grade = "C"
else:
    Eng_grade = "F"
if  Ur >= 90:
    Ur_grade = "A+"
elif Ur >= 80 and Ur < 90:
    Ur_grade = "A"
elif Ur >= 70 and Ur < 80:
    Ur_grade = "B+"
elif Ur >= 60 and Ur < 70:
    Ur_grade = "B"
elif Ur >= 50 and Ur < 60:
    Ur_grade = "C"
else:
    Ur_grade = "F"
if  Chem >= 90:
    Chem_grade = "A+"
elif Chem >= 80 and Chem < 90:
    Chem_grade = "A"
elif CS >= 70 and Chem < 80:
    Chem_grade = "B+"
elif Chem >= 60 and Chem < 70:
    Chem_grade = "B"
elif Chem >= 50 and Chem < 60:
    Chem_grade = "C"
else:
    Chem_grade = "F"

print("Math grade: ", MH_grade)
print("Computer Science grade: ", CS_grade)
print("English grade: ", Eng_grade)
print("Urdu grade: ", Ur_grade)
print("Chemistry grade: ", Chem_grade)