# operating-system-assignment_01


Secure Assignment Submission System

Overview

This Python script provides a Secure Assignment Submission System that allows students to submit assignments safely and ensures duplicate detection, file validation, and login monitoring. It also logs all submission and login activities for auditing purposes.

Key features:
	Submit assignments in .pdf or .docx formats.
	Prevent duplicate submissions based on filename and file content.
	Limit submission file size to 5 MB.
	View all submitted assignments.
	Simulate login with account lockout after 3 failed attempts.
	Detect rapid login attempts within 60 seconds.
	Maintain logs for both submissions and login activities.

Files
	submissions/ – Directory where all submitted files are stored.
	submission_log.txt – Logs submission events and duplicates.
	login_log.txt – Logs login attempts and account locks.
	secure_submission.py – Main Python script containing system logic.

Setup Instructions
	Ensure Python 3.x is installed.	
	Clone or download this repository.
	Navigate to the repository folder in your terminal.
	Run the script using:
	python secure_submission.py

Execution Steps

Main Menu appears:
====== Secure Submission System ======
1. Submit assignment
2. Check if file already submitted
3. List submitted assignments
4. Simulate login attempt
5. Exit
=====================================

Options:
	Submit assignment: Enter file path of the assignment.
	Only .pdf or .docx files allowed.
	Maximum file size: 5 MB.
	Prevents duplicate submissions.
	Check duplicate: Enter a filename to see if it has already been submitted.
	List submitted assignments: Shows all files stored in the submissions directory.
	Simulate login: Enter username and password.
	Default credentials: admin / 1234.
	Locks account after 3 failed attempts.
	Logs rapid attempts within 60 seconds.
	Exit: Close the system. 

