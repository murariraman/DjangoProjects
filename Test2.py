import pickle, Test1

f=open('abcd.dat', 'rb')

print('employee details')
while True:
    try:
        obj=pickle.load(f)
        obj.display()

    except EOFError as mess:
        print(mess)
        break

f.close()