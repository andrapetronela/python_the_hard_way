the_count = [1, 2, 3, 4, 5]
fruits = ['strawberries', 'cherries', 'oranges', 'apples']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for number in the_count:
    print(f'This is count {number}.')
    
    
for fruit in fruits:
    print (f'I have 5 {fruit}.')
    
for i in change:
    print (f'I have {i}.')
    
    
# adding elements to a list
#.append()

my_list = []

for i in range(0, 6):
    my_list.append(i)
print(my_list)