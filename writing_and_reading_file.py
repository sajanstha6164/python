#This is the way to write in any file
#student_file=open("student.txt","w")
#num=int(input("Enter the total number of new student: "))
#a=1
#while num>0:
#   student_file.write(name+"\n")
#    num=num-1
 #   a=a+1
#student_file.close()

#This is the way to read any file
student_file=open("student.txt","r")
#print(student_file.read())
print(student_file.readline())
for student in student_file.readline():
    print(student)
student_file.close()
