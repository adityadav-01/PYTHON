languages = ['Swift', 'Python', 'Go']

# Start of loop
for lang in languages:
    print(lang)
    print('-----')
# End of for loop


print('-------Loop Through a String---------')
language = 'Python'
# iterate over each character in language
for x in language:
    print(x)


print('-------range---------')
    # iterate from i = 0 to i = 3
for i in range(4):
    print(i)


print('----Nested for loops-----')
    # outer loop 
for i in range(2):
    # inner loop
    for j in range(2): 
        print(f"i = {i}, j = {j}")
  