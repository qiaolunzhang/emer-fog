import os
import psutil

# print(psutil.cpu_percent())
# virtual memory
print(psutil.virtual_memory())
# cpu usage
CPU_Pct=str(round(float(os.popen('''grep 'cpu ' /proc/stat | awk '{usage=($2+$4)*100/($2+$4+$5)} END {print usage }' ''').readline()),2))
print("CPU Usage = " + CPU_Pct)
# cpu temperature
temp = psutil.sensors_temperatures()
temp_current = temp['coretemp'][0][1]
print(temp_current)
# disk Usage
disk_usage_percentage = psutil.disk_usage("/")[3]
print(disk_usage_percentage)
