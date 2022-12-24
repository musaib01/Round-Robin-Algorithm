# SYED MUSAIB HUSSAIN
# 200901065
# CS-01-B
# IMPLEMENTATION OF ROUND ROBIN (RR) ALGORITHM
# LAB TASK


# Function to calculate waiting time
def findWaitingTime(processes, n, burstTime, waitingTime, quantum):  
    rem_burstTime = [0] * n 
  
    # Copy the burst time into rt[]  
    for i in range(n):  
        rem_burstTime[i] = burstTime[i] 

    # Current time  
    time = 0
  
    # Traversing in RR manner  
    while(1): 
        done = True
  
        # Traverse through all processes one by one  
        for i in range(n): 
              
            # If burst time of a process is greater than 0 then only need to process further  
            if (rem_burstTime[i] > 0): 

                # There is a pending process 
                done = False
                  
                if (rem_burstTime[i] > quantum): 
                  
                    # Increase the value of time i.e. shows how much time a process has been processed  
                    time += quantum  
  
                    # Decrease the burst time of current process by quantum  
                    rem_burstTime[i] -= quantum  
                  
                # If burst time is smaller than or equal to quantum. Last cycle for this process  
                else: 
                  
                    # Increase the value of time i.e. shows how much time a process has been processed  
                    time = time + rem_burstTime[i]  
  
                    # Waiting time = time - burstTime  
                    waitingTime[i] = time - burstTime[i]  
  
                    # As the process gets fully executed make its remaining burst time = 0  
                    rem_burstTime[i] = 0
                  
        # If all processes are done  
        if (done == True): 
            break
              
# Function to calculate turn around time  
def findTurnAroundTime(processes, n, burstTime, waitingTime, turnAroundTime): 
      
    # Calculating turnaround time  
    for i in range(n): 
        turnAroundTime[i] = burstTime[i] + waitingTime[i]  
  
  
# Function to calculate average waiting time and turn around time  
def findavgTime(processes, n, burstTime, quantum):  
    waitingTime = [0] * n 
    turnAroundTime = [0] * n  
  
    # Function to find waiting time of all processes  
    findWaitingTime(processes, n, burstTime, waitingTime, quantum)  
  
    # Function to find turn around time for all processes  
    findTurnAroundTime(processes, n, burstTime, waitingTime, turnAroundTime)  
  
    # Display processes along with all details  
    print("Processes", "  Burst Time", "  Waiting Time", "  Turn Around Time") 
    total_waitingTime = 0
    total_turnAroundTime = 0
    for i in range(n): 
  
        total_waitingTime = total_waitingTime + waitingTime[i]  
        total_turnAroundTime = total_turnAroundTime + turnAroundTime[i]  
        print("   ", i + 1, "         ", burstTime[i], "            ", waitingTime[i], "            ", turnAroundTime[i]) 

    # Display average times of processes
    print("\nAverage Waiting Time = %.5f "%(total_waitingTime)) 
    print("Average Turn Around Time = %.5f "% (total_turnAroundTime))  
      
# Driver code  
if __name__ =="__main__": 
      
    processes = [1, 2, 3, 4, 5] 
    n = 5  
    burstTime = [2, 6, 8, 4, 9]    
    quantum = 3
    findavgTime(processes, n, burstTime, quantum)
