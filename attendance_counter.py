import csv
from collections import defaultdict
from datetime import datetime

"""
attendance_counter.py

This script processes an attendance CSV file exported from Google Forms (or similar),
and generates two reports:
- attendance_absentees.csv: For each date, lists the number of absentees and their names.
- attendance_percentage.csv: For each person, lists the number of days present and their attendance percentage.

Usage:
    python attendance_counter.py

Make sure your attendance.csv file is in the same directory. The script REQUIRES the following exact column names:
- Timestamp: date and time of attendance (e.g., '17/04/2025 08:00:00')
- Name: name of the attendee

The script will NOT work if your CSV uses different column names.

Edit the filename in the __main__ block if your input file is named differently.
"""

def process_attendance(csv_filename):
    # First pass: collect all unique names
    all_names = set()
    rows = []
    with open(csv_filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row['Name'].strip()
            all_names.add(name)
            rows.append(row)

    # Second pass: group attendance by date
    attendance_by_date = defaultdict(set)
    for row in rows:
        try:
            date = datetime.strptime(row['Timestamp'], '%d/%m/%Y %H:%M:%S').date()
        except ValueError:
            # Try alternate format if needed
            date = datetime.strptime(row['Timestamp'].split()[0], '%d/%m/%Y').date()
        name = row['Name'].strip()
        attendance_by_date[str(date)].add(name)

    print("Date-wise absentee count and breakdown:")
    # Prepare to write to a new CSV
    output_filename = 'attendance_absentees.csv'
    with open(output_filename, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(['Date', 'Number Absent', 'Absentees'])
        for date in sorted(attendance_by_date):
            present = attendance_by_date[date]
            absent = sorted(all_names - present)
            num_absent = len(absent)
            print(f"{date}: {num_absent} absent")
            writer.writerow([date, num_absent, ', '.join(absent)])
    print(f"\nAbsentee report written to {output_filename}")

    # Calculate attendance percentage for each person
    total_days = len(attendance_by_date)
    attendance_count = {name: 0 for name in all_names}
    for date in attendance_by_date:
        for name in attendance_by_date[date]:
            attendance_count[name] += 1

    percentage_filename = 'attendance_percentage.csv'
    with open(percentage_filename, 'w', newline='', encoding='utf-8') as percfile:
        writer = csv.writer(percfile)
        writer.writerow(['Name', 'Days Present', 'Total Days', 'Attendance Percentage'])
        for name in sorted(all_names):
            days_present = attendance_count[name]
            percentage = (days_present / total_days) * 100 if total_days > 0 else 0
            writer.writerow([name, days_present, total_days, f"{percentage:.2f}%"])
    print(f"Attendance percentage report written to {percentage_filename}")

if __name__ == "__main__":
    process_attendance("attendance.csv")
