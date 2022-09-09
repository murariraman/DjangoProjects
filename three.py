# from sys import argv
# print(argv[0]+'     this is the only file here')
# every commandline is always treated as string argument
# from sys import argv
# print(argv[0])
# # print('raman'+'gaurav')
# print('raman'*10)
# print('this is the new thing ', sep='123')
# print(10*'raman')
# print('durga'+'software'+'solutions', sep=',')
# a,b,c=10,20,30
# print(a,b,c, sep=',')
#print('Hello', end='  ggg  ')

# print(10,20,30,40,50, sep=':', end='    ......')
# listone=[10,20,30,40,50]
# print(listone)
# t=(10,20,30,40,50)
# print(t)
# s={10,20,30,} # this is set
# print(s)
# print(type(s))
# formatting string here %d, %f, %str
#print("formatted string ", %(variable list))
# a,b,c=10,20,30
# print('a value is %d', a)
# name='durga'
# listone=[10,20,30,40]
# print('hello %s this is the list of marks %s' %(name, listone))
# # printing with replacement operator
# name='durga'
# salary=200
# state ='karnataka'
# print('hello {0} your salary is {1} and your state is {2}'.format(name, salary, state))
#print('hello {x} your salary is {y} and your home state is {z}'.format(x='sunny', y=2000, z='karnataka'))
# there are three types of flow control 

# there are three types of flow control conditional, iterative and transfer

"""""
conditional -- if else, if elif else, if elif 

iterative loop -- for each loop

transfer statement -- break continue pass

name=input('enter your name')
if name=='durga':
    print('hello durga', name)
else:
    print('entered wrong name')

    

# if elif else

brand=input('enter the brand name')
if brand=='rc':
    print('rc brand')

elif brand=='kf':
    print('fresher brand')

elif brand=='oc':
    print('this is officers choice brand')

else:
    print('there is no such brand here')
"""""
# printing the greatest of three numbers
# from cgi import print_arguments
# number1=int(input('enter the first number'))
# number2=int(input('enter the first2 number'))
# number3=int(input('enter the first3 number'))
# if number1>number2 and number1>number3:
#     print('greatest is number1', number1)
# elif number2>number3:
#     print(number2)
# else:
#     print(number3)
# defining the for loop here
# s=input('enter the string here')
# count=0
# for x in s:
#     count=count+1
#     print(x)
# print('the total number of characters is', count)
# for x in range(10):
#     #print(x)
#     print('hello', end='')

# when the number of iteration is not known in advance then go for while loop

# x=1
# while x<10:
#     print(x)
#     x+=1

# n=int(input('enter some number'))

# summation=0
# i=1
# while i<=n:
#     summation=summation+i
#     i=i+1

# print('the total summation is as follows', summation)

# name=''
# while name!='durga':
#     name=input('enter the name plz')
# name=''
# password=''
# while name!='durga' and password !='durga':
#     name=input('enter the name please')
#     password=input('enter the password please')
#     print('this is true confirmation code here durga')
# print('hello durga confirmation code here')
# infinite loop 
# i=0
# while True:
#     i=i+1
#     print('hello world')
# nested loop here
# for i in range(4):
#     for j in range(4):
#         print('i = ', i)
#         print('i={} and j={}'.format(i,j))
# flow control 
# i=0
# while True:
#     print(i)
#     i=i+1
#     if i==5:
#         print('you have reached the termination point')
#         break
# print('you have reached new the termination point here')

# there are three transfer statements here
# break, continue, pass
# for i in range(10):
#     if i == 7:
#         print('enough processing')
#         break
#     print('processing items')


# based on certain conditions if we want to break the loop execution

# cart=[10,20,30,50,100]

# for item in cart:
#     if item >90:
#         print('cannot process here', item)
#         break
#     print(' processing item', item)


# if we want to escape the outbound item and continue processing item 
# then we should go for flow control statement 'continue'

# listofname=['mohan', 'sonam', 'chintu', 'pintu', 'narendra']

# for name in listofname:
#     if len(name)>6:
#         #print('length is >6')

#         continue
#     print(name)


# remaining part of the continue statement would not get executed 

# newcart=[10,20,30,40,50,500]
# for item in newcart:
#     if item >499:
#         print('sorry connot process')
#         continue
#     print('processing item', item)

# numbers=[10,20,0,5,0,30]
# for n in numbers:
#     if n==0:
#         print('no division is possible here')
#         continue

#     print(100/n)
# for-else; while-else ; try except else finally

# loop(while/for) statements break else

# else means loop without break

# cart=[10,20,30,40,50,100]
# for item in cart:
#     if item >500:
#         print('sorry cannot process the item')
#         break
#     print('processing item', item)
# else:
#     print('congratulations all the items have been processed')

# defining the while else part here when all the conditions in while loop
# executed then else part will be executed here


# newitemlist=['raman', 'gaurv', 'golu', 'chintu', 'pintu']

# for item in newitemlist:
#     lgtitem=len(item)
#     i=0
#     while i<lgtitem:
#         print('character at {} is {}'.format((i+1), item[i]))
#         i+=1

#     else:
#         print('all the items has been processed')

# else:
#     print('all the items has been processed')
