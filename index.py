import os
#write a code to clear the console before printing
os.system('cls' if os.name == 'nt' else 'clear')


print('Hello world')



#write a code to generate fibonacci series
def fibonacci(n):
    a = 0
    b = 1
    if n == 1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c = a + b
            a = b
            b = c
            print(c)
fibonacci(10)

input('\n\nPress enter to exit\n\n')