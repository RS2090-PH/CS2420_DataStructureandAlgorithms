file = open("integers.txt", 'r')
the_sum = 0
for line in file:
    word_list = line.split() # since there are multiple numbers per line we split the first
    for word in wordlist:
        number = int(word) # then we iterate through the list of separated numbers and conver them
        the_sum += number
print("The sum is ", the_sum)
        
# or
# you can split and map all to an int before using the number values this way
file = open("integers.txt", 'r')
print("The sum is ", sum(map(int, file.read().split())))