
import pickle, Test

try:
    with open('abcd.dat', 'wb') as f:
        n=int(input('enter the number of employee'))
        if n!=0:
            for i in range(n):
                enumber=int(input('enter the emplyee number'))
                ename=input('enter the employee name')
                esalary=int(input('enter the employee salary'))
                eaddress=input('enter the address')
                eone=Test.Employee(enumber, ename, esalary, eaddress)

                pickle.dump(eone,f)
        else:
            print('please input the correct value')


except FileNotFoundError as message1:
    print(message1)