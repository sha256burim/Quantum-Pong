import qsharp
from QuantumComputer import EntangleQubits, SampleQuantumRandomNumberGenerator

#print("testing for one: ")
#print(EntangleQubits.simulate(Initial = 1)) #takes either a Zero or a One type definition. Because it is a built in type.

#bits = [1,1,1,1,1,1,1,1]

#print (bits)

#for i in bits:
#    print(EntangleQubits.simulate(Initial = i))

#print(" \n If the results are [1,1,1,1,1,1,1,1], then success")
# We import the 
# quantum operation from the namespace defined in the file QuantumComputer.qs
def randint(min, max):
    numrange = min + (max - min) 
    output = numrange + 1 # Variable to store the output
    while output > max:
        bit_string = [] # We initialise a list to store the bits that
        # will define our random integer
        for i in range(0, (numrange.bit_length())): # We need to call the quantum
            # operation as many times as bits are needed to define the
            # maximum of our range. For example, if max=7 we need 3 bits
            # to generate all the numbers from 0 to 7. 
            bit_string.append(SampleQuantumRandomNumberGenerator.simulate()) 
            # Here we call the quantum operation and store the random bit
            # in the list
        for x in bit_string:
            thatstring = str(x)
            stringofbits= "" + thatstring
        output = int(stringofbits, 10) 
    # Transform bit string to integer
    
    return output
    # We print the random number

print("The random number generated is " + str(randint(-4,4)))
print("The random number generated is " + str(randint(-4,4)))
print("The random number generated is " + str(randint(-4,4)))
print("The random number generated is " + str(randint(-4,4)))
print("The random number generated is " + str(randint(-4,4)))
print("The random number generated is " + str(randint(-4,4)))
print("The random number generated is " + str(randint(-4,4)))
print("The random number generated is " + str(randint(-4,4)))
