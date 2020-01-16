#   lambda <argument list> : <expression>
# used to avoid defining one-time functions

oldList = [1,2,3,4,5]
newList = list(filter(lambda number: number > 0, oldList))

# In this case, the anonymouse bool lambda function 
# is used to drop grades lower than zero