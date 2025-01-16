import os

check_disk_space = "wmic logicaldisk get size,freespace,caption"

os.system("systeminfo")
os.system(check_disk_space)