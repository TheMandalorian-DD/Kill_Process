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
    for process in psutil.process_iter():
        if process.name() == name:
            return process

def process_is_there(name):
    """ str -> bool
    Renvoie True si le process name est présent, False sinon."""
    for p in psutil.process_iter():
        if p.name() == name:
            return True
    return False

def run(process):
    """ Process ->
    Tant que le processus tourne, on recherche d'autre instance du même nom."""
    while process and process.is_running():
        if not find_and_kill_proc(process):
            time.sleep(10)
        



    


