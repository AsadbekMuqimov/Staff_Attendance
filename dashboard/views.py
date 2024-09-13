from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from main import models
from django.shortcuts import render, get_object_or_404, redirect
from main.models import Position, Shift, StaffShift
from .forms import PositionForm, ShiftForm, StaffShiftForm
from django.http import HttpResponse
from main.models import Staff, StaffAttendance, Position, Shift, StaffShift
from faker import Faker
import random





#
def staff_shift_list(request):
    staff_shifts = StaffShift.objects.all()
    return render(request, 'dashboard/staff/staff_shift_list.html', {'staff_shifts': staff_shifts})


def staff_shift_create(request):
    if request.method == 'POST':
        form = StaffShiftForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('staff_shift_list')
    else:
        form = StaffShiftForm()
    return render(request, 'dashboard/staff/staff_shift_form.html', {'form': form, 'title': 'Create Staff Shift'})


def staff_shift_update(request, pk):
    staff_shift = get_object_or_404(StaffShift, pk=pk)
    if request.method == 'POST':
        form = StaffShiftForm(request.POST, instance=staff_shift)
        if form.is_valid():
            form.save()
            return redirect('staff_shift_list')
    else:
        form = StaffShiftForm(instance=staff_shift)
    return render(request, 'dashboard/staff/staff_shift_form.html', {'form': form, 'title': 'Update Staff Shift'})


def staff_shift_delete(request, pk):
    staff_shift = get_object_or_404(StaffShift, pk=pk)
    if request.method == 'POST':
        staff_shift.delete()
        return redirect('staff_shift_list')
    return render(request, 'dashboard/shifts/staff_shift_confirm_delete.html', {'staff_shift': staff_shift})


def shift_list(request):
    shifts = Shift.objects.all()
    return render(request, 'dashboard/shifts/shift_list.html', {'shifts': shifts})


def shift_create(request):
    if request.method == 'POST':
        form = ShiftForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shift_list')
    else:
        form = ShiftForm()
    return render(request, 'dashboard/shifts/shift_form.html', {'form': form, 'title': 'Create Shift'})


def shift_update(request, pk):
    shift = get_object_or_404(Shift, pk=pk)
    if request.method == 'POST':
        form = ShiftForm(request.POST, instance=shift)
        if form.is_valid():
            form.save()
            return redirect('shift_list')
    else:
        form = ShiftForm(instance=shift)
    return render(request, 'dashboard/shifts/shift_form.html', {'form': form, 'title': 'Update Shift'})


def shift_delete(request, pk):
    shift = get_object_or_404(Shift, pk=pk)
    if request.method == 'POST':
        shift.delete()
        return redirect('shift_list')
    return render(request, 'dashboard/shifts/shift_confirm_delete.html', {'shift': shift})

def position_list(request):
    positions = Position.objects.all()
    return render(request, 'dashboard/positions/position_list.html', {'positions': positions})

# Create a new position (Create)
def position_create(request):
    if request.method == 'POST':
        form = PositionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('position_list')
    else:
        form = PositionForm()
    return render(request, 'dashboard/positions/position_create.html', {'form': form })

# Update an existing position (Update)
def position_update(request, pk):
    position = get_object_or_404(Position, pk=pk)
    if request.method == 'POST':
        form = PositionForm(request.POST, instance=position)
        if form.is_valid():
            form.save()
            return redirect('position_list')
    else:
        form = PositionForm(instance=position)
    return render(request, 'dashboard/positions/position_form.html', {'form': form, 'title': 'Update Position'})

# Delete a position (Delete)
def position_delete(request, pk):
    position = get_object_or_404(Position, pk=pk)
    if request.method == 'POST':
        position.delete()
        return redirect('position_list')
    return render(request, 'dashboard/positions/position_confirm_delete.html', {'position': position})


@login_required(login_url='dashboard:log_in')
def index(request):
    """Main section of admin"""
    user = User.objects.count()
    users = User.objects.all()
    staff = models.Staff.objects.count()
    context = {
        'user':user,
        'users':users,
        'staff':staff
    }
    return render(request, 'dashboard/index.html', context)


@login_required(login_url='dashboard:log_in')
def edit_profile(request, id):
    """User profile edit"""
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return redirect('dashboard:index')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        firstname = request.POST.get('firstname')
        surname = request.POST.get('surname')

        if password:
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('confirm_password')
            if new_password != confirm_password:
                pass
            else:
                user.set_password(new_password)

        user.username = username
        user.firstname = firstname
        user.surname = surname
        user.save()

        return redirect('dashboard:index')
    return render(request, 'dashboard/profile.html', {'user': user})



#Staff
def create_staff(request):
    """Add staff"""
    if request.method=="POST":
        firstname=request.POST['firstname']
        surname=request.POST['surname']
        models.Staff.objects.create(firstname=firstname, surname=surname, )
    return render(request, 'dashboard/staff/create.html')


def list_staff(request):
    """List of staff"""
    staff = models.Staff.objects.all()
    context = {
        'staff': staff,
    }

    #print(staff)  # Debugging print statement without colorama

    return render(request, 'dashboard/staff/list.html', context)



def update_staff(request, id):
    """Edit staff profile"""
    staff = models.Staff.objects.get(id=id)
    if request.method =='POST':
        staff.firstname=request.POST['firstname']
        staff.surname=request.POST['surname']
        staff.save()
        return redirect('dashboard:list_staff')
    return render(request, 'dashboard/staff/update.html')

        

def delete_staff(request, id):
    """Delete staff"""
    models.Staff.objects.get(id=id).delete()
    return redirect('dashboard:list_staff')




def list_attendance(request):
    """Group of reports"""
    attendance = models.StaffAttendance.objects.all()
    context = {
        'attendance':attendance,
    }
    
    return render(request, 'dashboard/attendance/list.html', context)





def log_in(request):
    """Login"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard:index')
    return render(request, 'auth/login.html')


def log_out(request):
    logout(request)
    """Logout"""
    return redirect('dashboard:index')


   
fake = Faker()

def populate_db(request):
    # Pozitsiyalarni yaratish
    positions = ['Manager', 'Waiter', 'Chef', 'Bartender']
    for name in positions:
        Position.objects.get_or_create(name=name)

    # Xodimlarni yaratish
    for _ in range(10):
        Staff.objects.get_or_create(
            firstname=fake.first_name(),
            surname=fake.last_name(),
        )

    # Siljishlarni yaratish
    for _ in range(5):
        Shift.objects.get_or_create(
            s_time=fake.time_object(),
            e_time=fake.time_object()
        )

    # Xodimlar va siljishlar ro'yxatini olish
    staff_list = Staff.objects.all()
    shift_list = Shift.objects.all()

    # Xodim almashinuvi yozuvlarini yaratish
    for _ in range(10):
        StaffShift.objects.get_or_create(
            staff=staff_list.order_by('?').first(),
            shift=shift_list.order_by('?').first(),
            start_time=fake.date_time_this_year()
        )

    # Xodimlarning ishtirok yozuvlarini yaratish
    for staff in staff_list:
        for _ in range(3):
            StaffAttendance.objects.get_or_create(
                staff=staff,
                s_time=fake.date_time_this_year()
            )

    return HttpResponse("Database populated with fake data!")


