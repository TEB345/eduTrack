from django.db import connection
from django.utils import timezone
from datetime import time
from .models import Student,Lecturer,Admin,Department,Attendance,Subject

def update_marks(student_id, assessment_code, new_marks):
    with connection.cursor() as cursor:
        cursor.callproc('update_student_marks', [student_id, assessment_code, new_marks])

def record_automatic_attendance(student):
    """
    Records attendance automatically when student logs in
    Only marks as Present or Absent (no Late status)
    """
    today = timezone.now().date()
    current_time = timezone.now().time()
    
    # Get the student's current subjects
    current_subjects = Subject.objects.filter(
        D_Code=student.department  # Assuming student has department field
    )
    
    # Determine which subject session is active now
    active_subject = get_current_subject(current_time)
    
    if active_subject and active_subject in current_subjects:
        # Check if attendance already recorded today
        existing_attendance = Attendance.objects.filter(
            studentNumber=student,
            subjectCode=active_subject,
            dateAndTime__date=today
        ).exists()
        
        if not existing_attendance:
            # Check if within class time (no late status)
            class_start = get_class_start_time(active_subject)
            class_end = get_class_end_time(active_subject)
            
            is_present = (class_start <= current_time <= class_end)
            
            Attendance.objects.create(
                studentNumber=student,
                subjectCode=active_subject,
                status='P' if is_present else 'A',  # Only Present or Absent
                method='AUTO',
                verified=False
            )

def get_current_subject(current_time):
    """
    Returns the subject that should have class at the current time
    """
    # Example implementation - adjust to your timetable
    timetable = {
        '08:00-09:30': Subject.objects.get(code='CS101'),
        '10:00-11:30': Subject.objects.get(code='MATH201'),
        '01:00-2:30': Subject.objects.get(code='INT316D'),
        # Add more time slots as needed
    }
    
    for time_range, subject in timetable.items():
        start_str, end_str = time_range.split('-')
        start = time(*map(int, start_str.split(':')))
        end = time(*map(int, end_str.split(':')))
        
        if start <= current_time <= end:
            return subject
    return None

def get_class_start_time(subject):
    """
    Returns the start time for a given subject
    """
    # Implement based on your timetable structure
    # Example: return time(8, 0) for CS101
    timetable = {
        'CS101': time(8, 0),
        'MATH201': time(10, 0),
        'INT316D': time(1, 0),
        # Add more subjects
    }
    return timetable.get(subject.code)

def get_class_end_time(subject):
    """
    Returns the end time for a given subject
    """
    # Implement based on your timetable structure
    # Example: return time(9, 30) for CS101
    timetable = {
        'CS101': time(9, 30),
        'MATH201': time(11, 30),
        'INT316D': time(2, 30),
        # Add more subjects
    }
    return timetable.get(subject.code)