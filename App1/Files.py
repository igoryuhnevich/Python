#------------------------------------------------------
# Programm by Igor Uk.
#
#
#Version     Date          Info
#1.0         24.11.24     Initial version
#Hello Hello
#------------------------------------------------------


inputfile = "App1/my_file.txt"
outputfile = "App1/my_file1.txt"

password_to_lookfor = "F"

myfile = open(inputfile,'r',encoding='utf-8')  # в переменной хранится pointer на файл.
myfile1 = open(outputfile,'a',encoding='utf-8')

for num, line in enumerate(myfile,1):
    if password_to_lookfor in line:
        print("Hello " + str(num) + ":" + line.strip())
        myfile1.write("find F in " + line)
    else:
        myfile1.write("not found - F" + line) 


myfile1.close()
myfile.close()        

