#print('How old are you?', end=' ')
#age = input()
#print('How tall are you?', end=' ')
#height = input()
#print('How much do you weight?', end=' ')
#weight = input()
#
#print(f"So, you're {age} old, {height} tall and {weight} heavy.")

# end=' ': print function waits for input on the same line; it doesn't add a new line



#age = input('How old are you? ')
#height = input('How tall are you? ')
#weight = input('How much do you weight? ')
#
#print(f"So, you're {age} old, {height} tall and {weight} heavy.")


from sys import argv

script, first, second, third = argv

print('The script is:', script)
print('Your first variable is:', first)
print('Your second variable is:', second)
print('Your third variable is:', third)
