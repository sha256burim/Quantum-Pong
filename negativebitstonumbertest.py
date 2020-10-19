
from bitstring import BitArray
#pip install bitstring

positivebitstring = ["0","0","0","0","0","0","0","1"]

negativebitstring = ["1","1","1","1","1","1","1","1"]

stringofbits = ''
for x in positivebitstring:
           stringofbits += x
           #print(stringofbits)
thisoutput = BitArray(bin=stringofbits)
print(thisoutput.int)

stringofotherbits = ''
for x in negativebitstring:
            stringofotherbits += x
            print(stringofotherbits)
output = BitArray(bin=stringofotherbits)

print(output.int)

exit()

b = BitArray(bin='00000001')
print(b.int)

output1 = '11111111'
b = BitArray(bin=output1)
print(b.int)