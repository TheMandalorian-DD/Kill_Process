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
            try:
                process.kill()
                if not killed:
                    killed = True
            except (psutil.AccessDenied, psutil.NoSuchProcess):
                pass
    return killed

def research_process_by_name(name):
    """ str -> Process
    Retourne le processus 'name'."""
    try:
        started = 0
        process = None
        for p in psutil.process_iter():
            if p.name() == name:
                if p.create_time() > started:
                    started = p.create_time()
                    process = psutil.Process(p.pid)
        return process
    except (psutil.AccessDenied, psutil.NoSuchProcess):
        return None
    

def run(process):
    """ Process ->
    Tant que le processus tourne, on recherche d'autre instance du même nom."""
    while (process and process.is_running()) or (process.status() == psutil.STATUS_RUNNING):
        if not find_and_kill_proc(process):
            time.sleep(10)
        



    


