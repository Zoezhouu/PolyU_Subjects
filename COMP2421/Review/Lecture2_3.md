# Lecture 2/3 - MIPS / Assembly language

**symbolic representation of machine language**

**Advantage:** exploit some hardware features
**Drawbacks:** machine specific

#### MIPS
**register-based architecture**
 - memory access
 - ALU operations
**key points:** registers, main memory, instructions

#### Registers
1. 32bits
2. how to refer: start with "$"
3. name
4. direct use register numbers

|   Register Number	|   alternative Name	|   Descriptions	|
|---	|---	|---	|
|   0  	|   zero	|   constant 0	|
|   1	|   \$at	|   reserved	|
|   2-3	|   \$v0 - $v1	|   result/output	|
|   4-7	|   \$a0 - $a3	|   argument/input	|
|   8-15	|   \$t0 - $t7	|   temporary register	|
|   16-23	|   \$s0 - $s7	|   saved in register and restore when not using it	|
|   24-25	|   \$t8 - $t9	|   temporary register	|
|   26-27	|   \$k0 - $k1	|   reserved	|
|   28	|   \$gp	|   global pointer	|
|   29	|   \$sp	|   stack pointer	|
|   30	|   \$s8/$fp	|   saved value/fram pointer	|
|   31	|   \$ra	|   return address	|

**other register: Hi and Lo, etc**

------

#### Memory Layout
 - **0x8000 0000 to 0xFFFF FFFF** is for operating system and ROM(used by user program)
 - **others are reserved** for computer operation


**basic fact**
unit: byte/8bits
total $2^{32}$ bytes memory
each byte has address:32 bits
**address range: 0x 0000 0000 to 0x FFFF FFFF**

**operation**
load: memory -> register
store: register -> memory

**MIPS Memory and address**
1. accessed in contiguous bytes(use first bytes)
   one byte: 8 bits
   one word: 4 bytes, 32 bits
   double word: 8 bytes, 64 bits
2. store instructions and data
   instruction: fixed length
   data: various bytes

------

# MIPS Instructions
**each instruction has 32 bits**
**3 type:R-type, I-type, J-type**

## R - type
1. ***format:***
   source register - rt & rs
   destination resgister - rd
   <span style="color:red">instruction rd, rs, rt </span>
   e.g. add \$t0, \$t1, \$t2 - add value in \$t1 and \$t2 and store result in \$t0
2. ***machine code:***
   6bits: operation code(000000)
   5bits: rs
   5bits: rt
   5bits: rd
   5bits: shamt - shift instructions(how many positions to shift)
   6bits: function
   e.g.**assembly lang: add \$t0, \$t1, \$t2**
   **machine language:**  
    |   op	|   rs	|   rt	|   rd	|   shamt	|   funct	|
    |---	|---	|---	|---	|---	|---	|
    |   000000  	|   01001	|   01010	|   01000	|   00000	|   100000	|
    |     	|   \$9(\$t1)	|   \$10(\$t2)	|   \$8(\$t0)	|   	|   add	|

   e.g.**assembly language: sll \$t5, \$t4, 2** 
   *shift the value in \$4 teo bits to the left and place result in \$t5*
   **machine language:**
    |   op	|   rs	|   rt	|   rd	|   shamt	|   funct	|
    |---	|---	|---	|---	|---	|---	|
    |   000000  	|   00000	|   01100	|   01101	|   00010	|   00000	|
    |     	|   	|   \$12(\$t4)	|   \$13(\$t5)	|   	|   sll	|
   exercise 3(\$t3) + 10 (\$t5), store in \$t1
   **assembly language: add \$t1, \$t3, \$t5**
   **machine language:** 
    |   op	|   rs	|   rt	|   rd	|   shamt	|   funct	|
    |---	|---	|---	|---	|---	|---	|
    |   000000  	|   01011	|   01100	|   01001	|   00010	|   100000	|
    |     	|   \$11(\$t3)	|   \$13(\$t5)	|   \$9(\$t1)	|   	|   add	|

## I - type
immediate value: store value directly within instruction
1. ***Format***
   instruction rs, rt, imm
   e.g. bitwise OR opoeration(ori)  
   ori rt, rs, imm
   *take bitwise OR between the value stored in rs and imm, them store the result in rt. //**load value stored in imm to target register**
   \$0 has 32 bits, imm has 16 bits( zero extension for 16-bit operand)
2. ***Machine code***
   operation: 6 bits
   rs: 5 bits
   rt 5 bits
   constant/address: 16 bits
   e.g.**assembly language: ori \$8, \$0, 0x2**
   **Machine Language:**
   |   op	|   rs	|   rt	|   constant/address	|
    |---	|---	|---	|---	|
    |   001101  	|   01000	|   01000	|   0000 0000 0000 0010	|
    |     ori	|   $0	|   $8	|   0x2	|
    exercise: use ori to lad decimal 17 into register $t1
    **assembly language: ori \$t1, \$0, 0x11**

### load value:
<span style="color:blue"> ori rt, rs, imm </span>
ori \$xx, \$0, 0x111
####load word: 
<span style="color:blue"> *lw, destreg, offset(basereg)*  </span>
memory address = base address + offset
**assembly language:** lw \$8,0x60($10-memory address value)
**machine language:**
|   op	|   base	|   set	|   offset	|
|---	|---	|---	|---	|
|   100011  	|   01010	|   01000	|   0000 0000 0110 0000	|
|    lw	|   $10	|   $8	|   0x60	|


### store word:
<span style="color:blue"> sw t, offset(basereg) </span>
**assemly language:** sw \$12, 0x50(\$13)


## J-type Instructions
1. format: instruction addr
2. e.g. j addr(jump to the instruction at address addr)
3. machine code:
   operation: 6bits
   address: 26bits

####jump instruction
**j addr**
operation code: 000010
address: shift left two position

    
------

## Bitwise Logic Operations
### ORI
**ori d, s, const**
 - ori \$8 \$0, 0x2(zero extention)
 - load constant into register $8
 - constant should only be non-negative integer
 - **if 2's complement:** after zero extension, it becomes position
 - **meaning for ALU:** zero extension, then do bitwise OR
 - **meaning for programmer:** ORI implement load function

### ANDI
 - **andi d, s, constant**
 - andi \$8, \$0, 0x2
 - clearing a register (\$8) - set all bits to 0
 - 0x2 - **unsigned or 2's conplement doesn't matter**


### XORI
 - **xori d, s, const**
 - similar to ori, andi
 - **meaning** know the difference

### AND, OR, XOR, NOR
 - and d, s, t
 - or d, s, t
 - xor d, s, t
 - nor d, s, t(not, flip)

### SHIFT
#### shift left logic(SLL)
**sll d, s, shft**
 - inplace shift: OK
 - no shift and inplace: no operation
 - no shift and not inplace: copy

#### shift right logic
**srl d, s, shft**
0001 -> 0000

#### shift right arithmetic
 - sra d, s, shft
 - 10100111
 - srl: padding leading 0
 - sra: recursivly adding leading one digit

#### SUMMARY: maniplate bit pattern

------

## Arithmetic Operations and memory access
 - form: unsigned or 2's complement form(same)
 - 32bits to represent integers but **(overflow detection)**
 - carry out bit(unsigned form)
 - both oprand have same sign, result opposite sign(overflow)

### add
**addu d, s, t(u overflow is ignored/unsigned)**
 - add d, s, t (s+t->d)
 - addiu d, s, const: add immediate unsigned, (s+const->d)

### sub
 - **subu/sub d, s, t (s-t->d)**
 - **no subi/subiu** addiu \$8, \$10, -3

### mul - 2 steps
 - ***need 2N bits***
 - Hi and Lo registers store the result
 - op1 * op2 = hi (bit 32-63) | lo(bit 0-31)
 - **mult s, t / multu s, t** (store in hi and lo) not check overflow
 - **access to hi and lo**
   - **mfhi d** move from hi to register d
   - **mflo d** move from lo to register d


### div
 - op1/op2: op1 = op2 * quotient + remainder
 - op1 / op2 = hi(remainder) | lo(quotient)
 - **div s, t / divu s, t** (s/t)

## memory access
 - **load: memory -> register** lw t, offset(basereg)
 - **store: register -> memory** sw t, offset(basereg)

------

## Control Program Flow
### jump
 - **j addr - go to **
 - fetch j addr - update addr - execute j addr
 - **after jump, need branch delay slot(no-operation instruction)**
 - because memory set to addr after  next instruction is executed
 - **implementation: unconditional loop**

1. branch delay slot
2. other branch instruction: implement control structure in high-level languages

### loop
simple loop
```
main:
   sll   $0, $0, 0
   sll   $0, $0, 0
   sll   $0, $0, 0
   sll   $0, $0, 0
   j     main
   addiu $8, $8, 1
```

addiu \$8, \$8, 1 will always execute (unconditional loop)


### conditional branch instructions
if certain condition is true, then instruction branch to new address
1. **compare bit pattern in $u and $v for beq and bne**
 - <span style="color:blue"> branch on equal: <\span>
 - beq u, v, addr # if \$u == \$v, branches to addr
 - <span style="color:blue"> branch on not equal: <\span> 
 - bne u, v, addr # if \$u != \$v, branches to addr

2. **others**
 - <span style="color:blue"> branch on less than zero: <\span> 
 - bltz s, addr # is \$s < 0, branch to addr
 - <span style="color:blue"> branch on grater than or equal to zero: <\span>
 - bgez s, addr #if $s >= 0, branches to zero

### Flow chart lecture 3 p67 - p70

### count loop(like for loop in C)
**combine conditional branch, jump, conditional set instructions**
 - conditional set instruction
 - <span style="color:blue"> set on less than: <\span> 
 - slt d, s, t # s,t are 2's complement, if \$s<\$t, set \$d=1, else \$d=0
 - <span style="color:blue"> unsigned: sltu d, s, t <\span> 
 - <span style="color:blue"> immediate:slti d, s, imm <\span> 
 - <span style="color:blue"> unsigned int: sltiu d, s, imm <\span> 

##### example: sum of array element: lecture 3 p81-87
##### example: test condition - negative or positive lecture 3p88 - 90

---

### subroutines
**\$ra register** (\$31)
 - holds the return addr
 - idea: store return address in $ra, when finished, program return that adress
 - implementation: **jal** and **jar**

instruction: **ja sub**
1. set \$ra to addr + 4
   - result: \$ra stores addr of (n+2)th instruction(jal is nth)
   - in memory: jal | branch delay slot | instruction(return)
2. set address to sub
3. example: lecture 4 p8

instruction: **jr \$ra**
 - set address to \$ra

#### calling convention
- \$t0 - \$t9: subroutines can use 
- \$s0 - \$s7: saved registers; subroutines should not use (if need to use it, save the value first and restore the value after use)
- \$a0 - \$a3: contain arguments for the subroutine
- \$v0 -\$v1: contain values returned from the subroutine
- example: lecture 4 p12

**simple convention:**
- use jal and jr with $ra to call subroutines
- donot call other routinse within a subroutine
- obey the conventional use of registers

#### Stack
 - store (grow/reduce)dynamic generated data in program
 - last in first out
 - push/pop operation
**PUSH**
 - **equal to:** subtract 4 from \$sp, then store item in \$sp
```
subu  $sp, $sp, 4    # point to the place for the new item
sw    $t0, ($sp)     # store the contents of $t0 as the new top
```
**POP**
 - **equal to:** copy item pointed at by \$sp and them add 4 to \$sp
```
lw    $t0, ($sp)     #copy top item to $t0
addu  $sp, $sp, 4    #point to the item beneath the old top
```

#### chain of subroutines - two problems
1. **use \$ra**
   - calls sub A, return addr is in \$ra
   - sub A calls sub B, where to store
   - use push and pop to store $ra into stack, then pop $ra before jr $ra
2. register problem
   - When Main calls sub A, sub A should not use \$s0 - \$ when sub A calls sub B, sub A should not use \$t0 - \$t9 which registers should sub A use?
   - **Solution:**allow sub A to use \$s0 - \$s7 but push \$s0 - \$s7 to stack before use, and restore when jr \$ra

**stack is to store dynamic data**

#### Stack-based Linkage Convention
- Subroutine call
  - push register \$t0 -\$t9 to stack
  - put arg values into \$a0 - \$a3
- subroutine beginning
  - call another subroutine, push \$ra to stack
  - push reg \$s0 - \$s7 to stack
- Subroutine Body
  - May use $t and $s if pushed to stack
  - May call another subroutine
- Subroutine Ending (done by the Callee)
  - Put returned values in \$v0 - \$v1
  - Pop registers \$s0 - \$s7 from stack (restore value)
  - Pop $ra
  - Return to caller using jr $ra
