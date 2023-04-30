# CPU scheduling

## Scheduling
- ready queue: the set of processes in memory that are ready to execute
- CPU scheduling(maximize CPU utilization in presence of multi-programming)
  - components
    - scheduler: select 1 for ready queue
    - dispatcher: allocates the CPU to the selected one
      - context switching, switch to user mode, resume the program
    - dispatch latency(time taken by stop current process, star another process): overhead
  - consideration
    - CPU utilization
    - Throughput
    - Turnaround time
    - waiting time
    - response time
## Algorithm
- turnaround time: finish time
- throughput: ? process / time(ms)
- response time: first get execute
### (first come first serve) FCFS scheduling
- equal to
  - RR scheduling when q → ∞
  - priority scheduling when priority is **process arrival time**

### (shortest job first) SJF scheduling
- optimal for non-preemptive scheduling(非抢占式调度)
  - shortest avg. waiting time
  - shortest svg. turnaround time
- equal to
  - Priority scheduling when priority is **CPU burst time**

### (shortest remaining time) SRT scheduling
- preemptive version of SJF
- 
### Priority scheduling
- Preemptive Priority Scheduling
  - stop when higher priority arrived
- Windows convention:
  - Largest value → first
- Linux convention:
  - Smallest value → first
### (rounding robin) RR scheduling
- time quantum(small unit of CPU)
- less than q(n-1) time unit
- higher turnaround time
- *q* small: excessive context switching
### Multi-level queues