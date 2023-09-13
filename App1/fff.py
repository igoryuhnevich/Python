"""
# Дата рождения с выводом на экран предложения. Словарь. 

months = {
    1:'Jannuary',
    2:'February',
    3:'Marth',
    4:'April',
    5:'may',
    6:'Juny',
    7:'July',
    8:'August',
    9:'September',
    10:'October',
    11:'November',
    12:'December' 
}

def season_events(number_of_month):
    if not isinstance(number_of_month,int) and 1 <= number_of_month <= 12:
        print ('Tratatatatatat')
    if number_of_month in range(3,6):
        print(f'You born in {months[number_of_month]}.ddddddddd')
    elif number_of_month in range(6,9):
        print(f'fopdkpfdok {months[number_of_month]}')
    else :
        print(f'dfdfdfdfD {months[number_of_month]}')

season_events(2) """

# Проверка пороля из 8 символов. 
#  
""" import string

def check_pass(pwd):
    err = {
        'length': 'password length less than 8 characters',
        'upper' : 'capital letters are missing',
        'lower' : 'lowercase letter are missing',
        'digits': 'there are no numbers in the password',
        'spec': 'there are no specsymbols in the password',
        'bad_symbols': 'noname symbols used in the password'
    }

    if len(pwd) == 8:
        err.pop('length')
    
    if pwd.lower() != pwd: """

# Посчитать кол-во прописных, строчных и пробелов. Инвертировать.    
string = 'GeeksforGeeks is a computer Science portal for Geeks'
newstring = ''
count1 = 0
count2 = 0
count3 = 0
  
for a in string:
  
    # Checking for uppercase letter and
    # converting to lowercase.
    if (a.isupper()) == True:
        count1 += 1
        newstring += (a.lower())
    # Checking for lowercase letter and
    # converting to uppercase.
    elif (a.islower()) == True:
        count2 += 1
        newstring += (a.upper())
    # Checking for whitespace letter and
    # adding it to the new string as it is.
    elif a.isspace() == True:
          count3 += 1
          newstring += a
        
print(newstring,count2,count3,count1)    




