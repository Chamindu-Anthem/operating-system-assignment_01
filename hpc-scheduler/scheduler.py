import os
import time
import json
from datetime import datetime

JOB_QUEUE_FILE = "job_queue.txt"
COMPLETED_FILE = "completed_jobs.txt"
LOG_FILE = "scheduler_log.txt"
TIME_QUANTUM = 5


def log_event(student_id, job_name, action, scheduling_type="N/A"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"{timestamp} | Student ID: {student_id} | Job: {job_name} | Action: {action} | Scheduling: {scheduling_type}\n")

def load_jobs(filename):
    if not os.path.exists(filename):
        return []
    with open(filename, "r") as f:
        jobs = [json.loads(line.strip()) for line in f if line.strip()]
    return jobs

def save_jobs(filename, jobs):
    with open(filename, "w") as f:
        for job in jobs:
            f.write(json.dumps(job) + "\n")


def view_pending_jobs():
    jobs = load_jobs(JOB_QUEUE_FILE)
    if not jobs:
        print("No pending jobs.")
        return
    print("Pending Jobs:")
    for idx, job in enumerate(jobs, 1):
        print(f"{idx}. Student ID: {job['student_id']}, Name: {job['job_name']}, Time: {job['execution_time']}s, Priority: {job['priority']}")

def view_completed_jobs():
    jobs = load_jobs(COMPLETED_FILE)
    if not jobs:
        print("No completed jobs.")
        return
    print("Completed Jobs:")
    for idx, job in enumerate(jobs, 1):
        print(f"{idx}. Student ID: {job['student_id']}, Name: {job['job_name']}, Time: {job['execution_time']}s, Priority: {job['priority']}")

def submit_job():
    student_id = input("Enter Student ID: ")
    job_name = input("Enter Job Name: ")
    while True:
        try:
            execution_time = int(input("Enter estimated execution time (seconds): "))
            break
        except ValueError:
            print("Please enter a valid integer.")
    while True:
        try:
            priority = int(input("Enter priority (1-10, 10 = highest): "))
            if 1 <= priority <= 10:
                break
            else:
                print("Priority must be between 1 and 10.")
        except ValueError:
            print("Please enter a valid integer.")

    job = {
        "student_id": student_id,
        "job_name": job_name,
        "execution_time": execution_time,
        "priority": priority
    }
    jobs = load_jobs(JOB_QUEUE_FILE)
    jobs.append(job)
    save_jobs(JOB_QUEUE_FILE, jobs)
    print(f"Job '{job_name}' submitted successfully.")
    log_event(student_id, job_name, "Submitted")

def process_jobs_round_robin():
    jobs = load_jobs(JOB_QUEUE_FILE)
    if not jobs:
        print("No jobs to process.")
        return

    completed_jobs = load_jobs(COMPLETED_FILE)
    print("Processing jobs using Round Robin...")
    while jobs:
        job = jobs.pop(0)
        time_slice = min(TIME_QUANTUM, job["execution_time"])
        print(f"Executing {job['job_name']} for {time_slice}s")
        time.sleep(time_slice)
        job["execution_time"] -= time_slice
        log_event(job["student_id"], job["job_name"], f"Executed {time_slice}s", "Round Robin")
        if job["execution_time"] <= 0:
            print(f"Job {job['job_name']} completed.")
            completed_jobs.append(job)
        else:
            jobs.append(job)

    save_jobs(JOB_QUEUE_FILE, jobs)
    save_jobs(COMPLETED_FILE, completed_jobs)
    print("All jobs processed using Round Robin.")

def process_jobs_priority():
    jobs = load_jobs(JOB_QUEUE_FILE)
    if not jobs:
        print("No jobs to process.")
        return

    completed_jobs = load_jobs(COMPLETED_FILE)
    print("Processing jobs using Priority Scheduling...")

    jobs.sort(key=lambda x: x["priority"], reverse=True)
    for job in jobs:
        print(f"Executing {job['job_name']} for {job['execution_time']}s")
        time.sleep(job["execution_time"])
        completed_jobs.append(job)
        log_event(job["student_id"], job["job_name"], f"Executed {job['execution_time']}s", "Priority Scheduling")
        print(f"Job {job['job_name']} completed.")

    save_jobs(JOB_QUEUE_FILE, [])
    save_jobs(COMPLETED_FILE, completed_jobs)
    print("All jobs processed using Priority Scheduling.")


def main():
    while True:
        print("\n====== HPC Job Scheduler ======")
        print("1. View pending jobs")
        print("2. Submit a job request")
        print("3. Process job queue (Round Robin)")
        print("4. Process job queue (Priority Scheduling)")
        print("5. View completed jobs")
        print("6. Exit")
        print("===============================")

        choice = input("Enter choice [1-6]: ")
        if choice == "1":
            view_pending_jobs()
        elif choice == "2":
            submit_job()
        elif choice == "3":
            process_jobs_round_robin()
        elif choice == "4":
            process_jobs_priority()
        elif choice == "5":
            view_completed_jobs()
        elif choice == "6":
            confirm = input("Are you sure you want to exit? (Y/N): ")
            if confirm.upper() == "Y":
                print("Exiting scheduler. Goodbye!")
                break
        else:
            print("Invalid choice. Please select 1-6.")

if __name__ == "__main__":
    main()
