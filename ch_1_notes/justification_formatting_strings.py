for exponent in range(7 * 11):
    print("%-3d%12d" % (exponent, 10 ** exponent))
    #%-3d justifies first 3char column to left
    #%12d justifies second 12char column to right
    
    
# decimals can determine floats
"%6.3f" % 3.14   # returns right justified ' 3.140'