import subprocess
import platform
import datetime

def execute_command(command):
    result = subprocess.run(command, 
                            shell=True, 
                            capture_output=True, 
                            text=True)
    output = "\n".join([line.strip() 
                        for line in result.stdout.splitlines() 
                        if line.strip()])
    print(output,"\n")

def check_date_time():
    today = datetime.datetime.today()
    print(today,"\n")

def check_disk_space():
    command = "wmic logicaldisk get size,freespace,caption"
    execute_command(command)

def check_ram():
    command = "wmic OS get FreePhysicalMemory,TotalVisibleMemorySize /Value"
    execute_command(command)

def sysinfo():
    print("System Name:", platform.system())  # e.g., "Windows"
    print("Node Name:", platform.node())      # Hostname of the machine
    print("Release:", platform.release())    # OS release
    print("Version:", platform.version())    # OS version
    print("Machine:", platform.machine())    # Machine type, e.g., "AMD64"
    print("Processor:", platform.processor(),"\n")  # Processor type

def sysinfo_all():
    command ="systeminfo"
    execute_command(command)

check_date_time()
check_disk_space()
check_ram
sysinfo()
# sysinfo_all()