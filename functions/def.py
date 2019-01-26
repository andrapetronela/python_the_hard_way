#def print_two(*args):
#    arg1, arg2 = args
#    print(f"arg1: {arg1}, arg2: {arg2}")
#    
#print_two('Zoe', 'Ping')


# same as:

#def two_args(arg1, arg2):
#    print(f"arg1: {arg1}, arg2: {arg2}")
#    
#two_args('Zoe', 'Pedro')


def hours_of_code(days, hours):
#    days = 365
#    hours_per_day = 4
    result = days * hours
    print(f"This means {result} hours and {round(result / 24, 2)} days.")
    
hours_of_code(365, 6)
#hours_of_code()

