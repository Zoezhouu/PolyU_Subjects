// lab 4 exercise - only D mode, no S mode
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int position; // position of "-1"
int noOfCustomer;
int pid;

void debug(int arrive[], int service[]);
void simulation(int argc, char *argv[]);

/* Terminal input should be:
 Debug mode: ./queue <mode D> XX XX -1 XX XX
 Simulation mode ./queue <mode S> <no. of child>[<seed> <arrival> <service>] ... 
 */
int main(int argc, char *argv[]){
    // Loop through the given args looking for "-1" keyword
    int i;
    for (i = 0; i < argc; i++) {
        // find "-1" keyword
        if (strcmp(argv[i], "-1") == 0) {
            position = i;
        }  
    }
    // printf("Position of '-1' is %d.\n", position);

    noOfCustomer = position - 2;
    int arrive_time[noOfCustomer]; // array for arrive_time
    int service_time[noOfCustomer]; // array for service_time

    // printf("number of customer is %d", noOfCustomer);
    // find if the second arg is D or S
    if (argv[1][0] == 'D'){
        int j;
        int i = 0;
        // save args before -1 into array arrive_time
        // printf("arrive time: ");
        for (j = 2; j < position; j++){
            arrive_time[i] = (int)argv[j][0] - 48;
            i++;
            // printf("%d ", arrive_time[j]);
        }
        i = 0;
        // save args after -1 into array service_time
        // printf("\nservice time: ");
        for (j = position + 1; j < argc; j++){
            service_time[i] = (int)argv[j][0] - 48;
            i++;
            // printf("%d ", service_time[i]);
        }
        // child id
        int childid = fork();
        if (childid > 0){
            pid = getpid();
            printf("Parent, pid %d: debug mode\n",getpid());
            exit(0);
        }
        else if (childid == 0){
            debug(arrive_time, service_time);
            exit(0);
        }
        else{
            printf("Fork failed.\n");
            exit(1);
        }
        printf("Parent, pid %d: child 1 complete execution", pid);
    }
    if (argv[1][0] == 'S'){
        simulation(argc, argv);
    }
    return 0;
}

//debug mode
void debug(int arrive_time[], int service_time[]){
    // printf("This is debug mode.\n");
    int temp_arrive_time = 0;
    int temp_depart_time = 0;
    int temp_wait_time = 0;
    int arrive_timeline[noOfCustomer];
    int depart_timeline[noOfCustomer];
    int wait_time[noOfCustomer];
    int i;

    printf("Child 1, pid %d: ", getpid());
    printf("%d customers arriving at ", noOfCustomer);
    for (i = 0; i < noOfCustomer; i++){
        temp_arrive_time += arrive_time[i];
        arrive_timeline[i] = temp_arrive_time;
        printf("%d ", arrive_timeline[i]);
    }
    printf("\n");

    printf("Child 1, pid %d: ", getpid());
    printf("%d customers requiring service for ", noOfCustomer);
    for (i = 0; i < noOfCustomer; i++){
        printf("%d ", service_time[i]);
    }
    printf("\n");

    // departure timeline
    temp_depart_time = arrive_timeline[0];
    // printf("%d customers departure at ", noOfCustomer);
    for (i = 0; i < noOfCustomer; i++){
        temp_depart_time += service_time[i];
        depart_timeline[i] = temp_depart_time;
        printf("%d ", depart_timeline[i]);
    }
    // printf("\n");

    // wait_time
    wait_time[0] = 0;
    // printf("%d customers wait for ", noOfCustomer);
    // printf("%d ", wait_time[0]);
    for (i = 1; i < noOfCustomer; i++){
        temp_wait_time = depart_timeline[i-1] - arrive_timeline[i];
        if (temp_wait_time < 0){
            temp_wait_time = 0;
        }
        wait_time[i] = temp_wait_time;
        // printf("%d ", wait_time[i]);
    }
    // printf("\n");
    
    int time_stop = depart_timeline[noOfCustomer - 1]; //11
    int timeline = 0;
    int left_customer = 0; // customer number
    int queue_length[time_stop + 1];// calculate queue length
    int temp_left_customer = 0;
    // printf("queue_length[time_stop]:");
    for (timeline = 0; timeline < time_stop; timeline++){
        for (i =  0; i < noOfCustomer; i++){
            if (timeline == arrive_timeline[i]){
                temp_left_customer++;
            }
            if (timeline == depart_timeline[i]){
                temp_left_customer--;
            }
        }
        queue_length[timeline] = temp_left_customer - 1;
        // printf(" %d", queue_length[timeline]);
    }
    queue_length[time_stop] = 0;
    // printf(" %d", queue_length[time_stop]);
    // printf("\n");

    i = 0;
    for (timeline = 0; timeline <= time_stop; timeline++){
        // printf("time %d: processing customer %d\n", timeline, i);
        if (timeline == arrive_timeline[i]){
            if(timeline == depart_timeline[i+1]){
                printf("Child 1, pid %d: ", getpid());
                printf("time %d ", timeline);
                printf("customer %d departs, customer %d arrives", i, i + 1);
            }
            else{
                left_customer++;
                printf("Child 1, pid %d: ", getpid());
                printf("time %d ", timeline);
                printf("customer %d arrives, ", i+1);
                if (i == 0){
                    printf("customer %d waits for %d, ", i+1, timeline - arrive_timeline[i]);
                }
            }
            printf("queue length %d\n", queue_length[timeline]); 

        }
        else{
            int j;
            for (j = 0; j < noOfCustomer; j++){
                if (timeline == depart_timeline[j]){
                    left_customer--;
                    printf("Child 1, pid %d: ", getpid());
                    printf("time %d ", timeline);
                    printf("customer %d departs, ", i);
                    if (timeline <= arrive_timeline[j+1]){
                        printf("customer %d waits for %d", i+1, timeline - arrive_timeline[j]);
                    }
                    printf("queue length %d\n", queue_length[timeline]); 
                }
            }
        }
        if (i > time_stop){
            break;
        }
        i++;
    }
    
    printf("Child 1, pid %d: ", getpid());
    printf("all customers served at time %d\n", time_stop); 

    int max= queue_length[0];
    for (i = 1; i < noOfCustomer; i++){
        if(max < queue_length[i]) max = queue_length[i];
    }
    int sum_queue_length = 0;
    for (i = 0; i < time_stop; i++){
        sum_queue_length += queue_length[i];
    }

    printf("Child 1, pid %d: ", getpid());
    printf("maximum queue length %d\n", max);
    printf("Child 1, pid %d: ", getpid());
    printf("average queue length %.3f\n", (float)sum_queue_length/time_stop);
    int sum_wait_time = 0;
    for (i = 0; i <  noOfCustomer; i++){
        sum_wait_time += wait_time[i];
    }   

    printf("Child 1, pid %d: ", getpid());
    printf("total waiting time %d\n", sum_wait_time);
    printf("Child 1, pid %d: ", getpid());
    printf("average waiting time %.3f\n", (float)sum_wait_time/noOfCustomer);
    printf("Child 1, pid %d: ", getpid());
    printf("child 1 complete execution\n");

    
    return;
}

//simulation mode
void simulation(int argc, char *argv[]){
    printf("This is simulation mode.\n");
    printf(" I don't finish code here");
    return;
}

