website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

str1 = " Hello World! "
result1 = str1.strip()
print(result1)

str2 = "www.furkankurt.com"
result2 = str2.replace("furkankurt","")
print(result2)

str3 = "course"
result3 = str3.upper()
print(result3)

str4 = "website"
result4 = str4.count("e")
print(result4)

result5 = str4.startswith("www")
print(result5)

result6 = str4.endswith('te')
print(result6)

result7 = str4.isalpha()
print(result7)

result8 = str4.isdigit()
print(result8)

result9 = str4.center(50,"*")
print(result9)

result10= str1.replace(" ","-")
print(result10)

result11 = course.split()
print(result11)