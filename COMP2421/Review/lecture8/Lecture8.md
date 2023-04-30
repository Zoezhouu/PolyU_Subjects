# Lecture 8 - Computer Memory & Cache Memory

## Different storage unit
- choose right memory
  - trade-off b/t performance & cost
  - design philosophy/techniques to use constrained cost to achieve better performance

- Memory 特征
  - Location
    - internal: register in processor, main memory
    - peripheral storage devices(I/O controller)
  - Access Method
    - sequential access(time to access: highly variable)
    - direct access(disk: unique address, time constance)
    - random access(main memory & cache, time constant)
  - performance 
    - access time(latency)
      - random(time take to perform READ/WRITE operation)
      - non-random(from time instruction issued to locating data position)
    - memory cycle time
      - random access memory
      - access time + additional time(required before second access can be made)
      - transfer rate = 1/memory cycle time
    - physical material
    - physical features
      - volatile memory
        - need power to maintain
      - non-volatile memory
        - non need to be charged all the time
      - erasable(register, hard-drive)
      - non-erasable(ROM(Read-only memory), CD)



## Why Memory Hierarchy

### Memory Hierarchy
- inboard memory
  - registers
  - cache
  - main memory
- outboard
  - magnetic disk
  - CD-ROM, CD-RW, DVD-RW, DVD-RAM
- Off-time storage
  - magnetic tape
  - MO, WORM


### Properties:
- cost/bit decreases
- capacity increases
- access time increase
- freq of access by processor decreases

- closer to processor:
  - faster, low capacity, expensive memory

- locality of reference: 
  - tends to cluster: 
  - clustering effect
    - increase hit ratio: use cache b/t Main memory & processor

- multiple level cache organization

## Interplay b/t Cache & Main Memory

### Main Memory Structure
- word: basic memory unit
- memory: 2^n addressable words
- block - K words: M = 2^n/K


### Cache System Structure
- m lines(each line has K words)
- m << M
- access mechanism:
  - access in memory
  - whole block copy to a line of cache

### Mapping Function
- direct Mapping
  - Q = M/m, Q blockes
- associative mapping
  - any block can go to any cache line

#### direct concept
- i = cache line number
- j = main memory block number
- i = j mod m
- address s+w bits
  - line-r: which line in cache
  - tag(s-r): current block
- pro & con
  - simple and inexpensive
  - dis: multiple block mapped to fixed cache line
  - low hit ration

associative mapping concept
- difference
  - block in memory can be mapped to any line in cache
  - s is tag(together with data)
  - no field to determine line number

algorithm for associative mapping
- LRU(least recently used)
  - 替换缓存中时间最⻓且未引⽤的块
- FIFO
- LFU(least frequent used)
- random

inconsistency b/t cache and main memory

- **Write Through**
  - All writes go to cache as well as main memory
    - traffic, slow down writes
- **Write Back**
  - in cache, then memory
    - extra bit to indicate update
    - replace, check this bit, write back to memory
    - I/O access cache, not direct memory


## Summary
![](lec6_summary1.png)
![](lec6_summary2.png)