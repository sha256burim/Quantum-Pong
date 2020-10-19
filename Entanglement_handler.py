import qsharp
from QuantumComputer import EntangleQubits

def EntangleCommunications(send):
    state = ''
    if send == True:
        state = 1
    elif send == False:
        state = 0
    else:
        state = 0
    return EntangleQubits(Initial = state) #takes either 1 or 0 as types you can pass through the .simulate call object

#uncoment to test
#print( EntangleCommunications(True))  
#print( EntangleCommunications(False))

