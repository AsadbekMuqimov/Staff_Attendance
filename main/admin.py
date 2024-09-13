from django.contrib import admin
from .models import Staff, StaffAttendance, Position, StaffShift, Shift



class StaffAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'surname')  # Admin panelda ko'rsatiladigan ustunlar
    search_fields = ('firstname', 'surname')  # Qidiruv uchun maydonlar

class StaffAttendanceAdmin(admin.ModelAdmin):
    list_display = ('staff', 's_time')  # Admin panelda ko'rsatiladigan ustunlar
    list_filter = ('staff',)  # Filtrlar
    search_fields = ('staff__firstname', 'staff__surname')  # Qidiruv uchun maydonlar

class PositionAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Admin panelda ko'rsatiladigan ustunlar

class ShiftAdmin(admin.ModelAdmin):
    list_display = ('s_time', 'e_time')  # Admin panelda ko'rsatiladigan ustunlar

class StaffShiftAdmin(admin.ModelAdmin):
    list_display = ('staff', 'shift', 'start_time')  # Admin panelda ko'rsatiladigan ustunlar
    list_filter = ('staff', 'shift')  # Filtrlar
    search_fields = ('staff__firstname', 'staff__surname', 'shift__s_time', 'shift__e_time')  # Qidiruv uchun maydonlar

# Admin panelda modellarni ro'yxatga olish
admin.site.register(Staff, StaffAdmin)
admin.site.register(StaffAttendance, StaffAttendanceAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(Shift, ShiftAdmin)
admin.site.register(StaffShift, StaffShiftAdmin)

    
    


