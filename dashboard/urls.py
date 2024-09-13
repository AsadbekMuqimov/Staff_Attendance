from django.urls import path
from . import views
from .views import populate_db

app_name = 'dashboard'

urlpatterns = [
    path('', views.index, name='index'),


    # Avtorizatsiya
    path('log-in/', views.log_in, name='log_in'),
    path('log-out/', views.log_out, name='log_out'),


    # Staff 
    path('create-staff', views.create_staff, name='create_staff'),
    path('list-staff', views.list_staff, name='list_staff'),
    path('update-staff/<int:id>/', views.update_staff, name='update_staff'),
    path('delete-staff/<int:id>/', views.delete_staff, name='delete_staff'),


    # Attendance reports
    path('list-attendance', views.list_attendance, name='list_attendance'),


    # Edit profile staff
    path('edit-profile/<int:id>/', views.edit_profile, name='edit_profile'),
    
    
    # Position
    path('positions/', views.position_list, name='position_list'),           # Read all
    path('positions/create/', views.position_create, name='position_create'), # Create
    path('positions/<int:pk>/update/', views.position_update, name='position_update'), # Update
    path('positions/<int:pk>/delete/', views.position_delete, name='position_delete'), # Delete
    
    
    # Shift
    path('shifts/', views.shift_list, name='shift_list'),           # Read all
    path('shifts/create/', views.shift_create, name='shift_create'), # Create
    path('shifts/<int:pk>/update/', views.shift_update, name='shift_update'), # Update
    path('shifts/<int:pk>/delete/', views.shift_delete, name='shift_delete'), # Delete
    
    # StaffShift
    path('staff-shifts/', views.staff_shift_list, name='staff_shift_list'),            # Read all
    path('staff-shifts/create/', views.staff_shift_create, name='staff_shift_create'), # Create
    path('staff-shifts/<int:pk>/update/', views.staff_shift_update, name='staff_shift_update'), # Update
    path('staff-shifts/<int:pk>/delete/', views.staff_shift_delete, name='staff_shift_delete'), # Delete
    
    path('populate-db/', populate_db, name='populate_db'),

]