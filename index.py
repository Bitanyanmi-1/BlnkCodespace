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


"""Declare and assign two variables with your name, age and city details
 and print each of them with proper descriptions"""
name = 'John Doe'
age = 25
city = 'New York'
print(f'My name is {name}, I am {age} years old and I live in {city}')


#write a code to crete dictionary with 5 key value pairs
dict = {
    'name': 'John Doe',
    'age': 25,
    'city': 'New York',
    'country': 'USA',
    'occupation': 'Software Developer'
}
print(dict)

#iterate through the dictionary and print the key value pairs
for key, value in dict.items():
    print(f'{key}: {value}')

#Calculate and print the quotient and remainder when 10 is divided by 3
quotient = 10 // 3
remainder = 10 % 3
print(f'\nQuotient: {quotient}, Remainder: {remainder}')
print(f'{quotient}')

    
input('\n\nPress enter to exit...')
