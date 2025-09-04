# Local_System_Monitor
A simple, real-time system monitor built with Python that displays CPU, memory, disk, and network usage directly in the terminal.

### Features
1. Shows CPU usage percentage updated every 2 seconds.
2. Displays memory usage (used and total) in gigabytes.
3. Displays disk usage (used and total) of the root partition in gigabytes.
4. Shows network data sent and received in megabytes.
5. Lightweight and easy to run on any Linux system with Python installed.

### Requirements
- Python 3.x
- `psutil` library

### Installation
1. Ensure Python 3 is installed:

python3 --version

text

2. Install the required `psutil` package:

pip3 install psutil

text

### Usage

1. Clone or download the `system_monitor.py` script.

2. Run the script:

python3 system_monitor.py

text

3. View real-time system statistics updated every 2 seconds. Press `Ctrl+C` to stop.

### How It Works

The script uses the `psutil` library to fetch system metrics such as CPU utilization, memory usage, disk usage, and network activity. It clears the terminal screen before each update for a clean display.

### Example Output

=== Local System Monitor ===

CPU Usage (%): 23.5 

Memory Usage (GB): 3.42 / 8.00

Disk Usage (GB): 100.12 / 250.00

Network Sent (MB): 1.25

Network Received (MB): 3.60

Updating every 2 seconds. Press Ctrl+C to exit.

text

### License

This project is licensed under the MIT License.

---

Feel free to fork, modify, and contribute improvements!
Let me know if you want it modified or expanded!
