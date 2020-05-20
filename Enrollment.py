print("Name: abc")
print("ID: 1234567")

count1005 = 0
count1405 = 0
sum1005 = 0
sum1405 = 0

userage = int(input("enter your age: "))
course = str(input("which course you are taking: "))

min1005 = userage
max1005 = userage
min1405 = userage
max1405 = userage

while userage != -1:
    if course.upper() == "COMP1005" :
        sum1005 += userage
        count1005 += 1
        if userage < min1005:
            min1005 = userage    
        if userage > max1005:
            max1005 = userage


    elif course.upper() == "COMP1405" :
        sum1405 += userage
        count1405 += 1
        if userage < min1405:
            min1405 = userage
        if userage > max1405:
            max1405 = userage

    userage = int(input("enter your age: "))
    course = str(input("which course you are taking: "))

if count1005 == 0:
  min1005 = "n/a"
  max1005 = "n/a"
  avg1005 = "n/a"
else:
  avg1005 = sum1005 / count1005  


if count1405 == 0:
  min1405 = "n/a"
  max1405 = "n/a"
  avg1405 = "n/a"
else:
  avg1405 = sum1405 / count1405  

print("COMP1005")
print("min age is " + str(min1005))
print("max age is " + str(max1005))
print("average age is " + str(avg1005))
print("COMP1405")
print("min age is " + str(min1405))
print("max age is " + str(max1405))
print("average age is " + str(avg1405))

if count1005 > count1405:
  print("There are more students in COMP1005 than COMP1405")
elif count1405 > count1005:
  print("There are more students in COMP1405 than COMP1005")
else:
  print("There are equal students in both COMP1005 and COMP1405")
