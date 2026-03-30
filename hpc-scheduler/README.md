# operating-system-assignment_01
HPC Job Scheduler

Overview
This Python-based HPC Job Scheduler simulates a High-Performance Computing (HPC) environment where students can submit jobs to be processed using either Round Robin (RR) or Priority Scheduling. The system keeps track of pending and completed jobs, logs all actions with timestamps, and ensures smooth scheduling for multiple job requests.

Key features:
	Submit jobs with execution time and priority.
	View pending and completed jobs.
	Process jobs using Round Robin scheduling with a configurable time quantum.
	Process jobs using Priority Scheduling.
	Logging of all job actions for tracking and auditing.

Files

	job_queue.txt – Stores pending jobs.
	completed_jobs.txt – Stores completed jobs.
	scheduler_log.txt – Logs job submission and execution events.
	scheduler.py – Main Python script containing the job scheduler logic.
Setup Instructions
	Ensure you have Python 3.x installed.
	Clone or download this repository.
	Navigate to the repository folder in your terminal/command prompt.
	No additional libraries are required, as it only uses built-in Python modules.

Execution Steps

	Open your terminal and navigate to the script folder.
	Run the scheduler:

python scheduler.py
	You will see the main menu:
====== HPC Job Scheduler ======
1. View pending jobs
2. Submit a job request
3. Process job queue (Round Robin)
4. Process job queue (Priority Scheduling)
5. View completed jobs
6. Exit
===============================

Choose an option by entering the corresponding number.
	Submit a job: Input Student ID, Job Name, estimated execution time, and priority.
	View pending jobs: Lists all jobs waiting in the queue.
	Process jobs (RR): Executes each job in Round Robin fashion with a time quantum of 5 seconds.
	Process jobs (Priority Scheduling): Executes jobs in order of descending priority.
	View completed jobs: Lists all finished jobs.
	Exit: Close the scheduler.


