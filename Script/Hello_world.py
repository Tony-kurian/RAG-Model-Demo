import platform
import os
import psutil
import socket

print("=" * 50)
print("SYSTEM CONFIGURATION")
print("=" * 50)

print(f"\nOS: {platform.system()} {platform.release()}")
print(f"OS Version: {platform.version()}")
print(f"Architecture: {platform.machine()}")
print(f"Processor: {platform.processor()}")
print(f"Hostname: {socket.gethostname()}")
print(f"Python Version: {platform.python_version()}")

print(f"\nCPU Cores (Logical): {os.cpu_count()}")
print(f"CPU Cores (Physical): {psutil.cpu_count(logical=False)}")
print(f"CPU Usage: {psutil.cpu_percent(interval=1)}%")

memory = psutil.virtual_memory()
print(f"\nTotal RAM: {memory.total / (1024**3):.2f} GB")
print(f"Available RAM: {memory.available / (1024**3):.2f} GB")
print(f"RAM Usage: {memory.percent}%")

disk = psutil.disk_usage('/')
print(f"\nTotal Disk: {disk.total / (1024**3):.2f} GB")
print(f"Used Disk: {disk.used / (1024**3):.2f} GB")
print(f"Free Disk: {disk.free / (1024**3):.2f} GB")
print(f"Disk Usage: {disk.percent}%")

print("\n" + "=" * 50)