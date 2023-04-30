# Lecture 1
# Course Overview + Number system and Computer Arithmetic


## Computer Organization
functional components

 - CPU (register, arithmetic&logic unit-ALU, Control Unit(timing, memory, IO control, CPU), Internal CPU Interconnection)
 - Main Memory
 - Input/Output
 - Systems Interconnection

data processing
data storage
data movement
control and management



## Number System
represent info and compute over representation
decimal/binary/hexadecimal
(representation of numbers)
### binary conversion
$\sum_{i=0}^{n-1} d_i\times B^{i} + \sum_{j=1}^{m} d_j \times (1/B)^j$

$ N = a_{n-1} \times 2^{n-1} +... + a_2 \times 2^2 + a_1 \times 2^1 + a_0$
$N = (a_{n-1} \times 2^{n-2} + ... + a_{2} \times 2^1 +a_1) \times 2 + a_0$



## Sign-magnitude Representation
 - -1 and +1
 - given sign: $2^{n-1}$ values
 - two sign: $2\times 2^{n-1} = 2^n$ values

## 2's Complement Representation
#### Rules:
1. positive numbers and zeros are represented in the same ....
   0xxxx
2. negative numbers represented as the complement of the corresponding positive numbers
   10000...(n+1 bits)

#### How to get the 2's complement
1. $A+B = 2^n$
2. Flip the bits
   then add 1

#### How to do arithmetic operation in 2's complement from
###### Addition
1. sign detection
2. detect if there's any overflow
3. overflow: if and only if the result has the opposite sign(not possible!)

###### Subtraction



#### representation in different bits
1. positive numbers
   e.g. 18 
   8 bit: 0001 0010
   16 bit: 0000 0000 0001 0010
   padding with leading 0's on the left
2. negative numbers
   e.g. -18
   8 bit: 1110 1110
   16 bit: 1111 1111 1110 1110
   padding with leading 1's on the left

#### Multiplication
shift and add
