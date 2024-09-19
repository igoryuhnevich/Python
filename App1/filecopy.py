import os 
import time

""" 
sourse = ['C:\\usr']

target_dir ='E:\\Backup'

target_poddir = target_dir + os.sep + time.strftime('%Y%m%d')

name_arch = time.strftime('%H%M%S')

if not os.path.exists(target_poddir):
    os.makedirs(target_poddir)
    print('Catalog is created',target_poddir)

target = target_poddir + os.sep + name_arch + '.ZIP'   

zip_command =  '7zFM {0} . -i {1}'.format(target, ' '.join(sourse))

print(zip_command)

if os.system(zip_command) == 0:
    print('Suseful!',target)
else:
    print('Error') """


 
source = ['E:\\teoriy','E:\\Users']
target_dir = "E:\\DDD"  # Подставьте тот путь, который вы будете 
#спользовать.
target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'
zip_command = '7z a -r {0} {1}'.format(target, ' '.join(source))

print(zip_command)
if os.system(zip_command) == 0:
    print('Резервная копия успешно создана в', target)
else:
    print('Создание резервной копии НЕ УДАЛОСЬ')
    