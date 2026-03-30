#!/bin/bash

# Author: Chamindu


LOG_FILE="system_monitor_log.txt"


log_action() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" >> $LOG_FILE
}


while true
do
    echo "=============================================="
    echo " University Data Centre System Admin Tool "
    echo "=============================================="
    echo "1. Show CPU & Memory Usage"
    echo "2. Show Top 10 Memory Consuming Processes"
    echo "3. Kill a Process"
    echo "4. Disk Inspection"
    echo "5. Log Archiving"
    echo "6. Exit"
    echo "=============================================="
    read -p "Enter choice [1-6]: " choice

    case $choice in
        1)
            echo "CPU & Memory Usage:"
            top -b -n1 | head -5
            log_action "Checked CPU and Memory usage"
            ;;
        
        2)
            echo "Top 10 Memory Consuming Processes:"
            ps -eo pid,user,%cpu,%mem,comm --sort=-%mem | head -11
            log_action "Viewed top 10 memory consuming processes"
            ;;

        3)
            read -p "Enter PID to terminate: " pid
         
            if [ "$pid" -le 100 ]; then
                echo "Cannot terminate critical system process!"
                log_action "Attempted to kill critical system process PID $pid"
            else
                read -p "Are you sure you want to terminate PID $pid? (Y/N): " confirm
                if [[ "$confirm" == "Y" || "$confirm" == "y" ]]; then
                    if kill $pid 2>/dev/null; then
                        echo "Process $pid terminated."
                        log_action "Killed process PID $pid"
                    else
                        echo "Failed to terminate process $pid (maybe does not exist)"
                        log_action "Failed to kill process PID $pid"
                    fi
                else
                    echo "Cancelled."
                fi
            fi
            ;;

        4)
            read -p "Enter directory path to inspect: " dir
            if [ -d "$dir" ]; then
                echo "Disk usage of $dir:"
                du -sh "$dir"
                log_action "Checked disk usage of $dir"
            else
                echo "Directory does not exist."
                log_action "Failed disk check on $dir"
            fi
            ;;

        5)
            mkdir -p ArchiveLogs
            echo "Archiving log files larger than 50MB..."
            for file in *.log
            do
                if [ -f "$file" ]; then
                    size=$(du -m "$file" | cut -f1)
                    if [ "$size" -gt 50 ]; then
                        timestamp=$(date '+%Y%m%d_%H%M%S')
                        gzip -c "$file" > "ArchiveLogs/${file}_${timestamp}.gz"
                        echo "Archived $file -> ArchiveLogs/${file}_${timestamp}.gz"
                        log_action "Archived $file"
                    fi
                fi
            done
           
            if [ -d "ArchiveLogs" ]; then
                total=$(du -sm ArchiveLogs | cut -f1)
                if [ "$total" -gt 1024 ]; then
                    echo "Warning: ArchiveLogs directory exceeds 1GB!"
                    log_action "ArchiveLogs exceeded 1GB"
                fi
            fi
            ;;

        6)
            read -p "Are you sure you want to exit? (Y/N): " confirm
            if [[ "$confirm" == "Y" || "$confirm" == "y" ]]; then
                log_action "User exited system"
                echo "Goodbye!"
                exit 0
            fi
            ;;

        *)
            echo "Invalid option. Please choose 1-6."
            ;;
    esac

    echo ""  
    read -p "Press Enter to continue..." temp
done
