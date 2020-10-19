# Quantum-Pong
Play PONG on a Quantum Computer - Quantum computing implementation in the game PONG

This project is a quantum computing implementation excercise on the classic game Pong. Through Microsofts QDK (Quantum Development Kit) Written in Q#. The main host program and the game engine are written in python to demonstrate cross language support between QDK and Python. However language and library dependencies must be met. 

Here we have implemented Qubit Entanglement between two qubits, and single Qubit based Quantum Random Number Generation within a given integer range.

Qubit Entanglement has been implemented through taking the input of the user/player through keystrokes, convertnig it into a boolean value and passing that as a quantum state between the <0| and <1| q-states onto a qubit, then the qubit goes through entanglement with another qubit. Afterwards we preform a measurement on the second qubit and pass that information onto the game code where it will be executed. Showing a working simulated entanglement use for transmitting data.

The Qubits in this case can be entangled in a single quantum processor, or between two quantum computers in two different geographical locations. The implications of communication through entanglement still stand. Although this demonstration runs purely on a simulated quantum computer.

Single Qubit based Random Number Generation has been implemented through initializing a Qubit, then putting it in a state of superposition. After that we take measurements on the state of the qubit, we convert those states into boolean values which we join into 8-bit length bitstrings, therefore generating bytes. These bytes are then converted to integers and filtered to stay within a user defined range. All of this is done through an algorithm i wrote to generate quantum generated random numbers within a given range for both signed and unsinged integers. The random number generation within a range are then used to determine a random velocity and impact angle on the ball in PONG, allowing the game to experience near life physics collision randomness. 
