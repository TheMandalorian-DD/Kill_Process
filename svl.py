import psutil
import time 
import math

def find_and_kill_proc(proc):
    """ Process -> bool
    Kills processes with the same name and returns True if at least one instance was killed, False otherwise."""
    killed = False
    for process in psutil.process_iter(['name']):
        if process == proc :
            continue
        if process.info['name'] == proc.name():
            process.kill()
            if not killed:
                killed = True  
    return killed

def research_process_by_name(name):
    """ str -> Process
    Returns the process 'name'."""
    started = math.inf
    process = None
    for p in psutil.process_iter():
        try:
            if p.name() == name:
                if p.create_time() < started:
                    started = p.create_time()
                    process = psutil.Process(p.pid)
        except (psutil.AccessDenied, psutil.NoSuchProcess):
            pass
    return process
    
    

def run(process):
    """ Process ->
    As long as the process is running, we are looking for another instance of the same name."""
    while (process and process.is_running()) or (process.status() == psutil.STATUS_RUNNING):
        if not find_and_kill_proc(process):
            time.sleep(10)
        



    


