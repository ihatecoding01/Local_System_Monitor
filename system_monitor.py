import psutil
import time
import os

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def bytes_to_gb(bytes_val):
    return bytes_val / (1024 ** 3)

def get_system_stats():
    cpu_percent = psutil.cpu_percent(interval=1)
    virtual_mem = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    net_io = psutil.net_io_counters()
    
    stats = {
        "CPU Usage (%)": cpu_percent,
        "Memory Usage (GB)": f"{bytes_to_gb(virtual_mem.used):.2f} / {bytes_to_gb(virtual_mem.total):.2f}",
        "Disk Usage (GB)": f"{bytes_to_gb(disk.used):.2f} / {bytes_to_gb(disk.total):.2f}",
        "Network Sent (MB)": f"{net_io.bytes_sent / (1024**2):.2f}",
        "Network Received (MB)": f"{net_io.bytes_recv / (1024**2):.2f}",
    }
    return stats

def main():
    while True:
        clear()
        stats = get_system_stats()
        print("=== Local System Monitor ===\n")
        for key, value in stats.items():
            print(f"{key}: {value}")
        print("\nUpdating every 2 seconds. Press Ctrl+C to exit.")
        time.sleep(2)

if __name__ == '__main__':
    main()
