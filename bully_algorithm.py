#bully algorithm
import random
n = 6

def set_coordinator(p):
    global global_coordinator
    print("process ",p," is the coordinator")    
    global_coordinator = p
        
def msg(p):
    print("process ",p,"sends to")
    greater_process = []
    for i in range(n):
        if(process_id[i]>p):
            print("process ",process_id[i])
            if(alive[i] == 1):
                print("ok message from ",process_id[i])
                greater_process+=[process_id[i]]
    if(len(greater_process)==0):
        set_coordinator(p)
        return True
    else:
        for i in range(len(greater_process)):
            flag = msg(greater_process[i])
            if(flag == True):
                break
    return True

def backtolife(p):
    if(alive[p] == 1):
        print("already alive dummy")
        return
    print("process ",p," back to life")
    alive[p] = 1
    global global_coordinator
    if(p > global_coordinator):
        set_coordinator(p)
    else:
        fail_identifier = set_fail_identifier(global_coordinator)
        msg(fail_identifier)

def kill(p):
    global global_coordinator
    alive[p] = 0
    if (p == global_coordinator):
        fail_identifier = set_fail_identifier(p)
        msg(fail_identifier)

def set_fail_identifier(fail_identifier):
    global global_coordinator
    while(fail_identifier == global_coordinator):
        fail_identifier = random.randint(0,n-1)
    print("process ",fail_identifier,"identifies the failure")
    return(fail_identifier)

process_id = [int(-1)]*n                             
for i in range(n):
    process_id[i]=i
                    
alive = [int(1)]*n                                   
global_coordinator = max(process_id)

kill(global_coordinator)
backtolife(5)







