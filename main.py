import sys

import psutil
import svl  
import time

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Error, too many parameters.")
        print("Usage : python3 {} <app.exe>".format(sys.argv[0]))
        exit()
    else:
        while True:
            if svl.process_is_there(sys.argv[1]):
                proc_found = svl.research_process_by_name(sys.argv[1])
                if proc_found:
                    svl.run(proc_found)
            else:
                time.sleep(10)
    
                

           
 