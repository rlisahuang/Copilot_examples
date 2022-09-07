'''
StackOverFlow:
https://stackoverflow.com/questions/273192/how-can-i-safely-create-a-nested-directory
How can I safely create a nested directory?
'''
#check if directory exists
#if not create directory and add new file    <= Natural language prompt for Copilot
#Written by Copilot:
import os

def create_dir(dir_name):
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
        print("Directory created")
    else:
        print("Directory already exists")
    return


'''StackOverFlow:
https://stackoverflow.com/questions/1854/how-to-identify-on-which-os-python-is-running-on
How to identify on which OS Python is running on?
'''
#How to identify on which OS Python is running on?
# Specify if OS python is Windows, Linux, or MacOS  <= Natural language prompt for Copilot
#Written by Copilot:
def os_identifier():
    if os.name == 'nt':
        return 'Windows'
    elif os.name == 'posix':
        return 'Linux'
    elif os.name == 'mac':
        return 'MacOS'
    else:
        return 'Unknown'


'''
StackOverFlow:
https://stackoverflow.com/questions/466684/how-can-i-return-system-information-in-python
How can I return system information in Python?
'''
#Using Python, how can information such as CPU usage, 
#memory usage (free, used, etc), process count, etc be returned 
#in a generic manner so that the same code can be run on Linux, Windows, BSD, etc?   <= Natural language prompt for Copilot
#Written by Copilot:
import psutil
def cpu_info():
    return psutil.cpu_percent()

def memory_info():
    return psutil.virtual_memory()

def process_count():
    return psutil.cpu_count()


def system_info_generic():
    print("System info:")
    print("OS:", os_identifier())
    print("CPU:", cpu_info())
    print("Memory:", memory_info())
    print("Process count:", process_count())
    return

system_info_generic()

