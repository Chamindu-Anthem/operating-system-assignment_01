# operating-system-assignment_01


University Data Centre System Admin Tool

Overview

This Bash script is a System Administration Tool designed to help university IT staff manage servers and monitor system resources. It provides CPU/memory monitoring, process management, disk inspection, and log archiving with automated logging of all actions.

Key features:
	View CPU and memory usage.
	List top 10 memory-consuming processes.
	Terminate processes safely (prevents killing critical system processes).
	Inspect disk usage for directories.
	Archive log files exceeding 50 MB into a dedicated folder.
	Automated logging of all system actions with timestamps.

Files

	system_monitor_log.txt – Logs all user actions.
	University_Admin_Tool.sh – Main Bash script.
	ArchiveLogs/ – Folder created to store archived log files.

Setup Instructions
	Ensure you are running a Linux system with Bash installed.
	Clone or download this repository.
	Make the script executable:
	chmod +x University_Admin_Tool.sh
Run the script:
./University_Admin_Tool.sh

Execution Steps
Main Menu appears:
==============================================
University Data Centre System Admin Tool
==============================================
1. Show CPU & Memory Usage
2. Show Top 10 Memory Consuming Processes
3. Kill a Process
4. Disk Inspection
5. Log Archiving
6. Exit
==============================================
Options:
	Show CPU & Memory Usage – Displays the top system usage metrics.
	Show Top 10 Memory Consuming Processes – Lists processes sorted by memory usage.
	Kill a Process – Prompts for a PID to terminate, confirms action, and prevents killing critical processes (PID ≤ 100).
	Disk Inspection – Check disk usage of a specified directory.
	Log Archiving – Compresses log files larger than 50 MB into ArchiveLogs/ and warns if archive exceeds 1 GB.
	Exit – Close the tool.

