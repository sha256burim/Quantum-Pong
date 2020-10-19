namespace QuantumComputer {
    open Microsoft.Quantum.Intrinsic;
    open Microsoft.Quantum.Canon;
    open Microsoft.Quantum.Convert;
    open Microsoft.Quantum.Math;
    open Microsoft.Quantum.Measurement;


//SetQubitState is defined that takes as a parameter a qubit and another parameter, desired, representing the state that we would like the qubit to be in. 
//The operation SetQubitState performs a measurement on the qubit using the operation M. 
//In Q#, a qubit measurement always returns either Zero or One. If the measurement returns a value not equal to the desired value, SetQubitState “flips” the qubit; 
//that is, it runs an X operation, which changes the qubit state to a new state in which the probabilities of a measurement returning Zero and One are reversed. 
//This way, SetQubitState always puts the target qubit in the desired state.

    operation SetQubitState(desired : Result, target : Qubit) : Unit {
           if (desired != M(target)) {          //M() Operation: Performs a measurement of a single qubit in the Pauli  Z basis.
               X(target);                       //X() Operation: Applies the Pauli X gate.
                                                //The Pauli-X gate acts on a single qubit. It is the quantum equivalent of the NOT gate 
                                                //for classical computers (with respect to the standard basis {\displaystyle |0\rangle }|0\rangle ,
                                                // {\displaystyle |1\rangle }|1\rangle , which distinguishes the Z-direction; 
                                                //in the sense that a measurement of the eigenvalue +1 corresponds to classical 1/true and -1 to 0/false)
           }
    }

    operation EntangleQubits(Initial : Result) : Result  {
        
        using ((q0, q1) = (Qubit(), Qubit())) {
            
                SetQubitState(Initial, q0);
                SetQubitState(Zero, q1);

                //H(q0);
                CNOT(q0,q1);        //Entangles the qubits q0 to q1
                let state = M(q1);  // takes the measurement on qubit q1 and applies it to the state variable. Taking the measurement changes the state of qubit q0

                SetQubitState(Zero, q0);    //we reset the state of the qubits for the next operation call
                SetQubitState(Zero, q1);


            return state; 
            
            //By doing a measurement on the entangled qubit we can confidently say that the probability of it being the same
            //as the first qubit is, or both of them being the same is, higher. 
            //Our CNOT has entangled the two qubits, so that whatever happens to one of them, happens to the other. 
            
        } 
        
    }

    operation SampleQuantumRandomNumberGenerator() : Result {
        using (q = Qubit())  {  // Allocate a qubit.
            H(q);               // Put the qubit to superposition. It now has a 50% chance of being 0 or 1.
            return MResetZ(q);  // Measure the qubit value.
        }
    }

    operation SampleRandomNumberInRange(max : Int) : Int {
        mutable bits = new Result[0];
        for (idxBit in 1..BitSizeI(max)) {
            set bits += [SampleQuantumRandomNumberGenerator()];
        }
        let sample = ResultArrayAsInt(bits);
        return sample > max
               ? SampleRandomNumberInRange(max)
               | sample;
    }

}