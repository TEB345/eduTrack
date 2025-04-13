from django.shortcuts import render, redirect, get_object_or_404
from .models import Student,Lecturer,Admin,Department,Attendance
from .forms import StudentForm,LecturerForm,AdminForm,DepartmentForm,AttendanceForm

#Home VIEW
def home(request):
    return render(request, 'home.html')

#Student VIEWS

def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'students/student_form.html', {'form': form})

def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/student_form.html', {'form': form})

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'students/student_confirm_delete.html', {'student': student})

#Lecturer VIEWS

def lecturer_list(request):
    lecturers = Lecturer.objects.all()
    return render(request, 'lecturers/lecturer_list.html', {'lecturers': lecturers})

def lecturer_create(request):
    if request.method == 'POST':
        form = LecturerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lecturer_list')
    else:
        form = LecturerForm()
    return render(request, 'lecturers/lecturer_form.html', {'form': form})

def lecturer_update(request, pk):
    lecturer = get_object_or_404(Lecturer, pk=pk)
    if request.method == 'POST':
        form = LecturerForm(request.POST, instance=lecturer)
        if form.is_valid():
            form.save()
            return redirect('lecturer_list')
    else:
        form = LecturerForm(instance=lecturer)
    return render(request, 'lecturers/lecturer_form.html', {'form': form})

def lecturer_delete(request, pk):
    lecturer = get_object_or_404(Lecturer, pk=pk)
    if request.method == 'POST':
        lecturer.delete()
        return redirect('lecturer_list')
    return render(request, 'lecturers/lecturer_confirm_delete.html', {'lecturer': lecturer})

#Admin VIEWS

def admin_list(request):
    admins = Admin.objects.all()
    return render(request, 'admin/admin_list.html', {'admins': admins})

def admin_create(request):
    if request.method == 'POST':
        form = AdminForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_list')
    else:
        form = AdminForm()
    return render(request, 'admin/admin_form.html', {'form': form})

def admin_update(request, pk):
    admin = get_object_or_404(Admin, pk=pk)
    if request.method == 'POST':
        form = AdminForm(request.POST, instance=admin)
        if form.is_valid():
            form.save()
            return redirect('admin_list')
    else:
        form = AdminForm(instance=admin)
    return render(request, 'admin/admin_form.html', {'form': form})

def admin_delete(request, pk):
    admin = get_object_or_404(Admin, pk=pk)
    if request.method == 'POST':
        admin.delete()
        return redirect('admin_list')
    return render(request, 'admin/admin_confirm_delete.html', {'admin': admin})

#Department VIEWS

def department_list(request):
    departments = Department.objects.all()
    return render(request, 'department/department_list.html', {'departments': departments})

def department_create(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('department_list')
    else:
        form = DepartmentForm()
    return render(request, 'department/department_form.html', {'form': form})

def department_update(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect('department_list')
    else:
        form = DepartmentForm(instance=department)
    return render(request, 'department/department_form.html', {'form': form})

def department_delete(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        department.delete()
        return redirect('department_list')
    return render(request, 'department/department_confirm_delete.html', {'department': department})

#Attendance VIEWS

def attendance_list(request):
    records = Attendance.objects.all()
    return render(request, 'attendance/attendance_list.html', {'records': records})

def attendance_create(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('attendance_list')
    else:
        form = AttendanceForm()
    return render(request, 'attendance/attendance_form.html', {'form': form})

def attendance_update(request, pk):
    record = get_object_or_404(Attendance, pk=pk)
    if request.method == 'POST':
        form = AttendanceForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('attendance_list')
    else:
        form = AttendanceForm(instance=record)
    return render(request, 'attendance/attendance_form.html', {'form': form})

def attendance_delete(request, pk):
    record = get_object_or_404(Attendance, pk=pk)
    if request.method == 'POST':
        record.delete()
        return redirect('attendance_list')
    return render(request, 'attendance/attendance_confirm_delete.html', {'record': record})