import psutil

# CPU Information
cpu = psutil.cpu_freq()
print("CPU Frequency: {} MHz".format(cpu.current))

# RAM Information
ram = psutil.virtual_memory()
print("Total RAM: {:.2f} GB".format(ram.total / (1024**3)))
print("Available RAM: {:.2f} GB".format(ram.available / (1024**3)))
print("Used RAM: {:.2f} GB".format(ram.used / (1024**3)))
print("RAM Usage Percentage: {:.2f}%".format(ram.percent))

# Disk Information
disk = psutil.disk_usage('/')
print("Total Disk Space: {:.2f} GB".format(disk.total / (1024**3)))
print("Free Disk Space: {:.2f} GB".format(disk.free / (1024**3)))
print("Used Disk Space: {:.2f} GB".format(disk.used / (1024**3)))
print("Disk Usage Percentage: {:.2f}%".format(disk.percent))


