# Lecture 5 - Interprocess Communication and Programming
## Interprocess communication
communicate & synchronize
- Application:
  - Data transfer and sharing
  - Event notification
  - Resource sharing
  - Process control
  - Synchronization

Mechanism
1. shared memory
   - 建立共享存储区，通过读写共享存储区来交换信息，由通信进程来确定交换的数据和位置，不受操作系统的控制
   - not practical in Unix/Linux
2. message passing - no shared variables
   - direct communication
     - name each other explicitly
     - one link one pair(bidirectional)
   - indirect communication
     - mailbox: for message to be directed and received(unique identifier for each)
     - process share 1 common mailbox
     - one link, many processes
     - one pair, several links
     - unidirectional or bidirectional
     - operation
       - 新 mailbox, send/receive message, destroy mailbox
   - synchornization
     - blocking(synchronous)
       - block send(sender blocked until之前message被接受)
       - block receive（receiver blocked until 新 message send）
     - non-blocking(no waiting)
       - non-blocking send
       - non-blocking receive(receive valid message, null if message not available)
   - buffering
     - capacity implementation
       - 0 capacity
         - no buffer, sender wait for receiver
       - bounded capacity
         - limited buffer, wait if queue is full
       - unbounded capacity
         - unlimited buffer, no waiting

Implementation
- IPC package: set up data structure in kernel space(persistent until deleted)
- system call: creation/deletion/writing/reading

## Unix/Linux interprocess communication
- shared memory mechanism(not practical in Unix/Linux)
  - protection mechanism/crash
  - cannot access memory space of other process
  - no sharing can be down
- Message passing mechanism
  - achieved via pipes & sockets 
    - Socket: conceptually looks like a named pipe.
  - pipe: unidirectional, FIFO, unstructured data stream (unnamed/named)
  - characteristics
    - buffer in kernel
    - operate in 1 direction
    - plumbing required
    - fixed max size
    - no data type transferred
    - simple flow control

## Unix/Linux unnamed pipe programming
- create pipe: `pipe(fd)`
- write data: `write(fd[1], buf, strlen(buf));`
- read data: `n=read(fd[0], buf2, 80);`
- child process: `fork()`
- read-end of pipe: `fd[0]`
- write end of pipe: `fd[1]`
- end be closed: `close()`
pipe b/t parent and child
- `pipe(fd)`
- `fork()`
- `close(fd[1])` `close(fd[0])`
## Communication topology
- star topology
- ring topology
- liner topology
- fully connected
- tree topology
- mesh
- hypercube
- bus topology
- 
## *Unix/Linux named pipe programming(not tested)*
