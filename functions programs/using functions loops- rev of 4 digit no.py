def reverse(n) :
    
    #if no digits remain
    if len(n)==0 :
        return n
    
    #else add the first digit to the end and recurse for remaining number
    return reverse(n[1:]) + n[0]


# the number to be reversed
num = 1749

#convert number to string 
num_string = str(num)

#call the recursive function to reverse num
reversed_num = reverse(num_string)

#output reversed number
print("Reversed Number is: " + reversed_num)
