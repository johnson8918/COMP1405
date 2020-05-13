print("Grade Calculator")
print("----------------------------------------")
name = input("Please enter student name: ")

assign =  0.5 * float(input(name + ", please enter your assignment grade: "))
test1 = float(input(name + ", please enter your midterm 1 grade: "))
test2 = float(input(name + ", please enter your midterm 2 grade: "))
exam = 0.26 * float(input(name + ", please enter your exam grade: "))

if test2 > test1 :
    midterm = (0.08 * test1) + (0.16 * test2)
else:
    midterm = 0.12 * (test1 + test2)


if (exam + midterm) < 50 :
    final = 2 * (midterm + exam)
else:
    final = assign + midterm + exam

print("----------------------------------------")
print("Your final grade is: ", final)
