import os


try:
  file = open ("App1\my_file.txt",'a',encoding='utf-8')
  try:
      """print(file.read(5))
      #file.seek(0)
      """
      """pos = file.seek(1)
      print(pos)"""

      """
      s= file.readlines()
      print(s)"""
      file.write('\nДА!')
      """s= file.readlines()
      print(s)"""
      file = open("App1\my_file.txt",'r',encoding='utf-8')
      print(file.readlines())
  finally:
    file.close()
except  FileNotFoundError:
    print('Tpapapapap')
except: 
    print('error')    

# alternative
with open("App1\my_file.txt",'r',encoding='utf-8') as file1:
    #---
    #---
     print('dsfdf')

try:
    with open("App1\my_file.txt",'a',encoding='utf-8') as file2:
        file2.write("LLLL\n")
        file2.write("DDDD\n")
        file2.write("SSSS\n")
except:
    print("dfdfdf")    

         
