# Google Form Attendance Counter for AttendoBot

This script is designed to process Google Form attendance spreadsheets used in conjunction with the [AttendoBot Discord bot](https://github.com/WilsonnnTan/AttendoBot.git). It helps automate attendance management for Discord communities using Google Forms and AttendoBot.

---

# Attendance Counter

This Python script processes an attendance CSV file (such as those exported from Google Forms) and generates two reports:

1. **attendance_absentees.csv**: For each date, lists the number of absentees and their names.
2. **attendance_percentage.csv**: For each person, lists the number of days present and their attendance percentage.

## Requirements
- Python 3.x
- The input CSV file (default: `attendance.csv`) should be in the same directory as the script.
- The CSV file MUST have the following exact column names:
    - `Timestamp`: The date and time of attendance (e.g., `17/04/2025 08:00:00`)
    - `Name`: The name of the attendee
- The script will NOT work if your CSV uses different column names.

## Usage
1. Place your attendance CSV file in the same directory as `attendance_counter.py` and name it `attendance.csv` (or change the filename in the script).
2. Run the script:
    
    ```bash
    python attendance_counter.py
    ```
3. After running, two new files will be created in the same directory:
    - `attendance_absentees.csv`: Shows, for each date, how many people were absent and who they were.
    - `attendance_percentage.csv`: Shows, for each person, how many days they were present and their attendance percentage.

## How it works
- The script reads all unique names from the attendance file.
- For each date, it determines who was present and who was absent.
- It writes a date-wise absentee breakdown to `attendance_absentees.csv`.
- It also counts, for each person, how many days they attended and calculates their attendance percentage, saving this to `attendance_percentage.csv`.

## Customization
- If your input file is named differently or has different column names, edit the `process_attendance()` call at the bottom of `attendance_counter.py`.
- You can further customize the script to add more analytics or output formats as needed.

## Example
Input (`attendance.csv`):

| Timestamp           | Name    |
|---------------------|---------|
| 17/04/2025 08:00:00 | Alice   |
| 17/04/2025 08:00:00 | Bob     |
| 18/04/2025 08:00:00 | Alice   |
| 18/04/2025 08:00:00 | Charlie |

Output (`attendance_absentees.csv`):

| Date       | Number Absent | Absentees |
|------------|---------------|-----------|
| 2025-04-17 | 1             | Charlie   |
| 2025-04-18 | 1             | Bob       |

Output (`attendance_percentage.csv`):

| Name    | Days Present | Total Days | Attendance Percentage |
|---------|--------------|------------|----------------------|
| Alice   | 2            | 2          | 100.00%              |
| Bob     | 1            | 2          | 50.00%               |
| Charlie | 1            | 2          | 50.00%               |

## License
MIT License. Free to use and modify.
