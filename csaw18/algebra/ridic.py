

#deal with this damn string
ridiculous = "((((8 + X) + (5 - 9)) * ((9 * 8) - (7 + 16))) - (((11 - 16) - (2 + 2)) + ((19 * 14) - (16 + 11)))) * ((((16 - 4) + (15 - 8)) - ((8 - 1) + (16 - 6))) - (((12 - 11) * (2 - 2)) - ((13 * 12) + (18 - 20)))) = 109356"
ridiculous = list(ridiculous)

for i, c in enumerate(ridiculous):
    if c is "(":
        temp_i = i+1
        while ridiculous[temp_i] is not ")":
            # If there are expressions nested within, or the X, skip
            if ridiculous[temp_i] is "(" or ridiculous[temp_i] is 'X': 
                break
            temp_i+=1
        else: 
            equation = ridiculous[i:temp_i+1]
            print "".join(equation)

        i+=1

        # If the while loop does not finish, the else section will not be executed.
        # Since that is the case, go to the next iteration
        continue

        
