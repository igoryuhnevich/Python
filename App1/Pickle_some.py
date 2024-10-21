import pickle

shoplistfile = 'App1\my_file2.data'

shoplist = ['fff','ggg','hhh']

f = open (shoplistfile, 'wb')

pickle.dump(shoplist,f)

f.close()

del shoplist

f = open(shoplistfile, 'rb')
storedlist = pickle.load(f)
print(storedlist)