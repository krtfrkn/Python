website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

courseNum = len(course)
print("Course number of char: "+ str(courseNum))

websiteWithoutWWW = website[:7]+website[10:]
print("Website without www: "+ websiteWithoutWWW)

websiteWithoutCom = website[:len(website)-3]
print("Website without com: "+ websiteWithoutCom)

withoutFirst15ofCourse = course[15:]
print("Without first 15 of course: "+ withoutFirst15ofCourse)

withoutLast15ofCourse = course[:len(course)-15]
print("Without last 15 of course: "+ withoutLast15ofCourse)

name , surname , age , job = "Furkan", "Kurt", 35, "Software Engineer"
sentence1 = f"My name is {name} {surname} and I'm {age} years old. I'm a {job}."
sentence2 = "My name is {0} {1} and I'm {2} years old. I'm a {3}.".format(name, surname, age, job)
print(sentence1)
print(sentence2)

threeTimes = "abc"
print("Three times: "+threeTimes * 3)

reverseOfCourse = course[::-1]
print("Reverse of course: "+reverseOfCourse)
