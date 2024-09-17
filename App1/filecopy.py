import os 
import time


sourse = ['C:\\usr','"C:\\VirtualBox VMs"']

target_dir ='E:\\Backup'

target_poddir = target_dir + os.sep + time.strftime('%Y%m%d')

name_arch = time.strftime('%H%M%S')

comment = input("Input the comment -->")
if len(comment) == 0:
    target = target_poddir + os.sep + name_arch + '.zip'
else : target = target_poddir + os.sep + '_'+ \
    comment.replace(' ','_') + '.zip'

if not os.path.exists(target_poddir):
    os.makedirs(target_poddir)
    print('Catalog is created',target_poddir)

zip_command = "zip -qr {0} {1}".format(target,' '.join(sourse))

if os.system(zip_command) == 0:
    print('Suseful!',target)
else:
    print('Error')

