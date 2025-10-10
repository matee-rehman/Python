#function syntax
def func():
    pass
print(func())

#Print statement in a function
def func():
   print('Hello world!')

func()


#Passing argument in function 
def func(greeting, name):
    return '{}, {}'.format(greeting,name)
print(func('Hi', 'Matee'))


#args &kwargs
def stud_func(*args, **kwargs):
    print(args)
    print(kwargs)
stud_func('Maths','compsci',name='matee',age='22')
    
#Practice Problem
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    """Return True for leap years, False for non-leap years."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    """Return number of days in that month in that year."""
    
    if not 1 <= month <= 12:
        return 'Invalid Month'
    
    if month == 2 and is_leap(year):
        return 29
    
    return month_days[month]

print (is_leap(2014))
print(days_in_month(2020,3))
