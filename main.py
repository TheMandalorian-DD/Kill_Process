import sys
import svl  
import time


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Error, too many parameters.")
        print("Usage : python3 {} <app.exe>".format(sys.argv[0]))
        exit()
    else:
        while True:
            try:
                proc_found = svl.research_process_by_name(sys.argv[1])
                if proc_found:
                    svl.run(proc_found)
                else:
                    time.sleep(10)
            except KeyboardInterrupt:
                exit()
    
    
    