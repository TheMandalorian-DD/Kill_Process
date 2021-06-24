import psutil
import time 

def find_and_kill_proc(proc):
    """ Process -> bool
    Kill les processus de même nom et renvoie True si au moins une instance a été kill, False sinon."""
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
    Retourne le processus 'name'."""
    started = 0
    process = None
    try:
        for p in psutil.process_iter():
            if p.name() == name:
                if p.create_time() > started:
                    started = p.create_time()
                    process = psutil.Process(p.pid)
    except psutil.NoSuchProcess:
        print("Process does not exist")
    return process

def run(process):
    """ Process ->
    Tant que le processus tourne, on recherche d'autre instance du même nom."""
    while (process and process.is_running()) or (process.status() == psutil.STATUS_RUNNING):
        if not find_and_kill_proc(process):
            time.sleep(10)
        



    


