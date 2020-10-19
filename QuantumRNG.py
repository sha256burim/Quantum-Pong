from bitstring import BitArray
import qsharp
from QuantumComputer import EntangleQubits, SampleQuantumRandomNumberGenerator


#Function is named randint to comply with previously written code that uses the randint function from the random py library
def randint(min, max):

    #find the range between the minimum and the maximum
    #Absolute value function makes sure that we don't overshoot the number range because of the negative sign.
    if (abs(min)==abs(max)): #if max and min are the same we take either of the number since we don't want to generate a zero length bitstring
        numrange = abs(min)
    elif (abs(min) > abs(max)):
        numrange = abs(min)
    else:
        numrange = abs(max) #otherwise we take the range of the higher number and then filter for lower range later in the code
                              

    output = numrange +1  # Variable to store the output

    while output > numrange:
        bit_string = [] # We initialise a bit array to store the bits we get from the quantum computer

        stringofbits = '' # We initialise an empty string to concatenate the bits into from the bit array

        for i in range(0, ((numrange+1).bit_length())):     #We get the range of the bits of our maximum bound
            bit_string.append(SampleQuantumRandomNumberGenerator.simulate())  #for each bit of the int of the maximum bound we call the quantum computer to generate a bit for us
        for x in bit_string:            
            thatstring = str(x) 
            stringofbits += thatstring      #We convert each bit in the bit array into a string literal and concatenate them into the previously initialized string
        output = BitArray(bin=stringofbits).int #then we convert the string of bits into a an int. and apply it to the output variable

        if (output < min):          #if the output is out of the lower bounds of the range, we call the function recursively until it is. 
            output = randint(min, max)
        if (output > max):          #if the output is higher than the upper bounds of the range, we do the same as above until it is. 
            output = randint (min, max)
        if (output == min or output == max):
            return output

        return output
 

def test_randint(min,max, count):
    
    count_min = 0
    count_max = 0
    count_neither = 0
    count_zeroes = 0
    count_lessthan_min=0
    count_morethan_max=0
    between_min_and_max = 0

    for j in range(count):
        test_output = randint(min, max)
        print(test_output)
        if (test_output == min):
            count_min += 1
        elif (test_output == max):
            count_max += 1
        elif (test_output < min):
            count_lessthan_min +=1
        elif (test_output > max):
            count_morethan_max +=1
        elif (test_output == min or test_output == max):
            between_min_and_max +=1
        elif (test_output != min or test_output != max):
            #print(test_output)
            count_neither +=1
        elif (test_output == 0):
            count_zeroes +=1
        
        

    print("min counted: ", count_min)
    print("max counted: ", count_max)
    print("neither counted: ", count_neither)
    print("Zeroes counted: ", count_zeroes)
    print("less than min counted: ", count_lessthan_min)
    print("More than max counted: ", count_morethan_max)
    print("Between min and max", between_min_and_max)
    print("Cycles counted: ", count)


#NOTE:Add error handling if for when some idiot adds both min and max as 0

#test_randint(-1,1,200) #uncomment to test for max and min distribution
#test_randint(-10,10, 200) #uncomment to test for distribution of everything else
#Code works some of the time, and some of the time it doesn't. It's a python thing. 