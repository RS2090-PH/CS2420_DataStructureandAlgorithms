file = open("integer.txt", 'r')
the_sum = 0
for line in file:
    line = line.strip() # strips the new line character from the line
    number = int(line) # converts the line to an int
    the_sum += number
print("The sum is ", the_sum)